#Dont run this file. It is supposed to remove few erranious character words.
#Will overwrite words.txt if run and might cause the program to misbehave
words = []
removable = "!:)(\",?"
with open('words.txt','r') as f:
    for line in f:
        for word in line.split():
            words.append(word.translate({ord(i): None for i in removable}))

write_file = "words.txt"

f = open(write_file, 'w')

for word in words:
    f.write(word+"\n")

f.close()
