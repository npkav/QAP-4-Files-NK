# Nickolas Kavanagh
# SD 12 QAP 4
# Project 1 – Python – Functions, Lists, and Data Files
# Project 3 - Javascript
# July 15, 2024 - July 26, 2024

## QAP 4 - Project 1 – Python – Functions, Lists, and Data Files

This code is an insurance premium calculator and claim management system.
    1. The program calculates insurance premiums based on user inputs.
    2. It manages customer information and claim details.
    3. It generates receipts and logs for each transaction.
    4. It allows for multiple calculations in a single session.

How to use:

The program will display a policy number and prompt you for various inputs:
    1. Personal information (name, birth date, address, etc.)
    2. Number of cars to insure
    3. Additional coverage options
    4. Payment method
    5. Claim information

After entering all required information, the program will:
    1. Calculate the premium and associated costs
    2. Generate a unique user ID
    3. Log the transaction details to a file named with the user ID
    4. The program will then ask if you want to exit and generate a receipt or continue with another calculation.

If you choose to exit:
    1. A receipt will be generated and displayed
    2. The program will terminate

If you choose to continue:
    1. The policy number will increment
    2. A new calculation cycle will begin

Key Features:
    1. Input validation for various fields (e.g., province, postal code, dates)
    2. Progress bar for file writing operations
    3. Flexible payment options (Full, Monthly, Down Payment)
    4. Claim logging and receipt generation

To use this program effectively, make sure you have:
    1. A "Const.dat" file in the same directory with the necessary constants (e.g., BASIC_PREMIUM, HST_RATE, etc.)
    2. Proper file read/write permissions in the directory where the program is running
    3. This program is designed for insurance agents or customers to quickly calculate premiums, log claims, and
    manage policy information in an interactive manner.



## QAP 4 - Project 3 – Javascript

1. The code defines a motelCustomer object with various properties including personal details, room preferences, and stay information.

2. Two methods are included in the object:
      getAge(): Calculates the customer's age based on their birth date.
      getDurationOfStay(): Calculates the length of stay in nights.

3. A template literal string customerDescription is created, which formats the customer's information into a readable description.
      The description includes:
        Name, age, and gender
        Duration of stay
        Room preferences
        Check-in and check-out dates
        Contact information and address
        Payment method

4. Finally, the description is logged to the console using console.log().

This code effectively creates a detailed customer profile for a motel guest and generates a formatted description of their stay.
