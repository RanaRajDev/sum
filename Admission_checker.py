def details():
    print("Congratulations, you are eligible for admission.")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    game = input("Enter your game: ")
    contact = input("Enter your contact number: ")

    print(f"Congratulations Mr./Ms. {name}, you are admitted.\nYour details are:\nName: {name}\nAge: {age}\nGame: {game} \nContact: {contact}")

marks = float(input("Enter your marks percentage: "))

if marks >= 90:
    details()
elif marks >= 80:
    if input("Are you OBC? (yes/no): ").lower() == 'yes':
        details()
    elif input("Are you SC/ST? (yes/no): ").lower() == 'yes':
        details()
    elif input("Are you EWS? (yes/no): ").lower() == 'yes':
        details()
    else:
        if input("Are you a sportsman? (yes/no): ").lower() == 'yes':
            details()
        else:
            print("Not admitted.")
elif marks >= 70:
    if input("Are you SC/ST? (yes/no): ").lower() == 'yes':
        details()
    elif input("Are you EWS? (yes/no): ").lower() == 'yes':
        details()
    else:
        if input("Are you a sportsman? (yes/no): ").lower() == 'yes':
            details()
        else:
            print("Not admitted.")
elif marks >= 60:
    if input("Are you EWS? (yes/no): ").lower() == 'yes':
        details()
    else:
        if input("Are you a sportsman? (yes/no): ").lower() == 'yes':
            details()
        else:
            print("Not admitted.")
elif marks >= 50:
    if input("Are you a sportsman? (yes/no): ").lower() == 'yes':
        details()
    else:
        print("Not admitted.")
else:
    print("Not admitted.")