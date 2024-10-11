# XML (eXtensible Markup Language) Basic

import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
    +1 7343034456
    </phone>
    <email hide="yes" />
   </person>'''

tree = ET.fromstring(data)

name = tree.find("name").text
phone = tree. find("phone").text
email_hide = tree.find("email").get("hide")


print("Name:", name)
print("Phone:", phone)
print("Email hidden:", email_hide)
