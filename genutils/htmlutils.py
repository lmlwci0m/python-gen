

class StyleElement(object):
    """Single element style.

Usage: StyleElement("section").add("width", "400px").add("color", "black")
    """

    BASE_STYLE_ADD = "\t{0:s}: {1:s};"
    BASE_GENERATE = "{0:s} {{\n{1:s}\n}}"

    def __init__(self, selector="p"):
        self.selector = selector
        self.styles = []

    def add(self, style, value):
        self.styles.append(StyleElement.BASE_STYLE_ADD.format(style, value))
        return self

    def __generate(self):
        return StyleElement.BASE_GENERATE.format(self.selector, "\n".join(self.styles))

    def __str__(self):
        return self.__generate()

    def __unicode__(self):
        return unicode(__generate())


class StyleSheet(object):

    def __init__(self):
        self.styles = []

    def append(self, *elements):
        for x in elements:
            self.styles.append(x)
        return self

    def __generate(self):
        return "\n".join(map(str, self.styles))        

    def __str__(self):
        return self.__generate()

    def __unicode__(self):
        return unicode(self.__generate())

    def __add__(self, element):
        return StyleSheet.append(self.styles).append(element.styles)


class TableElement(object):

    BASE_TABLE = '\t\t<table>\n{0:s}\n\t\t</table>'

    BASE_ROW = "<tr>\n{0:s}\n</tr>"
    BASE_CELL = "<td>{0:s}</td>"
    BASE_HEADERCELL = "<th>{0:s}</th>"
    BASE_CAPTION = "<caption>{0:s}</caption>"

    BASE_TBODY = "<tbody>{0:s}</tbody>"
    BASE_THEAD = "<thead><tr>{0:s}</tr></thead>"

    def __init__(self):
        self.headers = []
        self.caption = []
        self.rows = []

    def set_caption(self, caption):
        if (len(self.caption) == 0):
            self.caption.append(TableElement.BASE_CAPTION.format(caption))
        else:
            self.caption[0] = caption

    def set_headers(self, *headers):
        
        thead = TableElement.BASE_THEAD.format("\n".join([
                    TableElement.BASE_HEADERCELL.format(x) for x in headers
                ]))

        if (len(self.headers) == 0):
            self.headers.append(thead)
        else:
            self.headers[0] = thead

    def add(self, *cols):
        self.rows.append(
            TableElement.BASE_ROW.format("\n".join([
                TableElement.BASE_CELL.format(x) for x in cols
            ]))
        )

    def __generate(self):
        return TableElement.BASE_TABLE.format(
            "{0:s}\n{1:s}\n{2:s}".format(
                "".join(self.caption), 
                "".join(self.headers), 
                TableElement.BASE_TBODY.format("\n".join(self.rows))
            )
        )

    def __str__(self):
        return self.__generate()        

    def __unicode__(self):
        return unicode(self.__generate())


class HtmlElement(object):

    BASE_APPEND = '{0:s}\n{1:s}'

    def __append(self, element):
        return HtmlElement.BASE_APPEND.format(self.element, element)

    def __init__(self, element):
        self.element = element

    def __add__(self, element):
        return HtmlElement(self.__append(element))

    def __str__(self):
        return self.element

    def __unicode__(self):
        return unicode(self.element)


class HtmlGenerator(object):
    
    BASE_HTML = '<!DOCTYPE html>\n<html lang="{0:s}">\n{1:s}\n</html>\n'
    BASE_HEAD = '\t<head>\n{0:s}\n\t</head>'

    BASE_META = '\t\t<meta charset="{0:s}" />'
    BASE_TITLE = '\t\t<title>{0:s}</title>'
    BASE_STYLE = '\t\t<style>\n{0:s}\n\t\t</style>'

    BASE_BODY = '\t<body>\n{0:s}\n\t</body>'

    BASE_PAR = '\t\t<p>\n{0:s}\n\t\t</p>'
    BASE_SECTION = '\t\t<section>\n{0:s}\n\t\t</section>'
    BASE_HEADER = '\t\t<h{0:s}>\n{1:s}\n\t\t</h{0:s}>'


    def __init__(self):
        pass

    def html_out(self, content="\t<head></head>\n\t<body></body>", language="en"):
        return HtmlElement(HtmlGenerator.BASE_HTML.format(language, content))

    def head_out(self, content="<title>Page</title>"):
        return HtmlElement(HtmlGenerator.BASE_HEAD.format(content))

    def meta_out(self, charset="utf-8"):
        return HtmlElement(HtmlGenerator.BASE_META.format(charset))

    def title_out(self, title="Page"):
        return HtmlElement(HtmlGenerator.BASE_TITLE.format(title))

    def style_out(self, style=""):
        return HtmlElement(HtmlGenerator.BASE_STYLE.format(style))

    def body_out(self, body="<h1>Body</h1>"):
        return HtmlElement(HtmlGenerator.BASE_BODY.format(body))

    def par_out(self, content=""):
        return HtmlElement(HtmlGenerator.BASE_PAR.format(content))

    def section_out(self, content=""):
        return HtmlElement(HtmlGenerator.BASE_SECTION.format(content))

    def header_out(self, content="Header", level="1"):
        return HtmlElement(HtmlGenerator.BASE_HEADER.format(level, content))

    


def generate_html_file(filename='index.html'):
    with open(filename, "w") as f:
        f.write("<!DOCTYPE html>\n")
        f.write('<html lang="en">\n')
        f.write("\t<head>\n")
        f.write('\t\t<meta charset="utf-8" />\n')
        f.write("\t\t<title></title>\n")
        f.write("\t</head>\n")
        f.write("\t<body>\n")
        f.write("\t</body>\n")
        f.write("</html>\n")


def html_log_file(log, filename='log.html'):

    with open(filename, "w") as f:
        f.write("<!DOCTYPE html>\n")
        f.write('<html lang="en">\n')
        f.write("\t<head>\n")
        f.write('\t\t<meta charset="utf-8" />\n')
        f.write("\t\t<title>History</title>\n")
        f.write("\t\t<style>\n")
        f.write("\t\t\tbody { font-family: arial; }\n")
        f.write("\t\t\tp span:first-child {  }\n")
        f.write("\t\t</style>")
        f.write("\t</head>\n")
        f.write("\t<body>\n")

        f.write("\t\t<h1>History Log</h1>")

        previous = ""

        for x, y in log:

            if previous != x:

                if previous != "":
                    f.write("\t\t</fieldset>\n")
                f.write("\t\t<fieldset>\n")
                f.write("\t\t\t<legend>{0:s}</legend>\n".format(x))
                

                f.write("\t\t\t<p>\n")
                f.write("\t\t\t\t<span>{0:s}</span>\n".format(y[1:-1]))
                f.write("\t\t\t</p>\n")

            else:

                f.write("\t\t\t<p>\n")
                f.write("\t\t\t\t<span>{0:s}</span>\n".format(y[1:-1]))
                f.write("\t\t\t</p>\n")

            previous = x

        else:
            f.write("\t\t</fieldset>\n")
                

        f.write("\t</body>\n")
        f.write("</html>\n")


