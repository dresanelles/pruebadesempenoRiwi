# STUDENT MANAGEMENT

# Functions

def registerStudent():
        correctID = False
        while correctID == False:
            try:
                addID = int(input("Enter ID: "))
                correctID = True
            except ValueError:
                print("ERROR! Enter a valid value")
                continue
        name = (input("Name: "))
        lastName = input("Last Name: ")

        correctAge = False

        while correctAge == False:
            
            try:
                age = int(input("Age: "))
                correctAge = True
            except ValueError:
                print("ERROR! Enter a valid value")
            continue
        program = input("Program: ")
        state = input("State: ")
        students [len(students)+1] = {"id":addID,"name":name, "lastname":lastName,"age": age, "program": program, "state":state}
        
        print("\nStudent added!")

def searchStudent():
        search_id = int(input("\nIngresa ID: "))
        student_found = None
        for key, data in students.items():
            if data["id"] == search_id:
                student_found = data
        print("\nInformación\n")
        print(student_found)

def updateStudent():
    correctID = False
    while correctID == False:
        try:
            newID = int(input("Enter ID: "))
            correctID = True
        except ValueError:
            print("ERROR! Enter a valid value")
            continue
    newName = (input("Name: "))
    newLastName = input("Last Name: ")

    correctNewAge = False

    while correctNewAge == False:
        try:   
            newAge = int(input("Age: "))
            correctNewAge = True
        except ValueError:
            print("ERROR! Enter a valid value")
            continue
    newProgram = input("Program: ")
    newStatus = input("Status: ")
    students.update({"id":newID,"name":newName, "lastname": newLastName,"age": newAge, "program": newProgram, "state":newStatus})

    # Form 2
    # students["id"] = newID
    # students["name"] = newName
    # students["lastname"] = newLastName
    # students["age"] = newAge
    # students["program"] = newProgram
    # students["state"] = newStatus
    print("\n Update information!")

def deleteStudent():
    deleteID = int(input("\nEnter ID to delete: "))
    delete_student = None

    for llave, datos in students.items():
        if datos["id"] == deleteID:
            delete_student = True

            print(f'Delete student: {students[llave]}')
            delete_student = datos
            del students [llave]
            print("Successfully removed")
            break

# Main dictionary

students = {
    1: {
        "id": 1020,
        "name": "Kevin",
        "lastname": "Escorcia",
        "age": 30,
        "program": "Public Accounting",
        "state": "Active"
    },
    2: {
        "id": 1021,
        "name": "Luisa",
        "lastname": "De la Rosa",
        "age": 19,
        "program": "Medicine",
        "state": "Active"
    },
    3: {
        "id": 1022,
        "name": "Maria",
        "lastname": "Sanchez",
        "age": 19,
        "program": "Philosophy",
        "state": "Active"
    },
    4: {
         "id": 1023,
        "name": "Andres",
        "lastname": "Elles",
        "age": 28,
        "program": "Public Accounting",
        "state": "Active"       
    }
}


# Main loop 
test = False

while test == False:

    print("------ STUDENT MANAGEMENT ------\n")

    print("Menu: \n")

    print("1. Register ")
    print("2. Consult ")
    print("3. Search ")
    print("4. Update information ")
    print("5. Delete student")
    print("6. Exit")

    try:
        selection = int(input("\nSelect an option: "))
    except ValueError:
        print("Error, please enter valid information.")
        continue

    # New register

    if selection == 1:
        registerStudent()

    # Consult
    elif selection == 2:
       print(students)


    # Search

    elif selection == 3:
        searchStudent()


    # Update information

    elif selection == 4:
        updateStudent()

    # Delete Student

    elif selection == 5:
        deleteStudent()
    
    # Exit

    elif selection == 6:
        test = True
    
    else: 
        print("Error, please enter valid information")

        


