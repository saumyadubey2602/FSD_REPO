temperature = float(input("Enter the temperature in °C: "))
if temperature < 15:
    print("given temperature is cold")
elif 15 <= temperature <= 25:
    print("given temperature is warm")
else:
    print("given temperature is hot")


