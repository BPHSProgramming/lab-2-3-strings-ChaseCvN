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
firstnamecaps = fnamefirstletter+fnamerest.upper()
print(firstnamecaps)

lnamefirstletter = last_name[0].lower()
lnamerest = last_name[1:]
lastnamecaps = lnamefirstletter+lnamerest.upper()
print(lastnamecaps)

print("")

print("Task #2")
phrase = ('''Once you start down the dark path, forever will it dominate your destiny.''')
phraseupper = phrase.upper()
phraseencrypted = phraseupper.replace("A", "1")\
                        .replace("E", "2")\
                        .replace("I", "3")\
                        .replace("O", "4")\
                        .replace("U", "5")
                            
print(phraseencrypted)

print("")

print("Task #3")
phraselength = phrase.len()/3
phrasestart = phrase[0:phraselength]
phrasemiddle = phrase[phraselength:phraselength*2]
phraseend =  phrase[phraselength*2:phraselength*3]

print(phrasemiddle)
print(phasestart)
print(phraseend)

print("")

print("Task #4")





