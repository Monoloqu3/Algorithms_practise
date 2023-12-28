def vowels(string):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    test = []
    for letter in list(string.lower()):
        if letter in vowels_list:
            test.append(letter)
    return len(test)

if __name__ == '__main__':
    vowels('Why do you ask?')
