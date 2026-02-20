# Hospital Check-in Program
# Author: Jafet Perez Reyes & Aaron Sanchez
# Date: 2/10/2026


# this is where we're going to store this
patients = [
    {
    "Name": "Alex",
    "Age": 67,
    "Gender": "Both",
    "Date of Birth": "6/07/67",
    "Symptoms": "Pain",
    "Priority": "low"
    },
    {"Name": "Aex",
    "Age": 67,
    "Gender": "Both",
    "Date of Birth": "6/07/67",
    "Symptoms": "Pain",
    "Priority": "low"
    }
    ]





def search_patient(Name):
    
    for patient in patients: # for every dictionary in patients
        if patient["Name"] == Name: # if the name value in the dictionary is equal to the paramenter "Name"
                print()
                print("Patient found:")

                for key, value in patient.items(): # for every key and value in the items of the idctionary "patient"
                    print(f"{key}: {value}") # do this (printing the item's key and value)

                return # stop this function
    print("Patient not found.") # print if no found bc if it is the function will stop




 
# the variable patient is a local varible so its only defined inside the fuction





def add_patient(): 
    patient = { # our empty list
        "Name": None,
        "Age": None, 
        "Gender": None,
        "Date of Birth": None,
        "Symptoms": None,
        "Priority": None
        }
    
    for key in patient: # for every key in our paitent list
        patient[key] = input(key + ": ") # print that and get input

    for dictionaries in patients: # the dictionaries we have in this
        if patient["Name"] == dictionaries["Name"]: # if the thing we entered is in the databse
            print("Patient already exsists")
        else: #otherwise
            patients.append(patient) # add to database

            print(f"Patient {patient["Name"]}, has been successfully added")
            return




# We're going to have a main loop
# We're going to use "break" to get out of loop when when user wants to exit.





while True:
    print()
    print("==== Hospital Patient Check-in ====")
    print("1. Add Patient")
    print("2. Lookup Patient")
    print("3. Exit")

    try: # try this
        user_input = int(input())
        if user_input == 1:

            add_patient()

        elif user_input == 2:

            patient_name = input("Enter the patients name: ")
            search_patient(patient_name)

        elif user_input == 3:

            print("Goodbye!")
            break

    except ValueError: # if we get "value error"
        print()
        print("Please enter a number.")
