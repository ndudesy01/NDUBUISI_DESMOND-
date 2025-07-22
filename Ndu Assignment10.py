#10. Write a program to assign work based on day of week using if-elif-else.

day = input("Enter the day of the week: ").strip().lower()

if day == "monday":
    print("Work: Team meeting and planning.")
elif day == "tuesday":
    print("Work: Development tasks.")
elif day == "wednesday":
    print("Work: Code review.")
elif day == "thursday":
    print("Work: Testing and debugging.")
elif day == "friday":
    print("Work: Documentation and deployment.")
elif day == "saturday":
    print("Work: recap of all activities for the week.")
elif day == "sunday":
    print("Work: Day off.")
else:
    print("Invalid day entered.")