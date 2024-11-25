#defining a welcome function. so it will print: welcome and menu options.
def welcome():
    print("WELCOME TO BLOOD TYPE")
    print("Check which blood types can donate to a given blood type: 1")
    print("Check which blood types can receive donations from a given blood type: 2")
    print("Exit the program: 3")
    
welcome()

# Dictionary to save data information about blood compatibility.
blood_compatibility = {
    "A+": {"gives": ["A+", "AB+"], 
          "receives": ["A+", "A-", "O+", "O-"]},
    
    "A-": {"gives": ["A+", "A-", "AB+", "AB-"], 
           "receives": ["A-", "O-"]},
        
    "AB+": {"gives": ["AB+"], 
            "receives": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]},

    "AB-": {"gives": ["AB+", "AB-"], 
            "receives": ["AB-", "A-", "B-", "O-"]},

    "B+": {"gives": ["B+", "AB+"], 
           "receives": ["B+", "B-", "O+", "O-"]},

    "B-": {"gives": ["B+", "B-", "AB+", "AB-"], 
           "receives": ["B-", "O-"]},

    "O+": {"gives": ["O+", "A+", "B+", "AB+"], 
           "receives": ["O+", "O-"]},

    "O-": {"gives": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], 
           "receives": ["O-"]}

}

def blood_type_validation(blood):
    if blood in blood_compatibility:
        return True
    else:
        print(f"Blood type {blood} does not exist. Please type again.")
        return False    