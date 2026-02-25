# spell1.py
def read_word_list():
    wordList = []
    with open('scalable.txt', 'r') as f:
        for line in f:
            word = line.strip()
            wordList.append(word)
    return wordList
