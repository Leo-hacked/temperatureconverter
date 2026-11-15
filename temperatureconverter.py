#Leo Esparza
#Professor:Giles
#CIT-104-A.26AU
#Nov.15 2026
#Assignment chapter 9 Temperature Converter

# Imports EasyFrame from BreezyPythonGUI
from breezypythongui import EasyFrame

# Create the application class
class TemperatureConverter(EasyFrame):

    # Create the window and its components
    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")

        # Row 1: creates labels for Fahrenheit and Celsius
        self.addLabel("Fahrenheit", 0, 0)
        self.addLabel("Celsius", 0, 1)

        # Row 2: creates entry fields with starting values for Fahrenheit and Celsius
        self.fahrenheit = self.addFloatField(32.0, 1, 0)
        self.celsius = self.addFloatField(0.0, 1, 1)

        # Row 3 creates the buttons to convert between Fahrenheit and Celsius and assigns the conversion methods to the buttons
        self.addButton(text=">>>>", 
                       row=2, column=0,
                       command=self.convertToCelsius)

        self.addButton(text="<<<<", 
                       row=2, column=1,
                       command=self.convertToFahrenheit)

    # Convert Fahrenheit to Celsius
    def convertToCelsius(self):
        self.celsius.setNumber((self.fahrenheit.getNumber() - 32) * 5 / 9)

    # Convert Celsius to Fahrenheit
    def convertToFahrenheit(self):
        self.fahrenheit.setNumber(self.celsius.getNumber() * 9 / 5 + 32)

# Starts the application
def main():
    TemperatureConverter().mainloop()

# Calls the main function
if __name__ == "__main__":
    main()
