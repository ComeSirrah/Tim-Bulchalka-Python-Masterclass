class Tag(object):
    def __init__(self, name, contents):
        self.start_tag = f'<{name}>'
        self.end_tag = f'</{name}>'
        self.contents = contents

    def __str__(self):
        return f"{self.start_tag}{self.contents}{self.end_tag}"

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/htlm4/strict.dtd', '')
        self.end_tag = ''   # DOCTYPE has no end tag


class Head(Tag):
    def __init__(self, title):
        super().__init__('head',  '')
        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)


class Body(Tag):
    def __init__(self):
        super().__init__('body', '')    # Body contents will be built separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    # my_page = HtmlDoc('Demo HTML Doc')
    # my_page.add_tag('h1', 'Heading')
    # my_page.add_tag('h2', 'Subheading')
    # my_page.add_tag('p', 'This is a paragraph')
    # with open('test.html', 'w') as test_doc:
    #     my_page.display(file=test_doc)

    new_body = Body()

    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', 'unlike <strong>composition</strong>, aggregation uses existing instances '
                          'of objects to build up other objects.')
    new_body.add_tag('p', "The composed object doesnt actually own the objects of which it is composed. "
                          "If it's destroyed those objects continue to exist.")

    new_DocType = DocType()
    new_header = Head('Aggregation document')
    my_page = HtmlDoc(new_DocType, new_header, new_body)

    with open('test3.html', 'w') as test_3:
        my_page.display(file=test_3)
