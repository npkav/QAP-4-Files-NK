# Nickolas Kavanagh
# SD 12 QAP 4
# Project 1 – Python – Functions, Lists, and Data Files
# July 15, 2024 - July 26, 2024

##-----------------------##
##        IMPORTS        ##
##-----------------------##
import datetime
import sys


#-----------------------#
#       FUNCTIONS       #
#-----------------------#
def valid_province(province: str) -> bool:
    # Check if the province is valid
    valid_provinces = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
    province_upper = province.upper()
    if province_upper in valid_provinces:
        return True
    else:
        print(f"{province_upper} is not a valid province.")
        return False

def valid_postal_code(postal_code: str) -> bool:
    # Check if the length of the postal code is exactly 7 characters (including the space)
    if len(postal_code) != 7:
        return False
    
    # Check if the format is A1A 1A1
    if (postal_code[0].isalpha() and postal_code[1].isdigit() and postal_code[2].isalpha() and
        postal_code[3] == ' ' and postal_code[4].isdigit() and postal_code[5].isalpha() and postal_code[6].isdigit()):
        return True
    
    return False

def valid_date(date: str) -> bool:
    # Check if the date is valid in YYYY/MM/DD format
    try:
        datetime.datetime.strptime(date, '%Y/%m/%d')
        return True
    except ValueError:
        return False

def user_id_gen(first_name: str, last_name: str, birth_year: str) -> str:
    # Generate custom user ID
    return (first_name[:2] + last_name[:3] + birth_year[2:4]).upper()

def progress_bar(current, total, width=50):
    percent = float(current) / total
    filled = int(width * percent)
    bar = '=' * filled + '-' * (width - filled)
    sys.stdout.write(f'\r[{bar}] {percent:.0%}')
    sys.stdout.flush()

def generate_receipt(user_id, first_name, last_name):
    file_name = f"{user_id}.txt"
    try:
        with open(file_name, 'r') as file:
            file_content = file.readlines()
        
        print("\n" + "=" * 40)
        print(f"Receipt for user: {first_name} {last_name}")
        print("=" * 40)
        
        claims = []
        for line in file_content:
            print(line.strip())
            if line.startswith("Claim No.:"):
                claims.append(line.strip().split(": ")[1])
            elif line.startswith("Claim Date:"):
                claims[-1] += "," + line.strip().split(": ")[1]
            elif line.startswith("Claim Amount:"):
                claims[-1] += "," + line.strip().split(": $")[1]
        
        print("\nPrevious Claims:")
        print("Claim #      Claim Date     Amount")
        print("--------------------------------------")
        
        for claim in claims:
            claim_no, claim_date, claim_amount = claim.split(",")
            print(f"{claim_no:5}        {claim_date}      ${float(claim_amount):,.2f}")
        
        print(f"\n======================================")
        print(f"          End of Receipt")
        print(f"======================================")
    
    except FileNotFoundError:
        print(f"Error: File for User ID {user_id} not found.")

#-----------------------#
#       CONSTANTS       #
#-----------------------#
with open("Const.dat", "r") as f:
    lines = f.readlines()
    POLICY_NUM = int(lines[0].strip())
    BASIC_PREMIUM = float(lines[1].strip())
    ADD_CAR_DISCOUNT = float(lines[2].strip())
    EXTRA_LIABILITY_COST = float(lines[3].strip())
    GLASS_COVERAGE_COST = float(lines[4].strip())
    LOANER_CAR_COST = float(lines[5].strip())
    HST_RATE = float(lines[6].strip())
    PROCESSING_FEE = float(lines[7].strip())
    LIABILITY_COVERAGE_AMOUNT = float(lines[8].strip())
    NUM_PAYMENTS = int(lines[9].strip())


while True:
    # print policy number
    print(f"Policy No.: {POLICY_NUM}")
    #-----------------------#
    #         INPUTS        #
    #-----------------------#
    # Collect customer first name
    while True:
        CustFirst = str(input("Please enter your first name: ")).title()
        if not CustFirst.strip():
            print("ERROR: Customer first name must be entered before continuing.\n")
        else:
            print(f"First name: {CustFirst}\n")
            break

    # Collect customer last name
    while True:
        CustLast = str(input("Please enter your last name: ")).title()
        if not CustLast.strip():
            print("ERROR: Customer last name must be entered before continuing.\n")
        else:
            print(f"Last name: {CustLast}\n")
            break

    # Collect customer birth date
    while True:
        CustBirthDate = input("Please enter your birth date (YYYY/MM/DD): ")
        if not valid_date(CustBirthDate):
            print("ERROR: Customer birth date must be in valid format.\n")
        else:
            print(f"Birth date: {CustBirthDate}\n")
            break

    # Collect customer address
    while True:
        CustAddress = str(input("Please enter your address: ")).title()
        if not CustAddress.strip():
            print("ERROR: Customer address must be entered before continuing.\n")
        else:
            print(f"Address: {CustAddress}\n")
            break

    # Collect customer city
    while True:
        CustCity = str(input("Please enter your city: ")).title()
        if not CustCity.strip():
            print("ERROR: Customer city must be entered before continuing.\n")
        else:
            print(f"City: {CustCity}\n")
            break

    # Collect customer province
    while True:
        CustProvince = str(input("Please enter your province (XX): ")).upper()
        if not CustProvince.strip():
            print("ERROR: Customer province must be entered before continuing.\n")
        elif not valid_province(CustProvince):
            print("ERROR: Customer province must be valid.\n")
        else:
            print(f"Province: {CustProvince}\n")
            break

    # Collect customer postal code
    while True:
        CustPostal = str(input("Please enter your postal code (A1A 1A1): ")).upper()
        if not CustPostal.strip():
            print("ERROR: Customer postal code must be entered before continuing.\n")
        elif not valid_postal_code(CustPostal):
            print("ERROR: Customer postal code must be valid.\n")
        else:
            print(f"Postal code: {CustPostal}\n")
            break

    # Collect number of cars being insured
    while True:
        NumCars = int(input("Enter the number of cars being insured: "))
        if NumCars < 1:
            print("ERROR: Number of cars must be at least 1.\n")
        else:
            print(f"Number of cars being insured: {NumCars}\n")
            break

    # Collect options for extra liability up to $1,000,000 (enter Y for Yes or N for No)
    while True:
        with open("Const.dat", "r") as f:
            for i in range(8):  # Skip the first 8 lines
                next(f)
            coverage_amount = f.readline().strip()
        
        ExtraLiability = input(f"Do you want extra liability coverage up to ${LIABILITY_COVERAGE_AMOUNT:.2f}? (Y/N): ").upper()
        if ExtraLiability not in ['Y', 'N']:
            print("ERROR: Please enter Y for Yes or N for No.\n")
        else:
            print(f"Extra liability coverage: {ExtraLiability}\n")
            break

    # Collect options for glass coverage (enter Y for Yes or N for No)
    while True:
        GlassCoverage = input("Do you want glass coverage? (Y/N): ").upper()
        if GlassCoverage not in ['Y', 'N']:
            print("ERROR: Please enter Y for Yes or N for No.\n")
        else:
            print(f"Glass coverage: {GlassCoverage}\n")
            break

    # Collect options for loaner car (enter Y for Yes or N for No)
    while True:
        LoanerCar = input("Do you want a loaner car? (Y/N): ").upper()
        if LoanerCar not in ['Y', 'N']:
            print("ERROR: Please enter Y for Yes or N for No.\n")
        else:
            print(f"Loaner car: {LoanerCar}\n")
            break

    # Collect payment option
    while True:
        payment_options = ["Full", "Monthly", "Down Pay"]
        PaymentOption = input("Enter payment option (Full/Monthly/Down Pay): ").title()
        if PaymentOption not in payment_options:
            print("ERROR: Please enter a valid payment option (Full, Monthly, or Down Pay).\n")
        else:
            print(f"Payment option: {PaymentOption}\n")
            break

    # If Down Pay is selected, collect down payment amount
    if PaymentOption == "Down Pay":
        while True:
            try:
                DownPayment = float(input("Enter the amount of down payment: $"))
                if DownPayment <= 0:
                    print("ERROR: Down payment must be greater than $0.\n")
                else:
                    print(f"Down payment amount: ${DownPayment:.2f}\n")
                    break
            except ValueError:
                print("ERROR: Please enter a valid numeric value for the down payment.\n")

    # Enter claim number
    while True:
        ClaimNumber = input("Please enter your claim number: ")
        if not ClaimNumber.strip():
            print("ERROR: Claim number must be entered before continuing.\n")
        elif not ClaimNumber.isdigit():
            print("ERROR: Claim number must contain only digits.\n")
        elif len(ClaimNumber) != 5:
            print("ERROR: Claim number must be 5 digits long.\n")
        else:
            print(f"Claim number: {ClaimNumber}\n")
            break

    # Enter claim date
    while True:
        ClaimDate = input("Please enter your claim date (YYYY/MM/DD): ")
        if not valid_date(ClaimDate):
            print("ERROR: Claim date must be in valid format.\n")
        else:
            print(f"Claim date: {ClaimDate}\n")
            break

    # Enter claim amount
    while True:
        ClaimAmount = float(input("Please enter your claim amount: $"))
        if ClaimAmount <= 0:
            print("ERROR: Claim amount must be greater than $0.\n")
        else:
            print(f"Claim amount: ${ClaimAmount:.2f}\n")
            break

    # Display thank you message
    print(f"Thank you!\n")

    # Generate and display user reference ID
    UserID = user_id_gen(CustFirst, CustLast, CustBirthDate)
    print(f"Your user reference ID is: {UserID}\n")

    TempIDLog = f"{UserID}.txt"
    with open(TempIDLog, 'a') as file:
        file.write(f"----------------------------------------\n")
        file.write(f"Claim No.: {ClaimNumber}\n")
        file.write(f"Claim Date: {ClaimDate}\n")
        file.write(f"Claim Amount: ${ClaimAmount:.2f}\n")


    #-----------------------#
    #      CALCULATIONS     #
    #-----------------------#
    # Calculate premium for all cars
    PremiumCost = (BASIC_PREMIUM + sum([BASIC_PREMIUM * ADD_CAR_DISCOUNT for i in range(NumCars - 1)]))

    # Calculate extra cost
    ExtraCost = 0
    if ExtraLiability == 'Y':
        ExtraCost += (EXTRA_LIABILITY_COST * NumCars)
    if GlassCoverage == 'Y':
        ExtraCost += (GLASS_COVERAGE_COST * NumCars)
    if LoanerCar == 'Y':
        ExtraCost += (LOANER_CAR_COST * NumCars)

    # Calculate total insurance premium
    TotalPremium = (PremiumCost + ExtraCost)

    # Calculate HST
    HST = (TotalPremium * HST_RATE)

    # Calculate total cost
    TotalCost = (TotalPremium + HST)

    # Calculate monthly payment
    if PaymentOption in ['Monthly', 'Down Pay']:
        if PaymentOption == 'Down Pay':
            TotalCost -= DownPayment
        MonthlyPayment = ((TotalCost + PROCESSING_FEE) / NUM_PAYMENTS)
    else:
        MonthlyPayment = 0

    # Calculate invoice date and first payment date
    InvoiceDate = (datetime.date.today())
    FirstPaymentDate = ((InvoiceDate.replace(day=1) + datetime.timedelta(days=32)).replace(day=1))


    #-----------------------#
    #     LOG GENERATION    #
    #-----------------------#
    # Append insurance details to the user's log file, add progress bar
    total_lines = 11 if MonthlyPayment > 0 else 10
    with open(TempIDLog, 'a') as file:
        
        progress_bar(0, total_lines)
        print(" Writing insurance details to log file...")
        file.write(f"\nInsurance Premium Details:\n")
        
        progress_bar(1, total_lines)
        print(" Writing basic premium...")
        file.write(f"Basic Premium: ${PremiumCost:.2f}\n")
        
        progress_bar(2, total_lines)
        print(" Writing extra costs...")
        file.write(f"Extra Costs: ${ExtraCost:.2f}\n")
        
        progress_bar(3, total_lines)
        print(" Writing total premium...")
        file.write(f"Total Premium: ${TotalPremium:.2f}\n")
        
        progress_bar(4, total_lines)
        print(" Writing HST...")
        file.write(f"HST ({HST_RATE*100}%): ${HST:.2f}\n")
        
        progress_bar(5, total_lines)
        print(" Writing total cost...")
        file.write(f"Total Cost: ${TotalCost:.2f}\n")
        
        progress_bar(6, total_lines)
        print(" Writing monthly payment...")
        if MonthlyPayment > 0:
            file.write(f"Monthly Payment: ${MonthlyPayment:.2f}\n")
        
        progress_bar(7, total_lines)
        print(" Writing invoice date...")
        file.write(f"Invoice Date: {InvoiceDate}\n")
        
        progress_bar(8, total_lines)
        print(" Writing first payment date...")
        file.write(f"First Payment Date: {FirstPaymentDate}\n")

    # Append payment details to the user's log file
        progress_bar(9, total_lines)
        print(" Writing payment details to log file...")
        file.write(f"\nPayment Details:\n")
        
        progress_bar(10, total_lines)
        print(" Writing payment option...")
        file.write(f"Payment Option: {PaymentOption}\n")
        
        if PaymentOption == 'Down Pay':
            progress_bar(10.5, total_lines)
            print(" Writing down payment amount...")
            file.write(f"Down Payment: ${DownPayment:.2f}\n")
        
        progress_bar(11, total_lines)
        print(" Writing monthly payment...")
        file.write(f"Monthly Payment: ${MonthlyPayment:.2f}\n")

        file.write(f"----------------------------------------\n")

        print(f"\nWriting to {TempIDLog} complete!!")
    
    #-----------------------#
    #          EXIT         #
    #-----------------------#
    while True:
        ExitChoice = input("\nDo you want to exit and generate a receipt or continue with another calculation? (Exit/Continue): ").upper()
        if ExitChoice in ['EXIT', 'CONTINUE']:
            break
        else:
            print("ERROR: Please type Exit or Continue.\n")

    if ExitChoice == 'EXIT':
        print("\nThank you for using our insurance calculator. Goodbye!\n")
        generate_receipt(UserID, CustFirst, CustLast)
        break
    else:
        print("\nStarting a new insurance calculation...\n")
        
        # +1 to next policy number and update Const.dat
        with open("Const.dat", "r") as f:
            lines = f.readlines()
        
        POLICY_NUM = int(lines[0].strip()) + 1
        lines[0] = f"{POLICY_NUM}\n"
        
        with open("Const.dat", "w") as f:
            f.writelines(lines)

        print(f"New policy number: {POLICY_NUM}\n")
