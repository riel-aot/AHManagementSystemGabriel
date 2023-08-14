from doctor import Doctor
from facility import Facility
from laboratory import Laboratory
from patient import Patient
from management import Management

def display_menu():
    print("Main Menu")
    print("1. Display Doctors")
    print("2. Display Facilities")
    print("3. Display Laboratories")
    print("4. Display Patients")
    print("5. Add Patient")
    print("6. Exit")

def main():
    management_system = Management()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            Doctor.displayDoctorsList(management_system.doctors_list)
        elif choice == "2":
            Facility.displayFacilities(management_system.facilities_list)
        elif choice == "3":
            Laboratory.displayLabsList(management_system.labs_list)
        elif choice == "4":
            Patient.displayPatientsList(management_system.patients_list)
        elif choice == "5":
            Patient.addPatientToFile()
            management_system.patients_list = Patient.readPatientsFile()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
