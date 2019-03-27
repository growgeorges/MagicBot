import pyautogui
import pyscreeze
import time
import configparser
import datetime
import PyWinMouse

pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = False

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
inMatchSettingsButtonPixelPos1 = pyautogui.Point(x=eval(config["DEFAULT"]["inMatchSettingsButtonPixelPos1"])[0], y=eval(config["DEFAULT"]["inMatchSettingsButtonPixelPos1"])[1])
inMatchSettingsButtonPixelRGB1 = eval(config["DEFAULT"]["inMatchSettingsButtonPixelRGB1"])
inMatchSettingsButtonPixelPos2 = pyautogui.Point(x=eval(config["DEFAULT"]["inMatchSettingsButtonPixelPos2"])[0], y=eval(config["DEFAULT"]["inMatchSettingsButtonPixelPos2"])[1])
inMatchSettingsButtonPixelRGB2 = eval(config["DEFAULT"]["inMatchSettingsButtonPixelRGB2"])

class quickgrab:
    def __init__(self):
        self.isRunning = False
        self.timeBeforeConcede = 0
        self.mouse = PyWinMouse.Mouse()


    def startTheScript(self):
        count = 0
        while True:
            time.sleep(0.5)
            count += 1

            if not self.isRunning:
                print("pause")
                while not self.isRunning:
                    one = 1

            if(self.areWeInMainScreen()):
                self.goToPixAndClick(playButtonPixelPos)
                print("We are in MainScreen")

            if(self.areWeInBetweenMatchScreen()):
                time.sleep(self.timeBeforeConcede)
                self.goToPixAndClick(inBetweenSettingsButtonPixelPos1)
                print("We are in Between Matches")

            if(self.areWeInConcedeMenu()):
                self.goToPixAndClick(concedeButtonPos)
                print("We are in Concede Menu")

            if (self.areWeInMatchScreen()):
                time.sleep(self.timeBeforeConcede)
                self.goToPixAndClick(inBetweenSettingsButtonPixelPos1)
                print("We are in Match Screen")

            if count > 15:
                self.goToPixAndClick(pyautogui.Point(x=10, y=10))
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


    def click(self):
        self.mouse.left_down()
        time.sleep(0.2)
        self.mouse.left_up()

    def goToImgAndClick(self, path):
        try:
            Pix = pyautogui.locateCenterOnScreen(path)
            pyautogui.moveTo(Pix.x, Pix.y, 0)
            self.click()
        except pyscreeze.ImageNotFoundException:
            print("image non trouvee")

    def goToPixAndClick(self, Pix):
        pyautogui.moveTo(Pix.x, Pix.y, 0)
        self.click()

    def printMyPosInXSecs(self):
        time.sleep(3)
        print(pyautogui.position())

    def printMyRGB(self):
        print(pyautogui.pixel(inBetweenSettingsButtonPixelPos1.x, inBetweenSettingsButtonPixelPos1.y))

    def areWeInMainScreen(self):
        if pyautogui.pixel(playButtonPixelPos.x, playButtonPixelPos.y) == playButtonPixelRGB:
            return True
        else:
            return False

    def areWeInBetweenMatchScreen(self):
        if pyautogui.pixelMatchesColor(inBetweenSettingsButtonPixelPos1.x, inBetweenSettingsButtonPixelPos1.y, inBetweenSettingsButtonPixelRGB1)\
                or pyautogui.pixelMatchesColor(inBetweenSettingsButtonPixelPos2.x, inBetweenSettingsButtonPixelPos2.y, inBetweenSettingsButtonPixelRGB2):
                return True
        else:
            return False

    def areWeInConcedeMenu(self):
        if pyautogui.pixelMatchesColor(concedeButtonPos.x, concedeButtonPos.y, concedeButtonRGB):
            return True
        else:
            return False

    def areWeInMatchScreen(self):
        if pyautogui.pixelMatchesColor(inMatchSettingsButtonPixelPos1.x, inMatchSettingsButtonPixelPos1.y, inMatchSettingsButtonPixelRGB1)\
                or pyautogui.pixelMatchesColor(inMatchSettingsButtonPixelPos2.x, inMatchSettingsButtonPixelPos2.y, inMatchSettingsButtonPixelRGB2):
            return True
        else:
            return False