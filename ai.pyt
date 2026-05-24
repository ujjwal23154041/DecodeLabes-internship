# Advanced Rule-Based AI Chatbot

import datetime

print("===================================")
print(" 🤖 Welcome to AI Chatbot ")
print("===================================")
print("Type 'exit' to stop the chatbot.\n")

while True:

    user = input("You: ").lower()

    # Greetings
    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user == "good morning":
        print("Bot: Good Morning! Have a great day.")

    elif user == "good evening":
        print("Bot: Good Evening!")

    # Asking chatbot name
    elif user == "what is your name":
        print("Bot: My name is RuleBot.")

    # Asking about chatbot
    elif user == "how are you":
        print("Bot: I am working perfectly!")

    # Date and Time
    elif user == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif user == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    # Simple Calculator
    elif user == "calculator":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("Choose operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == "1":
            print("Result =", num1 + num2)

        elif choice == "2":
            print("Result =", num1 - num2)

        elif choice == "3":
            print("Result =", num1 * num2)

        elif choice == "4":
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Bot: Cannot divide by zero.")

        else:
            print("Bot: Invalid choice.")

    # Motivation
    elif user == "motivate me":
        print("Bot: Believe in yourself. You can achieve anything!")

    # Help Command
    elif user == "help":
        print("Bot: Available commands are:")
        print("- hello")
        print("- how are you")
        print("- what is your name")
        print("- date")
        print("- time")
        print("- calculator")
        print("- motivate me")
        print("- exit")

    # Exit command
    elif user == "bye" or user == "exit":
        print("Bot: Goodbye! Chat ended.")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that command.")