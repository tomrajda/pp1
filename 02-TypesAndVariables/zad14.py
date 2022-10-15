# Conversion Celsius unit to Kelvin and Fahrenheit
msg_1 = "Celsius to Kelvin and Fahrenheit conversion"
msg_2 = "Type temperature in Celsius degree: "
print(msg_1)

# Input data
celsiusTemp = int(input(msg_2))

# Calculation
kelvinTemp = celsiusTemp + 273.15
fahrenheitTemp = celsiusTemp * 1.8 + 32

# Output data
print(f"Kelvin temperature: {round(kelvinTemp, 1)} °K\n"
    f"Fahrenheit temperature: {round(fahrenheitTemp, 1)} °F")




