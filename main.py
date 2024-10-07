print("Welcome to ______ Chatbot! I am here to help you with your query.")
name = input("What is your name? ")
def user_info():
    try:
        age = int(input("How old are you? "))
        dob = input("What is your date of birth (DD/MM/YYYY): ")
        name = input("What is your full name (First name, other names, last name) \
        (Names must be separated by one space, special characters allowed)")
    except ValueError:
        print("Please enter a valid number.")
        continue
    return (age, dob, name)
while True:
    user_info()
    if age < 18:
        print("Please consult a parent/legal guardian with the creation of this account.\
        Enter information about the guardian, and reenter information about the child, if\
        you'd like (y, n).")
        if input(": ") == "y":
            continue
        user_info()
    print("\n\nHere are the list of options for making a bank account")
    for i in range(1, 11):
        print(f"Option {i}:")
    print("E to exit.")
    ui_op = input(
        "What kind of bank account do you want?(Type in the number of the option you will choose.)")
    if ui_op == "E":
        print("bye bye")
        break
