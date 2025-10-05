import os

# Path to Documents folder
doc_path = os.path.expanduser("~/Documents")

# Ensure Documents folder exists
if not os.path.exists(doc_path):
    os.makedirs(doc_path)

while True: # Main loop (which the users can select options on the menu)
    print("===============================")
    print(" Student Records Management ")
    print("1. Register Student")
    print("2. Open Student Record")
    print("3. Search by Name")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")
    print("===============================")

    try: # Get user choice
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number from 1-6.")
        continue 

    if choice == 1: # To register a student and save to a text file
        student_no = input("Student No.: ")
        last_name = input("Last Name: ")
        first_name = input("First Name: ")
        middle_initial = input("Middle Initial: ")
        program = input("Program: ")
        age = input("Age: ")
        gender = input("Gender: ")
        birthday = input("Birthday (MM/DD/YYYY): ")
        contact = input("Contact No.: ")
    
    #  Prepare data lines (this is the format of data that should be saved in the file)
        data = [ 
            f"Student No.: {student_no}",
            f"Full Name: {last_name}, {first_name} {middle_initial}.",
            f"Program: {program}",
            f"Age: {age}",
            f"Gender: {gender}",
            f"Birthday: {birthday}",
            f"Contact No.: {contact}"
        ]

    # Save to file (one file per student register, named by their student number)
        file_path = os.path.join(doc_path, f"{student_no}.txt")
        with open(file_path, "w") as f: # overwrite if file exists
            for line in data:
                f.write(line + "\n")

    # confirmation message if successfully saved
        print(f"Student record saved as {file_path}") 

    # Open student record and display content
    elif choice == 2:
        student_no = input("Enter Student No. to open: ")
        file_path = os.path.join(doc_path, f"{student_no}.txt")

    # Display student record if file exists
        try: 
            with open(file_path, "r") as f:
                print("\n--- Student Record ---") 
                for line in f:
                    print(line.strip())
                print("----------------------")
        except FileNotFoundError:
            print("Student record not found.")

    # Search student by name (last name or first name)
    elif choice == 3:
        search_name = input("Enter last name or first name to search: ").lower()
        found = False 
        for file_name in os.listdir(doc_path): # Loop through all files in Documents
            if file_name.endswith(".txt"): # Only consider text files
                file_path = os.path.join(doc_path, file_name)
                with open(file_path, "r") as f: # Open each file and read lines
                    lines = f.readlines() 
                    for line in lines:
                        if line.startswith("Full Name:") and search_name in line.lower():
                            print(f"\nFound in {file_name}:") # Display matching record
                            for l in lines:
                                print(l.strip()) # print one line at a time
                            print("----------------------")
                            found = True 
        if not found: 
            print("No student record found with that name.")

    # Update student record
    elif choice == 4:  
    # Get student number to update
        student_no = input("Enter Student No. to update: ") 
        file_path = os.path.join(doc_path, f"{student_no}.txt")

        if os.path.exists(file_path): # If file exists, proceed to update
            with open(file_path, "r") as f:
                lines = f.readlines()

            # Display current record
            print("\n--- Current Record ---")
            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}") 
            print("----------------------")

        # Get field to update (the user will choose which field to update)
            try:
                field_choice = int(input("Please enter what do you want to update (1-7): "))

                if 1 <= field_choice <= len(lines):
                    field_label = lines[field_choice - 1].split(":")[0]  # keep label

                # Get new value for the selected field
                    if field_choice == 2:  # Full Name special handling
                        print("Updating Full Name details...")
                        last_name = input("Last Name: ")
                        first_name = input("First Name: ")
                        middle_initial = input("Middle Initial: ")
                        lines[field_choice - 1] = f"Full Name: {last_name}, {first_name} {middle_initial}.\n"
                    else: # Other fields 
                        new_value = input(f"Enter new {field_label}: ") # Get new value
                        lines[field_choice - 1] = f"{field_label}: {new_value}\n" 

                    # Save updated file
                    with open(file_path, "w") as f: 
                        f.writelines(lines) # Write all lines back to file
                    print("Record updated successfully.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input. Please enter a number.") 
        else:
            print("Student record not found.")

    elif choice == 5:
        # Delete record
        student_no = input("Enter Student No. to delete: ") 
        file_path = os.path.join(doc_path, f"{student_no}.txt") # File path to delete
        if os.path.exists(file_path):
            os.remove(file_path) # Delete the file and its content
            print("Student record deleted successfully.")
        else:
            print("Student record not found.")
    
    # Exit the program
    elif choice == 6:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1-6.") # Handle invalid menu choice
