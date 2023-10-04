import time
import json
import pygame
import os
pygame.init()

class Main:
    def __init__(self, sprites=[], code=[], backdrops=[], variables=[], name=None):
        self.sprites = sprites
        self.backdrops = backdrops
        self.code = code
        self.screen = 'load'
        self.display = {}
        self.variables = variables
        if name == None:
            self.choose_file()
        while True:
            draw_screen()
    
    def draw_screen(self):
        if self.code == []:
            self.choose_file()
    
    def cursor(self):
        mouse = pygame.mouse.get_pos()
    
    def save(self):
        with open('scratch/' + self.name + '.txt', 'w') as f:
            for item in self.code:
                f.write(json.dumps(item) + '\n')
    
    def load(self, name):
        with open('scratch/' + name + '.txt') as f:
            lines = f.readlines()

        self.code = []
        for line in lines:
            self.code.append(json.loads(line))
        self.name = name
    
    def choose_file(self):
        files = list(os.walk('scratch/'))
        if files != []:
            show_files_1 = []
            counter = 0
            for _ in files:
                for item in _:
                    if counter == 3:
                        counter = 0
                    if counter == 2:
                        show_files_1.append(item[0])
                    counter += 1
            
            show_files = []
            
            for file in show_files_1:
                cur_word = ''
                for letter in file:
                    if letter == '.':
                        break
                    cur_word += letter
                show_files.append(cur_word)
            
            for item in show_files:
                print(item)
            while True:
                choosen = input('Choose which file you would like to load.\n')
                if choosen in show_files:
                    break
                print('That is not a valid file')
            self.load(choosen)
                

main = Main()