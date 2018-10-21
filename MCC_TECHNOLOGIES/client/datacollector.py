import random

# generate key
stKey =""
i=0
Uidkey= {}
while i <10:

    Uidkey[i] = random.randint(0,10)

    stKey= stKey + str(Uidkey.get(i))
    i= i+1
print( Uidkey)
print (stKey)
#generate the string

#generate Air HUmidity
i=0
AirH = {}
airst = ""
while i <3:

    AirH[i] = random.randint(0,10)
    airst= airst+ str(AirH.get(i))
    i= i+1
print( AirH)

#open file
f = open("bufferfile.txt","w+")
f.write(stKey+"\n")
f.close()
f= open ("bufferfile.txt","a+")
f.write(airst+"\n")
f.write(airst+"\n")
f.close()
