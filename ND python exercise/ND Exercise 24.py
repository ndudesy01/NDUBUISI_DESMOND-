#24> Take input temperature in Celsius and check if it9s hot (>35), warm (25335), or cold (<25).
temp = float(input("Enter temperature in Celsius: "))

if temp > 35:
    print("It's hot.")
elif 25 <= temp <= 35:
    print("It's warm.")
else:
    print("It's cold.")
