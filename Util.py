from OpenGL.GL import *
from collections import namedtuple

# define namedtuples
XYZ = namedtuple("XYZ", ['x', 'y', 'z'])
Color = namedtuple("Color", ['r', 'g', 'b'])

# define colors
white = Color(1.0, 1.0, 1.0)
red   = Color(1.0, 0.0, 0.0)
green = Color(0.0, 1.0, 0.0)
blue  = Color(0.0, 0.0, 1.0)

cubeVertices = (
    XYZ( 1, -1, -1),  # 0
    XYZ( 1,  1, -1),  # 1
    XYZ(-1,  1, -1),  # 2
    XYZ(-1, -1, -1),  # 3
    XYZ( 1, -1,  1),  # 4
    XYZ( 1,  1,  1),  # 5
    XYZ(-1, -1,  1),  # 6
    XYZ(-1,  1,  1)   # 7
)

cubeEdges = (
    (0, 1, 2),
    (0, 2, 3),
    (0, 3, 4),
    (3, 4, 6),
    (0, 1, 4),
    (1, 4, 5),
    (1, 2, 5),
    (2, 5, 7),
    (2, 3, 6),
    (2, 6, 7),
    (4, 6, 7),
    (4, 5, 7)
)


def cube(posX=0, posY=0, posZ=0, scaleX=10, scaleY=10, scaleZ=10, color=white):
    glBegin(GL_TRIANGLES)
    # colors=(white, green, blue, red)
    # i = 0
    glColor(color)
    for edge in cubeEdges:
        # if i > 3:
        #     i = 0
        # glColor(colors[i])
        # i+=1
        for vertex in edge:
            glVertex3fv(XYZ(
                cubeVertices[vertex].x * scaleX + posX,
                cubeVertices[vertex].y * scaleY + posY,
                cubeVertices[vertex].z * scaleZ + posZ
            ))
    glEnd()


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


