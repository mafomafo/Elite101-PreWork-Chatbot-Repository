print("Welcome to ______ Chatbot! I am here to help you with your query.")
name = input("What is your name? ")
while True:
  try:
    age = int(input("How old are you?"))
  except ValueError:
    print("Please enter a valid number.")
    continue
  print("\n\n")
  for i in range(1,11):
    print(f"Option {i}:")
  print("E to exit.")
  ui_op = input("What is your query?(Type in the number of the option you will choose.)")
  if ui_op == "E":
    print("bye bye")
    break
