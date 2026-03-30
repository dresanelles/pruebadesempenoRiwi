# Student Management System with Data Persistence

This program allows you to manage university student information based on criteria such as:

- ID number
- First and last name
- Age
- Program of study
- Status (Active or inactive)

The program allows you to perform the following functions: add students, display the student list, perform custom searches by ID number, update information, delete a student, and close the program completely.

## How to use:

Clone repository:

git clone https://github.com/dresanelles/pruebadesempenoRiwi.git

## Run:

prueba.py

## Key functions:

registerStudent(): Allows you to add a new student.

searchStudent(): Allows you to search for a student using their ID number.

updateStudent(): Updates a student's information.

## Example of use:

The user must choose one of the options shown in the main menu, which are as follows:

### 1. Add new user

Upon accessing this menu, the user will be asked for the following information:
- Enter ID number
- First name
- Last name
- Program of study
- Status (active / inactive)

Once the requested information is entered, a message will appear indicating that the student has been successfully added.

### 2. Search

All students saved in the database will be displayed with their respective information (ID, first name, last name, program, status).

### 3. Custom search

By entering the student's ID, the corresponding information (ID, first name, last name, program, status) can be viewed.

### 4. Update information

The user will be asked for the following information:

- Enter ID number
- First name
- Last name
- Program of study
- Status (active / inactive)

Once the data is entered, it will be updated in the data management system.

### 5. Delete User

You can delete a user by entering their ID. A message will then appear confirming that the user has been successfully deleted.

### 6. Exit

This option closes the program automatically.

## Concepts demonstrated:

- Input validation and error handling
- Use of for-while loops
- If/elif/else structure
- Data management
- Data updating
- Creation, use, and modification of dictionaries.
