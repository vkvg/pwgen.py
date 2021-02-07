# 30-09-2020 aloitettu salasanageneraattoriin, idea tuli xkcd:stä
# Ideana siis ottaa suomenkielisestä noin 94 000 sanan sanakirjasta valittu määrä sanoja
# Huomattavasti turvallisempi kuin 8-16 merkin salasanat, jos idea on pysyä muistissa

# Random on tarpeeksi hyvä moduuli tähän tarkoitukseen, salasanan idea ei ole olla satunnainen - otetaan myös mukaan os-moduuli wordlistin hakemista varten
import random, os

# Funktio getFilesInDir hankkii saatavilla olevat tiedostot suorituskansiosta
def getFilesInDir():
    return [f for f in os.listdir('.') if os.path.isfile(f) and f != __file__.split("/")[-1]]

# Kirjoitetaan funktio, joka valitsee parametrinä annetusta sanakirjalistasta valitun määrän verran sanoja; ts. salasanan
def createPassword(sequenceLength:int, wordlist:str):
    with open(wordlist, encoding="utf-8") as openedFile:
        availableWords = []
        for line in openedFile:
            availableWords.append(line.strip())
            
    
    # print(availableWords)
    randomSequence = ""

    for i in range(sequenceLength):
        randomSequence += f"{random.choice(availableWords)} "
    
    return str(randomSequence)

def askLength():
    while True:
        try:
            wordLength = int(input("Password length (words): "))
            return wordLength
        except TypeError:
            print("Error, try again")
def main():
    wordLength = askLength()
    filesInDirectory = getFilesInDir()

    if len(filesInDirectory) <= 0:
        print("\nNo wordlists found in script folder, try again")

    print("")

    for index, availableFile in enumerate(filesInDirectory):
        print(f"{index} {availableFile}")
    
    while True:
        try:
            selectedFile = int(input("\nSelect file index from list: "))
            break
        except:
            print("Error, try again")

    while True:
        print("\nGenerated passwords:\n")
        
        for i in range(10):
            print(createPassword(wordLength, filesInDirectory[selectedFile]))

        if input("\nRoll again (Y/N)?: ") == "N":
            break

if __name__ == "__main__":
    main()