class Laboratory:
    def __init__(self, lab_name, cost):
        self.lab_name = lab_name
        self.cost = cost

    @staticmethod
    def addLabToFile():
        lab_name = input("Enter Lab Name: ")
        cost = input("Enter Cost: ")
        with open("data/laboratories.txt", "a") as file:
            file.write(f"{lab_name}_{cost}\n")
        print("Lab added successfully!")

    @staticmethod
    def writeListOfLabsToFile(labs_list):
        with open("data/laboratories.txt", "w") as file:
            for lab in labs_list:
                file.write(f"{lab.lab_name}_{lab.cost}\n")
        print("Laboratories list written to file.")

    @staticmethod
    def displayLabsList(labs_list):
        print("Lab             Cost")
        print("--------------------")
        for lab in labs_list:
            print(f"{lab.lab_name:<16}{lab.cost}")
        print()

    @staticmethod
    def enterLaboratoryInfo():
        lab_name = input("Enter Lab Name: ")
        cost = input("Enter Cost: ")
        return Laboratory(lab_name, cost)

    @staticmethod
    def readLaboratoriesFile():
        labs_list = []
        with open("data/laboratories.txt", "r") as file:
            for line in file:
                lab_data = line.strip().split("_")
                lab = Laboratory(lab_data[0], lab_data[1])
                labs_list.append(lab)
        return labs_list
