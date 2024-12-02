DELIMITER = ','
def collectWords():
    words = []
    while True:
        feed = input('Insert word(empty stops): ')
        if feed == '':
            break
        else:
            words.append(feed)
    return DELIMITER.join(words)

def analyseWords(list1):
    words = 0
    lenth = 0
    for n in list1:
        words += 1
        lenth += len(n)
    Avg = lenth / words
    print(f'- {words} Words')
    print(f'- {lenth} Characters')
    print("- {:.2f} Average word length".format(Avg))
    return None

def main():
    print('Program starting.')
    words = collectWords()
    list2 = words.split(DELIMITER)
    analyseWords(list2)
    print('Program ending.\n')
    return None

main()
