import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

class Node():
    def __init__(self, number, color):

        self.number = number
        self.pos = (50, 50)
        self.radius = 20
        self.color = color

        #drawing the node on the screen
        pygame.draw.circle(screen, color, self.pos, self.radius)

nodes = []
edgeList = []

def drawNodes(mainNode = 0):
    screen.fill(WHITE)
    for edge in edgeList:
        pygame.draw.line(screen, BLACK, edge[0].pos, edge[1].pos, 1)

    for node in nodes:
        if node == mainNode:
            continue
        pygame.draw.circle(screen, node.color, node.pos, node.radius)
    if mainNode:
        pygame.draw.circle(screen, mainNode.color, mainNode.pos, mainNode.radius)
    pygame.display.flip()

def randomColor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def inCircle(node, event):
   return node.pos[0]-node.radius < event.pos[0] < node.pos[0] + node.radius and node.pos[1]-node.radius < event.pos[1] < node.pos[1] + node.radius 

def generateEdges():
    node1 = 0
    node2 = 0
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not node1 or (node1 and node2):
                    for node in reversed(nodes):
                        if inCircle(node, event):
                            print(node.number)
                            node1 = node
                            node2 = 0
                            break
                elif not node2:
                    for node in reversed(nodes):
                        if inCircle(node, event):
                            node2 = node
                            edgeList.append((node1, node2))
                            drawNodes()
                            break
                else:
                    node1 = 0
                    node2 = 0
            if event.type == pygame.KEYDOWN and event.unicode == 'e':
                return





done = False
clock = pygame.time.Clock()
screen.fill(WHITE)

colors = [BLUE, RED, GREEN]

selected = 0
numberOfNodes = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.unicode == 'n':
            nodes.append(Node(numberOfNodes, randomColor()))
            numberOfNodes += 1
        if event.type == pygame.KEYDOWN and event.unicode == 'e':
            generateEdges()
        if event.type == pygame.MOUSEMOTION and event.buttons != (1, 0, 0):
            selected = 0
        if event.type == pygame.MOUSEMOTION and event.buttons == (1, 0, 0):
            if selected:
                node.pos = event.pos
                drawNodes(node)
            else:
                for node in reversed(nodes):
                    if inCircle(node, event):
                        selected = 1
                        print(node.number)
                        node.pos = event.pos
                        drawNodes(node)
                        break

    pygame.display.flip()
    clock.tick(60)
        

pygame.quit() 
