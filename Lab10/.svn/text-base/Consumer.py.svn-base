import sys
import re
from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.clearButton.clicked.connect(self.Clear)
        self.lines=[self.addressLineEdit,self.cityLineEdit,self.emailLineEdit,self.firstNameLineEdit,self.lastNameLineEdit,self.stateLineEdit,self.zipLineEdit]
        self.saveToTargetButton.clicked.connect(self.Save)
        self.loadButton.clicked.connect(self.loadData)
        for item in self.lines:
            item.textChanged.connect(self.DataEntry)

    def Clear(self):
        for item in self.lines:
            item.clear()
        self.saveToTargetButton.setEnabled(False)
        self.loadButton.setEnabled(True)
        self.errorInfoLabel.clear()
    def DataEntry(self):
        self.saveToTargetButton.setEnabled(True)
        self.loadButton.setEnabled(False)
    def Save(self):
        self.errorInfoLabel.clear()
        for line in self.lines:
            if line.text() == "":
                self.errorInfoLabel.setText("Error: All entries must be populated")
                return
        if self.stateLineEdit.text() not in self.states:
            self.errorInfoLabel.setText("Error: The State must be one of the valid US states")
            return
        zip=re.match(r"\d\d\d\d\d",self.zipLineEdit.text())
        if not zip:
            self.errorInfoLabel.setText("Error: The Zip code must be a 5-digit number")
            return
        email=re.match(r"\w+@\w+\.\w+",self.emailLineEdit.text())
        if not email:
            self.errorInfoLabel.setText("Error: The Email must have a valid email format")
            return

        with open('target.xml', 'w') as file:
            file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            file.write('<user>\n')
            file.write('\t<FirstName>' + self.firstNameLineEdit.text() + '</FirstName>\n')
            file.write('\t<LastName>' + self.lastNameLineEdit.text() + '</LastName>\n')
            file.write('\t<Address>' + self.addressLineEdit.text() + '</Address>\n')
            file.write('\t<City>' + self.cityLineEdit.text() + '</City>\n')
            file.write('\t<State>' + self.stateLineEdit.text() + '</State>\n')
            file.write('\t<ZIP>' + self.zipLineEdit.text() + '</ZIP>\n')
            file.write('\t<Email>' + self.emailLineEdit.text() + '</Email>\n')
            file.write('</user>\n')

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """
        with open(filePath,"r") as file:
            lines=file.readlines()
            for line in lines[2:]:
                if 'FirstName' in line:
                    self.firstNameLineEdit.setText(line.strip()[11:-12])
                if 'LastName' in line:
                    self.lastNameLineEdit.setText(line.strip()[10:-11])
                if 'Address' in line:
                    self.addressLineEdit.setText(line.strip()[9:-10])
                if 'City' in line:
                    self.cityLineEdit.setText(line.strip()[6:-7])
                if 'State' in line:
                    self.stateLineEdit.setText(line.strip()[7:-8])
                if 'ZIP' in line:
                    self.zipLineEdit.setText(line.strip()[5:-6])
                if 'Email' in line:
                    self.emailLineEdit.setText(line.strip()[7:-8])

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
