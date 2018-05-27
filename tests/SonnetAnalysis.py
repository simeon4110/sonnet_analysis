import string

import nltk
from nltk.corpus import stopwords

from tests.connector import Connector


def remove_punctuation(value):
    result = ""
    for c in value:
        if c not in string.punctuation:
            result += c

    return result


def main():
    sonnets = Connector().get_all()
    stop_words = set(stopwords.words('english'))
    word_list = []

    print(stop_words)

    for x in range(0, len(sonnets)):
        for y in range(0, len(sonnets[x]['text'])):
            for z in (sonnets[x]['text'][y]).split():
                if z not in stop_words:
                    word_list.append(remove_punctuation(z))

    freq = nltk.FreqDist(word_list)
    freq.plot(50, cumulative=False)


main()
