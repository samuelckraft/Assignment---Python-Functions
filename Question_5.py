#Task 1
import operator
activities = []

calories = []

time_spent = []

def daily_exercise():
    while True:
        print("Activity Tracker:")
        print("1. Add activity")
        print("2. Calculate total calories burned")
        print("3. See daily summary")
        print("4. Exit")
        choice = input("Choose your option: ")
        if choice == "1":
            activities.append(input("What activity did you do today? "))
            calories.append(int(input("How many calories does that burn per minute? ")))
            time_spent.append(int(input("How long did you do it for? ")))
        elif choice == "2":
            calories_burned = sum(list(map(operator.mul, calories, time_spent)))
            print(f"Calories burned: {calories_burned}")
        elif choice == "3":
            print("Daily Summary: ")
            print(f"Activities: {activities}")
            print(f"Calories burned: {calories_burned}")
        elif choice == "4":
            break
        else:
            print("Invalid answer please try again")
            

daily_exercise()