import random
import pygame

pygame.init()

class Game():
    def __init__(self, root_width, num):
        self.num = num
        self.space = 20
        
        self.root_width = root_width
        self.width = (self.root_width - self.space*(self.num**(1/2) + 1)) / self.num**(1/2)

        self.color = "light blue"

        self.root = pygame.display.set_mode([self.root_width, self.root_width])
        self.xlocations = []
        self.ylocations = []


    def draw_rect(self):
        for row in range(int(self.num**(1/2))): #0
            for column in range(int(self.num**(1/2))): #0

                self.x =self.space*(column+1) + column*self.width
                self.y = self.space*(row+1) + row*self.width
                
                pygame.draw.rect(
                    self.root, self.color, 
                    (self.x, self.y, self.width, self.width))
                
                self.xlocations.append(
                    (self.x, self.x + self.width)
                )

                self.ylocations.append(
                    (self.space*(row+1) + row*self.width, self.space*(row+1) + row*self.width + self.width)
                )
        

    def mouse_loc(self):
        self.li = [False, False]
    
        for i in self.xlocations:
            if pygame.mouse.get_pos()[0] in range(int(i[0]), int(i[1])):
                self.li[0] = i

        for j in self.ylocations:
            if pygame.mouse.get_pos()[1] in range(int(j[0]), int(j[1])):
                self.li[1] = i

        if all(self.li):
            return self.li
        return False


game = Game(360, 4)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.mouse_loc() and pygame.mouse.get_pressed()[0]:
                print(pygame.mouse.get_pos())
                print(game.mouse_loc())

    game.draw_rect()
    pygame.display.update()