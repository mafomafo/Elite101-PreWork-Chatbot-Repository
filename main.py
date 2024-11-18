print("Welcome to ______ Chatbot! I am here to help you with your query.")
name = input("What is your name? ")


def user_info(dep_made):
    if not (dep_made):
        if input("Do you have $1000 dollars to make an initial deposit for the bank account:").lower() != "yes":
            print("Please be ready to deposit money next time.")
            return None
    print("All information is required.")
    age = int(input("How old are you? "))
    if age < 18:
        choice = input("Please consult a parent/legal guardian with the creation of this account.Enter information about the guardian, and reenter information about the child, ifyou'd like (y, n, stop).")
        if choice == "y":
            return minor_user_info(True, False)
        elif choice == "n":
            age = None
            return user_info(False)
        else:
            return None
    dob = input("What is your date of birth (DD/MM/YYYY): ")
    name = input(
        "What is your full name (First name, other names, last name)(Names must be separated by one space, special characters allowed)")
    ssn = input("What is your social security number? (xxx-xx-xxxx)")
    p_o_f = input(
        "Please provide proof of residency through a picture (Utility bill, lease agreement, etc)")
    address = input("What is your address?")
    p_n = input(
        "What is your phone number? (XX-XXX-XXX-XXX) Leave the international code blank if you live in the U.S")
    email = input("What is your email address?")
    return (age, dob, name, ssn, p_o_f, address, p_n, email)


def minor_user_info(dep_made, check):
    if not (dep_made):
        if input("Do you have $1000 dollars to make an initial deposit for the bank account:").lower() != "yes":
            print("Please be ready to deposit money next time.")
            return None
    print("You will enter the child's information here. If there is no information to be given, leave it blank. Some information is required, and will be stated.")
    age = int(input("How old are you? (Required)"))
    if age > 17 and check:
        print("You are registering for a bank account as a minor. You will be redirected to the account making process as an adult.")
        return user_info(False)
    dob = input("What is your date of birth (DD/MM/YYYY): (Required)")
    name = input("What is your full name (First name, other names, last name) (Names must be separated by one space, special characters allowed) (Required)")
    ssn = input("What is your social security number? (xxx-xx-xxxx) (Required)")
    p_o_r = input(
        "Please provide proof of relationship through a picture (Birth certificate, etc) (Required)")
    p_o_f = input(
        "Please provide proof of residency through a picture (Utility bill, lease agreement, etc) (Required)")
    address = input("What is your address? (Required)")
    p_n = input(
        "What is your phone number? (XX-XXX-XXX-XXX) Leave the international code blank if you live in the U.S")
    email = input("What is your email address?")
    enrollment = input(
        "Please provide a picture of a document that proves your child is enrolled in a school (School ID, Letter of Enrollment, etc) (Required)")
    print("All of the information that will be asked must be of the legal guardian of the minor.")
    return (age, dob, name, ssn, p_o_r, p_o_f, address, p_n, email, enrollment, "Adults info next", user_info(True))


temp = [{"name": "Savings Account",

         "Purpose": "Primarily for saving money and earning interest.",
         "Features": "Typically has limits on the number of withdrawals per month and may offer a modest interest rate.",
         "Availability for Minors": "Minors can often open savings accounts with a parent or guardian as a joint account holder or custodian."},
        {"name": "Checking Account",

         "Purpose": "Used for daily transactions like deposits, withdrawals, and payments.",
         "Features": "Includes features like debit cards, checks, and online banking. May or may not earn interest.",
         "Availability for Minors": "Many banks offer special checking accounts for minors, often called \"youth accounts\" or \"student accounts,\" that require a parent or guardian as a co-owner."},

        {"name": "Joint Account",

         "Purpose": "Shared by two or more individuals, providing both parties equal access to the funds.",
         "Features": "Both account holders can deposit and withdraw money.",
         "Availability for Minors": "Minors can be part of a joint account with a parent or guardian."},
        {"name": "Custodial Account",

         "Purpose": "Managed by a custodian (usually a parent) until the minor reaches the age of majority, at which point they gain full access.",
         "Features": "Can hold various assets, including cash, stocks, and bonds. It’s designed for saving money and investing for the child's future.",
         "Availability for Minors": "These accounts are set up for minors, but they cannot access the funds until they reach adulthood as defined by state law (usually 18 or 21)."}
        ]
while True:
    info = user_info(False)
    print(info)
    print("\n\nHere are the list of options for making a bank account")
    for ind, ele in enumerate(temp):
        if ele['name'] == "Custodial Account" and info[0] > 17:
            continue
        print(f"Option {ind + 1}: {ele['name']}")
        print(ele["Purpose"])
        print(ele["Features"])
        if info[0] < 18:
            print(ele["Availability for Minors"])
    print("E to exit.")
    ui_op = input(
        "What kind of bank account do you want?(Type in the number of the option you will choose.)")
    if ui_op == "E":
        print("bye bye")
        break
    else:
        print("Congratulations, your account has been made.")
        break
