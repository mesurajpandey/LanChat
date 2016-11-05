import socket
import sys
import Tkinter
from thread import *
from Tkconstants import *
import os

def createSocket(hostName):
    try:
        sck = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error,msg:
        print 'Failed to create socket. Error code:' +str(msg[0])+ ', Error message: ' + msg[1]
        sys.exit()
    print 'socket created'
    host = hostName
    port = 8882
    try:
        remote_ip = socket.gethostbyname(host)
        #remote_ip = socket.gethostbyaddr("192.168.1.15")
        print remote_ip
    except socket.gaierror:
        print 'Host name could not be resolved.Exiting..'
        sys.exit()

    #remote_ip = socket.gethostbyaddr("10.200.1.109")
    #remote_ip = socket.gethostbyname(hostName)
    sck.connect((remote_ip,port))
    #sck.connect(('192.168.1.15',port))
    
    print 'Socket connected to ' + host + ' on ip ' + str(remote_ip[2])
    return sck,remote_ip

def sendMessage(sck,message,label,textBox):
    print sck
    print message
    try:
        sck.sendall(message)
    except socket.error:
        print 'Send Failed'
        sys.exit()
    print 'message sent'
    label.config(text=label.cget("text")+"You Said: "+message)
    textBox.delete(0.0,END)
    textBox.mark_set("insert", "%d.%d" % (0, 0))
    #textBox.insert(1.0,"h\b")
    #textBox.delete(1.0,END)
    
    
    
def stopChat():
    tk1.destroy()
    

def startChat():
    tk1 = Tkinter.Tk()
    frame1 = Tkinter.Frame(tk1,relief=RIDGE,borderwidth=2)
    frame1.pack(fill=BOTH,expand=1)
    textBox = Tkinter.Text(frame1,height=2,width=30,background='white')
    textBox.pack(fill=X,expand=1,side=BOTTOM)
    label = Tkinter.Label(frame1,text="",height = 10, width = 30)
    label.pack(fill=X,expand=1,side=TOP)
    button = Tkinter.Button(frame1,text="Close",command=tk1.destroy)
    button.pack(side=BOTTOM)
    sck,ip = createSocket(currentHost)
    allChatBox.append(label)
    PersonIpAndBoxLabel[ip] = label;
    connectedIPs[ip] = 1;
    #connectedHosts[currentChat] = label
    #sck = ""
    textBox.bind('<Return>',lambda event: sendMessage(sck,textBox.get("1.0",END),label,textBox))
    
    print 'chat Box Created'
    tk1.mainloop()
        

def createChatBox():
    #new_thread = start_new_thread(startChat,())
    #connectedHosts[currentChatBoxID] = 1
    startChat()
    #connectedHosts[currentChatBoxId] = 1
    


def createButton(textValue):
    currentHost = textValue
    #currentChatBoxId = identifier
    button = Tkinter.Button(frame,text=textValue,command=createChatBox) #TODO: Has to pass identifier as an argument
    button.pack(side=LEFT)

def getAllHosts():
    os.system('net view > conn.tmp')
    f = open('conn.tmp','r')
    f.readline();f.readline();f.readline()

    conn = []
    host = f.readline()
    while host[0] == '\\':
        conn.append(host[2:host.find(' ')])
        host = f.readline()
    hosts = conn
    f.close()

def runServer():
    HOST = ""
    PORT = 8882
    try:
        sck = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error,msg:
        print 'Failed to create socket. Error code:' +str(msg[0])+ ', Error message: ' + msg[1]
        sys.exit()
    print 'Server socket created'
    
    try:
        sck.bind((HOST,PORT))
    except socket.error,msg:
        print 'Bind Failed. Error code: ' + str(msg[0]) + ' message: ' + msg[1]
        sys.exit()

    print 'Socket Bind Complete'
    sck.listen(10)
    print 'Socket now listening'
    while 1:
        conn,addr = sck.accept()
        print 'Connected with ' + addr[0] + ' : ' + str(addr[1])
        data = conn.recv(1024)
        if data:
            #for ip in connectedIPs:
            #    if ip==addr[0]:
                    #print connectedIps.index(ip)
                    #chatBox = allChatBox[i] #in connectedIps.index(ip)
            print connectedIPs[addr[0]]
            if connectedIPs[addr[0]]==0:
                remote_ip = socket.gethostbyaddr(addr[0])
                currentHost = remote_ip[0]
                startChat()
            PersonIpAndBoxLabel[addr[0]].config(text=currentHost +" Said: "+data)
            #print ip
                    #if not chatBox:
                    #    remote_ip = socket.gethostbyaddr(ip)
                    #    currentHost = remote_ip[0]
                    #    startChat()
                    #allChatBox[i].config(text=currentHost +" Said: "+data)
                    #break
            #print addr[0]+" says: "+data
            # TODO:has to display in the chat Box
    
hosts = []
allChatBox = []
connectedHosts = []

currentChatBoxID = -1
currentHost = "JIWAN-PC"
#getAllHosts()
start_new_thread(runServer,())
tk = Tkinter.Tk()
frame = Tkinter.Frame(tk,relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = Tkinter.Label(frame,text = "Hello, World")
label.pack(fill=X,expand=1)


############################TODO:get all IPs
connectedIPs = {"192.168.1.15":0,"192.168.1.15":0}
PersonIpAndBoxLabel = {"192.168.1.15":Tkinter.Label,"192.168.1.15":Tkinter.Label}
createButton("Suraj")
#connectedHosts.append(0)
createButton("Sandip")
###################################
#connectedHosts.append(0)
tk.mainloop()
