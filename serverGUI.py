# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import serverLogic
import sys

class Application(object):
    def __init__(self ,master=None):
        app = QtWidgets.QApplication(sys.argv)    
        MainWindow = QtWidgets.QMainWindow()
        self.setupUi(MainWindow)
        self.server = None
        self.connectBtns()
        self.threadpool = QtCore.QThreadPool()
        MainWindow.show()
        sys.exit(app.exec_())
       
    # GUI SETUP
    def setupUi(self, MainWindow):
        self.createMainWindow(MainWindow)
        self.createConnectedListView()
        self.createMessageBtns()
        self.createTopMenu()
        self.createMessageListView()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def connectBtns(self):
        self.goDownBtn.clicked.connect(self.changeServerState)
        self.clrMsgBtn.clicked.connect(self.clearMessages)
        self.disconnectAllBtn.clicked.connect(self.disconnectAll)
        self.disconnectSelectBtn.clicked.connect(self.disconnectSingle)
        self.sendSelectBtn.clicked.connect(self.sendIndivdMsg)
        self.sendAllBtn.clicked.connect(self.sendBroadcastMsg)

    def createMainWindow(self, MainWindow):
        MainWindow.setObjectName("Server")
        MainWindow.resize(800, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
       
    def createConnectedListView(self):
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QtCore.QRect(-1, -1, 331, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.connectedClients = QtWidgets.QLabel(self.frame)
        self.connectedClients.setGeometry(QtCore.QRect(10, 80, 251, 16))
        self.connectedClients.setObjectName("connectedClients")
        self.connectedListView = QtWidgets.QListWidget(self.frame)
        self.connectedListView.setGeometry(QtCore.QRect(10, 101, 311, 181))
        self.connectedListView.setObjectName("connectedListView")

    def createMessageBtns(self):
        self.frame2 = QtWidgets.QFrame(self.frame)
        self.frame2.setGeometry(QtCore.QRect(10, 340, 311, 80))
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.sendIndividualMessage = QtWidgets.QLabel(self.frame2)
        self.sendIndividualMessage.setGeometry(QtCore.QRect(10, 10, 291, 16))
        self.sendIndividualMessage.setObjectName("sendIndividualMessage")
        self.sendIndivdLine = QtWidgets.QLineEdit(self.frame2)
        self.sendIndivdLine.setGeometry(QtCore.QRect(10, 30, 201, 22))
        self.sendIndivdLine.setObjectName("sendIndivdLine")
        self.sendSelectBtn = QtWidgets.QPushButton(self.frame2)
        self.sendSelectBtn.setGeometry(QtCore.QRect(10, 50, 201, 21))
        self.sendSelectBtn.setObjectName("sendSelectBtn")
        self.frame3 = QtWidgets.QFrame(self.frame)
        self.frame3.setGeometry(QtCore.QRect(10, 420, 311, 80))
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setObjectName("frame3")
        self.broadcastMessage = QtWidgets.QLabel(self.frame3)
        self.broadcastMessage.setGeometry(QtCore.QRect(10, 10, 291, 16))
        self.broadcastMessage.setObjectName("broadcastMessage")
        self.sendAllLine = QtWidgets.QLineEdit(self.frame3)
        self.sendAllLine.setGeometry(QtCore.QRect(10, 30, 201, 22))
        self.sendAllLine.setObjectName("sendAllLine")
        self.sendAllBtn = QtWidgets.QPushButton(self.frame3)
        self.sendAllBtn.setGeometry(QtCore.QRect(10, 50, 201, 21))
        self.sendAllBtn.setObjectName("sendAllBtn")
        self.disconnectSelectBtn = QtWidgets.QPushButton(self.frame)
        self.disconnectSelectBtn.setGeometry(QtCore.QRect(10, 280, 161, 28))
        self.disconnectSelectBtn.setObjectName("disconnectSelectBtn")
        self.disconnectAllBtn = QtWidgets.QPushButton(self.frame)
        self.disconnectAllBtn.setGeometry(QtCore.QRect(170, 280, 151, 28))
        self.disconnectAllBtn.setObjectName("disconnectAllBtn")

    def createTopMenu(self):
        self.port = QtWidgets.QLabel(self.frame)
        self.port.setGeometry(QtCore.QRect(20, 10, 55, 16))
        self.port.setObjectName("port")
        self.portLine = QtWidgets.QLineEdit(self.frame)
        self.portLine.setGeometry(QtCore.QRect(20, 30, 51, 31))
        self.portLine.setObjectName("portLine")
        self.goDownBtn = QtWidgets.QPushButton(self.frame)
        self.goDownBtn.setGeometry(QtCore.QRect(90, 30, 93, 31))
        self.goDownBtn.setObjectName("goDownBtn")
        self.clrMsgBtn = QtWidgets.QPushButton(self.frame)
        self.clrMsgBtn.setGeometry(QtCore.QRect(200, 30, 93, 31))
        self.clrMsgBtn.setObjectName("clrMsgBtn")
    
    def createMessageListView(self):
        self.frame4 = QtWidgets.QFrame(self.centralwidget)
        self.frame4.setGeometry(QtCore.QRect(330, 0, 471, 571))
        self.frame4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame4.setObjectName("frame4")
        self.messagesListView = QtWidgets.QListWidget(self.frame4)
        self.messagesListView.setGeometry(QtCore.QRect(10, 30, 451, 531))
        self.messagesListView.setObjectName("messagesListView")
        self.messages = QtWidgets.QLabel(self.frame4)
        self.messages.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.messages.setObjectName("messages")
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Server", "Server"))
        self.sendIndividualMessage.setText(_translate("MainWindow", "Send Individual Message:"))
        self.sendSelectBtn.setText(_translate("MainWindow", "Send To Selected"))
        self.broadcastMessage.setText(_translate("MainWindow", "Broadcast Message:"))
        self.sendAllBtn.setText(_translate("MainWindow", "Send To All"))
        self.disconnectSelectBtn.setText(_translate("MainWindow", "Disconnect Selected"))
        self.disconnectAllBtn.setText(_translate("MainWindow", "Disconnect All"))
        self.connectedClients.setText(_translate("MainWindow", "Connected Clients"))
        self.port.setText(_translate("MainWindow", "Port:"))
        self.goDownBtn.setText(_translate("MainWindow", "Go Up"))
        self.clrMsgBtn.setText(_translate("MainWindow", "CLR MSG"))
        self.messages.setText(_translate("MainWindow", "Messages:"))

    #INTERACTIVE METHODS
    def clearMessages(self):
        self.messagesListView.clear()

    def changeServerState(self):
        _translate = QtCore.QCoreApplication.translate
        if self.server != None:
            self.server.stopThread()
            self.server = None
            self.connectedListView.clear()
            self.goDownBtn.setText(_translate("MainWindow", "Go Up"))
            self.updateMessages("Server Offline")
        else:
            port = self.portLine.text()
            if self.server == None:    
                try:
                    self.server = serverLogic.Server(self, port)
                    self.threadpool.start(self.server)
                    self.goDownBtn.setText(_translate("MainWindow", "Go Down"))
                    self.updateMessages("Server Online")
                except:
                    self.updateMessages("Invalid Port")
        
    def sendBroadcastMsg(self):
        try:
            msg = self.sendAllLine.text()
            self.server.sendMsgToAll(msg)
            self.sendAllLine.setText('')
        except:
            self.updateMessages("Could not send broadcast message")

    def sendIndivdMsg(self):
        try:
            self.server.sendMsg(self.sendIndivdLine.text(), self.connectedListView.currentItem().text())
            self.sendIndivdLine.setText('')
        except:
            self.updateMessages("Could not send private message")

    def disconnectAll(self):
        try:
            self.server.sendMsgToAll("Kicking all clients")
            self.server.disconnectAll()
            self.connectedListView.clear()
        except:
            self.updateMessages("Could not kick clients")

    def disconnectSingle(self):
        try:
            toDisconnect = self.connectedListView.takeItem(self.connectedListView.currentRow())
            self.server.disconnect(toDisconnect.text())
        except:
            self.updateMessages("Could not kick client")

    def updateMessages(self, msg):
        self.messagesListView.addItem(msg)

    def addConnection(self, connection):
        self.connectedListView.addItem(connection)

    def removeConnection(self, connection):
        removedIP = self.connectedListView.findItems(connection, QtCore.Qt.MatchExactly)
        removedIP = removedIP[0]
        self.connectedListView.takeItem(self.connectedListView.row(removedIP))