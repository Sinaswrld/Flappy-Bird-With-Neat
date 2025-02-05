import pygame
import neat
import time
import os 
import random 

WIN_WIDTH = 600
MIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")))
BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))

class Bird: 
  IMGS = BIRD_IMGS
  MAX_ROTATION = 25
  ROT_VEL = 20
  ANIMATION_TIME = 5
  
  def __init__(self,x,y):
    self.x = x 
    self.y = y
    self.tilt = 0 