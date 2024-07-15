##DEFINING AUTHOR CHUNKS##


profile_size = 10000

#####TEXT PRE-PROCESSING#####################################################################
#All text files are opened for reading and then the
#a substring of length profile_size is taken for encoding
#the profile vector.


#Hornblower - C.S. Forester
forester = open(r"texts/forester.txt", "r", encoding="utf8")
forester = forester.read()
forester = forester.strip()
forester = forester[:profile_size]

#Collection of Shakespeare works
shakespeare = open(r"texts/shakespeare.txt", "r", encoding="utf8")
shakespeare = shakespeare.read()
shakespeare = shakespeare.strip()
shakespeare = shakespeare[:profile_size]

#Moby Dick - Herman Melville
melville = open(r"texts/melville.txt", "r", encoding="utf8")
melville = melville.read()
melville = melville.strip()
melville = melville[:profile_size]

#The Silmarillion - J.R.R Tolkien
tolkien = open(r"texts/tolkien.txt", "r", encoding="utf8")
tolkien = tolkien.read()
tolkien = tolkien.strip()
tolkien = tolkien[:profile_size]

#Maldoror - Comte de Lautreamont
lautreamont = open(r"texts/lautreamont.txt", "r", encoding="utf8")
lautreamont = lautreamont.read()
lautreamont = lautreamont.strip()
lautreamont = lautreamont[:profile_size]

#Alice in Wonderland - Lewis Caroll
caroll = open(r"texts/caroll.txt", "r", encoding="utf8")
caroll = caroll.read()
caroll = caroll.strip()
caroll = caroll[:profile_size]

