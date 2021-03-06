from astar import AStar
from bfs import BFS
from dfs import DFS
import pygame, os
from pygame.locals import *
import sys
from random import randint


class Path:
    def __init__(self, w, h, grid_size=25, algo="BFS"):
        self.width, self.height = w, h
        self.grid_size = grid_size
        self.algo = algo

        self.start = (randint(0, w), randint(0, h))
        self.end = (randint(0, w), randint(0, h))
        self.reset()

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
                if (i, j) in self.walls:
                    pygame.draw.rect(screen, (0, 0, 0), rect)

        for i in range(self.width):
            pygame.draw.line(screen, (0, 0, 0), (i * self.grid_size, 0), (i * self.grid_size, self.height * self.grid_size), 1)

        for i in range(self.height):
            pygame.draw.line(screen, (0, 0, 0), (0, i * self.grid_size), (self.width * self.grid_size, i * self.grid_size), 1)

        if len(self.path_lines) >= 2:
            pygame.draw.lines(screen, (0, 0, 0), False, self.path_lines, 2)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
                if event.key == K_SPACE:
                    self.pause = not self.pause
                if event.key == K_r:
                    self.reset()
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                wall = (pos[0] // self.grid_size, pos[1] // self.grid_size)
                if pygame.mouse.get_pressed()[0] and wall not in self.visited:
                    self.walls.append(wall)
                elif pygame.mouse.get_pressed()[2]:
                    if wall in self.walls:
                        self.walls.remove(wall)

    def display_screen(self, screen):
        screen.fill((255, 255, 255))

        self.display(screen)

        pygame.display.update()
        pygame.display.flip()

    def run_logic(self):
        if not self.done and not self.pause:
            self.algorithm_step()

    def algorithm_step(self):
        self.visited = self.algorithm.step(self.walls, self.end)
        if self.end in self.visited:
            self.done = True
            self.path = self.algorithm.backtrace(self.end, self.start)
            self.get_lines()

    def get_centre(self, p):
        return (p[0] * self.grid_size + self.grid_size // 2, p[1] * self.grid_size + self.grid_size // 2)
    
    def get_lines(self):
        for p in self.path:
            self.path_lines.append(self.get_centre(p))
        self.path_lines.append(self.get_centre(self.start))

    def reset(self):
        self.walls = []

        self.done = False
        self.pause = True
        self.visited = []
        self.path = []
        self.path_lines = []

        if self.algo == "BFS":
            self.algorithm = BFS(self.start, self.width, self.height)
        elif self.algo == "DFS":
            self.algorithm = DFS(self.start, self.width, self.height)
        elif self.algo == "AStar":
            self.algorithm = AStar(self.start, self.width, self.height)
        

def main(algo="BFS"):
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Path Finding")

    os.environ['SDL_VIDEO_CENTERED'] = "True"

    width, height = 1000, 800
    grid_size = 25

    screen = pygame.display.set_mode((width, height))

    done = False
    clock = pygame.time.Clock()
    path = Path(width // grid_size, height // grid_size, grid_size=grid_size, algo=algo)

    while not done:
        done = path.events()
        path.run_logic()
        path.display_screen(screen)

        clock.tick(60)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in ["BFS", "DFS", "AStar"]:
            main(sys.argv[1])
        else:
            print("Algorithm %s not supported.\nTry BFS, DFS or AStar" % sys.argv[1])
    else:
        main()
