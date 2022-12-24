# Import Libraries

from PyQt5 import QtCore, QtGui, QtWidgets

# "calculation" variable holds expression to be evaluated
calculation = ""

# Updates expression and display when any button clicked
def update_calculation(ui, symbol):
    global calculation
    calculation += str(symbol)
    ui.Label_Display.setText(calculation)

# Evaluates "calculation" expression   
def evaluate_calculation(ui):
    try:
        global calculation
        calculation = str(eval(calculation))
        ui.Label_Display.setText(calculation)
        
    except:
        clear_field
        ui.Label_Display.setText("Error")

# Clears display label
def clear_field():
    global calculation
    calculation = ""
    ui.Label_Display.setText(calculation)

# Stylesheet for buttons
stylesheet1 = (
                "background-color: #192C3B;\n"
                "color: #F8F8F8;\n"
                "font-family: Helvetica;\n"
                "font-size: 30px;\n"
                "border-radius: 5px;\n"
                "padding: 5px;")

# Stylesheet for evaluate button
stylesheet2  = (
                "background-color: rgb(253, 132, 31);\n"
                "color: #F8F8F8;\n"
                "font-family: Helvetica;\n"
                "font-size: 30px;\n"
                "border-radius: 5px;")

# PyQt5 UI Elements
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        # Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 440)
        MainWindow.setMinimumSize(QtCore.QSize(330, 440))
        MainWindow.setMaximumSize(QtCore.QSize(330, 440))
        MainWindow.setStyleSheet("background-color: #0D161E;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Display Label
        self.Label_Display = QtWidgets.QLabel(self.centralwidget)
        self.Label_Display.setGeometry(QtCore.QRect(10, 10, 310, 70))
        self.Label_Display.setStyleSheet(stylesheet1)
        self.Label_Display.setObjectName("Label_Display")

        # '0' Button
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(80, 300, 60, 60))
        self.btn_0.setStyleSheet(stylesheet1)
        self.btn_0.setObjectName("btn_0")
        self.btn_0.setText("0")

        # '1' Button
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(10, 230, 60, 60))
        self.btn_1.setStyleSheet(stylesheet1)
        self.btn_1.setObjectName("btn_1")
        self.btn_1.setText("1")

        # '2' Button
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(80, 230, 60, 60))
        self.btn_2.setStyleSheet(stylesheet1)
        self.btn_2.setObjectName("btn_2")
        self.btn_2.setText("2")

        # '3' Button
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(150, 230, 60, 60))
        self.btn_3.setStyleSheet(stylesheet1)
        self.btn_3.setObjectName("btn_3")
        self.btn_3.setText("3")

        # '4' Button
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(10, 160, 60, 60))
        self.btn_4.setStyleSheet(stylesheet1)
        self.btn_4.setObjectName("btn_4")
        self.btn_4.setText("4")

        # '5' Button
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(80, 160, 60, 60))
        self.btn_5.setStyleSheet(stylesheet1)
        self.btn_5.setObjectName("btn_5")
        self.btn_5.setText("5")

        # '6' Button
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(150, 160, 60, 60))
        self.btn_6.setStyleSheet(stylesheet1)
        self.btn_6.setObjectName("btn_6")
        self.btn_6.setText("6")

        # '7' Button
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(10, 90, 60, 60))
        self.btn_7.setStyleSheet(stylesheet1)
        self.btn_7.setObjectName("btn_7")
        self.btn_7.setText("7")

        # '8' Button
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(80, 90, 60, 60))
        self.btn_8.setStyleSheet(stylesheet1)
        self.btn_8.setObjectName("btn_8")
        self.btn_8.setText("8")

        # '9' Button
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(150, 90, 60, 60))
        self.btn_9.setStyleSheet(stylesheet1)
        self.btn_9.setObjectName("btn_9")
        self.btn_9.setText("9")

        # 'Left Bracket' Button
        self.btn_lb = QtWidgets.QPushButton(self.centralwidget)
        self.btn_lb.setGeometry(QtCore.QRect(10, 300, 60, 60))
        self.btn_lb.setStyleSheet(stylesheet1)
        self.btn_lb.setObjectName("btn_lb")
        self.btn_lb.setText("(")

        # 'Right Bracket' Button
        self.btn_rb = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rb.setGeometry(QtCore.QRect(150, 300, 60, 60))
        self.btn_rb.setStyleSheet(stylesheet1)
        self.btn_rb.setObjectName("btn_rb")
        self.btn_rb.setText(")")

        # 'Add' Button
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(220, 90, 100, 60))
        self.btn_add.setStyleSheet(stylesheet1)
        self.btn_add.setObjectName("btn_add")
        self.btn_add.setText("+")

        # 'Subtract' Button
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sub.setGeometry(QtCore.QRect(220, 160, 100, 60))
        self.btn_sub.setStyleSheet(stylesheet1)
        self.btn_sub.setObjectName("btn_sub")
        self.btn_sub.setText("-")

        # 'Multiply' Button
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mul.setGeometry(QtCore.QRect(220, 230, 100, 60))
        self.btn_mul.setStyleSheet(stylesheet1)
        self.btn_mul.setObjectName("btn_mul")
        self.btn_mul.setText("*")

        # 'Divide' Button
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setGeometry(QtCore.QRect(220, 300, 100, 60))
        self.btn_div.setStyleSheet(stylesheet1)
        self.btn_div.setObjectName("btn_div")
        self.btn_div.setText("/")

        # 'Clear' Button
        self.btn_clr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clr.setGeometry(QtCore.QRect(10, 370, 150, 60))
        self.btn_clr.setStyleSheet(stylesheet1)
        self.btn_clr.setObjectName("btn_clr")
        self.btn_clr.setText("C")

        # 'Result/Evaluate' Button
        self.btn_result = QtWidgets.QPushButton(self.centralwidget)
        self.btn_result.setGeometry(QtCore.QRect(170, 370, 150, 60))
        self.btn_result.setStyleSheet(stylesheet2)
        self.btn_result.setObjectName("btn_result")
        self.btn_result.setText("=")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Update expression when buttons clicked
        self.btn_0.clicked.connect(lambda: update_calculation(self, "0"))
        self.btn_1.clicked.connect(lambda: update_calculation(self, "1"))
        self.btn_2.clicked.connect(lambda: update_calculation(self, "2"))
        self.btn_3.clicked.connect(lambda: update_calculation(self, "3"))
        self.btn_4.clicked.connect(lambda: update_calculation(self, "4"))
        self.btn_5.clicked.connect(lambda: update_calculation(self, "5"))
        self.btn_6.clicked.connect(lambda: update_calculation(self, "6"))
        self.btn_7.clicked.connect(lambda: update_calculation(self, "7"))
        self.btn_8.clicked.connect(lambda: update_calculation(self, "8"))
        self.btn_9.clicked.connect(lambda: update_calculation(self, "9"))
        self.btn_lb.clicked.connect(lambda: update_calculation(self, "("))
        self.btn_rb.clicked.connect(lambda: update_calculation(self, ")"))
        self.btn_add.clicked.connect(lambda: update_calculation(self, "+"))
        self.btn_sub.clicked.connect(lambda: update_calculation(self, "-"))
        self.btn_mul.clicked.connect(lambda: update_calculation(self, "*"))
        self.btn_div.clicked.connect(lambda: update_calculation(self, "/"))
        self.btn_clr.clicked.connect(lambda: clear_field())
        self.btn_result.clicked.connect(lambda: evaluate_calculation(self))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))





# Run UI window
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
