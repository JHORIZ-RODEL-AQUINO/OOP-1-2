def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32

        def Fahrenheit_to_Celsius(self):  # reversed process
            return (self.conversion() - 32) * 5 / 9

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

        def Kelvin_to_Celsius(self):  # reversed process
            return self.conversion() - 273.15

    tempInCelsius = float(input("Enter the temperature in Celsius: "))
    convert1 = CelsiusToKelvin(tempInCelsius)
    print(str(convert1.conversion()) + " Kelvin")
    convert2 = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert2.conversion()) + " Fahrenheit")

    print(f"\n{convert1.conversion()} = {convert1.Kelvin_to_Celsius()} Celsius")
    print(f"\n{convert2.conversion()} = {convert2.Fahrenheit_to_Celsius()} Celsius")


main()
