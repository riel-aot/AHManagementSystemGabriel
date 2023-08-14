from doctor import Doctor
from facility import Facility
from laboratory import Laboratory
from patient import Patient

class Management:
    def __init__(self):
        self.doctors_list = Doctor.readDoctorsFile()
        self.facilities_list = Facility.readFacilitiesFile()
        self.labs_list = Laboratory.readLaboratoriesFile()
        self.patients_list = Patient.readPatientsFile()
        
    @staticmethod
    def DisplayMenu():
        print("Welcome to Alberta Hospital (AH) Management system")
        print("Select from the following options, or select 0 to stop:")
        print("1 - Doctors")
        print("2 - Facilities")
        print("3 - Laboratories")
        print("4 - Patients")
        print()

    def run(self):
        while True:
            self.DisplayMenu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.doctors_menu()
            elif choice == "2":
                 self.facilities_menu()
            elif choice == "3":
                self.laboratories_menu()
            elif choice == "4":
                self.patients_menu()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def doctors_menu(self):
        while True:
            print("Doctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")
            print()

            choice = input("Enter your choice: ")

            if choice == "1":
                Doctor.displayDoctorsList(self.doctors_list)
            elif choice == "2":
                doctor_id = input("Enter the doctor ID: ")
                doctor = Doctor.searchDoctorById(self.doctors_list, doctor_id)
                if doctor:
                    Doctor.displayDoctorInfo(doctor)
                else:
                    print("Doctor not found.")
            elif choice == "3":
                doctor_name = input("Enter the doctor name: ")
                doctor = Doctor.searchDoctorByName(self.doctors_list, doctor_name)
                if doctor:
                    Doctor.displayDoctorInfo(doctor)
                else:
                    print("Doctor not found.")
            elif choice == "4":
                Doctor.addDoctorToFile()
                self.doctors_list = Doctor.readDoctorsFile()
            elif choice == "5":
                doctor_id = input("Please enter the ID of the doctor you want to edit: ")
                doctor = Doctor.searchDoctorById(self.doctors_list, doctor_id)
                if doctor:
                    doctor.editDoctorInfo()
                    Doctor.writeListOfDoctorsToFile(self.doctors_list)
                else:
                    print("Doctor not found.")
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def facilities_menu(self):
        while True:
            print("Facilities Menu:")
            print("1 - Display Facilities list")
            print("2 - Add Facility")
            print("3 - Back to the Main Menu")
            print()

            choice = input("Enter your choice: ")

            if choice == "1":
                Facility.displayFacilities(self.facilities_list)
            elif choice == "2":
                Facility.addFacility()
                self.facilities_list = Facility.readFacilitiesFile()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please enter a valid option.")
    
    def laboratories_menu(self):
        while True:
            print("Laboratories Menu:")
            print("1 - Display laboratories list")
            print("2 - Add laboratory")
            print("3 - Back to the Main Menu")
            print()
            
            choice = input("Enter your choice: ")

            if choice == "1":
                labs_list = Laboratory.readLaboratoriesFile()
                Laboratory.displayLabsList(labs_list)
            elif choice == "2":
                Laboratory.addLabToFile()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please enter a valid option.")
    
    def patients_menu(self):
        while True:
            print("Patients Menu:")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu")
            print()

            choice = input("Enter your choice: ")

            if choice == "1":
                Patient.displayPatientsList(self.patients_list)
            elif choice == "2":
                patient_id = input("\nEnter the patient ID: ")
                patient = Patient.searchPatientById(self.patients_list, patient_id)
                if patient:
                    patient.displayPatientInfo()
                else:
                    print("\nCan't find the patient with the same ID on the system")
            elif choice == "3":
                Patient.addPatientToFile()
                self.patients_list = Patient.readPatientsFile()
            elif choice == "4":
                patient_id = input("\nPlease enter the ID of the patient you want to edit: ")
                patient = Patient.searchPatientById(self.patients_list, patient_id)
                if patient:
                    patient.editPatientInfo()
                    Patient.writeListOfPatientsToFile(self.patients_list)
                else:
                    print("\nCan't find the patient with the same ID on the system")
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a valid option.")
# Example usage
if __name__ == "__main__":
    management_system = Management()
    management_system.run()
