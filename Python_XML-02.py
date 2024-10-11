import xml.dom.minidom

domtree = xml.dom.minidom.parse("people.xml")
group = domtree.documentElement
people = group.getElementsByTagName("person")

for person in people:
    print(f"--Person {person.getAttribute("id")} --")

    name = person.getElementsByTagName("name")[0].childNodes[0].nodeValue
    age = person.getElementsByTagName("age")[0].childNodes[0].nodeValue
    weight = person.getElementsByTagName("weight")[0].childNodes[0].nodeValue
    height = person.getElementsByTagName("height")[0].childNodes[0].nodeValue


    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Weight: {weight}")
    print(f"Height: {height}")

people[0].getElementsByTagName("name")[0].childNodes[0].nodeValue = "Robert Greene"
people[0].setAttribute("id", "200")
people[0].setAttribute("newattr", "Hello")

domtree.writexml(open("people.xml", "w"))
