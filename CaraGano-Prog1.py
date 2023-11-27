#Cara Gano
#CIT 257 Program 1

temperature = int(input("Please enter a temperature value to convert: "))

degConvert = input("To convert to either Fahrenheit or Celsius enter either F or C: ")

if degConvert == 'f' or degConvert == 'F':
    degC = round(1.8 * temperature + 32, 1)

    print(str(temperature) + " degrees C" + " = " + str(degC) + " degrees F")

elif degConvert == 'c' or degConvert == 'C':
    degF = round((temperature - 32) / 1.8, 1)

    print(str(temperature) + " degrees F" + " = " + str(degF) + " degrees C")

else:
    print("Please enter either C, c, F or f. Goodbye.")
    quit()
        
