class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def formatPatientInfo(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"

    def displayPatientInfo(self):
        print("ID   Name                   Disease         Gender          Age")
        print(f"{self.pid:<5}{self.name:<24}{self.disease:<16}{self.gender:<16}{self.age:<16}")

    @staticmethod
    def enterPatientInfo():
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        disease = input("Enter Disease: ")
        gender = input("Enter Gender: ")
        age = input("Enter Age: ")
        return Patient(pid, name, disease, gender, age)

    @staticmethod
    def readPatientsFile():
        patients_list = []
        with open("data/patients.txt", "r") as file:
            for line in file:
                patient_data = line.strip().split("_")
                patient = Patient(patient_data[0], patient_data[1], patient_data[2], patient_data[3], patient_data[4])
                patients_list.append(patient)
        return patients_list

    @staticmethod
    def searchPatientById(patients_list, pid):
        for patient in patients_list:
            if patient.pid == pid:
                return patient
        return None

    @staticmethod
    def displayPatientsList(patients_list):
        print("ID   Name                   Disease         Gender          Age")
        print("--------------------------------------------------------------")
        for patient in patients_list:
            patient.displayPatientInfo()
        print()

    @staticmethod
    def writeListOfPatientsToFile(patients_list):
        with open("data/patients.txt", "w") as file:
            for patient in patients_list:
                file.write(patient.formatPatientInfo() + "\n")
        print("Patients list written to file.")

    @staticmethod
    def addPatientToFile():
        new_patient = Patient.enterPatientInfo()
        with open("data/patients.txt", "a") as file:
            file.write(new_patient.formatPatientInfo() + "\n")
        print("Patient added successfully!")


