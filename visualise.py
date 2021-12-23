from bfs import BFS
from dfs import DFS
import pygame, os
from pygame.locals import *
import numpy as np


class Path:
    def __init__(self, w, h, grid_size=25):
        self.width, self.height = w, h
        self.grid_size = grid_size
        self.grid = np.zeros((w, h))

        self.start = (5, 10)
        self.end = (20, 10)

        self.done = False
        self.pause = False
        self.visited = []
        self.path = []

        self.bfs = BFS(self.start, w, h)

    def display(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                rect = pygame.Rect(i * self.grid_size, j * self.grid_size, self.grid_size, self.grid_size)
                if (i, j) in self.visited:
                    pygame.draw.rect(screen, (234, 255, 52), rect)
                if (i, j) in self.path:
                    pygame.draw.rect(screen, (100, 255, 100), rect)
                if (i, j) == self.start:
                    pygame.draw.rect(screen, (0, 255, 0), rect)
                elif (i, j) == self.end:
                    pygame.draw.rect(screen, (255, 0, 0), rect)

        for i in range(self.width):
            pygame.draw.line(screen, (0, 0, 0), (i * self.grid_size, 0), (i * self.grid_size, self.height * self.grid_size), 1)

        for i in range(self.height):
            pygame.draw.line(screen, (0, 0, 0), (0, i * self.grid_size), (self.width * self.grid_size, i * self.grid_size), 1)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
                if event.key == K_SPACE:
                    self.pause = not self.pause

    def display_screen(self, screen):
        screen.fill((255, 255, 255))

        self.display(screen)

        pygame.display.update()
        pygame.display.flip()

    def run_logic(self):
        if not self.done and not self.pause:
            self.bfs_step()

    def bfs_step(self):
        self.visited = self.bfs.step()
        if self.end in self.visited:
            self.done = True
            self.path = self.bfs.backtrace(self.end, self.start)
        

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Path Finding")

    os.environ['SDL_VIDEO_CENTERED'] = "True"

    width, height = 650, 650
    grid_size = 25

    screen = pygame.display.set_mode((width, height))

    done = False
    clock = pygame.time.Clock()
    path = Path(width // grid_size, height // grid_size, grid_size=grid_size)

    while not done:
        done = path.events()
        path.run_logic()
        path.display_screen(screen)

        clock.tick(60)


if __name__ == "__main__":
    main()
