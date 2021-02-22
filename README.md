# port-forwarding
The code below shows the implementation of a client-server TCP communication using port forwarding.

## Requirements:
 - Python 3
 - Local ip address

#### Finding local ip address:
 -Linux: `ifconfig -a`  
 -Mac OS: `ipconfig getifaddr en0`<br />
 -Windows: `ipconfig`
###### Substitute the Host address within the client.py file with your ip address

## Run:
  1. Run the server:
     `cd ./server`
     `python3 server.py`
  3. Run the client:
     `cd ./client`
     `python3 client.py`<br />
 -You will be asked to choose POST or GET request. Make sure that if you choose GET option, the file name that you'll choose later is available in the target machine. If you choose POST request you should specify a file within your computer that will be transferred to the server's machine.
##Remark
 The faster's branch code demonstrates the transfer of a whole file at once. The idea is to retrieve the size of the target file then send it to the client or server depending on the type of the request. Using this methodology the time and space complexity will significantly decrease.
 
#### The Architect: **Louai Zaiter**
