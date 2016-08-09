# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

class CalculatorConsumer(QMainWindow, Ui_Calculator):

    def __init__(self, parent=None):
        super(CalculatorConsumer, self).__init__(parent)
        self.setupUi(self)
        self.btn0.clicked.connect(self.NumClicked)
        self.btn1.clicked.connect(self.NumClicked)
        self.btn2.clicked.connect(self.NumClicked)
        self.btn3.clicked.connect(self.NumClicked)
        self.btn4.clicked.connect(self.NumClicked)
        self.btn5.clicked.connect(self.NumClicked)
        self.btn6.clicked.connect(self.NumClicked)
        self.btn7.clicked.connect(self.NumClicked)
        self.btn8.clicked.connect(self.NumClicked)
        self.btn9.clicked.connect(self.NumClicked)
        self.btnPlus.clicked.connect(self.OpClicked)
        self.btnMinus.clicked.connect(self.OpClicked)
        self.btnMultiply.clicked.connect(self.OpClicked)
        self.btnDivide.clicked.connect(self.OpClicked)
        self.btnClear.clicked.connect(self.ClearClicked)
        self.btnEqual.clicked.connect(self.EqualClicked)
        self.btnDot.clicked.connect(self.NumClicked)
        self.chkSeparator.stateChanged.connect(self.Seperator)
        self.operand1="0"
        self.operand2="0"
        self.operator=None
        self.result=0

    def NumClicked(self):
        if self.txtDisplay.text() == "0.":
            if self.sender().text()=="0":
                return
            else:
                self.txtDisplay.setText(self.sender().text())
        else:
            self.txtDisplay.setText(self.txtDisplay.text()+self.sender().text())

        if self.operator==None:
            self.operand1+=self.sender().text()
        else:
            self.operand2+=self.sender().text()

        if len(self.txtDisplay.text())>12:
            self.txtDisplay.setText("MAXIMUM 12 DIGITS")

    def OpClicked(self):
        if self.operator == None:
            self.operator=self.sender().text()
        else:
            self.EqualClicked()
            self.operator=self.sender().text()
        self.txtDisplay.setText(self.txtDisplay.text()+self.sender().text())
    def EqualClicked(self):
        if self.operator == "+":
            self.result=float(self.operand1)+float(self.operand2)
            self.Display(self.result)
        elif self.operator == "x":
            self.result=float(self.operand1)*float(self.operand2)
            self.Display(self.result)
        elif self.operator == "-":
            self.result=float(self.operand1)-float(self.operand2)
            self.Display(self.result)
        elif self.operator == "/":
            if float(self.operand2) == 0.0:
                self.txtDisplay.setText("Error! Division by zero")
            else:
                self.result=float(self.operand1)/float(self.operand2)
                self.Display(self.result)

        self.operand1=self.result
        self.operand2="0"
        self.operator=None
    def Display(self,number):
        decimal=int(self.cboDecimal.currentText())
        if decimal==0:
            self.txtDisplay.setText(str(format(round(number))))
        elif decimal==1:
            self.txtDisplay.setText(str(format(number,".1f")))
        elif decimal==2:
            self.txtDisplay.setText(str(format(number,".2f")))
        elif decimal==3:
            self.txtDisplay.setText(str(format(number,".3f")))
        elif decimal==4:
            self.txtDisplay.setText(str(format(number,".4f")))
        elif decimal==5:
            self.txtDisplay.setText(str(format(number,".5f")))

    def Seperator(self):
        if self.chkSeparator.isChecked():
            self.txtDisplay.setText('{0:,}'.format(float(self.txtDisplay.text())))
        else:
            if "," in self.txtDisplay.text():
                i=self.txtDisplay.text()
                i=i.replace(",","")
                self.txtDisplay.setText(i)

    def ClearClicked(self):
        self.txtDisplay.setText("0.")
        self.operand1="0"
        self.operand2="0"
        self.operator=None

currentApp = QApplication(sys.argv)
currentForm = CalculatorConsumer()

currentForm.show()
currentApp.exec_()
