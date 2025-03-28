import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time
import math
from .world import World
from .ecosystem import Ecosystem

class Game:
    def __init__(self):
        # Disable pygame sound to avoid ALSA warnings
        pygame.mixer.quit()
        pygame.init()
        
        self.display = (1280, 720)
        pygame.display.set_mode(self.display, DOUBLEBUF|OPENGL)
        gluPerspective(45, (self.display[0]/self.display[1]), 0.1, 100.0)
        glTranslatef(0.0, -5.0, -20)
        glEnable(GL_DEPTH_TEST)
        
        self.world = World()
        self.ecosystem = Ecosystem()
        self.ecosystem.initialize()
        
        self.clock = pygame.time.Clock()
        self.last_time = time.time()
        
    def _draw_sphere(self, radius):
        """Draw a sphere using quad strips"""
        slices = 10
        stacks = 10
        for i in range(stacks):
            lat0 = 3.14 * (-0.5 + float(i-1)/stacks)
            z0 = radius * math.sin(lat0)
            zr0 = radius * math.cos(lat0)
            
            lat1 = 3.14 * (-0.5 + float(i)/stacks)
            z1 = radius * math.sin(lat1)
            zr1 = radius * math.cos(lat1)
            
            glBegin(GL_QUAD_STRIP)
            for j in range(slices+1):
                lng = 2 * 3.14 * float(j-1)/slices
                x = math.cos(lng)
                y = math.sin(lng)
                glNormal3f(x * zr0, y * zr0, z0)
                glVertex3f(x * zr0, y * zr0, z0)
                glNormal3f(x * zr1, y * zr1, z1)
                glVertex3f(x * zr1, y * zr1, z1)
            glEnd()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True
        
    def update(self):
        current_time = time.time()
        delta_time = current_time - self.last_time
        self.last_time = current_time
        
        self.world.update(delta_time)
        self.ecosystem.update(delta_time)
        
    def render(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        # Set lighting based on time of day
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        
        # Render world
        self.world.render()
        
        # Render entities
        glColor3f(0,1,0)  # Green for plants
        for plant in self.ecosystem.plants:
            glPushMatrix()
            glTranslatef(plant.position[0], plant.position[1], plant.position[2])
            self._draw_sphere(0.2)
            glPopMatrix()
            
        glColor3f(1,0.5,0)  # Orange for animals
        for animal in self.ecosystem.animals:
            glPushMatrix()
            glTranslatef(animal.position[0], animal.position[1], animal.position[2])
            self._draw_sphere(0.3)
            glPopMatrix()
        
        pygame.display.flip()
        self.clock.tick(60)
        
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.render()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
