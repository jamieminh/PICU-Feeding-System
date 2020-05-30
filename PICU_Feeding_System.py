from database import patient_tree
from AVL_tree import NodePatientRankValue, AVLTree
from Patient import Patient


def low_risk_feed(pat, day):
    weight = pat.weight
    grv_crit = pat.GRV_crit
    from_HR = True if pat.patient_id[0] == 'A' else False

    if day == 0 or (day == 3 and from_HR is True):  # 1st day for LR or 4th day for HR
        feed = "5ML/2HRS" if weight <= 40 else "20ML/2HRS"
        pat.setFeed(day, 0, feed)
        pat.setFeed(day, 2, feed)
        pat.setIssue(day, 0, "NONE")
        pat.setIssue(day, 2, "NONE")

    # loop through hours
    for i in range(12):
        # for LR: start at hr 0 and check every 2 hrs (even hours)
        # for HR changed to LR: start at hr 1 and check every 2 hrs (odd hours)
        hr = i * 2 if from_HR is False else i * 2 + 1
        hr_grv = pat.getGRV(day, hr)

        if hr_grv != '':  # day[hr] has GRV reading
            if int(hr_grv) <= grv_crit:
                feed = "10ML/2HRS" if weight <= 40 else "30ML/2HRS"
                pat.setFeed(day, hr, feed)

                if hr + 2 < 24:
                    pat.setFeed(day, hr + 2, feed)
                pat.setIssue(day, hr, "NONE")
                pat.cont_stop = 0
            else:
                pat.setFeed(day, hr, "NO FEEDING")
                pat.cont_stop += 1

                if pat.cont_stop >= 3:  # 3rd continuous occurrence of FEEDING STOPPED
                    pat.setIssue(day, hr, "REFER DIETITIAN")
                else:
                    pat.setIssue(day, hr, "FEEDING STOPPED")

    # decide condition at the end of every day
    for j in range(23, 0, -1):
        last_issue = pat.getIssue(day, j)
        if last_issue != '':
            pat.setIssue(day, 23, last_issue)  # set ISSUE at the end of the day
            pat.setCondition(day, last_issue)

            # count total number of NONE, FEEDING STOPPED, DIETITIAN
            if last_issue == "NONE":
                pat.none += 1
            elif last_issue == "FEEDING STOPPED":
                pat.feeding_stopped += 1
            elif last_issue == "REFER DIETITIAN":
                pat.dietitian += 1
            break

# ------------------ EVALUATE PATIENTS THROUGH 5 DAYS --------------------
def evaluation():
    def lr_feed_in_order(node, day):
        if node is None:
            return
        lr_feed_in_order(node.left, day)
        low_risk_feed(node.patient, day)
        print("PATIENT %s - %s" % (node.patient.patient_id, ', '.join(node.patient.condition_list[0:day + 1])))
        lr_feed_in_order(node.right, day)

    for d in range(5):  # 5 days
        print("DAY", (d + 1))
        lr_feed_in_order(patient_tree.root, d)
        print("\n")


# ------------------ RANK PATIENTS AFTER EVALUATION --------------------
# sort by DECREASING None count, then by ASCENDING dietitian count, then by ASCENDING feeding_stopped count
# but instead of sorting multiple times, with rankValue calculation, we only need to sort once

def rank_patient():
    ranked_tree = AVLTree()

    def in_order_recur(node):
        if node is None:
            return
        in_order_recur(node.left)
        node.patient.setRankValue()
        ranked_tree.insert(NodePatientRankValue(node.patient))
        in_order_recur(node.right)

    def in_order_recur_rank(node):
        if node is None:
            return
        in_order_recur_rank(node.right)
        pat = node.patient
        pat.displayRankInfo()
        in_order_recur_rank(node.left)

    in_order_recur(patient_tree.root)
    in_order_recur_rank(ranked_tree.root)

# ------------------ DISPLAY FULL INFORMATION OF A PATIENT --------------------
def pat_info(pat_id):
    patient = patient_tree.search(pat_id)
    if type(patient) is Patient:  # if patient is found
        patient.displayInfo()


if __name__ == "__main__":
    evaluation()

    def menu():
        print("-" * 100 + "\n---All patients have been evaluated. What do you want to do?--")
        print("     Enter corresponding number or anything else to Exit Application\n"
              "     1. Rank Patients\n"
              "     2. See full information of a patient\n"
              )

        cmd = input()
        if cmd == '1':
            rank_patient()
        elif cmd == '2':
            pat_id = input("Enter patient's id: ")
            pat_info(pat_id.upper())
        else:
            return

        again = input("\nDo you want to work on something else? (Yes/No): ")
        if again.lower() == 'yes':
            menu()

    menu()
