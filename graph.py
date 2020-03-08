import pygame
import random
import json

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

path = 'C:\\Users\\Marius\\Documents\\'

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

class Node():
    def __init__(self, number, color, pos = (50, 50), radius = 20):

        self.number = number
        self.color = color
        self.pos = pos
        self.radius = radius

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
                            node1 = node
                            node2 = 0
                            break
                elif not node2:
                    for node in reversed(nodes):
                        if inCircle(node, event):
                            node2 = node
                            if (node1, node2) in edgeList:
                                edgeList.remove((node1, node2))
                            elif (node2, node1) in edgeList:
                                edgeList.remove((node2, node1))
                            else:
                                edgeList.append((node1, node2))
                            drawNodes()
                            break
                else:
                    node1 = 0
                    node2 = 0
            if event.type == pygame.KEYDOWN and event.unicode == 'e':
                return

def deleteNode():
    global edgeList
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for node in nodes:
                    if inCircle(node, event):
                        edgeList = [edge for edge in edgeList if not node in edge]
                        nodes.remove(node)
                        break
                drawNodes()
                    
            if event.type == pygame.KEYDOWN and event.unicode == 'd':
                return

def exportNodes(name):
    allInfo = {}
    for node in nodes:
       allInfo[node.number] = {}
       allInfo[node.number]['pos'] = node.pos
       allInfo[node.number]['color'] = node.color
       allInfo[node.number]['radius'] = node.radius
    allInfo['edges'] = [(edge[0].number, edge[1].number) for edge in edgeList]
    with open(path + name + '.json', 'w') as file:
        json.dump(allInfo, file, indent=4)

def importNodes(name):
    global edgeList, nodes
    nodes = []
    edgeList = []
    with open(path + name + '.json' , 'r') as f:
        dictt = json.load(f)
    for number in dictt:
        if number == 'edges':
            edgeList = [(nodes[i[0]-1], nodes[i[1]-1]) for i in dictt[number]]
            continue
        nodes.append(Node(int(number), dictt[number]['color'], dictt[number]['pos'], dictt[number]['radius']))
    drawNodes()
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
        if event.type == pygame.KEYDOWN and event.unicode == 'd':
            deleteNode()
        if event.type == pygame.KEYDOWN and event.unicode == 'o':
            exportNodes('nodesInfo')
        if event.type == pygame.KEYDOWN and event.unicode == 'i':
            importNodes('nodesInfo')
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
                        node.pos = event.pos
                        drawNodes(node)
                        break

    pygame.display.flip()
    clock.tick(60)
        

pygame.quit() 