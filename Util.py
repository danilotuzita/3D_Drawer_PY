from OpenGL.GL import *
from OpenGL.GLUT import *
from collections import namedtuple

import Light

# defines
LIGHT_SCALE = 0.25

# define namedtuples
XYZ = namedtuple("XYZ", ['x', 'y', 'z'])
Color = namedtuple("Color", ['r', 'g', 'b'])
L = Light.Light
P = Light.Pos

# define colors
white = Color(1.0, 1.0, 1.0)
red   = Color(1.0, 0.0, 0.0)
green = Color(0.0, 1.0, 0.0)
blue  = Color(0.0, 0.0, 1.0)

# lights
lightsPos = list()
lightsColor = list()


def box(posX=0, posY=0, posZ=0, scaleX=1, scaleY=1, scaleZ=1, color=white):
    glColor(color)
    glPushMatrix()
    glScalef(scaleX * 10, scaleY * 10, scaleZ * 10)
    # o translate é dividido pela escala para garantir consistencia no translate
    glTranslatef((posX / 10) / scaleX, (posY / 10) / scaleY, (posZ / 10) / scaleZ)
    glutSolidCube(1)
    glPopMatrix()


def sphere(posX=0, posY=0, posZ=0, scaleX=1, scaleY=1, scaleZ=1, color=white, quality=16):
    glColor(color)
    glPushMatrix()
    glScalef(scaleX * 10, scaleY * 10, scaleZ * 10)
    glTranslatef((posX / 10) / scaleX, (posY / 10) / scaleY, (posZ / 10) / scaleZ)
    glutSolidSphere(1, quality, quality)
    glPopMatrix()


def cylinder(posX=0, posY=0, posZ=0, scaleX=1, scaleY=1, scaleZ=1, color=white, quality=8):
    glColor(color)
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    glScalef(scaleX, scaleZ, scaleY)
    glTranslatef((posX / 10) / scaleX, (posY / 10) / scaleY, (posZ / 10) / scaleZ)
    glutSolidCylinder(1, 1, quality, 1)
    glPopMatrix()


def line(x0=0, y0=0, z0=0, x1=0, y1=1, z1=0, color=white, width=1):
    glLineWidth(width)
    glBegin(GL_LINES)
    glColor(color)
    glVertex3f(x0, y0, z0)
    glVertex3f(x1, y1, z1)
    glEnd()


def drawLights():
    global LIGHT_SCALE
    for i in range(len(lightsPos)):
        sphere(lightsPos[i].x, lightsPos[i].y, lightsPos[i].z, LIGHT_SCALE, LIGHT_SCALE, LIGHT_SCALE, lightsColor[i], 8)


def addLight(pos=P(0, 0, 0, 1), ambient=L(1, 1, 1, 1), diffuse=L(1, 1, 1, 1), specular=L(1, 1, 1, 1), on=True):
    lightsPos.append(pos)
    lightsColor.append(Color(diffuse.r, diffuse.g, diffuse.b))
    Light.createLight(pos, ambient, diffuse, specular, on)


def drawAxys():
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor(green)
    glVertex3f(2000.0, 0.0, 0.0)
    glVertex3f(-2000.0, 0.0, 0.0)
    glColor(red)
    glVertex3f(0.0, 0.0, 2000.0)
    glVertex3f(0.0, 0.0, -2000.0)
    glColor(blue)
    glVertex3f(0.0, -2000.0, 0.0)
    glVertex3f(0.0, 2000.0, 0.0)
    glEnd()


