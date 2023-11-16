from OpenGL.GL import *
from OpenGL.GLUT import *


def init():
   glViewport(0, 0, 500, 500)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   glOrtho(-900.0, 900, -900.0, 900, 0.0, 1.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()


def DrawPixel(x, y):
   glBegin(GL_POINTS)
   glVertex2f(x, y)
   glEnd()


def DrawCirclepoints(x, y, x_c, y_c):
   glBegin(GL_POINTS)
   x_0, y_0 = y, x
   x_1, y_1 = x, y
   x_2, y_2 = -x, y
   x_3, y_3 = -y, x
   x_4, y_4 = -y, -x
   x_5, y_5 = -x, -y
   x_6, y_6 = x, -y
   x_7, y_7 = y, -x
   glVertex2f(x_0 + x_c, y_0 + y_c)
   glVertex2f(x_1 + x_c, y_1 + y_c)
   glVertex2f(x_2 + x_c, y_2 + y_c)
   glVertex2f(x_3 + x_c, y_3 + y_c)
   glVertex2f(x_4 + x_c, y_4 + y_c)
   glVertex2f(x_5 + x_c, y_5 + y_c)
   glVertex2f(x_6 + x_c, y_6 + y_c)
   glVertex2f(x_7 + x_c, y_7 + y_c)

   glEnd()


def drawCircle(radius, x_c, y_c):
   d = 1 - radius
   x = 0
   y = radius
   DrawCirclepoints(x, y, x_c, y_c)
   while x < y:
       if d <= 0:
           d = d + 2 * x + 3
           x += 1
       else:
           d = d + 2 * x - 2 * y + 5
           x += 1
           y -= 1
       DrawCirclepoints(x, y, x_c, y_c)


def find_zone(dx,dy):

    if abs(dx) >= abs(dy):  # Modulus
        if dx >= 0:
            if dy >= 0:
                return 0
        if dx < 0:
            if dy >= 0:
                return 3
        if dx < 0:
            if dy < 0:
                return 4
        if dx >= 0:
            if dy < 0:
                return 7
    else:
        if dx >= 0:
            if dy >= 0:
                return 1
        if dx < 0:
            if dy >= 0:
                return 2
        if dx < 0:
            if dy < 0:
                return 5
        if dx >= 0:
            if dy < 0:
                return 6


def convert_to_zone0(x1, y1, x2, y2, zone):
   a = 0
   b = 0
   c = 0
   d = 0

   if zone == 0:
       a = x1
       b = y1
       c = x2
       d = y2

   elif zone == 1:
       a = y1
       b = x1
       c = y2
       d = x2

   elif zone == 2:
       a = y1
       b = -x1
       c = y2
       d = -x2

   elif zone == 3:
       a = -x1
       b = y1
       c = -x2
       d = y2

   elif zone == 4:
       a = -x1
       b = -y1
       c = -x2
       d = -y2

   elif zone == 5:
       a = -y1
       b = -x1
       c = -y2
       d = -x2

   elif zone == 6:
       a = -y1
       b = x1
       c = -y2
       d = x2

   elif zone == 7:
       a = x1
       b = -y1
       c = x2
       d = -y2

   return a, b, c, d


def drawline(x1, y1, x2, y2):
   dx = x2 - x1
   dy = y2 - y1
   zone = find_zone(dx, dy)

   x1, y1, x2, y2 = convert_to_zone0(x1, y1, x2, y2, zone)
   X0 = []
   Y0 = []
   d = []

   dx = x2 - x1
   dy = y2 - y1
   D = 2 * dy - dx

   d = d + [D]
   dNE = 2 * (dy - dx)
   dE = 2 * dy

   x = x1
   y = y1
   while x <= x2:
       a = x
       b = y
       X0 += [x]
       Y0 += [y]

       a, b = convert_to_origin_zone(a, b, zone)
       DrawPixel(a, b)
       x = x + 1
       if D > 0:
           y = y + 1
           D = D + dNE
       else:
           D = D + dE
           d += [D]


def convert_to_origin_zone(x, y, zone):
    if zone==0:
        x,y=x,y
        return [x,y]
    if zone==1:
        x,y=y,x
        return [x, y]
    if zone==2:
        x,y=-y,x
        return [x, y]
    if zone==3:
        x,y=-x,y
        return [x, y]
    if zone==4:
        x,y=-x,-y
        return [x, y]
    if zone==5:
        x,y=-y,-x
        return [x, y]
    if zone==6:
        x,y=y,-x
        return [x, y]
    if zone==7:
        x,y=x,-y
        return [x, y]

print("To see the sun use input between 0 to 125")
a = int(input("Enter the position of Sun : "))
b = int(input("Enter the height of the sun : "))
print("To avoid crash enter the position of human less than 650")
h = int(input("Enter the position of human : "))


def showScreen():
   glColor3f(0,0,1)
   radius = 500
   drawline(-1000, -400, 1000, -400)
   drawline(100, -250, 1000, -250)

   glColor3f(1,1,1)
   drawline(130, -320, 200, -320)#road mark
   drawline(250, -320, 320, -320)
   drawline(370, -320, 440, -320)
   drawline(490, -320, 560, -320)
   drawline(610, -320, 680, -320)
   drawline(730, -320, 800, -320)
   drawline(850, -320, 920, -320)

   glColor3f(1, 0, 1) #carlines
   drawline(-450, 100, -150, 100)
   drawline(-850, -100, -850, -300)
   drawline(-850, -300, -780, -300)
   drawline(-150, 100, -150, -90)
   drawline(970, -320, 1000, -320)
   drawline(-20, -300, 100, -300)
   drawline(-450, 100, -450, -300)
   drawline(-850, -100, 100, -100)
   drawline(100, -97, 100, -300)
   drawline(-630, -300, -180, -300)
   drawline(-850, -150, -780, -150)
   drawline(-780, -100, -780, -150)
   drawline(20, -150, 100, -150)
   drawline(20, -150, 20, -100)


   ##################   #human in car   ##########################################################
   glColor3f(0.5,0.5,0.5)

   drawline(-260, 0, -260, -100) #right
   drawline(-340, 0, -340, -100)#left
   drawCircle(radius // 14, -300, 30)

   glColor3f(0, 1, 1) ##### ONLY FOR COLOR

   x1=750
   x2=850
   y1=125
   y2= -250
   l=x1-h
   x_c = -180
   k= 100
############## HUMAN 1  ####################################


   if l<=x_c:
       glColor3f(1, 0, 0)
       drawCircle(radius // 6, x_c, 200)
       drawCircle(radius // 80, -210, 210)
       drawCircle(radius // 80, -140, 210)
       drawCircle(radius // 25, -182, 160)


       glColor3f(89 / 255, 25 / 255, 29 / 255)

       drawline(-150, -160, 120, -160)
       drawline(80, -350, 220, -350)

       print("Told you it would crash")
       print("Stay aware while you are on roads!!!!!!")
       glColor3f(1, 0, 0)
       # w
       drawline(-800, -500, -700, -700)
       drawline(-700, -700, -650, -600)
       drawline(-650, -600, -600, -700)
       drawline(-600, -700, -525, -500)
       # A
       drawline(-400, -500, -300, -500)
       drawline(-400, -500, -400, -700)
       drawline(-300, -500, -300, -700)
       drawline(-400, -600, -300, -600)
       # S
       drawline(-200, -500, -100, -500)
       drawline(-200, -500, -200, -600)
       drawline(-200, -600, -100, -600)
       drawline(-100, -600, -100, -700)
       drawline(-200, -700, -100, -700)
       # T
       drawline(0, -500, 100, -500)
       drawline(50, -500, 50, -700)
       # E
       drawline(200, -500, 300, -500)
       drawline(200, -600, 300, -600)
       drawline(200, -700, 300, -700)
       drawline(200, -500, 200, -700)
       # !
       drawline(400, -500, 400, -650)
       drawline(400, -690, 400, -720)

   elif  l>x_c and l<=k:
       glColor3f(1, 0, 0)
       drawline(l, y1, l, -100)
       drawline(x2 - h, y1, x2 - h, -100)
       drawline(x2 - 50 - h, y2 + 200, x2 - 50 - h, -70)
       drawline(l, 0, x2 - h, 0)

       drawCircle(radius // 6, l+50, 200)
       drawCircle(radius // 50,l+10, 210)
       drawCircle(radius // 50,l+80, 210)
       drawCircle(radius // 25, l+50, 160)

       print("Told you it would crash")
       print("Stay aware while you are on roads!!!!!!")
       glColor3f(1, 0, 0)
       # w
       drawline(-800, -500, -700, -700)
       drawline(-700, -700, -650, -600)
       drawline(-650, -600, -600, -700)
       drawline(-600, -700, -525, -500)
       # A
       drawline(-400, -500, -300, -500)
       drawline(-400, -500, -400, -700)
       drawline(-300, -500, -300, -700)
       drawline(-400, -600, -300, -600)
       # S
       drawline(-200, -500, -100, -500)
       drawline(-200, -500, -200, -600)
       drawline(-200, -600, -100, -600)
       drawline(-100, -600, -100, -700)
       drawline(-200, -700, -100, -700)
       # T
       drawline(0, -500, 100, -500)
       drawline(50, -500, 50, -700)
       # E
       drawline(200, -500, 300, -500)
       drawline(200, -600, 300, -600)
       drawline(200, -700, 300, -700)
       drawline(200, -500, 200, -700)
       # !
       drawline(400, -500, 400, -650)
       drawline(400, -690, 400, -720)


   else:
       drawline(l, y1, l, y2)
       drawline(x2 - h, y1, x2 - h, y2)
       drawline(x2 - 50 - h, y2 + 200, x2 - 50 - h, y2)
       drawline(l, 0, x2-h, 0)



       ############################## EYES AND HEAD ################################

       drawCircle(radius // 6, 800 - h, 200)
       drawCircle(radius // 40, 770 - h, 200)
       drawCircle(radius // 40, 840 - h, 200)
       print("You are safe")
       glColor3f(0.5, 0.5, 0.5)
       # S
       drawline(-500, -500, -400, -500)
       drawline(-500, -500, -500, -600)
       drawline(-500, -600, -400, -600)
       drawline(-400, -600, -400, -700)
       drawline(-500, -700, -400, -700)
       # A
       drawline(-300, -500, -200, -500)
       drawline(-300, -500, -300, -700)
       drawline(-200, -500, -200, -700)
       drawline(-300, -600, -200, -600)
       # F
       drawline(-100, -500, 0, -500)
       drawline(-100, -500, -100, -700)
       drawline(-100, -600, 0, -600)
       # E
       drawline(100, -500, 200, -500)
       drawline(100, -600, 200, -600)
       drawline(100, -700, 200, -700)
       drawline(100, -500, 100, -700)
       # !
       drawline(300, -500, 300, -650)
       drawline(300, -690, 300, -720)




############################# CAR TIRES AND DOOR KNOB ##################################
   glColor3f(1,0.5,0)
   drawCircle(radius // 7, -700,-300) #outer tyre
   drawCircle(radius //7, -100,-300)#outer tyre
   drawCircle(radius // 20, -700, -300) #inner right tyre

   drawCircle(radius // 20, -100, -300)#knob
   drawCircle(radius // 35, -400, -170)#knob


#############################  SUN ###############################
   radius = 500

   x_c = 500-(10*a)
   y_c = 600-b
   for i in range(100):
       glColor3f(255 / 255, 140 / 255, 0 / 255)
       drawCircle(radius // 4, x_c, y_c)
       radius-=5

   glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
glutCreateWindow("PROJECT01")
glutDisplayFunc(showScreen)

init()

glutMainLoop()