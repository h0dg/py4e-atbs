import xml.etree.cElementTree as ET # think of as = alias

data = '''<person> 
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''
# ''' syntax is all one string. \n are included

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))