#reverse
company_name = str('Spinomenal')
print(company_name[::-1])


#Assurance
role = 'Quality Assurance Specialist'
print(role[8:17])


#"SLOT MACHINE"
slot_code = "S1L0T9M2A4C6H8I3N7E"
print(slot_code[::2])


#middle characters
game_title = "Demi gods V"

length = len(game_title)

if length % 2 != 0:
    middle_index = length // 2
    middle_chars = game_title[middle_index]
else:
    middle_index = length // 2
    middle_chars = game_title[middle_index - 1:middle_index + 1]


print(middle_chars)


#
symbols = ["Cherry", "Bell", "Bar", "Seven", "Diamond", "Star"]
new_symbols = symbols[1:5]
print(new_symbols)


#
statement = "Yoga is fun"
seperated = statement.split()
reversed_word = [word[::-1] for word in seperated]
print (reversed_word)


#
symbols = ["Cherry", "Bell", "Bar", "Seven", "Diamond", "Star"]
k = 3

first = symbols[-k:]
new = first + symbols[:-k]

print(new)


#
slot = [["Cherry", "Bell", "Bar"], ["Diamond", "Seven", "Star"], ["Lemon", "Orange", "Plum"]]
newslot = slot[0][0], slot[1][1], slot[2][2]

print(newslot)

#
reel = [["Cherry", "Bell", "Bar"], ["Diamond", "Seven", "Star"], ["Lemon", "Orange", "Plum"]]
mirror = [list[::-1] for list in reel]
print(mirror)