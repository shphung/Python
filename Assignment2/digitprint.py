import turtle

t = turtle
t.pensize(2)
t.hideturtle()
t.left(90)
t.speed('fastest')

def print_zero() :
    long()
    long()
    short()
    short()
    short()
    return

def print_one() :
    short()
    short()
    short()
    long()
    long()
    return

def print_two() :
    short()
    short()
    long()
    short()
    long()
    return

def print_three() :
    short()
    short()
    long()
    long()
    short()
    return

def print_four() :
    short()
    long()
    short()
    short()
    long()
    return

def print_five() :
    short()
    long()
    short()
    long()
    short()
    return

def print_six() :
    short()
    long()
    long()
    short()
    short()
    return

def print_seven() :
    long()
    short()
    short()
    short()
    long()
    return

def print_eight() :
    long()
    short()
    short()
    long()
    short()
    return

def print_nine() :
    long()
    short()
    long()
    short()
    short()

    
def long():
    t.fd(14)
    t.up()
    t.bk(14)
    t.right(90)
    t.fd(6)
    t.left(90)
    t.down()
    
def short():
    t.fd(6)
    t.up()
    t.bk(6)
    t.right(90)
    t.fd(6)
    t.left(90)
    t.down()

t.up()
t.goto(0, -50)
t.down()
 
