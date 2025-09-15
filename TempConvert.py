#TempConvert.py
#Name:
#Date:
#Assignment:
print("Temperature Converter")
print("Adam McLaughlin \t Fall 2025 \t Lab3")
print("")

def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = float(input("Enter Temperature in Fahrenheit to Convert to Celcius: "))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = round((tempF - 32) * 5 / 9, 1)
  #Output converted temperature.
  print(f"{tempF}°F is {tempC}°C.")



if __name__ == '__main__':
  main()
