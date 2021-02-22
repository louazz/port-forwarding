import socket
import os

Host = '0.0.0.0'
Port = 8080
#create a stream socket "s"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #bind the Host to the port
    s.bind((Host,Port))
    # 5 is the number of client that could be connected simultanously
    s.listen(5)
    #accept requests / server is up
    conn, addr = s.accept()
    print("successfully connected by", addr)
    #wait to recieve the type of the request
    data=  conn.recv(1024)
    while True:
        #if the request is a GET request (data are encoded using utf-8)
        if data.decode("utf-8")=="GET":
            print("GET request recieved from client")
            #wait for file name
            file= conn.recv(1024)
            #decode file name
            file_name=file.decode("utf-8")
            #get the file size
            file_size=os.stat(file_name).st_size
            #convert file size to byte
            tmp= file_size.to_bytes(2, byteorder='big')
            #send file size
            conn.send(tmp)
            # open the file in read mode (copy)
            f=open(file_name,"rb")
            print("Sending file")
            #extract the whole file
            whole_file= f.read(file_size)
            #send the whole file
            conn.send(whole_file)
            #close the file
            f.close()
            print("file sent")
            #close connection
            conn.close()
        if data.decode("utf-8")=="POST":
            print("POST request from client: recieved")
            #wait for file name
            file= conn.recv(1024)
            #decode file name
            file_name=file.decode("utf-8")
            #get the file size
            size=conn.recv(1024)
            #create a file with the same file name or open existing one with same file name
            f=open(file_name,"wb")
            print("writing file")
            #extract the recieved file
            whole_file=conn.recv(int.from_bytes(size, 'big'))
            print(whole_file)
            #write the data in the new file
            f.write(whole_file)
            #close the file
            f.close()
            print("file recieved and written")
            #close connection
            conn.close()
