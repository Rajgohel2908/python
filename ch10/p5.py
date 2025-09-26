from random import randint

class train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked for Train No. :{self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train No.{self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"Fare for Train No. :{self.trainNo} from :{fro} to :{to} is {randint(500, 2000)}")

a = train(56749)
a.getfare("Bhavnagar", "Ahmedabad")
a.book("Bhavnagar", "Ahmedabad")
a.getstatus()