import socket
import select
from PyQt5 import QtCore

class Server(QtCore.QRunnable):
    def __init__(self, GUI, port, *args, **kwargs):
        super(Server, self).__init__()
        self.port = port
        self.GUI = GUI
        self.serverOpen = True
        self.sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockL.bind(("", int(self.port)))
        self.sockL.listen(2)
        self.listOfSockets = [self.sockL]

    def stopThread(self):
        self.disconnectAll()
        self.sockL.close()
        self.listOfSockets.remove(self.sockL)
        self.serverOpen = False

    def disconnect(self, IP):
        for sock in self.listOfSockets:
            if sock == self.sockL:
                continue
            sock.send(bytearray(f"[{IP}] Got kicked by server", "ASCII"))
            if str(sock.getpeername()) == IP:
                self.listOfSockets.remove(sock)
                sock.close()
        self.msgToServer(f"[{IP}] Kicked")

    def disconnectAll(self):
        _ = self.listOfSockets.copy()
        for sock in _:
            if sock == self.sockL:
                continue
            self.listOfSockets.remove(sock)
            sock.close()

    def sendMsg(self, msg, IP):
        for sock in self.listOfSockets:
            if sock == self.sockL:
                continue
            if str(sock.getpeername()) == IP:   
                sock.send(bytearray(f"[SERVER - TO YOU] {msg}", "ASCII"))
        self.msgToServer(f"[SERVER - TO {IP}] {msg}")

    def sendMsgToAll(self, msg):
        msg = f"[SERVER - TO ALL] {msg}"
        for sock in self.listOfSockets:
            if sock == self.sockL:
                continue
            sock.send(bytearray(msg, "ASCII"))
        self.msgToServer(msg)

    def msgToServer(self, msg):
        self.GUI.updateMessages(msg)

    def addClientConnection(self, msg):
        self.GUI.addConnection(msg)

    def clientDisconnected(self, adr):
        self.GUI.removeConnection(adr)
        
    def run(self):
        while self.serverOpen:
            try:
                tup = select.select(self.listOfSockets, [], [])
                sock = tup[0][0]
                if sock == self.sockL:
                    clts, adr = self.sockL.accept()
                    self.listOfSockets.append(clts)
                    msg = f"[{adr}] connected"
                    self.msgToServer(msg)
                    self.addClientConnection(str(adr))
                    for sock in self.listOfSockets:
                        if sock == self.sockL:
                            continue
                        sock.send(bytearray(msg, "ASCII"))
                else:
                    data = sock.recv(2048)
                    if not data: 
                        self.listOfSockets.remove(sock)
                        msg = f"[{sock.getpeername()}] disconnected"
                        self.msgToServer(msg)
                        self.clientDisconnected(str(sock.getpeername()))
                        for sock1 in self.listOfSockets:
                            if sock1 == self.sockL:
                                continue
                            sock1.send(bytearray(msg,"ASCII"))
                        sock.close()
                    else:
                        data = data.decode("ASCII")
                        msg = f"[{sock.getpeername()}] {data}"
                        self.msgToServer(msg)
                        for sock1 in self.listOfSockets:
                            if sock1 == self.sockL:
                                continue
                            sock1.send(bytearray(msg,"ASCII"))
            except:
                continue  

