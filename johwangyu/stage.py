import pygame

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 1

class PowerUp:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Portal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.ellipse(screen, (128, 0, 128), (self.x, self.y, 30, 80))

def init_stage(blocks_positions, enemy_positions, powerup_positions, portal_position):
    blocks = [Block(x, y) for x, y in blocks_positions]
    enemies = [Enemy(x, y) for x, y in enemy_positions]
    powerups = [PowerUp(x, y) for x, y in powerup_positions]
    portal = Portal(*portal_position)
    return blocks, enemies, powerups, portal

stages = {
    1: ([(100, 365), (500, 350), (70, 190), (180, 270)],  # 파란색 발판
        [(600, 315), (200, 165)],  # 초록색 적
        [(110, 165), (220, 235), (520, 330)],  # 노란색 코인
        (770, 365)),  # 포탈 위치 추가
####################################################################################################
    2: ([(170, 350), (80, 200), (50, 275), (320, 300), (420, 210), (550, 130), (501, 360)],
        [(1, 315), (300, 165), (590, 95)],
        [(120, 165), (590, 95), (535, 310)],
        (760, 250)),
####################################################################################################
    3: ([(250, 350), (450, 250), (500, 350), (100, 290)],
        [(100, 315),(250, 250), (400, 115), (600, 250)],
        [(140, 255), (590, 265), (520, 330)],
        (760, 365))
}
