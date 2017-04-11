import psycopg2 #Needed to connect to database
from PyQt4 import QtCore, QtGui

#connecing to the postgresql database
conn = psycopg2.connect(database="network", user="postgres", password="###########", host="127.0.0.1", port="5432")
cur = conn.cursor()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(443, 271)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.employee_id = QtGui.QTextEdit(self.centralwidget)
        self.employee_id.setGeometry(QtCore.QRect(140, 20, 251, 31))
        self.employee_id.setObjectName(_fromUtf8("employee_id"))

        self.firstname = QtGui.QTextEdit(self.centralwidget)
        self.firstname.setGeometry(QtCore.QRect(140, 60, 251, 31))
        self.firstname.setObjectName(_fromUtf8("firstname"))

        self.lastname = QtGui.QTextEdit(self.centralwidget)
        self.lastname.setGeometry(QtCore.QRect(140, 110, 251, 31))
        self.lastname.setObjectName(_fromUtf8("lastname"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 111, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 111, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.insertbtn = QtGui.QPushButton(self.centralwidget)
        self.insertbtn.setGeometry(QtCore.QRect(10, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.insertbtn.setFont(font)
        self.insertbtn.setObjectName(_fromUtf8("insertbtn"))
        self.insertbtn.clicked.connect(self.insert)

        self.viewemployeesbtn = QtGui.QPushButton(self.centralwidget)
        self.viewemployeesbtn.setGeometry(QtCore.QRect(240, 170, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.viewemployeesbtn.setFont(font)
        self.viewemployeesbtn.setObjectName(_fromUtf8("viewemployeesbtn"))
        self.viewemployeesbtn.clicked.connect(self.viewEmployee)

        self.viewlogsbtn = QtGui.QPushButton(self.centralwidget)
        self.viewlogsbtn.setGeometry(QtCore.QRect(120, 170, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.viewlogsbtn.setFont(font)
        self.viewlogsbtn.setObjectName(_fromUtf8("viewlogsbtn"))
        self.viewlogsbtn.clicked.connect(self.viewlog)

        self.updatebtn = QtGui.QPushButton(self.centralwidget)
        self.updatebtn.setGeometry(QtCore.QRect(20, 220, 150, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.updatebtn.setFont(font)
        self.updatebtn.setObjectName(_fromUtf8("updatebtn"))
        self.updatebtn.clicked.connect(self.update)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Postgresql DB", None))
        self.label.setText(_translate("MainWindow", "Employee ID:", None))
        self.label_2.setText(_translate("MainWindow", "First Name: ", None))
        self.label_3.setText(_translate("MainWindow", "Last Name:", None))
        self.insertbtn.setText(_translate("MainWindow", "Insert", None))
        self.viewemployeesbtn.setText(_translate("MainWindow", "View Employees Table", None))
        self.viewlogsbtn.setText(_translate("MainWindow", "View Logs", None))
        self.updatebtn.setText(_translate("MainWindow", "Update Last Name", None))
    
     def insert(self):
        empid = self.employee_id.toPlainText()
        fname = self.firstname.toPlainText()
        lname = self.lastname.toPlainText()
        cur.execute("INSERT INTO employees (employee_id, first_name, last_name)VALUES (%s, %s, %s)", (empid, fname, lname))
        conn.commit()
        print("Inserted: Employee ID: "+empid+"\nFirst Name: "+fname+"\nLast Name: "+lname)

    def viewEmployee(self):
        cur.execute('SELECT * FROM employees;')
        rows = cur.fetchall()
        for records in rows:
            print(records)
        print("\n")

    def update(self):
        sql="""
        UPDATE employees 
        SET last_name = '{0}'
        WHERE employee_id = {1}""".format(self.lastname.toPlainText(), self.employee_id.toPlainText())
        cur.execute(sql)
        conn.commit()

     def viewlog(self):
        cur.execute('SELECT * FROM employee_audits;')
        rows = cur.fetchall()
        for records in rows:
          print(records)
        print("\n")
  
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
