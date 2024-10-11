import xml.sax

class PeopleHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current = ""
        self.name = ""
        self.age = ""
        self.weight = ""
        self.height = ""
        self.content = ""

    def startElement(self, name, attrs):
        self.current = name
        if name == "person":
            print(f"-- Person {attrs["id"]} --")

            self.name = ""
            self.age = ""
            self.weight = ""
            self.height = ""



    def character(self, content):
        self.name += content.strip()


    def endElement(self, name):
        if name == "name":
            self.name = self.content
            print(f"Name: {self.name}")
        elif name == "age":
            self.age = self.content
            print(f"Age: {self.age}")
        elif name == "weight":
            self.weight = self.content
            print(f"Weight: {self.weight}")
        elif name == "height":
            self.height = self.content
            print(f"Height: {self.height}")

        self.content = ""


handler = PeopleHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)

with open("people.xml", "r") as file:
    parser.parse(file)
