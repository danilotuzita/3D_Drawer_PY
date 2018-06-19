import Util
from collections import namedtuple
from OpenGL.GL import *

Pos = namedtuple("Pos", ['x', 'y', 'z', 'inf'])
Color = namedtuple("Color", ['r', 'g', 'b'])
Light = namedtuple("Light", ['r', 'g', 'b', 'a'])

# guarda as contstantes do OpenGL
LIGHTS = (GL_LIGHT0, GL_LIGHT1, GL_LIGHT2, GL_LIGHT3, GL_LIGHT4, GL_LIGHT5, GL_LIGHT6, GL_LIGHT7)
count = -1  # guarda as luzes criadas

# define lights   # tipos das listas
lights = list()   # LightStatus
ambient = list()  # Light
diffuse = list()  # Light
specular = list() # Light
positions = list()# Pos

specularity = Light(0.9, 0.9, 0.9, 1)
matSpecularity = 1


def createLight(amb, dif, spec, pos, on=True):
    global count
    count += 1
    lights.append(on)
    ambient.append(amb)
    diffuse.append(dif)
    specular.append(spec)
    positions.append(pos)


def handleLighting():
    # Define os parâmetros para cada uma das luzes
    for i in range(len(lights)):
        glLightfv(LIGHTS[i], GL_AMBIENT, ambient[i])
        glLightfv(LIGHTS[i], GL_DIFFUSE, diffuse[i])
        glLightfv(LIGHTS[i], GL_SPECULAR, specular[i])
        glLightfv(LIGHTS[i], GL_POSITION, positions[i])
        if lights[i]:
            glEnable(LIGHTS[i])


def setupLighting():
    createLight(
        Light(0.2, 0.2, 0.2, 1),
        Light(0.7, 0.7, 0.7, 1),
        Light(0.1, 0.1, 0.1, 1),
        Pos(0.0, 150.0, 0.0, 1)
    )
    createLight(
        Light(0.0, 0.0, 0.0, 1),
        Light(0.3, 0.8, 0.2, 1),
        Light(0.5, 0.5, 0.5, 1),
        Pos(0.0, 90.0, 90.0, 1),
        False
    )

    glMaterialfv(GL_FRONT, GL_SPECULAR, specularity)  # Define a refletância do material
    glMateriali(GL_FRONT, GL_SHININESS, matSpecularity)  # Define a concentração do brilho
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # Ativa o uso da luz ambiente
    glEnable(GL_COLOR_MATERIAL) # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_LIGHTING)       # Habilita o uso de iluminação
    glEnable(GL_DEPTH_TEST)     # Habilita o depth-buffering
    glShadeModel(GL_SMOOTH)     # Habilita o modelo de colorização de Gouraud
    handleLighting()


def disableLight(light):
    if light <= len(lights):
        glDisable(LIGHTS[light])


def enableLight(light):
    if light <= len(lights):
        glEnable(LIGHTS[light])


def toggleLight(light):
    if lights[light]:
        disableLight(light)
        lights[light] = False
    else:
        enableLight(light)
        lights[light] = True

