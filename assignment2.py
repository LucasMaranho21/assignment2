#defining a welcome function. so it will print: welcome and menu options.
def welcome():
    print("="*40)
    print("WELCOME TO BLOOD TYPE")
    print("="*40)
    print("1. Check which blood types can donate to a given blood type: ")
    print("2. Check which blood types can receive donations from a given blood type: ")
    print("3. Exit the program: ")


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
#validation function for blood type.
def blood_type_validation(blood):
    if blood in blood_compatibility:
        return True
    else:
        print(f"Blood type {blood} does not exist. Please type again.")
        return False  

def menu_validation_choice(menu_choice):
    if menu_choice in ["1","2","3"]:
        return True
    else:
        print(f"menu choice is not recognized. Please type 1, 2 or 3 only")
        return False

#function to bring the gives blood from the blood compatibility
def get_gives(blood):
    return blood_compatibility[blood]["gives"]

#function to bring the receives blood from the blood compatibility
def get_receives(blood):
    return blood_compatibility[blood]["receives"]

# main function to run the system.
def main():
    while True:
        welcome()
        menu_choice = input("Type 1,2,3: ").strip()
        
        if not menu_validation_choice(menu_choice):
            continue
        
        if menu_choice == "3":
            print("bye")
            break

        blood = input("blood type (e.g., A+, O-, AB+): ")
        
        if not blood_type_validation(blood):
            continue
        
        if menu_choice == "1":
            gives = get_gives(blood)
            print(f"Blood Type {blood} can donate to {gives}" )
        
        if menu_choice == "2":
            receives = get_receives(blood)
            print(f"Blood Type {blood} can receive donations from: {receives}")

if __name__ == "__main__":
    main()