from socket import *
import pickle
import ssl

serverHost="localhost"
serverPort = 8082

server_cert = 'server.crt'
server_key = 'server.key'
client_certs = 'client.crt'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(certfile=server_cert, keyfile=server_key)   # Loading the cerficate generated
context.load_verify_locations(cafile=client_certs)


serverSocket = socket(AF_INET,SOCK_STREAM)  # Creating socket 
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print("The server is ready to receive") # Confirming server side




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
        while (l[r-i][c]==(not color)) and 0<=(r-i)<=7:
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
        while (l[r][c+i]==(not color)) and 0<=(c+i)<=7:
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
        while (l[r-i][c+i]==(not color)) and 0<=(c+i)<=7 and 0<=(r-i)<=7:
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
    con, addr = serverSocket.accept()
    connectionSocket = context.wrap_socket(con, server_side=True)
    l = pickle.loads(connectionSocket.recv(1024))
    print()
    for el in l:
            for le in el:
                if le==2:
                    print("_",end="|")
                else:
                    print(le,end="|")
            print()


    # Checking if player 1 won
    res=finish(0)
    if (res==-1):
        jolt=1
        print("\nP1 wins")
        connectionSocket.close()



    else:
        print("\nIt is your turn now")
        r2=int(input("Enter row for p2 "))
        c2=int(input("Enter col for p2 "))
        print()

        # Checking if move is valid or invalid
        valid=change(r2,c2,1)
        while valid==-1:
            print("Invalid Position")
            r2=int(input("Enter row for p2 "))
            c2=int(input("Enter col for p2 "))
            print()
            valid=change(r2,c2,1)
        
        for el in l:
            for le in el:
                if le==2:
                    print("_",end="|")
                else:
                    print(le,end="|")
            print()

        res=finish(1)
        if (res==-1):
            jolt=2
            

        # Checking if player 1 wins
        if jolt==1:
            print("\nP1 wins")
        elif jolt==2:
            print("\nP2 wins")


    print()
    connectionSocket.send(pickle.dumps(l))  #Send updated list
    print()
    connectionSocket.close()











































# from tkinter import *
# from socket import *
# import pickle
# import ssl

# window=Tk()
# window.title("Othello Player 2")
# # window.geometry("930x650+0+0")
# window.resizable(width=True, height=True)
# window.configure(background='black')  #algae green



















# tops = Frame(window, bg ='#2E8B57', pady =2, width = 2500, height=60, relief = RIDGE)
# tops.grid(row=0, column =0)

# lblTitle = Label(tops, font=('arial',50,'bold'),text="Othello Game", bd=21, bg='Black',fg='White',justify = CENTER)
# lblTitle.grid(row=0,column = 0)

# mainFrame = Frame (window, bg = 'Powder Blue', bd=10,width = 1350, height=600, relief=RIDGE) 
# mainFrame.grid(row=1,column=0)

# leftFrame = Frame (mainFrame ,bd=3, width =750, height=500, pady=1, padx=10, bg="#2E8B57", relief=RIDGE)
# leftFrame.pack(side=LEFT)

# rightFrame = Frame (mainFrame,bd=3, width =560, height=500, padx=10, pady=2, bg="#2E8B57", relief=RIDGE)
# rightFrame.pack(side=RIGHT)

# rightFrame1=Frame(rightFrame , width=560, height=200, padx=10, pady=2, bg="#2E8B57", relief=RIDGE) 
# rightFrame1.grid(row=0, column=0,padx=10, pady=2, sticky="nsew")

# rightFrame2 = Frame(rightFrame, width =560, height=250, padx=10, pady=2, bg="#2E8B57", relief=RIDGE)
# rightFrame2.grid(row=1,column=0,padx=10, pady=2, sticky="nsew")

# rightFrame3=Frame(rightFrame , width=560, height=150, padx=10, pady=2, bg="#2E8B57", relief=RIDGE) 
# rightFrame3.grid(row=2, column=0)

# l=[]
# for i in range(8):
#     ls=[]    
#     for j in range(8):
#         if (i==3 and j==3) or (i==4 and j==4):
#             ls.append(1)
#         elif (i==3 and j==4) or (i==4 and j==3): 
#             ls.append(0)
#         else:
#             ls.append(2)
#     l.append(ls)
# print(l)


# colorcoding={"Black":0, "White":1, "#98FF98":2}

# def clicked(l,r,c):
#     return

# btn00 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[0][0]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn00.grid(column=1, row=1, sticky = S+N+E+W)
# btn01 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[0][1]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn01.grid(column=2, row=1, sticky = S+N+E+W)
# btn02 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[0][2]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn02.grid(column=3, row=1, sticky = S+N+E+W)
# btn03 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[0][3]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn03.grid(column=4, row=1, sticky = S+N+E+W)
# btn04 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[0][4]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn04.grid(column=5, row=1, sticky = S+N+E+W)
# btn05 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[0][5]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn05.grid(column=6, row=1, sticky = S+N+E+W)
# btn06 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[0][6]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn06.grid(column=7, row=1, sticky = S+N+E+W)
# btn07 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[0][7]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn07.grid(column=8, row=1, sticky = S+N+E+W)
# btn10 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[1][0]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn10.grid(column=1, row=2, sticky = S+N+E+W)
# btn11 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[1][1]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn11.grid(column=2, row=2, sticky = S+N+E+W)
# btn12 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[1][2]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn12.grid(column=3, row=2, sticky = S+N+E+W)
# btn13 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[1][3]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn13.grid(column=4, row=2, sticky = S+N+E+W)
# btn14 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[1][4]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn14.grid(column=5, row=2, sticky = S+N+E+W)
# btn15 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[1][5]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn15.grid(column=6, row=2, sticky = S+N+E+W)
# btn16 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[1][6]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn16.grid(column=7, row=2, sticky = S+N+E+W)
# btn17 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[1][7]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn17.grid(column=8, row=2, sticky = S+N+E+W)
# btn20 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[2][0]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn20.grid(column=1, row=3, sticky = S+N+E+W)
# btn21 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[2][1]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn21.grid(column=2, row=3, sticky = S+N+E+W)
# btn22 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[2][2]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn22.grid(column=3, row=3, sticky = S+N+E+W)
# btn23 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[2][3]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn23.grid(column=4, row=3, sticky = S+N+E+W)
# btn24 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[2][4]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn24.grid(column=5, row=3, sticky = S+N+E+W)
# btn25 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[2][5]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn25.grid(column=6, row=3, sticky = S+N+E+W)
# btn26 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[2][6]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn26.grid(column=7, row=3, sticky = S+N+E+W)
# btn27 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[2][7]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn27.grid(column=8, row=3, sticky = S+N+E+W)
# btn30 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[3][0]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn30.grid(column=1, row=4, sticky = S+N+E+W)
# btn31 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[3][1]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn31.grid(column=2, row=4, sticky = S+N+E+W)
# btn32 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[3][2]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn32.grid(column=3, row=4, sticky = S+N+E+W)
# btn33 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[3][3]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn33.grid(column=4, row=4, sticky = S+N+E+W)
# btn34 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[3][4]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn34.grid(column=5, row=4, sticky = S+N+E+W)
# btn35 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[3][5]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn35.grid(column=6, row=4, sticky = S+N+E+W)
# btn36 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[3][6]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn36.grid(column=7, row=4, sticky = S+N+E+W)
# btn37 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[3][7]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn37.grid(column=8, row=4, sticky = S+N+E+W)
# btn40 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[4][0]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn40.grid(column=1, row=5, sticky = S+N+E+W)
# btn41 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[4][1]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn41.grid(column=2, row=5, sticky = S+N+E+W)
# btn42 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[4][2]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn42.grid(column=3, row=5, sticky = S+N+E+W)
# btn43 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[4][3]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn43.grid(column=4, row=5, sticky = S+N+E+W)
# btn44 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[4][4]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn44.grid(column=5, row=5, sticky = S+N+E+W)
# btn45 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[4][5]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn45.grid(column=6, row=5, sticky = S+N+E+W)
# btn46 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[4][6]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn46.grid(column=7, row=5, sticky = S+N+E+W)
# btn47 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[4][7]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn47.grid(column=8, row=5, sticky = S+N+E+W)
# btn50 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[5][0]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn50.grid(column=1, row=6, sticky = S+N+E+W)
# btn51 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[5][1]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn51.grid(column=2, row=6, sticky = S+N+E+W)
# btn52 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[5][2]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn52.grid(column=3, row=6, sticky = S+N+E+W)
# btn53 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[5][3]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn53.grid(column=4, row=6, sticky = S+N+E+W)
# btn54 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[5][4]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn54.grid(column=5, row=6, sticky = S+N+E+W)
# btn55 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[5][5]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn55.grid(column=6, row=6, sticky = S+N+E+W)
# btn56 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[5][6]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn56.grid(column=7, row=6, sticky = S+N+E+W)
# btn57 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[5][7]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn57.grid(column=8, row=6, sticky = S+N+E+W)
# btn60 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[6][0]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn60.grid(column=1, row=7, sticky = S+N+E+W)
# btn61 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[6][1]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn61.grid(column=2, row=7, sticky = S+N+E+W)
# btn62 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[6][2]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn62.grid(column=3, row=7, sticky = S+N+E+W)
# btn63 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[6][3]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn63.grid(column=4, row=7, sticky = S+N+E+W)
# btn64 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[6][4]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn64.grid(column=5, row=7, sticky = S+N+E+W)
# btn65 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[6][5]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn65.grid(column=6, row=7, sticky = S+N+E+W)
# btn66 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[6][6]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn66.grid(column=7, row=7, sticky = S+N+E+W)
# btn67 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[6][7]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn67.grid(column=8, row=7, sticky = S+N+E+W)
# btn70 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[7][0]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn70.grid(column=1, row=8, sticky = S+N+E+W)
# btn71 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[7][1]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn71.grid(column=2, row=8, sticky = S+N+E+W)
# btn72 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[7][2]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn72.grid(column=3, row=8, sticky = S+N+E+W)
# btn73 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[7][3]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn73.grid(column=4, row=8, sticky = S+N+E+W)
# btn74 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[7][4]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn74.grid(column=5, row=8, sticky = S+N+E+W)
# btn75 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[7][5]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn75.grid(column=6, row=8, sticky = S+N+E+W)
# btn76 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[7][6]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn76.grid(column=7, row=8, sticky = S+N+E+W)
# btn77 = Label(leftFrame, text="O",bg="#98FF98", fg=list(colorcoding.keys())[l[7][7]],width=3,height=1,borderwidth=2,relief="solid",highlightbackground="Black", font=('Ariel', 26))
# btn77.grid(column=8, row=8, sticky = S+N+E+W)







# lblGames=Label(rightFrame2, font=('arial', 20, 'bold'), text=" ",padx=2, pady=2, bg="#2E8B57",width=10) 
# lblGames.grid (row=0, column=1, sticky=W)
# lbl=Label(rightFrame2, font=('arial', 20, 'bold'), text="Row:",padx=2, pady=2, bg="#2E8B57") 
# lbl.grid (row=1, column=0, sticky=W)
# lblWon=Label(rightFrame2, font=('arial', 20, 'bold'), text=" ",padx=2, pady=2, bg="#2E8B57",width=10) 
# lblWon.grid (row=1, column=1, sticky=W)
# entry_row = Entry(rightFrame2, font=('arial', 20, 'bold'),width="5")
# entry_row.grid(row=1, column=1)
# lbl=Label(rightFrame2, font=('arial', 20, 'bold'), text="Column:",padx=2, pady=2, bg="#2E8B57") 
# lbl.grid (row=2, column=0, sticky=W)
# entry_column = Entry(rightFrame2, font=('arial', 20, 'bold'),width="5")
# entry_column.grid(row=2, column=1)

# lblUsername=Label(rightFrame1, font=('arial', 20, 'bold'), text="",padx=2, pady=2, bg="#2E8B57",width=10) 
# lblUsername.grid (row=0, column=1, sticky=W)
# lbl=Label(rightFrame1, font=('arial', 20, 'bold'), text="Color: ",padx=2, pady=2, bg="#2E8B57") 
# lbl.grid (row=1, column=0, sticky=W)
# lblTurn=Label(rightFrame1, font=('arial', 20, 'bold'), text="White",padx=2, pady=2, bg="#2E8B57",width=12) 
# lblTurn.grid (row=1, column=1, sticky=W)































# serverHost="localhost"
# serverPort = 8082

# server_cert = 'server.crt'
# server_key = 'server.key'
# client_certs = 'client.crt'

# context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# context.verify_mode = ssl.CERT_REQUIRED
# context.load_cert_chain(certfile=server_cert, keyfile=server_key)
# context.load_verify_locations(cafile=client_certs)


# serverSocket = socket(AF_INET,SOCK_STREAM)
# serverSocket.bind(("",serverPort))
# serverSocket.listen(1)
# print("The server is ready to receive")



















# def change(r,c,color):
#     global l,b
    
#     if r>0 and r<7 and c>0 and c<7:
#         mid(r,c,color)

#     elif (r==0 and c==0) or (r==0 and c==7) or (r==7 and c==0) or (r==7 and c==7):
#         corn(r,c,color)

#     elif r==0 or c==0 or r==7 or c==7:
#         edge(r,c,color)
    
#     if flag==0:
#         return -1

# def N(r,c,color):
#     global l,flag
#     if l[r-1][c]==(not color):
#         i=1
#         while (l[r-i][c]==(not color)) and 0<=(r-i)<=7:
#             i=i+1
#         if (-1!=r-i) or (r-i!=8):
#             if l[r-i][c]==color:
#                 j=1
#                 while l[r-j][c]==(not color):
#                     l[r-j][c]=color
#                     b[r-j][c]=groups[str(color)]
#                     j=j+1
#                 l[r][c]=color
#                 flag=1

# def E(r,c,color):
#     global l,flag
#     if l[r][c+1]==(not color):
#         i=1
#         while (l[r][c+i]==(not color)) and 0<=(c+i)<=7:
#             i=i+1
#         if (-1!=c+i) or (c+i!=8):
#             if l[r][c+i]==color:
#                 j=1
#                 while l[r][c+j]==(not color):
#                     l[r][c+j]=color
#                     b[r][c+j]=groups[str(color)]
#                     j=j+1
#                 l[r][c]=color
#                 flag=2

# def S(r,c,color):
#     global l,flag
#     if l[r+1][c]==(not color):
#         i=1
#         while (l[r+i][c]==(not color)) and 0<=(r+i)<=7:
#             i=i+1
#         if (-1!=r+i) or (r+i!=8):
#             if l[r+i][c]==color:
#                 j=1
#                 while l[r+j][c]==(not color):
#                     l[r+j][c]=color
#                     b[r+j][c]=groups[str(color)]
#                     j=j+1
#                 l[r][c]=color
#                 flag=3

# def W(r,c,color):
#     global l,flag
#     if l[r][c-1]==(not color):
#         i=1
#         while (l[r][c-i]==(not color)) and 0<=(c-i)<=7:
#             i=i+1
#         if (-1!=c-i) or (c-i<=8):
#             if l[r][c-i]==color:
#                 j=1
#                 while l[r][c-j]==(not color):
#                     l[r][c-j]=color
#                     b[r][c-j]=groups[str(color)]
#                     j=j+1
#                 l[r][c]=color
#                 flag=4

# def NW(r,c,color):
#     global l,flag
#     if l[r-1][c-1]==(not color):
#         i=1
#         while (l[r-i][c-i]==(not color)) and 0<=(c-i)<=7 and 0<=(r-i)<=7:
#             i=i+1
#         if (-1!=c-i) or (c-i!=8):  #c-i==r-i condition satisfied for both
#             if l[r-i][c-i]==color:
#                 j=1
#                 while l[r-j][c-j]==(not color):
#                     l[r-j][c-j]=color
#                     b[r-j][c-j]=groups[str(color)]
#                     j=j+1
#                 l[r][c]=color
#                 flag=5

# def NE(r,c,color):
#     global l,flag
#     if l[r-1][c+1]==(not color):
#         i=1
#         while (l[r-i][c+i]==(not color)) and 0<=(c+i)<=7 and 0<=(r-i)<=7:
#             i=i+1
#         if (-1!=c+i) or (c+i!=8):  #c-i==r-i condition satisfied for both
#             if l[r-i][c+i]==color:
#                 j=1
#                 while l[r-j][c+j]==(not color):
#                     l[r-j][c+j]=color
#                     b[r-j][c+j]=groups[str(color)]
#                     j=j+1
#                 l[r][c]=color
#                 flag=6

# def SE(r,c,color):
#     global l,flag
#     if l[r+1][c+1]==(not color):
#         i=1
#         while (l[r+i][c+i]==(not color)) and 0<=(c+i)<=7 and 0<=(r+i)<=7:
#             i=i+1
#         if (-1!=c+i) or (c+i!=8):  #c-i==r-i condition satisfied for both
#             if l[r+i][c+i]==color:
#                 j=1
#                 while l[r+j][c+j]==(not color):
#                     l[r+j][c+j]=color
#                     b[r+j][c+j]=groups[str(color)]
#                     j=j+1
#                 l[r][c]=color
#                 flag=7

# def SW(r,c,color):
#     global l,flag
#     if l[r+1][c-1]==(not color):
#         i=1
#         while (l[r+i][c-i]==(not color)) and 0<=(c-i)<=7 and 0<=(r+i)<=7:
#             i=i+1
#         if (-1!=c-i) or (c-i!=8):  #c-i==r-i condition satisfied for both
#             if l[r+i][c-i]==color:
#                 j=1
#                 while l[r+j][c-j]==(not color):
#                     l[r+j][c-j]=color
#                     b[r+j][c-j]=groups[str(color)]
#                     j=j+1
#                 l[r][c]=color
#                 flag=8


# def mid(r,c,color):
#     global flag,l
#     flag=0
#     print("\n",l[r][c],"\n")
#     N(r,c,color)
#     E(r,c,color)
#     S(r,c,color)
#     W(r,c,color)
#     NW(r,c,color)
#     NE(r,c,color)
#     SE(r,c,color)
#     SW(r,c,color)
#     print("\n",l[r][c],"\n")

    
# def corn(r,c,color):
#     global flag,l
#     flag=0
#     if (r==0 and c==0):
#         E(r,c,color)
#         SE(r,c,color)
#         S(r,c,color)

#     elif (r==0 and c==7):
#         W(r,c,color)
#         SW(r,c,color)
#         S(r,c,color)

#     elif (r==7 and c==0):
#         N(r,c,color)
#         NE(r,c,color)
#         E(r,c,color)
    
#     elif (r==7 and c==7):
#         N(r,c,color)
#         NW(r,c,color)
#         W(r,c,color)


# def edge(r,c,color):
#     global flag,l
#     flag=0
#     if (r==0):
#         E(r,c,color)
#         S(r,c,color)
#         W(r,c,color)
#         SE(r,c,color)
#         SW(r,c,color)
    
#     elif (r==7):
#         N(r,c,color)
#         E(r,c,color)
#         W(r,c,color)
#         NW(r,c,color)
#         NE(r,c,color)

#     elif (c==0):
#         N(r,c,color)
#         E(r,c,color)
#         S(r,c,color)
#         NE(r,c,color)
#         SE(r,c,color)

#     elif (c==7):
#         N(r,c,color)
#         S(r,c,color)
#         W(r,c,color)
#         NW(r,c,color)
#         SW(r,c,color)


# def finish(color):
#     return str(l).find(str(int(not color)))



# groups={"0":"O","1":"X"}
# jolt=0

# l=[]
# for i in range(8):
#     ls=[]    
#     for j in range(8):
#         if (i==3 and j==3) or (i==4 and j==4):
#             ls.append(1)
#         elif (i==3 and j==4) or (i==4 and j==3): 
#             ls.append(0)
#         else:
#             ls.append(2)
#     l.append(ls)


# b=[]
# for i in range(8):
#     ls=[]    
#     for j in range(8):
#         if (i==3 and j==3) or (i==4 and j==4):
#             ls.append('o')
#         elif (i==3 and j==4) or (i==4 and j==3): 
#             ls.append('x')
#         else:
#             ls.append(2)
#     b.append(ls)
# for el in l:
#         print(el)







# def clickSubmit():
#     con, addr = serverSocket.accept()
#     connectionSocket = context.wrap_socket(con, server_side=True)
#     print("SSL established. Peer: {}".format(connectionSocket.getpeercert()))
#     l = pickle.loads(connectionSocket.recv(1024))
#     for el in l:
#             print(el)

#     res=finish(0)
#     if (res==-1):
#         jolt=1
#         print("\nP1 wins")
#         connectionSocket.close()



#     else:
#         print("\nIt is your turn now")
#         # r2=int(input("Enter row for p2 "))
#         # c2=int(input("Enter col for p2 "))
#         r2=int(entry_row.get())
#         c2=int(entry_column.get())

#         valid=change(r2,c2,1)
#         while valid==-1:
#             print("Invalid Position")
#             # r2=int(input("Enter row for p2 "))
#             # c2=int(input("Enter col for p2 "))
#             r2=int(entry_row.get())
#             c2=int(entry_column.get())
#             valid=change(r2,c2,1)

#         for el in l:
#             print(el)

#         res=finish(1)
#         if (res==-1):
#             jolt=2
            


#         if jolt==1:
#             print("\nP1 wins")
#         elif jolt==2:
#             print("\nP2 wins")

#     # capitalizedSentence = sentence.upper()
   
#     connectionSocket.send(pickle.dumps(l))
        
#     connectionSocket.shutdown(socket.SHUT_RDWR)
#     connectionSocket.close()



# btnSubmit=Button(rightFrame3, text="Submit", font=('arial', 17, 'bold'), height = 1, width =20,command=clickSubmit)
# btnSubmit.grid (row=2, column=0 ,padx=6, pady=11)

# window.mainloop()



















































































# # from socket import *
# # import pickle
# # import ssl

# # serverHost="localhost"
# # serverPort = 8082

# # server_cert = 'server.crt'
# # server_key = 'server.key'
# # client_certs = 'client.crt'

# # context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# # context.verify_mode = ssl.CERT_REQUIRED
# # context.load_cert_chain(certfile=server_cert, keyfile=server_key)
# # context.load_verify_locations(cafile=client_certs)


# # serverSocket = socket(AF_INET,SOCK_STREAM)
# # serverSocket.bind(("",serverPort))
# # serverSocket.listen(1)
# # print("The server is ready to receive")














# # def change(r,c,color):
# #     global l,b
    
# #     if r>0 and r<7 and c>0 and c<7:
# #         mid(r,c,color)

# #     elif (r==0 and c==0) or (r==0 and c==7) or (r==7 and c==0) or (r==7 and c==7):
# #         corn(r,c,color)

# #     elif r==0 or c==0 or r==7 or c==7:
# #         edge(r,c,color)
    
# #     if flag==0:
# #         return -1

# # def N(r,c,color):
# #     global l,flag
# #     if l[r-1][c]==(not color):
# #         i=1
# #         while (l[r-i][c]==(not color)) and 0<=(r-i)<=7:
# #             i=i+1
# #         if (-1!=r-i) or (r-i!=8):
# #             if l[r-i][c]==color:
# #                 j=1
# #                 while l[r-j][c]==(not color):
# #                     l[r-j][c]=color
# #                     b[r-j][c]=groups[str(color)]
# #                     j=j+1
# #                 l[r][c]=color
# #                 flag=1

# # def E(r,c,color):
# #     global l,flag
# #     if l[r][c+1]==(not color):
# #         i=1
# #         while (l[r][c+i]==(not color)) and 0<=(c+i)<=7:
# #             i=i+1
# #         if (-1!=c+i) or (c+i!=8):
# #             if l[r][c+i]==color:
# #                 j=1
# #                 while l[r][c+j]==(not color):
# #                     l[r][c+j]=color
# #                     b[r][c+j]=groups[str(color)]
# #                     j=j+1
# #                 l[r][c]=color
# #                 flag=2

# # def S(r,c,color):
# #     global l,flag
# #     if l[r+1][c]==(not color):
# #         i=1
# #         while (l[r+i][c]==(not color)) and 0<=(r+i)<=7:
# #             i=i+1
# #         if (-1!=r+i) or (r+i!=8):
# #             if l[r+i][c]==color:
# #                 j=1
# #                 while l[r+j][c]==(not color):
# #                     l[r+j][c]=color
# #                     b[r+j][c]=groups[str(color)]
# #                     j=j+1
# #                 l[r][c]=color
# #                 flag=3

# # def W(r,c,color):
# #     global l,flag
# #     if l[r][c-1]==(not color):
# #         i=1
# #         while (l[r][c-i]==(not color)) and 0<=(c-i)<=7:
# #             i=i+1
# #         if (-1!=c-i) or (c-i<=8):
# #             if l[r][c-i]==color:
# #                 j=1
# #                 while l[r][c-j]==(not color):
# #                     l[r][c-j]=color
# #                     b[r][c-j]=groups[str(color)]
# #                     j=j+1
# #                 l[r][c]=color
# #                 flag=4

# # def NW(r,c,color):
# #     global l,flag
# #     if l[r-1][c-1]==(not color):
# #         i=1
# #         while (l[r-i][c-i]==(not color)) and 0<=(c-i)<=7 and 0<=(r-i)<=7:
# #             i=i+1
# #         if (-1!=c-i) or (c-i!=8):  #c-i==r-i condition satisfied for both
# #             if l[r-i][c-i]==color:
# #                 j=1
# #                 while l[r-j][c-j]==(not color):
# #                     l[r-j][c-j]=color
# #                     b[r-j][c-j]=groups[str(color)]
# #                     j=j+1
# #                 l[r][c]=color
# #                 flag=5

# # def NE(r,c,color):
# #     global l,flag
# #     if l[r-1][c+1]==(not color):
# #         i=1
# #         while (l[r-i][c+i]==(not color)) and 0<=(c+i)<=7 and 0<=(r-i)<=7:
# #             i=i+1
# #         if (-1!=c+i) or (c+i!=8):  #c-i==r-i condition satisfied for both
# #             if l[r-i][c+i]==color:
# #                 j=1
# #                 while l[r-j][c+j]==(not color):
# #                     l[r-j][c+j]=color
# #                     b[r-j][c+j]=groups[str(color)]
# #                     j=j+1
# #                 l[r][c]=color
# #                 flag=6

# # def SE(r,c,color):
# #     global l,flag
# #     if l[r+1][c+1]==(not color):
# #         i=1
# #         while (l[r+i][c+i]==(not color)) and 0<=(c+i)<=7 and 0<=(r+i)<=7:
# #             i=i+1
# #         if (-1!=c+i) or (c+i!=8):  #c-i==r-i condition satisfied for both
# #             if l[r+i][c+i]==color:
# #                 j=1
# #                 while l[r+j][c+j]==(not color):
# #                     l[r+j][c+j]=color
# #                     b[r+j][c+j]=groups[str(color)]
# #                     j=j+1
# #                 l[r][c]=color
# #                 flag=7

# # def SW(r,c,color):
# #     global l,flag
# #     if l[r+1][c-1]==(not color):
# #         i=1
# #         while (l[r+i][c-i]==(not color)) and 0<=(c-i)<=7 and 0<=(r+i)<=7:
# #             i=i+1
# #         if (-1!=c-i) or (c-i!=8):  #c-i==r-i condition satisfied for both
# #             if l[r+i][c-i]==color:
# #                 j=1
# #                 while l[r+j][c-j]==(not color):
# #                     l[r+j][c-j]=color
# #                     b[r+j][c-j]=groups[str(color)]
# #                     j=j+1
# #                 l[r][c]=color
# #                 flag=8


# # def mid(r,c,color):
# #     global flag,l
# #     flag=0
# #     print("\n",l[r][c],"\n")
# #     N(r,c,color)
# #     E(r,c,color)
# #     S(r,c,color)
# #     W(r,c,color)
# #     NW(r,c,color)
# #     NE(r,c,color)
# #     SE(r,c,color)
# #     SW(r,c,color)
# #     print("\n",l[r][c],"\n")

    
# # def corn(r,c,color):
# #     global flag,l
# #     flag=0
# #     if (r==0 and c==0):
# #         E(r,c,color)
# #         SE(r,c,color)
# #         S(r,c,color)

# #     elif (r==0 and c==7):
# #         W(r,c,color)
# #         SW(r,c,color)
# #         S(r,c,color)

# #     elif (r==7 and c==0):
# #         N(r,c,color)
# #         NE(r,c,color)
# #         E(r,c,color)
    
# #     elif (r==7 and c==7):
# #         N(r,c,color)
# #         NW(r,c,color)
# #         W(r,c,color)


# # def edge(r,c,color):
# #     global flag,l
# #     flag=0
# #     if (r==0):
# #         E(r,c,color)
# #         S(r,c,color)
# #         W(r,c,color)
# #         SE(r,c,color)
# #         SW(r,c,color)
    
# #     elif (r==7):
# #         N(r,c,color)
# #         E(r,c,color)
# #         W(r,c,color)
# #         NW(r,c,color)
# #         NE(r,c,color)

# #     elif (c==0):
# #         N(r,c,color)
# #         E(r,c,color)
# #         S(r,c,color)
# #         NE(r,c,color)
# #         SE(r,c,color)

# #     elif (c==7):
# #         N(r,c,color)
# #         S(r,c,color)
# #         W(r,c,color)
# #         NW(r,c,color)
# #         SW(r,c,color)


# # def finish(color):
# #     return str(l).find(str(int(not color)))



# # groups={"0":"O","1":"X"}
# # jolt=0
# # global l
# # l=[]
# # for i in range(8):
# #     ls=[]    
# #     for j in range(8):
# #         if (i==3 and j==3) or (i==4 and j==4):
# #             ls.append(1)
# #         elif (i==3 and j==4) or (i==4 and j==3): 
# #             ls.append(0)
# #         else:
# #             ls.append(2)
# #     l.append(ls)


# # b=[]
# # for i in range(8):
# #     ls=[]    
# #     for j in range(8):
# #         if (i==3 and j==3) or (i==4 and j==4):
# #             ls.append('o')
# #         elif (i==3 and j==4) or (i==4 and j==3): 
# #             ls.append('x')
# #         else:
# #             ls.append(2)
# #     b.append(ls)
# # for el in l:
# #         print(el)







# # while True:
# #     con, addr = serverSocket.accept()
# #     connectionSocket = context.wrap_socket(con, server_side=True)
# #     print("SSL established. Peer: {}".format(connectionSocket.getpeercert()))
# #     l = pickle.loads(connectionSocket.recv(1024))
# #     for el in l:
# #             print(el)

# #     res=finish(0)
# #     if (res==-1):
# #         jolt=1
# #         print("\nP1 wins")
# #         connectionSocket.close()



# #     else:
# #         print("\nIt is your turn now")
# #         r2=int(input("Enter row for p2 "))
# #         c2=int(input("Enter col for p2 "))

# #         valid=change(r2,c2,1)
# #         while valid==-1:
# #             print("Invalid Position")
# #             r2=int(input("Enter row for p2 "))
# #             c2=int(input("Enter col for p2 "))
# #             valid=change(r2,c2,1)

# #         for el in l:
# #             print(el)

# #         res=finish(1)
# #         if (res==-1):
# #             jolt=2
            


# #         if jolt==1:
# #             print("\nP1 wins")
# #         elif jolt==2:
# #             print("\nP2 wins")

# #     # capitalizedSentence = sentence.upper()
# #     connectionSocket.send(pickle.dumps(l))
# #     connectionSocket.shutdown(socket.SHUT_RDWR)
# #     connectionSocket.close()