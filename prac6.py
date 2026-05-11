def expert_system():
    print(" Medical Expert System")
    print("Answer the following questions with yes/no\n")

    fever = input("Do you have fever? ").lower()
    cough = input("Do you have cough? ").lower()
    headache = input("Do you have headache? ").lower()
    stomach = input("Do you have stomach pain? ").lower()

    print("\n Diagnosis Result:")

    if fever == "yes" and cough == "yes":
        print("You may have Flu or Viral Infection.")
        print("Advice: Take rest and consult a doctor.")

    elif fever == "yes" and headache == "yes":
        print("You may have Migraine or Fever-related issue.")
        print("Advice: Drink water and take proper rest.")

    elif stomach == "yes":
        print("You may have Gastric problem.")
        print("Advice: Avoid spicy food and consult doctor if pain continues.")

    else:
        print("No serious symptoms detected.")
        print("Advice: Maintain healthy lifestyle.")


expert_system()