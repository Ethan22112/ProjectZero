# list exploration / experiment

fruit_list = {'apple', 'banana', 'cherry', 'dragonfruit'}

for item in fruit_list:

    print()

    #print the whole word
    print(f'Fruit Name: {item}')

    #print the first letter
    print(f'First Letter Of Fruit Name: {item[0]}')

    #print the first TWO letters
    print(f'First two letters of the Fruit are {item[:2]}')