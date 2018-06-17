from OpenGL.GL import *
from OpenGL.GLU import *
import math

# defines arrow keys
UP = 101
DOWN = 103
LEFT = 100
RIGHT = 102


class Camera(object):
    def __init__(self):
        self.yaw = -25
        self.pitch = 0
        self.speed = 3

        self.eyeX = 25
        self.eyeY = 25
        self.eyeZ = -100

        self.lookX = 0
        self.lookY = 0
        self.lookZ = 0

        self.fov = 60
        self.fAspect = 16/9

    def getEye(self):
        return {'eyeX': self.eyeX, 'eyeY': self.eyeY, 'eyeZ': self.eyeZ}

    def getLook(self):
        return {'lookX': self.lookX, 'lookY': self.lookY, 'lookZ': self.lookZ}

    def lookAt(self):
        glLoadIdentity()
        gluLookAt(self.eyeX, self.eyeY, self.eyeZ, self.lookX, self.lookY, self.lookZ, 0, 1, 0)

    def look(self):
        self.lookX = self.eyeX
        self.lookY = self.eyeY
        self.lookZ = self.eyeZ
        tpitch = self.pitch * math.pi / 180
        tyaw = self.yaw * math.pi / 180

        self.lookY += math.asin(tpitch)
        self.lookX += math.asin(tyaw)
        self.lookZ += math.acos(tyaw)
        self.lookAt()

    def handleLook(self, key):
        # TODO: FIX SIN / COS
        tyaw = self.yaw * math.pi / 180
        strafeYaw = (self.yaw + 90) * math.pi / 180
        if key == b'w':
            self.eyeX += self.speed * math.asin(tyaw)
            self.eyeZ += self.speed * math.acos(tyaw)
        if key == b's':
            self.eyeX -= self.speed * math.asin(tyaw)
            self.eyeZ -= self.speed * math.acos(tyaw)
        if key == b'a':
            self.eyeX += self.speed * math.asin(strafeYaw)
            self.eyeZ += self.speed * math.acos(strafeYaw)
        if key == b'd':
            self.eyeX -= self.speed * math.asin(strafeYaw)
            self.eyeZ -= self.speed * math.acos(strafeYaw)

        self.look()

    def handleEye(self, key):
        # TODO: FIX SIN / COS
        if key == UP:
            self.pitch += 3
            if self.pitch >= 90:
                self.pitch = 90
        if key == DOWN:
            self.pitch -= 3
            if self.pitch <= -90:
                self.pitch = -90
        if key == LEFT:
            self.yaw += 3
        if key == RIGHT:
            self.yaw -= 3

        self.look()