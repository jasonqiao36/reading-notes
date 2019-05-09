import html


def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


if __name__ == '__main__':
    print(htmlize(str))
