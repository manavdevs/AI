# Greeting
print("Hello! I am AI Bot.")
name = input("What is your name? ")

print(f"Nice to meet you, {name}!")

# Loop to continue chatting
while True:

    # Ask mood
    mood = input("How are you feeling today? (good/bad/okay): ").lower()

    if mood == "good":
        print("That's great to hear!")

        hobby = input("What is your favorite hobby? ")
        print(f"{hobby} sounds really fun!")

    elif mood == "bad":
        print("I'm sorry to hear that.")

        activity = input("What do you usually do to relax? ")
        print(f"{activity} might help you feel better!")

    else:
        print("Sometimes it's hard to describe feelings.")

    # Continue chatting?
    cont = input("Do you want to continue chatting? (yes/no): ").lower()

    if cont != "yes":
        break

# Farewell
print(f"It was nice chatting with you, {name}. Goodbye!")