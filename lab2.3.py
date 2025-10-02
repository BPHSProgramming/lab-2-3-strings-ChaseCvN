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
phraselength = int(len(phrase)/3)
phrasestart = phrase[0:phraselength]
phrasemiddle = phrase[phraselength:phraselength*2]
phraseend =  phrase[phraselength*2:phraselength*3]

print(phrasemiddle)
print(phrasestart)
print(phraseend)

print("")

print("Task #4")
number = input("Please input a 5 digit number\t")
number1 = int(number[0])
number2 = int(number[1])
number3 = int(number[2])
number4 = int(number[3])
number5 = int(number[4])
finalnum = number1+number2+number3+number4+number5
print(number1,"+",number2,"+",number3,"+",number4,"+",number5,"=",finalnum)


print("Task #5")

print("")

newphrase = "Why, you stuck-up half-witted scruffy-looking nerf herder"

#everyother = 
#everyotherbackwards = 


print("Task #6")

print("")

from datetime import date


today = date.today()

today = today.strftime("%Y,%B,%d")


print(f"The date today is {today}")

month = today[5:len(today)-3]
day = today[len(today)-2:]
year = today[0:4]
print("This is day",day,"of,",month,"of the year",year )