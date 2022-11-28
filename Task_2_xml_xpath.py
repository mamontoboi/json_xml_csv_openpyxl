# Створіть XML-файл із вкладеними елементами та скористайтеся мовою пошуку XPATH.
# Спробуйте здійснити пошук вмісту за створеним документом XML,
# ускладнюючи свої запити та додаючи нові елементи, якщо буде потрібно.

from xml.etree import ElementTree as ET
from random import randint

tree = ET.parse('reed2.xml')
root = tree.getroot()  # root is iterable. tree is not

# access by index (course - 0, element - 4)
print(root[0][4].text)

# findall returns the list of objects (not value)
crses = tree.findall('.//title')
days = tree.findall('course/days')
at_start = tree.findall('.//start_time')  # or
# at_start = tree.findall('course/time/start_time')
till_end = tree.findall('course/time/end_time')

for crses, days, start, end in zip(crses, days, at_start, till_end):
    print(f'The class "{crses.text}" is scheduled on {days.text} from {start.text} till {end.text}.')

# to get value of attribute
start = root.get('start')
print(f'The curriculum of Reed is {start}')

# to set attr to every course in the root
for course in root:
    ttl = course.find('title')
    ttl.set('descr', f'interesting in scale fm 1 to 5: {randint(1, 5)}')
    # to set attr to 'building' in every course
    building = course.find('.//building')
    building.set('condition', f'{randint(1, 5)}')

# to add attribute to every crse in every course
for course in tree.findall('course'):
    crs = course.find('crse')
    crs.set('id', 'number')

# to find an attribute 'description' in tag 'title'
for course in root:
    ttl = course.find('title').text
    description = course.get('descr')
    if description is not None:
        print(f'{ttl} description says that this is {description}')

# to find an attribute "building condition"
for course in root:
    ttl = course.find('title').text
    blt = course.find('.//building')  # or:
    # blt = course.find('place/building')
    cond = blt.get('condition')
    if cond:
        print(f"{ttl} classes building condition is {cond}")

# to obtain dictionary of tag's attribute
for course in root:
    attr = course.attrib
    if len(attr) > 0:
        print(attr)
    # to find attribute of 'building'
    building_cond = course.find('place/building')
    if len(building_cond.attrib) > 0:
        print(building_cond.attrib)

# to add attribute to every course
cnt = 1
for course in tree.findall('course'):
    course.set('num', str(cnt))
    cnt += 1
    # updates <course> to <course num="1">

# to delete an attribute from every course
for course in tree.findall('course'):
    del(course.attrib['num'])
    # returns to <course>


# another way to numerate every course in the root
for num, course in enumerate(tree.findall('course')):
    course.set('id', str(num))

# to find id='4'
id_4 = root.find("course[@id='4']")
print(id_4.attrib)

# to change element:
for course in root.findall('course/instructor'):
    course.tag = 'teacher'
    course.text = 'David Attenborough'

# to get all id attributes in element 'course'
lst_of_all_atters = root.findall('.//course[@id]')
for item in lst_of_all_atters:
    print(item.attrib)

# creation of new element
# teacher = ET.fromstring("<teacher>Dr.Chuck</teacher>\n")
# # or
# passing_grade = ET.Element("passing_grade")
# passing_grade.text = '75'  # all info bound for file.xml must be str

# to add an element to the file
# for course in root:
    # course.insert(6, teacher)
    # course.append(passing_grade)

# write needs to be made to save changes in the file (or to save to another file)
tree.write('reed.xml')
