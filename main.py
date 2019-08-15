import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import os
import csv
import time
from Structures.score import StackScore, NodeScore
from Structures.scoreboard import QueueScoreBoard, NodeScoreBoard
from Structures.users import DoublyLinkedListUser, NodeUser
from Structures.snake import NodeSnake, ListSnake

def mainMenu(window):
    titleOfWindow(window,' MAIN MENU ')          #paint title
    window.addstr(7,30,  '1. Play')             #paint option 1
    window.addstr(9,30,  '2. Scoreboard')       #paint option 2
    window.addstr(11,30, '3. User Selection')   #paint option 3
    window.addstr(13,30, '4. Reports')         #paint option 4
    window.addstr(15,30, '5. Bulk Loading')    #paint option 5
    window.addstr(17,30, '6. Exit')            #paint option 6        
    window.timeout(-1)                         #wait for an input thru the getch() function

def mainMenu2(window,name):
    titleOfWindow(window,' MAIN MENU ')          #paint title
    window.addstr(7,30,  '1. Play')             #paint option 1
    window.addstr(9,30,  '2. Scoreboard')       #paint option 2
    window.addstr(11,30, '3. User Selection')   #paint option 3
    window.addstr(13,30, '4. Reports')         #paint option 4
    window.addstr(15,30, '5. Bulk Loading')    #paint option 5
    window.addstr(17,30, '6. Exit')            #paint option 6                 
    window.timeout(-1)                         #wait for an input thru the getch() function


def titleOfWindow(window,nameTitle):
    window.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
    window.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
    positionTitle = round((80-len(nameTitle))/2)    #center the new title to be painted
    window.addstr(0,positionTitle,nameTitle)           #paint the title on the screen

def waitEsc(window):
    outKey = window.getch()
    while outKey!=27:
        outKey = window.getch()

#**********************************************************************************************************
#--------------------------------SELECCION DE USUARIOS-----------------------------------------------------
#**********************************************************************************************************
def windowUsers(window):   
    nombreJugador = " "  
    titleOfWindow(window, ' PLAY ')     
    window.addstr(10,12, '<<<====')  
    window.addstr(10,55, '====>>>')
    window.addstr(15,27, 'Press Enter to select Name')
    aux = listaUsuarios.returnHead()
    window.addstr(10,33, aux.name)    
    key = -1
    while key == -1 :

        key = window.getch()
        if key == 10:  #significa que presiono ENTER
            nombreJugador = aux.name
            break          
        elif key == KEY_LEFT:
            titleOfWindow(window, ' PLAY ')     
            window.addstr(10,12, '<<<====')  
            window.addstr(10,55, '====>>>')
            window.addstr(15,27, 'Press Enter to select Name')
            window.addstr(10,33, aux.previous.name) 
            aux = aux.previous
            key = -1            
        elif key == KEY_RIGHT:
            titleOfWindow(window, ' PLAY ')     
            window.addstr(10,12, '<<<====')  
            window.addstr(10,55, '====>>>')
            window.addstr(15,27, 'Press Enter to select Name')
            window.addstr(10,33, aux.next.name) 
            aux = aux.next
            key = -1                    
        else:
            key = -1   
    return nombreJugador

#**********************************************************************************************************
#-------------------------------- TABLA DE PUNTAJES--------------------------------------------------------
#**********************************************************************************************************
def windowScoreBoard(window):
    titleOfWindow(window, ' ScoreBoard')    
    window.addstr(5,25,'Name')
    window.addstr(5,45,'Score')    
    size = listscoreboard.sizeQueue
    temp = listscoreboard.getHead()

    for i in range(0,size):
        window.addstr(6+i,25,temp.name)
        window.addstr(6+i,45,str(temp.score))
        temp = temp.next
    
#**********************************************************************************************************
#--------------------------------SECCION DE REPORTES------------------------------------------------------
#**********************************************************************************************************
def windowReport(window):
    titleOfWindow(window, ' REPORTS ')
    window.addstr(7,30,  '1. Snake Report')            
    window.addstr(9,30,  '2. Score Report')     
    window.addstr(11,30, '3. ScoreBoard Report')
    window.addstr(13,30, '4. Users Report')            
    window.addstr(15,30, '5. Return Main Menu') 
    key = -1
    while key == -1:
        key = window.getch()

        if(key == 49): #option 1
            #report to snake
            listsnake.graphSnake()
            key = -1
        elif(key == 50): #option 2
            #report score
            listScore.graphStack()
            key = -1
        elif(key == 51): #option 3
            #report scoreboard
            listscoreboard.graphScoreBoard()
            key = -1
        elif (key == 52): #option 4
            listaUsuarios.graphicUserList()
            key = -1     
        elif (key == 53): #option 5 - exit
            break           
        else:
            key = -1   
        
#**********************************************************************************************************
#--------------------------------CARGA MASIVA DE USUARIOS--------------------------------------------------
#**********************************************************************************************************
def windowBulkLoading(window):    
    filename = ""
    titleOfWindow(window,'BULK LOADING')
    window.addstr(2,4,'Ingrese Ruta de Archivo: ')
    window.addstr(3,4,' ')    
    curses.echo()
    salir = 0
    key = -1
    while key == -1:
        key = window.getch()       
        if(key != 10):
            filename=filename+str(chr(key))
            key=-1              
        elif (key == 10 ):  # 10 is enter in ASCII            
            archivo = open(filename)
            read = csv.DictReader(archivo,delimiter=',')
            for linea in read:
                listaUsuarios.add(NodeUser(linea['nombre']))
            window.addstr(5,4,'***File Loaded With Success***')
            archivo.close()
            curses.noecho()                   
            while salir == 0:
                window.addstr(8,4,'presione Esc para regresar al Menu.')
                salir = window.getch()
                if salir == 27:
                    break
                else:
                    salir = 0
        else:
            key=-1

#**********************************************************************************************************
#--------------------------------SECCION DE JUGAR SNAKE----------------------------------------------------
#**********************************************************************************************************

def windowSnake(window):
    titleOfWindow(window,'SNAKE RELOADED')
    window.addstr(0,3, 'Player: ') 
    window.addstr(0,11, namePlayer ) 
    window.addstr(0,67, 'Score: ') 
    window.addstr(0,73, '00') 

    #INICIO DE VARIABLES
    key = KEY_RIGHT  # por defecto empieza hacia la derecha
    puntuacion = 0   # puntucaion inicial 0
    pos_x=3 
    pos_y=3
    posX_food = 0
    posY_food = 0
    largoSnake = 8

    #dibuja la cadena de 3 #
    for i in range(0,largoSnake):    
        window.addstr(pos_y,pos_x+i,'#')
    while key != 27:
        window.timeout(100)    
        keystroke = window.getch()                
        if keystroke is not -1: 
            key = keystroke    
        if key == KEY_RIGHT:  
            titleOfWindow(window,'SNAKE RELOADED')
            window.addstr(0,3, 'Player: ') 
            window.addstr(0,11, namePlayer ) 
            window.addstr(0,67, 'Score: ') 
            window.addstr(0,73, '00')               
            for i in range(0,largoSnake):
                window.addch(pos_y, pos_x+i,' ')           
            pos_x += 1
            for i in range(0,largoSnake):
                window.addch(pos_y, pos_x+i,'#')
        elif key == KEY_LEFT:              
            titleOfWindow(window,'SNAKE RELOADED')
            window.addstr(0,3, 'Player: ') 
            window.addstr(0,11, namePlayer ) 
            window.addstr(0,67, 'Score: ') 
            window.addstr(0,73, '00')                
            for i in range(0,largoSnake):
                window.addch(pos_y, pos_x-i,' ')           
            pos_x -= 1
            for i in range(0,largoSnake):
                window.addch(pos_y, pos_x-i,'#')       
        elif key == KEY_UP:   
            titleOfWindow(window,'SNAKE RELOADED')
            window.addstr(0,3, 'Player: ') 
            window.addstr(0,11, namePlayer ) 
            window.addstr(0,67, 'Score: ') 
            window.addstr(0,73, '00')                      
            for i in range(0,largoSnake):
                window.addch(pos_y-i, pos_x,' ')           
            pos_y -= 1
            for i in range(0,largoSnake):
                window.addch(pos_y-i, pos_x,'#')    
        elif key == KEY_DOWN:              
            titleOfWindow(window,'SNAKE RELOADED')
            window.addstr(0,3, 'Player: ') 
            window.addstr(0,11, namePlayer ) 
            window.addstr(0,67, 'Score: ') 
            window.addstr(0,73, '00')  
            for i in range(0,largoSnake):
                window.addch(pos_y+i, pos_x,' ')           
            pos_y += 1
            for i in range(0,largoSnake):
                window.addch(pos_y+i, pos_x,'#')       

#////////////////////////////////////////////////////////////////////////////////////////////////////////
################################## BEGIN EXECUTION ######################################################
#////////////////////////////////////////////////////////////////////////////////////////////////////////

#object to work users lista doble enlazada circular
listaUsuarios = DoublyLinkedListUser()
#object to work Score Board with queue
listscoreboard = QueueScoreBoard()
"""
listscoreboard.queue(NodeScoreBoard("juan",34))
listscoreboard.queue(NodeScoreBoard("miriam",10))
listscoreboard.queue(NodeScoreBoard("lucas",90))
listscoreboard.queue(NodeScoreBoard("maria",4))
listscoreboard.queue(NodeScoreBoard("gaby",25))
listscoreboard.queue(NodeScoreBoard("luis",2))
listscoreboard.queue(NodeScoreBoard("sofia",120))
listscoreboard.queue(NodeScoreBoard("hanna",10))
listscoreboard.queue(NodeScoreBoard("mercedes",50))
listscoreboard.queue(NodeScoreBoard("fernanda",37))
listscoreboard.queue(NodeScoreBoard("JOSEFA",12))
"""
#object to work snake with lista doblemente enlazada
listsnake = ListSnake()
#object to work Score with stack
listScore = StackScore()

namePlayer = "unknown"
totalScore = 0
tempScore = 0

#creation of main windows
stdscr = curses.initscr() 
window = curses.newwin(30,80,0,0) 
window.keypad(True)     
curses.noecho()         
curses.curs_set(0)    
#execute main menu  
mainMenu(window)      

inputKey = -1
while(inputKey==-1):
    #get a key entered for keyboard
    inputKey = window.getch()  
########################################################################3333 
    #option1, 49 is ASCII 1  ->>>>> JUGAR
    if(inputKey==49):        
        if namePlayer=="unknown":
            nombre = ""
            titleOfWindow(window,'REGISTER ERROR')
            window.addstr(5,20, 'NO Player SELECTION')     
            window.addstr(7,20, 'ENTER YOUT NAME') 
            window.addstr(8,20, '') 
            curses.echo()
            salir = 0
            key = -1
            while key == -1:
                key = window.getch()       
                if(key != 10):
                    nombre=nombre+str(chr(key))
                    key=-1              
                elif (key == 10 ):  # 10 is enter in ASCII            
                    listaUsuarios.add(NodeUser(nombre))
                    namePlayer = nombre                    
                    curses.noecho()                   
                    while salir == 0:
                        window.addstr(11,20,'PRESS ENTER TO CONTINUE.')
                        salir = window.getch()
                        if salir == 10:
                            windowSnake(window)                                                             
                        else:
                            salir = 0
                else:
                    key=-1                      
        else:
            windowSnake(window)        
            waitEsc(window)
        mainMenu(window)         
        inputKey=-1
###########################################################################
    #option2, 50 is ASCII 2 ----->>>> SCORE BOARD
    elif(inputKey==50):
        windowScoreBoard(window)
        waitEsc(window)
        mainMenu(window)
        inputKey=-1
#************************************************************************************************
    #option3, 51 is ASCII 3 --->> USUARIOS  <<<---------------------finished option
    elif(inputKey==51):
        nombre = windowUsers(window) 
        namePlayer = nombre             
        mainMenu2(window,nombre)
        inputKey=-1
#********************************************************************************************************    
    #option4, 52 is ASCII 4  ----->>>> REPORTS
    elif(inputKey==52):
        windowReport(window)        
        mainMenu(window)
        inputKey=-1
    #option5, 53 is ASCII 5  -------->>>>> CARGA ARCHIVO <<<----------finished option
    elif(inputKey==53):
        windowBulkLoading(window)        
        mainMenu(window)
        inputKey=-1
    #option6, 54 is ASCII 6
    elif(inputKey==54):
        pass
    #stay input in -1
    else:
        inputKey=-1

#return terminal
curses.endwin() 
