import html
from functools import singledispatch
import numbers
from collections import abc


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return f'<pre>{content}</pre>'


@htmlize.register(numbers.Integral)
def _(n):
    return f'<pre>{n} 0x{0:n}</pre>'


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


if __name__ == '__main__':
    print(htmlize([1, 2, 3]))
