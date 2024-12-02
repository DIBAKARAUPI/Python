def frameWord(n):
    DELIMITER = '*'
    print(DELIMITER * (len(n) + 4))
    print(DELIMITER, n, DELIMITER)
    print(DELIMITER * (len(n) + 4))
    return None

def main():
    print("Program starting.")
    Pword = input("Insert word: ")
    print()
    frameWord(Pword)
    print()
    print("Program ending.")
    return None

main()
