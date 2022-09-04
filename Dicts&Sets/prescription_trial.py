from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    prescription.remove(warfarin)
    prescription.add(edoxaban)
    print(patient, prescription)


    # for patient_name, medications_taken in patients[patient]:
    #     # if warfarin in medications_taken:
    #     #     medications_taken.remove(warfarin)
    #     #     medications_taken.add(edoxaban)
    #     # else:
    #     #     continue
    #     # print(patient_name, medications_taken)

