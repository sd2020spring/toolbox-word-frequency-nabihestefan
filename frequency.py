"""Analyze the word frequencies in a book downloaded from Project Gutenberg."""

import string


def getWordList(filename):
    """Read the specified project Gutenberg book.

    Header comments, punctuation, and whitespace are stripped away. The function
    returns a list of the words used in the book as a list. All words are
    converted to lower case.
    """
    temp = ""
    i = 0
    file = open(filename)
    words = []
    for line in file:
        line.strip()
        l = len(line)
        i = 0
        while i < l:
            if line[i] in string.punctuation or line[i] in string.whitespace:
                if(temp != ""):
                    words.append(temp)
                    temp = ""
            else:
                temp += line[i].lower()
            i+=1

    return(words)


def getTopNWords(words, n):
    """Take a list of words as input and return a list of the n most
    frequently-occurring words ordered from most- to least-frequent.

    Parameters
    ----------
    word_list: [str]
        A list of words. These are assumed to all be in lower case, with no
        punctuation.
    n: int
        The number of words to return.

    Returns
    -------
    int
        The n most frequently occurring words ordered from most to least.
    frequently to least frequentlyoccurring
    """
    d = dict()
    for word in words:
        d[word] = d.get(word, 0) + 1
    s = sorted(d.items(), key=lambda x: x[1], reverse=True)
    top = []
    for i in range(n):
        t = s[i]
        top.append(t[0])
    return(top)



if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation)
    print("Inferno")
    print(getTopNWords(getWordList("Inferno"), 10))
    print()
    print("Candide")
    print(getTopNWords(getWordList("Candide"), 10))
    print()
    print("CompleteShakespeare")
    print(getTopNWords(getWordList("CompleteShakespeare"), 10))
