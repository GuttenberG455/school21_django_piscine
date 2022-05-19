
from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='html', attr=attr, content=content, tag_type='double')


class Head(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='head', attr=attr, content=content, tag_type='double')


class Body(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='body', attr=attr, content=content, tag_type='double')


class Title(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='title', attr=attr, content=content, tag_type='double')


class Meta(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='meta', attr=attr, content=content, tag_type='simple')


class Img(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='img', attr=attr, content=content, tag_type='simple')


class Table(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='table', attr=attr, content=content, tag_type='double')


class Th(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='th', attr=attr, content=content, tag_type='double')


class Tr(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='tr', attr=attr, content=content, tag_type='double')


class Td(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='td', attr=attr, content=content, tag_type='double')


class Ul(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='ul', attr=attr, content=content, tag_type='double')


class Ol(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='ol', attr=attr, content=content, tag_type='double')


class Li(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='li', attr=attr, content=content, tag_type='double')


class H1(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='h1', attr=attr, content=content, tag_type='double')


class H2(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='h2', attr=attr, content=content, tag_type='double')


class P(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='p', attr=attr, content=content, tag_type='double')


class Div(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(attr=attr, content=content, tag_type='double')


class Span(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='span', attr=attr, content=content, tag_type='double')


class Hr(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='hr', attr=attr, content=content, tag_type='double')


class Br(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='br', attr=attr, content=content, tag_type='double')


if __name__ == '__main__':
    html = Html([Head(Elem('title', content=Text('my title'))),
                Body([
                    H1(Text("h1 text")), H2(Text("h2 text")),
                    P(Text("par1")), P(Text("par2")),
                    Div(Text("div1")), Div(Text("div2")),
                    Span(Text("span1")), Span(Text("span2")),
                    Table([Tr([
                        Th(Text("Name")), Th(Text("Phone"))
                    ]), Tr([
                        Td(Text("Zhora")), Td(Text("IPhone"))
                    ])])])])
    f = open("new.html", "w")
    f.write(html.__str__())
    # print(html)
    f.close()
    print(Html([Head(), Body()]))
