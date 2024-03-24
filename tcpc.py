from socket import *
import pickle
import ssl

serverName = "localhost"
serverPort = 8082

server_sni_hostname = 'pritpreeth.com'
server_cert = 'server.crt'
client_cert = 'client.crt'
client_key = 'client.key'

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=server_cert)
context.load_cert_chain(certfile=client_cert, keyfile=client_key)   # Loading the certificate generated
# print("SSL established. Peer: {}".format(clientSocket.getpeercert()))







# Checking if pawn is in the corner, edge or middle
def change(r,c,color):
    global l,b
    
    if r>0 and r<7 and c>0 and c<7:
        mid(r,c,color)

    elif (r==0 and c==0) or (r==0 and c==7) or (r==7 and c==0) or (r==7 and c==7):
        corn(r,c,color)

    elif r==0 or c==0 or r==7 or c==7:
        edge(r,c,color)
    
    if flag==0:
        return -1

# Box above pawn
def N(r,c,color):
    global l,flag
    if l[r-1][c]==(not color):
        i=1
        while 0<=(r-i)<=7 and (l[r-i][c]==(not color)):
            i=i+1
        if (-1!=r-i) or (r-i!=8):
            if l[r-i][c]==color:
                j=1
                while l[r-j][c]==(not color):
                    l[r-j][c]=color
                    b[r-j][c]=groups[str(color)]
                    j=j+1
                l[r][c]=color
                flag=1

# Box right of pawn
def E(r,c,color):
    global l,flag
    if l[r][c+1]==(not color):
        i=1
        while 0<=(c+i)<=7 and (l[r][c+i]==(not color)):
            i=i+1
        if (-1!=c+i) or (c+i!=8):
            if l[r][c+i]==color:
                j=1
                while l[r][c+j]==(not color):
                    l[r][c+j]=color
                    b[r][c+j]=groups[str(color)]
                    j=j+1
                l[r][c]=color
                flag=2

# Box below pawn
def S(r,c,color):
    global l,flag
    if l[r+1][c]==(not color):
        i=1
        while (l[r+i][c]==(not color)) and 0<=(r+i)<=7:
            i=i+1
        if (-1!=r+i) or (r+i!=8):
            if l[r+i][c]==color:
                j=1
                while l[r+j][c]==(not color):
                    l[r+j][c]=color
                    b[r+j][c]=groups[str(color)]
                    j=j+1
                l[r][c]=color
                flag=3

# Box left of pawn
def W(r,c,color):
    global l,flag
    if l[r][c-1]==(not color):
        i=1
        while (l[r][c-i]==(not color)) and 0<=(c-i)<=7:
            i=i+1
        if (-1!=c-i) or (c-i<=8):
            if l[r][c-i]==color:
                j=1
                while l[r][c-j]==(not color):
                    l[r][c-j]=color
                    b[r][c-j]=groups[str(color)]
                    j=j+1
                l[r][c]=color
                flag=4

# Box to the top left of pawn
def NW(r,c,color):
    global l,flag
    if l[r-1][c-1]==(not color):
        i=1
        while (l[r-i][c-i]==(not color)) and 0<=(c-i)<=7 and 0<=(r-i)<=7:
            i=i+1
        if (-1!=c-i) or (c-i!=8):  #c-i==r-i condition satisfied for both
            if l[r-i][c-i]==color:
                j=1
                while l[r-j][c-j]==(not color):
                    l[r-j][c-j]=color
                    b[r-j][c-j]=groups[str(color)]
                    j=j+1
                l[r][c]=color
                flag=5

# Box to the top right of pawn
def NE(r,c,color):
    global l,flag
    if l[r-1][c+1]==(not color):
        i=1
        while 0<=(c+i)<=7 and 0<=(r-i)<=7 and (l[r-i][c+i]==(not color)):
            i=i+1
        if (-1!=c+i) or (c+i!=8):  #c-i==r-i condition satisfied for both
            if l[r-i][c+i]==color:
                j=1
                while l[r-j][c+j]==(not color):
                    l[r-j][c+j]=color
                    b[r-j][c+j]=groups[str(color)]
                    j=j+1
                l[r][c]=color
                flag=6

# Box to the down right of pawn
def SE(r,c,color):
    global l,flag
    if l[r+1][c+1]==(not color):
        i=1
        while (l[r+i][c+i]==(not color)) and 0<=(c+i)<=7 and 0<=(r+i)<=7:
            i=i+1
        if (-1!=c+i) or (c+i!=8):  #c-i==r-i condition satisfied for both
            if l[r+i][c+i]==color:
                j=1
                while l[r+j][c+j]==(not color):
                    l[r+j][c+j]=color
                    b[r+j][c+j]=groups[str(color)]
                    j=j+1
                l[r][c]=color
                flag=7

# Box to the down left of pawn
def SW(r,c,color):
    global l,flag
    if l[r+1][c-1]==(not color):
        i=1
        while (l[r+i][c-i]==(not color)) and 0<=(c-i)<=7 and 0<=(r+i)<=7:
            i=i+1
        if (-1!=c-i) or (c-i!=8):  #c-i==r-i condition satisfied for both
            if l[r+i][c-i]==color:
                j=1
                while l[r+j][c-j]==(not color):
                    l[r+j][c-j]=color
                    b[r+j][c-j]=groups[str(color)]
                    j=j+1
                l[r][c]=color
                flag=8


# Update if move is in the middle of the board
def mid(r,c,color):
    global flag,l
    flag=0
    N(r,c,color)
    E(r,c,color)
    S(r,c,color)
    W(r,c,color)
    NW(r,c,color)
    NE(r,c,color)
    SE(r,c,color)
    SW(r,c,color)


# Update if move is in the corner of the board
def corn(r,c,color):
    global flag,l
    flag=0
    if (r==0 and c==0):
        E(r,c,color)
        SE(r,c,color)
        S(r,c,color)

    elif (r==0 and c==7):
        W(r,c,color)
        SW(r,c,color)
        S(r,c,color)

    elif (r==7 and c==0):
        N(r,c,color)
        NE(r,c,color)
        E(r,c,color)
    
    elif (r==7 and c==7):
        N(r,c,color)
        NW(r,c,color)
        W(r,c,color)


#Update if move is in the edge of the board
def edge(r,c,color):
    global flag,l
    flag=0
    if (r==0):
        E(r,c,color)
        S(r,c,color)
        W(r,c,color)
        SE(r,c,color)
        SW(r,c,color)
    
    elif (r==7):
        N(r,c,color)
        E(r,c,color)
        W(r,c,color)
        NW(r,c,color)
        NE(r,c,color)

    elif (c==0):
        N(r,c,color)
        E(r,c,color)
        S(r,c,color)
        NE(r,c,color)
        SE(r,c,color)

    elif (c==7):
        N(r,c,color)
        S(r,c,color)
        W(r,c,color)
        NW(r,c,color)
        SW(r,c,color)


def finish(color):
    return str(l).find(str(int(not color)))



groups={"0":"O","1":"X"}
jolt=0
global l
l=[]
for i in range(8):
    ls=[]    
    for j in range(8):
        if (i==3 and j==3) or (i==4 and j==4):
            ls.append(1)
        elif (i==3 and j==4) or (i==4 and j==3): 
            ls.append(0)
        else:
            ls.append(2)
    l.append(ls)


b=[]
for i in range(8):
    ls=[]    
    for j in range(8):
        if (i==3 and j==3) or (i==4 and j==4):
            ls.append('o')
        elif (i==3 and j==4) or (i==4 and j==3): 
            ls.append('x')
        else:
            ls.append(2)
    b.append(ls)



print("\nHi Welcome to Othello")
print("                 ~ Prithvi and Preetham") 

print("\nRULES:")
print("Othello is a board game played by two players on an 8x8 grid. Each player has discs of a distinct")
print("color, usually black and white. The game starts with four discs placed in the center of the grid in a ")
print("specific pattern, with two of each color diagonally adjacent to each other.\n")
print("Players take turns placing one disc of their color on the board. A player must place a disc so that it ")
print("'flanks' at least one opposing disc in a straight line. Flanked discs are flipped to the current ")
print("player's color.\n")
print("The game ends when the board is filled or neither player can make a legal move. The player with")
print("the most discs of their color on the board wins.\n")

for el in l:
            for le in el:
                if le==2:
                    print("_",end="|")
                else:
                    print(le,end="|")
            print()





while True:
    soc = socket(AF_INET, SOCK_STREAM)  # Creating socket
    clientSocket = context.wrap_socket(soc, server_side=False, server_hostname=server_sni_hostname) # Wrapping ssl to socket connection

    clientSocket.connect((serverName,serverPort))   # Connect to server
    # Checking if player 2 won
    res=finish(1)
    if (res==-1):
        jolt=2
        print("\nP2 wins")
        clientSocket.close()



    else:
        print("\nIt is your turn")
        r1=int(input("Enter row for p1 "))
        c1=int(input("Enter col for p1 "))
        print()
        
        # Checking if move is valid or invalid
        valid=change(r1,c1,0)
        while valid==-1:
            print("Invalid Position")
            r1=int(input("Enter row for p1 "))
            c1=int(input("Enter col for p1 "))
            print()
            valid=change(r1,c1,0)

        for el in l:
            for le in el:
                if le==2:
                    print("_",end="|")
                else:
                    print(le,end="|")
            print()

        res=finish(0)
        if (res==-1):
            jolt=1
            

        # Checking if player 1 wins
        if jolt==1:
            print("\nP1 wins")
        elif jolt==2:
            print("\nP2 wins")





        print()
        clientSocket.send(pickle.dumps(l))          #Send updated list
        l = pickle.loads(clientSocket.recv(1024))   # Recieve updated list
        print()
        for el in l:
            for le in el:
                if le==2:
                    print("_",end="|")
                else:
                    print(le,end="|")
            print()
            
        clientSocket.close()

