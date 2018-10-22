def main():
    counter = 0
    sentence = input('Please enter a sentence: ')
    for ch in sentence:
        if ch == 't' or ch == 'T':
            counter += 1
    print(f'There are {counter} T\'s in your sentence')


main()

city = 'Providence'
counter = 0
while counter < len(city):
    print(city[counter])
    counter += 1
