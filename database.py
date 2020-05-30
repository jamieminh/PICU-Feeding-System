import csv
from AVL_tree import AVLTree, NodePatient
from pprint import pprint
from Patient import Patient

patient_tree = AVLTree()

patient_ids = ["A1", "A2", "A3", "B1", "B2", "B3", "B4", "B5", "B6", "B7"]
patient_csv = list(map(lambda pat: "PATIENT DATA - PATIENT " + pat + ".csv", patient_ids))


for i in range(len(patient_ids)):
    with open("patients\\" + patient_csv[i]) as file:
        reader = csv.reader(file)
        data = list(reader)
        # pprint(data)
        risk = data[0][1]  # get risk (LR/HR)
        age = data[0][2].split(" ")[1]  # get age
        weight = data[0][4].split(" ")[1]  # get weight (kg)
        feeding_chart = []

        for j in range(5):
            feeding_chart.append([data[k + 3] for k in range(24 * j, 24 * (j + 1))])

        patient = Patient(patient_ids[i], risk, int(age), float(weight), feeding_chart)
        patient_tree.insert(NodePatient(patient))
