def showOptions():
    print('''Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit''')
    return None

def askChoice():
    Choice = input('Your choice: ')
    if Choice.isnumeric():
        return int(Choice)
    else:
        print('Unknown option!\n')
        return 10

def main():
    print('Program starting.')
    count = 0
    while True:
        showOptions()
        choice = askChoice()
        if choice == 1:
            print(f'Current count - {count}\n')
        elif choice == 2:
            count += 1
            print('Count increased!\n')
        elif choice == 3:
            count = 0
            print('Cleared count!\n')
        elif choice == 0:
            print('Exiting program.\n')
            break
        elif choice == 10:
            continue
        else:
            print('Unknown option!\n')
    print('Program ending.\n')
    return None

main()
