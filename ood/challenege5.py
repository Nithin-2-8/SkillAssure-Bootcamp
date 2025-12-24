class Patient:
    def __init__(self, name, ward):
        self.name = name
        self.ward = ward
        self.assigned_surgeon = None

class Surgeon:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def operate(self, patient):
        """Assigns the surgeon to the patient and adds patient to surgeon's list."""
        self.patients.append(patient)
        patient.assigned_surgeon = self

    # Query 2: List patients operated by this surgeon
    def get_my_patients(self):
        return [p.name for p in self.patients]

class HospitalSystem:
    def __init__(self):
        self.patients = []

    def admit_patient(self, patient):
        self.patients.append(patient)

    # Query 1: Total number of patients being operated (assigned to a surgeon)
    def get_total_operated_patients(self):
        return len([p for p in self.patients if p.assigned_surgeon is not None])

    # Query 3: List patients in a specific ward
    def get_patients_in_ward(self, ward_name):
        return [p.name for p in self.patients if p.ward == ward_name]

# Main Method 
def main():
    # 1. Create the System
    hospital = HospitalSystem()

    # 2. Create Surgeons
    dr_straus = Surgeon("Dr. Straus")
    dr_hank = Surgeon("Dr. Hank")

    # 3. Create Patients
    p1 = Patient("Tony ", "ICU")
    p2 = Patient("Steve ", "General Ward")
    p3 = Patient("Bruce ", "ICU")
    p4 = Patient("Natasha", "General Ward")

    # 4. Admit Patients to Hospital
    hospital.admit_patient(p1)
    hospital.admit_patient(p2)
    hospital.admit_patient(p3)
    hospital.admit_patient(p4)

    # 5. Perform Operations (Assign Surgeons)
    # Dr. Straus operates on Tony and Bruce
    dr_straus.operate(p1)
    dr_straus.operate(p3)
    
    # Dr. Hank operates on Steve
    dr_hank.operate(p2)
    # Natasha is admitted but not operated on yet

    # 6. Execute Queries & Print Results
    print(" Hospital Report")
    
    # Query 1: Total operated patients 
    print(f"Total Patients Operated: {hospital.get_total_operated_patients()}")

    # Query 2: List patients by Surgeon
    print(f"Patients of {dr_straus.name}: {dr_straus.get_my_patients()}")
    print(f"Patients of {dr_hank.name}: {dr_hank.get_my_patients()}")

    # Query 3: List patients in a specific Ward
    print(f"Patients in ICU: {hospital.get_patients_in_ward('ICU')}")
    print(f"Patients in General Ward: {hospital.get_patients_in_ward('General Ward')}")

if __name__ == "__main__":
    main()