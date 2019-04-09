import reprlib
import re

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))

    def __repr__(self):
        return 'Sentence:{}'.format(reprlib.repr(self.text))


if __name__ == '__main__':
    text = """You-Get is a tiny command-line utility to download media contents from the Web"""
    s = Sentence(text=text)
    # print(s.words)
    # for word in s:
    #     print(word)

    from collections.abc import Iterable

    print(issubclass(Sentence, Iterable))
    print(iter(s))  # 判断是否可迭代，以后不再用isinstance(s, Iterable)
