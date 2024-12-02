def menu(word: str) -> list:
    print('''Options:
1 - Insert word
2 - Show current word
3 - Show current word in reverse
0 - Exit''')
    choice = input('Your choice: ')
    if choice == '1':
        word = input('Insert word: ')
    elif choice == '2':
        print(f'Current word - \"{word}\"')
    elif choice == '3':
        print(f'Word reversed - \"{word[::-1]}\"')
    elif choice == '0':
        print('Exiting program.')
    else:
        print('Unknown option! try again.')
    return [word, choice]

def main():
    word = ''
    print('Program starting.')
    while True:
        i = menu(word)
        word = i[0]
        choice = i[1]
        if choice == '0':
            break
        print()
    print('\nProgram ending.')
    return None

main()
