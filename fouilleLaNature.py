import re
import json
import tkinter

minuscules = "[a-zàâäçéèêëîïôöùûüÿ]"
majuscules = "[A-ZÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸ]"
titres = "Mme|M|Dre|Dr|Pr"
commenceParUneMaj = f"{majuscules}{minuscules}+"
nomPropre = titres + "\s" + commenceParUneMaj  


def moyHarmonique(p:list, r:list)->float:
    moyHarmonique = 0
    for precision, rappel in p, r : 
        p / r
    return 1 / moyHarmonique

def moyArithmetique(p:list, r:list)->float:
    return 1 / moyHarmonique(1/p, 1/r)

FN = 1
VN = 1
VP = 1
FP = 1
precision = VP / (VP + FP)
rappel = VP / (VP + FN)
precisions = []
rappels = []
# f_mesure = moyHarmonique(precisions, rappels)
# f_mesure = moyArithmetique(precisions, rappels)

extraitV1_JSON = 'extrait/v1/v1_ocr.json'
extraitV2_JSON = 'extrait/v2/v2_ocr.json'
extraitV3_JSON = 'extrait/v3/v3_ocr.json'
extraitV4_JSON = 'extrait/v4/v4_ocr.json'
extraitV5_JSON = 'extrait/v5/v5_ocr.json'

listeNoms = 'listeNoms.json'

def readJSONFile(file)->dict:
    with open(file, 'r') as f:
        extraitV1 = json.load(f)
    return extraitV1

def writeJSONFile(data, file)->None:
    with open(file, 'w') as f:
        json.dump(data, f)

def rechercheNomsPropres()->list[str]:
    occNomsPropre = []
    for entree in readJSONFile(extraitV1_JSON)["pages"]:
        search = re.search(nomPropre, entree[1][1])
        if (search != None):
            occNomsPropre.append(search)
    return occNomsPropre

def afficheNomsPropres(listeNP)->None:
    for entree in listeNP:
        print(str(entree) + "\n")

afficheNomsPropres(rechercheNomsPropres())