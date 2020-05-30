from restrict import check_attribute
from pprint import pprint
import math


@check_attribute
class Patient:
    patient_id = str
    risk = str
    age = int
    weight = float
    GRV_crit = int
    rankValue = int

    def __init__(self, patient_id, status, age, weight, feeding_chart):
        self.patient_id = patient_id
        self.risk = status
        self.age = age
        self.weight = weight
        self.GRV_crit = (math.floor(weight * 5) if weight <= 40 else 250)  # grv_crit = 250 for children > 40kg
        self.feeding_chart = feeding_chart
        [self.none, self.feeding_stopped, self.dietitian] = [0, 0, 0]
        self.condition_list = ['N/A' for i in range(5)]
        self.cont_stop = 0
        self.rankValue = 0

    def displayInfo(self):
        print("\n{:<20}: {}\n{:<20}: {}\n{:<20}: {}\n{:<20}: {}\n{:<20}: {}\n{:<20}: "
              .format("Patient ID", self.patient_id, "Status", self.risk, "Age", self.age,
                      "Weight", self.weight, "GRV Critical", self.GRV_crit, "Feeding Chart"))
        pprint(self.feeding_chart)

    def setCondition(self, day, condition):
        self.condition_list[day] = condition

    def setRankValue(self):
        self.rankValue = self.none * 10 - self.feeding_stopped - self.dietitian * 3
        # each NONE worth 10 points, for every FEEDING STOPPED, total point is reduced by 1
        # each REFER DIETITIAN equals 3 FEEDING STOP, so for every REFER DIETITIAN, total point is reduced by 3

    def setFeed(self, day, hour, feed):
        self.feeding_chart[day][hour][2] = feed

    def getFeed(self, day, hour):
        return self.feeding_chart[day][hour][2]

    def setIssue(self, day, hour, issue):
        self.feeding_chart[day][hour][4] = issue

    def getIssue(self, day, hour):
        return self.feeding_chart[day][hour][4]

    def setGRV(self, day, hour, grv):
        self.feeding_chart[day][hour][3] = grv

    def getGRV(self, day, hour):
        return self.feeding_chart[day][hour][3]

    def displayRankInfo(self):
        print("PATIENT %s - NONE: %d; FEEDING STOPPED: %d; REFER DIETITIAN: %d => Total rank point: %d"
                      % (self.patient_id, self.none, self.feeding_stopped, self.dietitian, self.rankValue))
