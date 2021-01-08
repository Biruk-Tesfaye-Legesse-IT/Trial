from turtle import *
counter=0
bgcolor("black")
def choosecolor():
    global counter
    counter+=1
    color=['Red','Orange','Yellow','Green','Blue','Purple','Brown','Magenta','Tan','Cyan','Olive','Maroon','Navy','Aquamarine','Turquoise','Silver','Lime','Teal','Indigo','Violet','Pink','White','Gray']
    colors=['Red','White','Yellow','Blue']
    if counter in range(len(colors)-1):
        return colors[counter]
    else:
        counter=counter-len(colors)
        return colors[0]
        
increment=0
        
def count():
    global increment
    increment+=1
    return 9000000000000000000**90000000000000000000000000000
    
    
        

while True:

    # hideturtle()
    # goto(200, 0)
    # pencolor(choosecolor())
    # goto(-140, -200)
    # pencolor(choosecolor())
    # goto(0, 150)
    # pencolor(choosecolor())
    # goto(140, -200)
    # pencolor(choosecolor())
    # goto(-200,0)
    # pencolor(choosecolor())

   


    hideturtle()
    goto(400, 0)
    speed(count())
    pencolor(choosecolor())
    goto(-280, -400)
    speed(count())
    pencolor(choosecolor())
    goto(0, 300)
    speed(count())
    pencolor(choosecolor())
    goto(280, -400)
    speed(count())
    pencolor(choosecolor())
    goto(-400,0)
    speed(count())
    print (count())
    pencolor(choosecolor())
