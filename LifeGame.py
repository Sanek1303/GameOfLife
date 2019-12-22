import pygame as pg
import random
import numpy as np


class GameofLife:
    def __init__(self, width = 640, height = 480, cell_size = 10, speed = 10,  randomize = False):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        
        # делаем размер окна
        self.screen_size = width, height
        
        self.screen = pg.display.set_mode(self.screen_size)
        
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        
        self.randomize = randomize
        
        self.speed = speed
        
        
    def draw_grid(self):
        for x in range(0, self.width, self.cell_width):
            pg.draw.line(self.screen, pg.Color('Black'), 
                         (x,0), (x, self.height))
        for y in range(0, self.height, self.cell_height):
            pg.draw.line(self.screen, pg.Color('Black'),
                         (0,y), (self.width, y))   
            
            
    def cell_list(self):
        self.clist = np.zeros(self.cell_size*self.cell_size)    
        for i in range(self.cell_size):        
           for j in range(self.cell_size):
               if self.randomize == True:
                   self.clist[i * self.cell_size + j] = random.choice([True, False])
               else:
                   self.clist[i * self.cell_size + j] = False        
        self.clist.resize(self.cell_size, self.cell_size)  
        print(self.clist)
        
    
    def draw_cell_list(self):        
        for i in range (self.cell_size):
            for j in range (self.cell_size):
                if self.clist[i][j] == True:
                    RCT = pg.Rect(self.cell_width * i + 1, self.cell_height * j + 1, self.cell_height - 1, self.cell_width - 1)
                    pg.draw.rect(self.screen, pg.Color('green'), RCT)
                if self.clist[i][j] == False:
                    RCT = pg.Rect(self.cell_width * i + 1, self.cell_height * j + 1, self.cell_height - 1, self.cell_width - 1)
                    pg.draw.rect(self.screen, pg.Color('white'), RCT)
                    
    
    def get_neighbours(self, i, j):
        cnt = 0
        if  i + 1 < self.cell_size and j + 1 < self.cell_size and self.clist[i + 1][j + 1] == True: 
            cnt+=1
        if i - 1 >= 0 and j - 1 >= 0 and self.clist[i - 1][j - 1] == True: 
            cnt+=1
        if j - 1 >= 0 and i + 1 < self.cell_size and self.clist[i + 1][j - 1] == True: 
            cnt+=1
        if i - 1 >= 0 and j + 1 < self.cell_size and self.clist[i - 1][j + 1] == True: 
            cnt+=1
        if  j + 1 < self.cell_size and self.clist[i][j + 1] == True: 
            cnt+=1
        if i + 1 < self.cell_size and self.clist[i + 1][j] == True: 
            cnt+=1
        if  i - 1 >= 0 and self.clist[i - 1][j] == True: 
            cnt+=1
        if j - 1 >= 0 and self.clist[i][j - 1] == True : 
            cnt+=1
        return cnt
        
                    
    def new_gen(self):
        self.is_alive = np.zeros(self.cell_size*self.cell_size)
        self.is_alive.resize(self.cell_size, self.cell_size)
        for i in range(self.cell_size):
            for j in range(self.cell_size):
                if self.clist[i][j] == True and (self.get_neighbours(i, j) == 2 or self.get_neighbours(i, j) == 3):
                    self.is_alive[i][j] = True
                elif self.clist[i][j] == False and self.get_neighbours(i, j) == 3:
                    self.is_alive[i][j] = True
                elif self.clist[i][j] == True and (self.get_neighbours(i, j) > 3 or self.get_neighbours(i, j) < 2):
                    self.is_alive[i][j] = False
        print(self.is_alive)
        for i in range(self.cell_size):
            for j in range(self.cell_size):
                self.clist[i][j] = self.is_alive[i][j]                            
      
      
    def run(self):
        pg.init()
        clock = pg.time.Clock()
        pg.display.set_caption('Game of Life')
        self.screen.fill(pg.Color('white'))
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.draw_grid()            
            self.draw_cell_list()            
            self.new_gen()
            pg.display.flip()             
            clock.tick(self.speed)
        pg.quit()         
               
        
        
if __name__ == '__main__':
    game = GameofLife(640, 640, 20, randomize = True)
    game.cell_list()
    game.run()
    #print(game.get_neighbours(5, 6))
    #game.new_gen()
    
    #game.draw_cell_list()

                    
        