from OpenGL.GL import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def drawAxys():
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(2000.0, 0.0, 0.0)
    glVertex3f(-2000.0, 0.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 2000.0)
    glVertex3f(0.0, 0.0, -2000.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, -2000.0, 0.0)
    glVertex3f(0.0, 2000.0, 0.0)
    glEnd()
