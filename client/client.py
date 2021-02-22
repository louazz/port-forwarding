import socket
import os

Host = '192.168.0.8' #change the Host to your ip address
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
        #get file size
        size=c.recv(1024)
        #create a new file with "copied_file" name
        f= open("copied_file","wb")
        print("getting file")
        #recieve the whole file at once
        whole_file=c.recv(int.from_bytes(size, 'big'))
        #write the whole file's data into the new file
        f.write(whole_file)
        print(whole_file)
        #close file
        f.close()
        print("well recieved")
    if(command=="POST"):
        #open file in read mode (copy)
        f= open(file, "rb")
        print("sending file")
        #get file size
        file_size=os.stat(file).st_size
        #convert file size to byte
        tmp= file_size.to_bytes(2, byteorder='big')
        c.send(tmp)
        #extract the whole file
        whole_file= f.read(file_size)
        print(whole_file)
        #send the whole file
        c.send(whole_file)
        #close file
        f.close()
        print("well sent")
    #close connection
    c.close()
