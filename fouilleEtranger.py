import re

minuscules = "[a-zàâäçéèêëîïôöùûüÿ]"
majuscules = "[A-ZÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸ]"
titres = "^Mme$|^M$|^Dre$|^Dr$"

occMeursault = []

etranger = open('etranger.txt', 'r', encoding="utf-8")
print(etranger.read())

for mot in etranger :
    if (re.search("Meursault", mot) != None) :
        occMeursault.append(re.search("Meursault", mot))

for occ in occMeursault : 
    print(occ, '\n') 
