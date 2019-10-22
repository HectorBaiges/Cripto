"""f = open("D:/UNI/C/Practica1/2019_09_03_12_44_05_hector.baiges.Cifrado","r",encoding="utf8")

#f = open("D:/UNI/C/Practica1/prueva.txt","r",encoding="utf8")
#print(f.read())
frequencies = {} 
line = f.readline()
i = 1
while line:
    for char in line: 
        if char in frequencies: 
            frequencies[char] += 1
        else: 
            frequencies[char] = 1
    line = f.readline()

# Show Output
print(sorted(frequencies))
sorted_d = sorted((value, key) for (key,value) in frequencies.items())
for k,v in frequencies.items():
    print ("%s -> %s" %(k,v))
print("/////// SORTED /////// ")
print(*sorted_d, sep = "\n") 
f.close()"""

import sys
import codecs

#file = open(filename, "rt")
f = codecs.open("D:/UNI/C/Practica1/2019_09_03_12_44_05_hector.baiges.Cifrado","r",encoding="utf8")
f2 = codecs.open("D:/UNI/C/Practica1/des.Cifrado","w",encoding='utf-8')
contents = f.read()
print("hola")

print(contents ,"\n")
newcontents = contents.replace('ω','a')
newcontents = newcontents.replace('μ', 'n')
newcontents = newcontents.replace('γ', 'e')
newcontents = newcontents.replace('ε', 'g')
newcontents = newcontents.replace('κ', 'l')
newcontents = newcontents.replace('η', 'i')
newcontents = newcontents.replace('ρ', 's')
newcontents = newcontents.replace('ζ', 'h')
newcontents = newcontents.replace('λ', 'm')
newcontents = newcontents.replace('ν', 'o')
newcontents = newcontents.replace('ι', 'k')
newcontents = newcontents.replace('ς', 't')
newcontents = newcontents.replace('υ', 'w')
newcontents = newcontents.replace('π', 'r')
newcontents = newcontents.replace('β', 'd')
newcontents = newcontents.replace('ϊ', 'b')
newcontents = newcontents.replace('χ', 'y')
newcontents = newcontents.replace('ξ', 'p')
newcontents = newcontents.replace('θ', 'j')
newcontents = newcontents.replace('α', 'c')
newcontents = newcontents.replace('σ', 'u')
newcontents = newcontents.replace('δ', 'f')
newcontents = newcontents.replace('τ', 'v')
newcontents = newcontents.replace('φ', 'x')
newcontents = newcontents.replace('ο', 'q')
newcontents = newcontents.replace('ψ', 'z')

print(newcontents)
f2.write(newcontents) 

f.close()