import socket

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
            # open the file in read mode (copy)
            f=open(file_name,"rb")
            print("Sending file")
            #extract the first line
            line= f.read(1024)
            while(line):
                #send the line to the client
                conn.send(line)
                #extract the next line
                line=f.read(1024)
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
            #crate a file with the same file name or open existing one with same file name
            f=open(file_name,"wb")
            print("writing file")
            #extract the recieved first line
            line=conn.recv(1024)
            while line:
                #write the line extracted
                f.write(line)
                #extract the recieved next line
                line=conn.recv(1024)
            #close the file
            f.close()
            print("file recieved and written")

            #close connection
            conn.close()
