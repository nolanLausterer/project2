from PyQt5.QtWidgets import *
from gui import *
import random
import time
#import requests

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.label_10.setHidden(True)
        self.label_11.setHidden(True)
        self.pushButton_2.setHidden(True)
        self.label_16.setHidden(True)
        self.pushButton.clicked.connect(lambda: self.spin())
        self.pushButton_2.clicked.connect(lambda: self.cashOut())

    """
    Constructor for GUI 
    """

    def spin(self) -> None:
        self.label_16.setHidden(True)
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'l','m','n','p','r','s','t','w','z']
        vowels = ['a','e','i','o','u','y']
        position = random.randint(0, 14)
        consonant1 = consonants[position]
        position = random.randint(0, 14)
        consonant2 = consonants[position]
        position = random.randint(0,5)
        vowel = vowels[position]

        vowelScramble = random.randint(0,2)

        if vowelScramble == 0:
            self.label_5.setText(vowel)
            self.label_6.setText(consonant1)
            self.label_7.setText(consonant2)
        if vowelScramble == 1:
            self.label_6.setText(vowel)
            self.label_5.setText(consonant1)
            self.label_7.setText(consonant2)
        if vowelScramble == 2:
            self.label_7.setText(vowel)
            self.label_5.setText(consonant1)
            self.label_6.setText(consonant2)

        self.word = (self.label_5.text() + self.label_6.text() + self.label_7.text()).upper()
        bet = self.spinBox.value()
        self.wait()

        if self.isWord(self.word):
            self.label_10.setHidden(False)
            self.label_10.setText('              You made a word!')
            self.label_11.setHidden(True)
            self.spinBox.setValue(bet * 2)
            self.spinBox.setDisabled(True)
            self.pushButton_2.setHidden(False)
        else:
            self.label_10.setHidden(False)
            self.label_10.setText('No word found!')
            self.label_11.setHidden(False)
            self.label_11.setText('You lost $ ' + str(self.spinBox.value()))
            self.spinBox.setValue(5)
            self.spinBox.setDisabled(False)
            self.pushButton_2.setHidden(True)

        """
        This function creates a random sequence of character and checks a file to 
        see if a 3 letter word has been made, it changes the output based upon if the 
        isWord function is true or false
        """

    def isWord(self, word: str) -> bool:
        existInDict = False
        with open(r'3letterWords.txt', 'r') as file:
            allWords = file.read()
            if word in allWords:
                existInDict = True

        """
        This function checks if the passed characters form a word by scanning through a 
        scrabble certified text file of all possible words
        :param word: string consisting of three characters
        :return: Boolean true if word exists, false if not 
        """
        return existInDict

    def wait(self) -> None:
        time.sleep(0.25)
        """
        This function is a delay 
        """

    def cashOut(self) -> None:
        self.label_5.setText('-')
        self.label_6.setText('-')
        self.label_7.setText('-')

        if self.isWord(self.word):
            self.label_11.setHidden(False)
            self.label_10.setText(' You Won!!')
            self.spinBox.setDisabled(False)
            self.label_11.setText('Winnings = $ ' + str(self.spinBox.value()))
        else:
            self.label_10.setText(' You Lost!!')
            self.label_11.setHidden(True)
            self.label_11.setText(str(self.spinBox.value()))

        self.spinBox.setValue(0)
        self.pushButton_2.setHidden(True)
        self.label_16.setHidden(False)
        time.sleep(0.5)
        """
        This function is used to cash out the winnings from the current bet 
        """
