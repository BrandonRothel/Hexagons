# Importing pygame module
import pygame
from pygame.locals import *
from time import sleep
import math
import random as rd

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((1000, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))

side = 100
apothem = math.sqrt(3) * side / 2
vertex = []
lines = []

def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)

def interpolate_points(x1, y1, x2, y2, num_points):
    """
    Interpolates between two points (x1, y1) and (x2, y2) to generate `num_points` intermediate points.
    
    Args:
        x1 (float): x-coordinate of the first point.
        y1 (float): y-coordinate of the first point.
        x2 (float): x-coordinate of the second point.
        y2 (float): y-coordinate of the second point.
        num_points (int): Number of intermediate points to generate.
    
    Returns:
        List[Tuple[float, float]]: A list of (x, y) coordinates representing the interpolated points.
    """
    interpolated_points = []
    for i in range(num_points):
        t = i / (num_points - 1)  # Interpolation parameter (ranges from 0 to 1)
        x_interpolated = (1 - t) * x1 + t * x2
        y_interpolated = (1 - t) * y1 + t * y2
        interpolated_points.append((x_interpolated, y_interpolated))
    return interpolated_points

def drawHexagon(locX, locY):
    color = random_color()

    thickness = 20
    # Using draw.rect module of
    # pygame to draw the line
    apothem = math.sqrt(3) * side / 2
    currentVertexes = []

    point1 = [locX+(side/2), locY+apothem]
    if point1 not in currentVertexes:
        vertex.append(point1)
        currentVertexes.append(point1)
    point2 = [locX+(side), locY]
    if point2 not in currentVertexes:
        vertex.append(point2)
        currentVertexes.append(point2)
    point3 = [locX+(side/2), locY-apothem]
    if point3 not in currentVertexes:
        vertex.append(point3)
        currentVertexes.append(point3)
    point4 = [locX-(side/2), locY-apothem]
    if point4 not in currentVertexes:
        vertex.append(point4)
        currentVertexes.append(point4)
    point5 = [locX-(side), locY]
    if point5 not in currentVertexes:
        vertex.append(point5)
        currentVertexes.append(point5)
    point6 = [locX-(side/2), locY+apothem]
    if point6 not in currentVertexes:
        vertex.append(point6)
        currentVertexes.append(point6)

    #print(point1)
    #print("\n")
    #print(point2)
    #print("\n")
    #print(point3)
    #print("\n")
    #print(point4)
    #print("\n")
    #print(point5)
    #print("\n")
    #print(point6)
    #print("\n")
    
    thisLine = [point6, point1]
    if thisLine not in lines:
        lines.append(thisLine)
        pygame.draw.line(window, color, 
                     [point6[0], point6[1]], 
                     [point1[0], point1[1]], thickness)
        pygame.display.update()
        sleep(.1)
    thisLine = [point1, point2]
    if thisLine not in lines:
        lines.append(thisLine)
        pygame.draw.line(window, color, 
                     [point1[0], point1[1]], 
                     [point2[0], point2[1]], thickness)
        pygame.display.update()
        sleep(.1)
    thisLine = [point2, point3]
    if thisLine not in lines:
        lines.append(thisLine)
        pygame.draw.line(window, color, 
                     [point2[0], point2[1]], 
                     [point3[0], point3[1]], thickness)
        pygame.display.update()
        sleep(.1)
    thisLine = [point3, point4]
    if thisLine not in lines:
        lines.append(thisLine)
        pygame.draw.line(window, color, 
                     [point3[0], point3[1]], 
                     [point4[0], point4[1]], thickness)
        pygame.display.update()
        sleep(.1)
    thisLine = [point4, point5]
    if thisLine not in lines:
        lines.append(thisLine)
        pygame.draw.line(window, color, 
                     [point4[0], point4[1]], 
                     [point5[0], point5[1]], thickness)
        pygame.display.update()
        sleep(.1)
    thisLine = [point5, point6]
    if thisLine not in lines:
        lines.append(thisLine)
        pygame.draw.line(window, color,  
                     [point5[0], point5[1]], 
                     [point6[0], point6[1]], thickness)
        pygame.display.update()
        sleep(.1)

    for point, elem in enumerate(currentVertexes):
        #interPoints = []
        interPoints = interpolate_points(elem[0], elem[1], currentVertexes[(point+1) % len(currentVertexes)][0], currentVertexes[(point+1) % len(currentVertexes)][1], 5)
        for interPoint in interPoints:
            color = random_color()
            pygame.draw.circle(window, color, interPoint, 10)
            pygame.display.update()
            sleep(.1)

    pygame.display.update()
    sleep(1)

def nextCenter(centerPoint, direction):
    match direction:
        case "1":
            newCenter = [centerPoint[0]+ (side*1.5),centerPoint[1]-apothem]
            return newCenter
        case "2":
            newCenter = [centerPoint[0]+ (side*1.5),centerPoint[1]+apothem]
            return newCenter
        case "3":
            newCenter = [centerPoint[0],centerPoint[1]+apothem*2]
            return newCenter
        case "4":
            newCenter = [centerPoint[0]- (side*1.5),centerPoint[1]+apothem]
            return newCenter
        case "5":
            newCenter = [centerPoint[0]- (side*1.5),centerPoint[1]-apothem]
            return newCenter
        case "6":
            newCenter = [centerPoint[0],centerPoint[1]-apothem*2]
            return newCenter


running = True
while running:
    for event in pygame.event.get():
        centerPoint = [200, 300]
        drawHexagon(centerPoint[0],centerPoint[1])
        centerPoint = nextCenter(centerPoint, "1")
        drawHexagon(centerPoint[0],centerPoint[1])
        centerPoint = nextCenter(centerPoint, "2")
        drawHexagon(centerPoint[0],centerPoint[1])
        centerPoint = nextCenter(centerPoint, "1")
        drawHexagon(centerPoint[0],centerPoint[1])
        centerPoint = nextCenter(centerPoint, "3")
        drawHexagon(centerPoint[0],centerPoint[1])
        if event.type == pygame.QUIT:
            running = False
        print(vertex)
        for points in vertex:
            color = random_color()
            pygame.draw.circle(window, color, points, 10)
            pygame.display.update()
        sleep(100)




# Draws the surface object to the screen.
pygame.display.update()

sleep(300)