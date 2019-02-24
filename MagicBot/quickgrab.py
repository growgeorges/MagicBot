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
inBetweenSettingsButtonPixelPos = pyautogui.Point(x=eval(config["DEFAULT"]["inBetweenSettingsButtonPixelPos"])[0], y=eval(config["DEFAULT"]["inBetweenSettingsButtonPixelPos"])[1])
inBetweenSettingsButtonPixelRGB = eval(config["DEFAULT"]["inBetweenSettingsButtonPixelRGB"])
concedeButtonPos = pyautogui.Point(x=eval(config["DEFAULT"]["concedeButtonPos"])[0], y=eval(config["DEFAULT"]["concedeButtonPos"])[1])
concedeButtonRGB = eval(config["DEFAULT"]["concedeButtonRGB"])
inMatchSettingsButtonPixelPos = pyautogui.Point(x=eval(config["DEFAULT"]["inMatchSettingsButtonPixelPos"])[0], y=eval(config["DEFAULT"]["inMatchSettingsButtonPixelPos"])[1])
inMatchSettingsButtonPixelRGB = eval(config["DEFAULT"]["inMatchSettingsButtonPixelRGB"])

#positions and colors
"""
playButtonPixelPos = pyautogui.Point(x=1707, y=1006)
playButtonPixelRGB = (255, 255, 255)
inBetweenSettingsButtonPixelPos = pyautogui.Point(x=1886, y=21)
inBetweenSettingsButtonPixelRGB = (105, 105, 105)
concedeButtonPos = pyautogui.Point(x=936, y=643)
concedeButtonRGB = (247, 98, 98)
inMatchSettingsButtonPixelPos = pyautogui.Point(x=955, y=98)
inMatchSettingsButtonPixelRGB = (204, 204, 204)
"""


class quickgrab:
    def __init__(self):
        self.isRunning = False
        self.timeBeforeConcede = 0

    def startTheScript(self):
        self.isRunning = True
        print(self.timeBeforeConcede)
        count = 0
        while self.isRunning:
            print(datetime.datetime.now())
            time.sleep(0.5)
            count += 1
            if(areWeInMainScreen()):
                goToPixAndClick(playButtonPixelPos)
                #print("We are in MainScreen")

            if(areWeInBetweenMatchScreen()):
                time.sleep(5)
                goToPixAndClick(inBetweenSettingsButtonPixelPos)
                #print("We are in Between Matches")

            if(areWeInConcedeMenu()):
                goToPixAndClick(concedeButtonPos)
                #print("We are in Concede Menu")

            if (areWeInMatchScreen()):
                time.sleep(5)
                goToPixAndClick(inBetweenSettingsButtonPixelPos)
                #print("We are in Match Screen")

            if count > 15:
                goToPixAndClick(pyautogui.Point(x=10, y=10))
                count = 0

    def getPosIn3Secs(self):
        time.sleep(3)
        return pyautogui.position()

    def getColorIn3Secs(selfself):
        time.sleep(3)
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
    print(pyautogui.pixel(inBetweenSettingsButtonPixelPos.x, inBetweenSettingsButtonPixelPos.y))

def areWeInMainScreen():
    if pyautogui.pixel(playButtonPixelPos.x, playButtonPixelPos.y) == playButtonPixelRGB:
        return True
    else:
        return False

def areWeInBetweenMatchScreen():
    if pyautogui.pixelMatchesColor(inBetweenSettingsButtonPixelPos.x, inBetweenSettingsButtonPixelPos.y, inBetweenSettingsButtonPixelRGB):
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




