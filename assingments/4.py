def askDimension(i) -> float:
    PPrompt = float(input(f"Insert {i}: "))
    return PPrompt


def calcRectangleArea() -> float:
    Width = askDimension("width")
    Height = askDimension("height")
    Sum = Width * Height
    return Sum

def main():
    print("Program starting.")
    Area = calcRectangleArea()
    print()
    print(f"Area is {Area}²")
    print("Program ending.")
    return None

main()
