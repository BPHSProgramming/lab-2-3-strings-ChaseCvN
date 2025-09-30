#Chase Ewing
#Period 8
#9/30/25



print("Task #1")
name = input("What is your first and last name\t")
namespace= name.find(" ")
first_name =  name[0:namespace]
last_name = name[namespace+1:]
print(first_name.title(),last_name.title())

fnamefirstletter = first_name[0].lower()
fnamerest = first_name[1:]
firstnamecaps = fnamefirstletter,fnamerest.upper()
print(firstnamecaps)

lnamefirstletter = last_name[0].lower()
lnamerest = last_name[1:]
lastnamecaps = lnamefirstletter,lnamerest.upper()
print(lastnamecaps)

print("Task #2")
phrase = ('''Once you start down the dark path, forever will it dominate your destiny.''')
phraseupper = phrase.upper()
phraseencrypted = phrase.replace("a", "1"),phrase.replace("e", "2"),phrase.replace("i", "3"),phrase.replace("o", "4"),phrase.replace("u", "5")
print(phrase)
print(phraseupper)
print(phraseencrypted)



