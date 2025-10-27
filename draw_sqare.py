# draw_square.py

# Author: Joel Villemaire

# Date: October

# Function to draw a square of any given size

def draw_square(size):
    """

    Draw a square shape in the terminal using the given size.
    :param size: Integer that represents the width and height of the square.
    """

    # Ensure you provide a valid size
    if size < 0:
        print("Please enter a number greater than zero.")
        return

    # Loop to print each row of the square
    for i in range(size):
        print("* " * size)

    # test
if __name__ == "__main__":
      draw_square(7)