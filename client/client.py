import socket

Host = '192.168.61.93'
Port = 8080
#
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    
    c.connect((Host,Port))
    command= input("Enter GET or POST method \n")
    c.send(command.encode('utf-8'))
    file=input("enter file name \n")
    c.send(file.encode('utf-8'))
    if(command=="GET"):
        f= open("copied_file","wb")
        print("getting file")
        line=c.recv(1024)
        while line:
            f.write(line)
            print(line)
            line=c.recv(1024)
        f.close()
        print("well recieved")
    if(command=="POST"):
        f= open(file, "rb")
        print("sending file")
        line= f.read(1024)
        while line:
            c.send(line)
            line= f.read(1024)
        f.close()
        print("well sent")
    c.close()
