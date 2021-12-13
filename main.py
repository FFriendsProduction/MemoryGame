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
        self.xlocations = self.ylocations = []

        self.queqe = {(20, 20), (190, 20)}
        self.comparison = set()

    def draw_rect(self):
        for row in range(int(self.num**(1/2))): #0
            for column in range(int(self.num**(1/2))): #0

                self.x =self.space*(column+1) + column*self.width
                self.y = self.space*(row+1) + row*self.width
                
                pygame.draw.rect(
                    self.root, self.color, 
                    (self.x, self.y, self.width, self.width))
                
                self.xlocations.append((self.x, self.x + self.width))

                self.ylocations.append(
                    (self.space*(row+1) + row*self.width, self.space*(row+1) + row*self.width + self.width))

    def mouse_loc(self):
        self.li = [False, False]
    
        for i in self.xlocations:
            if pygame.mouse.get_pos()[0] in range(int(i[0]), int(i[1])):
                self.li[0] = i

        for j in self.ylocations:
            if pygame.mouse.get_pos()[1] in range(int(j[0]), int(j[1])):
                self.li[1] = j

        return self.li

    def pick(self):
        if self.mouse_loc() and pygame.mouse.get_pressed()[0]:
            try:
                x = int(self.mouse_loc()[0][0])
                y = int(self.mouse_loc()[1][0])
                pygame.draw.rect(self.root, "green", (x, y, self.width, self.width))
                self.comparison.add((x, y))
                print(self.queqe)
                print(self.comparison)
                self.check(self.comparison)
            except:
                print("pick doğru çalışmadı")

    def check(self, comparison):
        if len(comparison) == len(self.queqe) and comparison == self.queqe:
            print("Tamamdır")

    def highlight(self):
        pass


game = Game(360, 4)
clock = pygame.time.Clock()

run = True
while run:

    clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    game.draw_rect()
    game.pick()
    pygame.display.update()
