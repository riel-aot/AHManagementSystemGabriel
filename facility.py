class Facility:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def addFacility():
        facility_name = input("Enter Facility Name: ")
        with open("data/facilities.txt", "a") as file:
            file.write(facility_name + "\n")
        print("Facility added successfully!")

    @staticmethod
    def writeListOfFacilitiesToFile(facilities_list):
        with open("data/facilities.txt", "w") as file:
            for facility in facilities_list:
                file.write(facility.name + "\n")
        print("Facilities list written to file.")

    @staticmethod
    def displayFacilities(facilities_list):
        print("Facilities Menu:")
        print("1 - Display Facilities list")
        print("2 - Add Facility")
        print("3 - Back to the Main Menu")
        print()
        
        choice = input("Enter your choice: ")

        if choice == "1":
            Facility.displayFacilitiesList(facilities_list)
        elif choice == "2":
            Facility.addFacility()
        elif choice == "3":
            pass  # This option will be handled in the main management loop
        else:
            print("Invalid choice. Please enter a valid option.")

    @staticmethod
    def displayFacilitiesList(facilities_list):
        print("The Hospital Facilities are:")
        for facility in facilities_list:
            print(facility.name)
        print()

    @staticmethod
    def readFacilitiesFile():
        facilities_list = []
        with open("data/facilities.txt", "r") as file:
            for line in file:
                facility_name = line.strip()
                facility = Facility(facility_name)
                facilities_list.append(facility)
        return facilities_list
