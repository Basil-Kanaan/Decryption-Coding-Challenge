import hashlib
import itertools

occurrences = {'p':1,
               'o':1,
               'u':2,
               'l':1,
               't':4,
               'r':1,
               'y':1,
               'w':1,
               'i':1,
               's':2,
               'a':1,
               'n':1,
               ' ':2}

def EliminateWords(file):
    data = [line.strip() for line in file.readlines()]
    print(data)
    data_o = []
    for index, word in enumerate(data):
        if all([True if letter in 'ailnoprstuwy ' else False for letter in word]):
            if all([True if word.count(letter) <= occurrences[letter]
                    else False
                    for letter in word]):
                data_o.append(word)
        print(index, word)

    print('# of Valid Words:', len(data_o))
    data_o = [word+'\n' for word in data_o]

    return data_o


def UnHash(file):
    words = [line.strip() for line in file.readlines()]
    print(words)
    for anagram in [" ".join(perm) for perm in itertools.permutations(words, 3) if
                    len(" ".join(perm)) == 20]:
        print("Checking: " + anagram)
        if hashlib.md5(anagram.encode('utf-8')).hexdigest() == 'e4820b45d2277f3844eac66c903e84be':
            print("WE GOT EM: " + anagram)
            quit()


with open('wordlist.txt', 'r+') as f:
    data = EliminateWords(f)

    with open('new_words.txt', 'r+') as f2:
        #for line in data:
        #    f2.write(line)
        #f2.seek(0)
        UnHash(f2)

