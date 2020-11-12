from collections import defaultdict # można wymienić kilka po przecinku
from collections import OrderedDict
from collections import Counter

PUNCTUATIONS = {".", "?", "...", ":", "!", ",", "-", ";"}


def generate_words(path):
    with open(path, encoding='utf-8') as infile:
        for line in infile:
            line = line.strip()
            for punct in PUNCTUATIONS:
                line = line.replace(punct, " ")
            for word in line.split():
                yield word


def count_words_desc(path):
    output = defaultdict(int)
    words = generate_words(path)
    for word in words:
        output[word] += 1
    # output = dict(sorted(output.items(), key=lambda item: item[1], reverse=True))
    output = OrderedDict(sorted(output.items(), key=lambda item: item[1], reverse=True))
    return output


def count_digrams(path):
    return _count_n_grams(path, 2, 20)


def count_trigrams(path):
    return _count_n_grams(path, 3, 20)


def _count_n_grams(path, n, size):  # size to raczej parametr dla wypisywania niż zliczania
    words = list(generate_words(path))  # czy to trzeba wczytywać całe do pamięci?
    ngrams = list(zip(*[words[i:] for i in range(n)]))

    ngrams = Counter(ngrams)
    ngrams = OrderedDict(sorted(ngrams.items(), key=lambda item: item[1], reverse=True))

    for i in list(ngrams)[:20]: # dlaczego 20?
        yield i, ngrams[i]  # polecam nazwę key, jeśli iterujemy po słowniku
    ith_element = ngrams[list(ngrams)[size - 1]]

    for i in list(ngrams)[size:]:
        if ith_element == ngrams[i]:
            yield i, ngrams[i]
        else:
            break


# gen = generate_words("potop.txt")
# for line in gen:
#     print(line)
print(count_words_desc("potop.txt"))

digram = count_digrams("potop.txt")
print(list(digram))

trigram = count_trigrams("potop.txt")
print(list(trigram))
