# -*- coding: utf-8 -*-

import socket
import threading
import config
import getPack
import createPack
import SignUp, SignIn, clientSearch
import pickle

'''
PACKET

"REQUEST_TYPE": 1 - sendData/ 2 - signUp/ 3 - chLogin/
                4 - chPasswrd/ 5 - signIn/ 6 - findClient/
"ADRESSER_NAME": loginA
"ADRESSER_PASSWORD": password
"ADRESSEE_NAME": loginB
"DATA": message
'''
 
options = config.serverSettings()
online = {}

def closeconn(connection):
    connection.close()

def launchServer():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(options.address())
    sock.listen(options.maxConn())
    while True:
        connection, (clientIP, clientPort) = sock.accept()
        if clientIP not in options.stopList():
            #add in log about new connection
            thread = threading.Thread(target = packetProcessing,
                                  args = (connection, 1))
            thread.daemon = True 
            thread.start()
            print(online)
        
        else:
            #add in log about stoplist-user attempt
            closeconn(connection)
        
    
def packetProcessing(connection, k):
    while connection:
        try:
            packet = getPack.packetRecv(connection)                           
            request_type = {'1': sendData, 
            '2': regist, 
            '3': chLogin, 
            '4': chPasswrd, 
            '5': auth, 
            '6': findClient}[packet["REQUEST_TYPE"]](connection, packet)
        except TypeError:
            connection.close()
            continue
    else:
        connection.close()
    

def sendData(connection, packet):
    print(packet)
    loginA = packet["ADRESSER_NAME"]
    loginB = packet["ADRESSEE_NAME"]
    if loginB in online:
        online[loginB].sendall(createPack.create('1', loginA, None, loginB, packet["DATA"]))
    else:
        connection.sendall(createPack.create('1', loginA, None, None, '0'.encode('utf-8')))


def regist(connection, packet):
    login = packet["ADRESSER_NAME"]
    password = packet["ADRESSER_PASSWORD"]
    status = SignUp.addUser(options.DB(), login, password)
    connection.sendall(createPack.create('2', login, None, None, status))
    connection.close()
        

def chLogin(connection, packet):
    login = packet["ADRESSER_NAME"]
    password = packet["ADRESSER_PASSWORD"]
    status = changeLogPass.change(options.DB(), 1, login, password, packet["DATA"])
    connection.sendall(createPack.create('3', login, None, None, status))


def chPasswrd(connection, packet):
    login = packet["ADRESSER_NAME"]
    password = packet["ADRESSER_PASSWORD"]
    status = changeLogPass.change(options.DB(), 2, login, password, packet["DATA"])
    connection.sendall(createPack.create('4', login, None, None, status))


def auth(connection, packet):
    login = packet["ADRESSER_NAME"]
    password = packet["ADRESSER_PASSWORD"]
    status = SignIn.authentication(options.DB(), login, password)
    connection.sendall(createPack.create('5', login, None, None, status))
    if status:
        online.update({login:connection})
    

def findClient(connection, packet):
    loginA = packet["ADRESSER_NAME"]
    loginB = packet["ADRESSEE_NAME"]
    status = clientSearch.find(options.DB(), loginB)
    if status:
        if loginB in online:
            status = "1 1"
        else:
            status = "1 0"
    connection.sendall(createPack.create('6', loginA, loginB, None, status))
    

def offClient(connection, packet):
    login = packet["ADRESSER_NAME"]
    online.pop(login, connection)
    connection.close()
    
    
def main():
    #logging settings
    launchServer()
    


if __name__ == "__main__":
    main()