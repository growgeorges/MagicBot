import pyautogui
import pyscreeze
import time
import configparser
import datetime

pyautogui.PAUSE = 0.2

#on set up la config
config = configparser.ConfigParser()
config.read("config.ini")


playButtonPixelPos = pyautogui.Point(x=eval(config["DEFAULT"]["playButtonPixelPos"])[0], y=eval(config["DEFAULT"]["playButtonPixelPos"])[1])
playButtonPixelRGB = eval(config["DEFAULT"]["playButtonPixelRGB"])
inBetweenSettingsButtonPixelPos1 = pyautogui.Point(x=eval(config["DEFAULT"]["inBetweenSettingsButtonPixelPos1"])[0], y=eval(config["DEFAULT"]["inBetweenSettingsButtonPixelPos1"])[1])
inBetweenSettingsButtonPixelRGB1 = eval(config["DEFAULT"]["inBetweenSettingsButtonPixelRGB1"])
inBetweenSettingsButtonPixelPos2 = pyautogui.Point(x=eval(config["DEFAULT"]["inBetweenSettingsButtonPixelPos2"])[0], y=eval(config["DEFAULT"]["inBetweenSettingsButtonPixelPos2"])[1])
inBetweenSettingsButtonPixelRGB2 = eval(config["DEFAULT"]["inBetweenSettingsButtonPixelRGB2"])
concedeButtonPos = pyautogui.Point(x=eval(config["DEFAULT"]["concedeButtonPos"])[0], y=eval(config["DEFAULT"]["concedeButtonPos"])[1])
concedeButtonRGB = eval(config["DEFAULT"]["concedeButtonRGB"])
inMatchSettingsButtonPixelPos = pyautogui.Point(x=eval(config["DEFAULT"]["inMatchSettingsButtonPixelPos"])[0], y=eval(config["DEFAULT"]["inMatchSettingsButtonPixelPos"])[1])
inMatchSettingsButtonPixelRGB = eval(config["DEFAULT"]["inMatchSettingsButtonPixelRGB"])

class quickgrab:
    def __init__(self):
        self.isRunning = False
        self.timeBeforeConcede = 0


    def startTheScript(self):
        count = 0
        while True:
            time.sleep(0.5)
            count += 1

            if not self.isRunning:
                print("pause")
                while not self.isRunning:
                    one = 1

            if(areWeInMainScreen()):
                goToPixAndClick(playButtonPixelPos)
                print("We are in MainScreen")

            if(areWeInBetweenMatchScreen()):
                time.sleep(self.timeBeforeConcede)
                goToPixAndClick(inBetweenSettingsButtonPixelPos1)
                print("We are in Between Matches")

            if(areWeInConcedeMenu()):
                goToPixAndClick(concedeButtonPos)
                print("We are in Concede Menu")

            if (areWeInMatchScreen()):
                time.sleep(self.timeBeforeConcede)
                goToPixAndClick(inBetweenSettingsButtonPixelPos1)
                print("We are in Match Screen")

            if count > 15:
                goToPixAndClick(pyautogui.Point(x=10, y=10))
                count = 0

    def getPosIn3Secs(self):
        time.sleep(3)
        return pyautogui.position()

    def getColorIn3Secs(selfself):
        time.sleep(3)
        return pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)

    def getPosNow(self):
        return pyautogui.position()

    def getColorNow(self):
        return pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)


def click():
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()

def goToImgAndClick(path):
    try:
        Pix = pyautogui.locateCenterOnScreen(path)
        pyautogui.moveTo(Pix.x, Pix.y, 0)
        click()
    except pyscreeze.ImageNotFoundException:
        print("image non trouvee")

def goToPixAndClick(Pix):
    pyautogui.moveTo(Pix.x, Pix.y, 0)
    click()

def printMyPosInXSecs():
    time.sleep(3)
    print(pyautogui.position())

def printMyRGB():
    print(pyautogui.pixel(inBetweenSettingsButtonPixelPos1.x, inBetweenSettingsButtonPixelPos1.y))

def areWeInMainScreen():
    if pyautogui.pixel(playButtonPixelPos.x, playButtonPixelPos.y) == playButtonPixelRGB:
        return True
    else:
        return False

def areWeInBetweenMatchScreen():
    #if pyautogui.pixelMatchesColor(inBetweenSettingsButtonPixelPos1.x, inBetweenSettingsButtonPixelPos1.y, inBetweenSettingsButtonPixelRGB1)\
     #       or pyautogui.pixelMatchesColor(inBetweenSettingsButtonPixelPos2.x, inBetweenSettingsButtonPixelPos2.y, inBetweenSettingsButtonPixelRGB2):
    if pyautogui.pixelMatchesColor(inBetweenSettingsButtonPixelPos2.x, inBetweenSettingsButtonPixelPos2.y, inBetweenSettingsButtonPixelRGB2):
            return True
    else:
        return False

def areWeInConcedeMenu():
    if pyautogui.pixelMatchesColor(concedeButtonPos.x, concedeButtonPos.y, concedeButtonRGB):
        return True
    else:
        return False

def areWeInMatchScreen():
    if pyautogui.pixelMatchesColor(inMatchSettingsButtonPixelPos.x, inMatchSettingsButtonPixelPos.y, inMatchSettingsButtonPixelRGB):
        return True
    else:
        return False