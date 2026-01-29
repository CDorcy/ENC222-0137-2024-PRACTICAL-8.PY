import math

class Square:
    def __init__(self, length):
        self._side = length
        print(f"Square Constructor called for side length {self._side}")

    def __del__(self):
        print(f"Square Destructor called for side length {self._side}")

    def get_peri(self):
        return 4 * self._side

    def get_area(self):
        return self._side * self._side

class Cube(Square):
    def __init__(self, length):
        super().__init__(length)
        print(f"Cube Constructor called for side length {self._side}")

    def __del__(self):
        print(f"Cube Destructor called for side length {self._side}")
        # The base class destructor will be automatically called by Python's garbage collection

    def get_area(self):
        # Overrides the Square's get_area to calculate surface area (6 * side^2)
        return 6 * self._side * self._side

    def get_volume(self):
        return math.pow(self._side, 3)

if __name__ == "__main__":
    length = 5.0

    print("--- Creating a Square object ---")
    my_square = Square(length)
    print(f"Square Side Length: {length}")
    print(f"Square Perimeter: {my_square.get_peri()}")
    print(f"Square Area: {my_square.get_area()}")

    print("\n--- Creating a Cube object ---")
    my_cube = Cube(length)
    
    print(f"Cube Side Length: {length}")
    print(f"Cube Base Perimeter (inherited): {my_cube.get_peri()}") 
    print(f"Cube Surface Area (Overridden): {my_cube.get_area()}") 
    print(f"Cube Volume: {my_cube.get_volume()}")

    print("\n--- Program End (Destructors called automatically) ---")

