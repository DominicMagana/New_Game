# File created by: DOminic Magana
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed it so that now I have a game over feature when you go off to the sides

# This file was created by: Dominic Magana
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 
# goals:I want to create a game over feature
# rules:

# import libs
import pygame
import sys
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")



# create game class in order to pass properties to the sprites file
#
class Game:
    def __init__(self):
        # init game window etc.
        self.coins = pygame.sprite.Group()
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        # self.score = 0
        # self.death = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        # platform placement
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # self.all_sprites.add(self.plat1)
        # self.platforms.add(self.plat1)
        # This is to add my character to the game and actually display it
        self.all_sprites.add(self.player)
        # To add all my platforms 
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        # This is to add my little green mobs to the game 
        for i in range(0,10):
            m = Mob(20,20,(0,255,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            # This is so that it is in normal time and the rest calls the other functions 
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    # This is for when you quit the game, the game stops running and if you click spacebar, you jump
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def update(self):
        self.all_sprites.update()
        # I am calling the over function here to make sure it runs continusly
        self.over()
        # if the player is falling
        if self.player.vel.y > 0:
            # This block is if for the player collides with a platform, what will happen
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.standing = True
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
            else:
                self.player.standing = False
# This is for my Game over feature for my game
    def over(self):
        # if player goes out of this boundry self.player.death is True which is called later on line117
        if self.player.pos.x > 800 or self.player.pos.x < 0:
            self.player.death = True
            print ('True')
        # if player is not out of boundry self.player.death is false
        elif self.player.pos.x > 0 or self.player.pos.x < 800:
            self.player.death = False
            print ('false')
    def draw(self):
        # draws the screen blue
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        # if player is standing on a platform, it displays this 
        if self.player.standing:
            self.draw_text("I hit a platform", 24, WHITE, WIDTH/2, HEIGHT/2)
        # self.player.death is true than draw a black screen with the words game over written
        if self.player.death == True:
            # the screen is drawn black
            self.screen.fill(BLACK)
            print ('works')
            self.draw_text("Game Over", 35, WHITE, WIDTH/2, HEIGHT/2)
        # This is kinda of a loop hole because I just want it to display this message down below
        if self.player.death == False:
            self.draw_text("If you move off screen it is game over", 24, WHITE, WIDTH/3, HEIGHT/3)
           
        # is this a method or a function?
        pg.display.flip()
        # this is for the draw text feature, so that everytime you call upon draw text, it renders whatever code is here
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    # def get_mouse_now(self):
    #     x,y = pg.mouse.get_pos()
    #     return (x,y)
        


# instantiate the game class...
g = Game()


# kick off the game loop

while g.running:
            g.new()
     



     
