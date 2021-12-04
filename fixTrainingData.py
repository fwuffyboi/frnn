# credit to JolteonYellow on GitHub for making this file! thanks dude!! :)
# run this on replit it no work on windows ;-;

import re
import os

trainingDataFile = open("rawTrainingData.txt", "r")


def removeAllLine():
    print("Deleting empty lines...")
    with open('rawTrainingData.txt', "r") as inputFile, open("./SFC_EL.txt", "w") as outputFile:
        for line in inputFile:
            if line.strip():
                outputFile.write(line)

            elif line == "Tweets did not appear!":
                return False

    print("Done!")


def checkEachLine():
    print("Deleting extra characters...")
    with open('./SFC_EL.txt') as inputFile, open("./SFC_EC.txt", "w") as outputFile:
        for line in inputFile:
            testText = re.search('^[a-zA-Z0-9?><;,{}[\]\-_+=!@#$%\^&*|\'\". ]*$', line)
            if testText:
                outputFile.write(line)

    print("Done!")


def dontPing():  # XD
    print("Deleting @'s...")
    with open('./SFC_EC.txt') as inputFile, open("rawTrainingData.txt", "w") as outputFile:
        for line in inputFile:
            replaceAts = line.replace('@', '@/')
            outputFile.write(replaceAts)

    print("Done!")


def removeTempFiles():
    print("Removing temporary files..")
    if os.path.exists("./SFC_EC.txt"):
        os.remove("./SFC_EC.txt")
    if os.path.exists("./SFC_EL.txt"):
        os.remove("./SFC_EL.txt")

    print("Done!")


removeAllLine()
checkEachLine()
dontPing()
removeTempFiles()
