class Doctor:
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def formatDrInfo(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"

    def enterDrInfo(self):
        self.doctor_id = input("Enter Doctor ID: ")
        self.name = input("Enter Doctor Name: ")
        self.specialization = input("Enter Specialization: ")
        self.working_time = input("Enter Working Time: ")
        self.qualification = input("Enter Qualification: ")
        self.room_number = input("Enter Room Number: ")

    @staticmethod
    def readDoctorsFile():
        doctors_list = []
        with open("data/doctors.txt", "r") as file:
            for line in file:
                data = line.strip().split("_")
                doctor = Doctor(data[0], data[1], data[2], data[3], data[4], data[5])
                doctors_list.append(doctor)
        return doctors_list

    @staticmethod
    def searchDoctorById(doctors_list, doctor_id):
        for doctor in doctors_list:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None

    @staticmethod
    def searchDoctorByName(doctors_list, doctor_name):
        for doctor in doctors_list:
            if doctor.name == doctor_name:
                return doctor
        return None

    
    @staticmethod
    def displayDoctorInfo(doctor):
        print("Id   Name                   Speciality      Timing          Qualification   Room Number")
        print(f"{doctor.doctor_id:<5} {doctor.name:<22} {doctor.specialization:<15} {doctor.working_time:<15} {doctor.qualification:<15} {doctor.room_number:<10}")

    def editDoctorInfo(self):
        self.name = input("Enter New Name: ")
        self.specialization = input("Enter New Specialization: ")
        self.working_time = input("Enter New Working Time: ")
        self.qualification = input("Enter New Qualification: ")
        self.room_number = input("Enter New Room Number: ")

    @staticmethod
    def displayDoctorsList(doctors_list):
        print("Doctors Menu:")
        print("1 - Display Doctors list")
        print("2 - Search for doctor by ID")
        print("3 - Search for doctor by name")
        print("4 - Add doctor")
        print("5 - Edit doctor info")
        print("6 - Back to the Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Id   Name                   Speciality      Timing          Qualification   Room Number")
            print("-------------------------------------------------------------------------------------")
            for doctor in doctors_list:
                Doctor.displayDoctorInfo(doctor)
            print("\nBack to the prevoius Menu")
        elif choice == "2":
            doctor_id = input("\nEnter the doctor Id: ")
            doctor = Doctor.searchDoctorById(doctors_list, doctor_id)
            if doctor:
                print("\nId   Name                   Speciality      Timing          Qualification   Room Number")
                print("-------------------------------------------------------------------------------------")
                Doctor.displayDoctorInfo(doctor)
            else:
                print("\nCan't find the doctor with the same ID on the system")
            print("\nBack to the prevoius Menu")
        elif choice == "3":
            doctor_name = input("\nEnter the doctor name: ")
            doctor = Doctor.searchDoctorByName(doctors_list, doctor_name)
            if doctor:
                print("\nId   Name                   Speciality      Timing          Qualification   Room Number")
                print("-------------------------------------------------------------------------------------")
                Doctor.displayDoctorInfo(doctor)
            else:
                print("\nCan't find the doctor with the same name on the system")
            print("\nBack to the prevoius Menu")
        elif choice == "4":
            Doctor.addDoctorToFile()
            doctors_list = Doctor.readDoctorsFile()
        elif choice == "5":
            doctor_id = input("\nPlease enter the id of the doctor that you want to edit their information: ")
            doctor = Doctor.searchDoctorById(doctors_list, doctor_id)
            if doctor:
                doctor.editDoctorInfo()
                Doctor.writeListOfDoctorsToFile(doctors_list)
                print("\nDoctor information updated successfully!")
            else:
                print("\nCan't find the doctor with the same ID on the system")
            print("\nBack to the prevoius Menu")

        elif choice == "6":
            print("Back to the Main Menu")
        else:
            print("Invalid choice. Please enter a valid option.") 
        pass


    @staticmethod
    def addDoctorToFile():
        new_doctor = Doctor.enterDrInfo()
        with open("data/doctors.txt", "a") as file:
            file.write(new_doctor.formatDrInfo() + "\n")
        print("Doctor added successfully!")

    @staticmethod
    def writeListOfDoctorsToFile(doctors_list):
        with open("data/doctors.txt", "w") as file:
            for doctor in doctors_list:
                file.write(doctor.formatDrInfo() + "\n")
        print("Doctors list written to file.")