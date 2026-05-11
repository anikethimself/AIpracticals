def chatbot():
    print("🤖 Chatbot: Hello! Welcome to Customer Support.")
    print("Type 'exit' to end chat.\n")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("🤖 Chatbot: Thank you! Visit again")
            break

        elif "hello" in user or "hi" in user:
            print("🤖 Chatbot: Hello! How can I help you?")

        elif "order" in user:
            print("🤖 Chatbot: You can track your order in 'My Orders' section.")

        elif "payment" in user:
            print("🤖 Chatbot: We accept UPI, Credit Card, and Debit Card.")

        elif "refund" in user:
            print("🤖 Chatbot: Refund will be processed within 5-7 days.")

        elif "delivery" in user:
            print("🤖 Chatbot: Delivery usually takes 3-5 working days.")

        elif "cancel" in user:
            print("🤖 Chatbot: You can cancel your order before it is shipped.")

        else:
            print("🤖 Chatbot: Sorry, I didn't understand. Please try again.")


chatbot()