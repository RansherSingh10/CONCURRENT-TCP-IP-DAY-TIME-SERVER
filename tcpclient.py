import socket
def client():
    
    s=socket.socket()
    
    host='127.0.0.1'
    port=15000
    s.connect((host,port))
    while(True):
        print("Type in your request: ", end='')
        num=(input())
        if(num == 'quit'):
            s.close()
            break

        s.send(num.encode())
        data=s.recv(1024).decode()
        print('This is the response: '+ data)
        
client()
