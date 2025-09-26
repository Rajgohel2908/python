from random import randint

class train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(raj, fro, to):
        print(f"Ticket is booked for Train No. :{raj.trainNo} from {fro} to {to}")

    def getstatus(raj):
        print(f"Train No.{raj.trainNo} is running on time")

    def getfare(raj, fro, to):
        print(f"Fare for Train No. :{raj.trainNo} from :{fro} to :{to} is {randint(500, 2000)}")

a = train(56749)
a.getfare("Bhavnagar", "Ahmedabad")
a.book("Bhavnagar", "Ahmedabad")
a.getstatus()