import reprlib
import re

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)
        # return iter('ok')

    def __repr__(self):
        return 'Sentence:{}'.format(reprlib.repr(self.text))


class SentenceIterator:
    """
    注意，这种实现比较麻烦，不好！
    """
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == '__main__':
    text = """You-Get is a utility"""
    s = Sentence(text=text)
    si = SentenceIterator('hah')
    for i in si:
        print(i)

    from collections.abc import Iterable, Iterator

    print(issubclass(SentenceIterator, Iterator))
    print(isinstance(SentenceIterator(''), Iterator))  # 判断是否可迭代，以后不再用isinstance(s, Iterable)
