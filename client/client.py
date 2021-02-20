import socket

Host = '192.168.61.93' #change the Host to your ip address
Port = 8080
#start a socket stream
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    #connect the host with the port
    c.connect((Host,Port))
    command= input("Enter GET or POST method \n")
    #send input GET or POST
    c.send(command.encode('utf-8'))
    file=input("enter file name \n")
    #send file name
    c.send(file.encode('utf-8'))
    if(command=="GET"):
        #create a new file with "copied_file" name
        f= open("copied_file","wb")
        print("getting file")
        #recieve the first line
        line=c.recv(1024)
        while line:
            #write the recieved line
            f.write(line)
            print(line)
            #recieve next line
            line=c.recv(1024)
        #close file
        f.close()
        print("well recieved")
    if(command=="POST"):
        #open file in read mode (copy)
        f= open(file, "rb")
        print("sending file")
        #extract the first line
        line= f.read(1024)
        while line:
            #send the extracted line
            c.send(line)
            #extract the next line
            line= f.read(1024)
        #close file
        f.close()
        print("well sent")
    #close connection
    c.close()
