class AdvancedCalculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        result = x + y
        self.history.append(f"Added {x} and {y}: {result}")
        return result

    def subtract(self, x, y):
        result = x - y
        self.history.append(f"Subtracted {y} from {x}: {result}")
        return result

    def multiply(self, x, y):
        result = x * y
        self.history.append(f"Multiplied {x} and {y}: {result}")
        return result

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        result = x / y
        self.history.append(f"Divided {x} by {y}: {result}")
        return result

    def convert_units(self, value, from_unit, to_unit):
        conversion_factors = {
            'meters_to_feet': value * 3.28084,
            'feet_to_meters': value / 3.28084,
            'liters_to_gallons': value * 0.264172,
            'gallons_to_liters': value / 0.264172,
        }
        return conversion_factors[f'{from_unit}_to_{to_unit}']

    def get_history(self):
        return self.history

    def scientific_function(self, function, *args):
        import math
        if function == 'sin':
            return math.sin(*args)
        elif function == 'cos':
            return math.cos(*args)
        elif function == 'tan':
            return math.tan(*args)
        else:
            raise ValueError(f"Function {function} not supported")

# Example usage:
if __name__ == '__main__':
    calculator = AdvancedCalculator()
    print(calculator.add(5, 3))  # Output: 8
    print(calculator.convert_units(1, 'meters', 'feet'))  # Output: 3.28084
    print(calculator.scientific_function('sin', math.pi / 2))  # Output: 1.0
    print(calculator.get_history())  # Output: Calculation history
