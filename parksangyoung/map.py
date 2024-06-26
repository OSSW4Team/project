from block import Block, MovingBlock
from obstacle import Spike
from portal import Portal

class Map1: # 1스테이지
    initial_character_x = 100
    initial_character_y = 400
    portal = Portal(720, 50, 70, 70, 'map2', 'images/portal.png')
    blocks = [  
        Block(100, 500, image_path='C:/OSSW4/Img/block.png'),
        Block(300, 400, image_path='C:/OSSW4/Img/block.png'),
        Block(500, 300, image_path='C:/OSSW4/Img/block.png'),
        Block(700, 200, image_path='C:/OSSW4/Img/block.png')
    ]

class Map2: # 2스테이지
    initial_character_x = 50
    initial_character_y = 100
    portal = Portal(720, 50, 70, 70, 'map3', 'images/portal.png')
    blocks = [
        Block(50, 100, image_path='C:/OSSW4/Img/block.png'),
        Block(250, 400, image_path='C:/OSSW4/Img/block.png'),
        Block(500, 300, image_path='C:/OSSW4/Img/block.png'),
        Block(600, 200, image_path='C:/OSSW4/Img/block.png')
    ]

class Map3: # 3스테이지
    initial_character_x = 0
    initial_character_y = 300
    portal = Portal(720, 150, 70, 70, 'map4', 'images/portal.png')
    blocks = [
        Block(0, 300, image_path='C:/OSSW4/Img/block.png'),
        Block(100, 300, image_path='C:/OSSW4/Img/block.png'),
        Block(200, 300, image_path='C:/OSSW4/Img/block.png'),
        Block(300, 300, image_path='C:/OSSW4/Img/block.png'),
        Block(400, 300, image_path='C:/OSSW4/Img/block.png'),
        Block(500, 300, image_path='C:/OSSW4/Img/block.png'),
        Block(600, 300, image_path='C:/OSSW4/Img/block.png'),
        Block(700, 300, image_path='C:/OSSW4/Img/block.png')
    ]
    spikes = [
    Spike(100, 250),
    Spike(100, 280),
    Spike(150, 250),
    Spike(150, 280),
    Spike(200, 250),
    Spike(200, 280),
    Spike(300, 250),
    Spike(300, 280),
    Spike(350, 250),
    Spike(350, 280),
    Spike(400, 250),
    Spike(400, 280),
    Spike(500, 250),
    Spike(500, 280),
    Spike(550, 250),
    Spike(550, 280),
    Spike(600, 250),
    Spike(600, 280)
    ]

class Map4: # 4스테이지
    initial_character_x = 0
    initial_character_y = 550
    portal = Portal(720, 45, 70, 70, 'map5', 'images/portal.png')
    blocks = [
        Block(0, 550, image_path='C:/OSSW4/Img/block.png'),
        MovingBlock(400, 525, move_range=200, speed=2, image_path='C:/OSSW4/Img/block.png'),
        Block(700, 425, image_path='C:/OSSW4/Img/block.png'),
        MovingBlock(400, 300, move_range=200, speed=3, image_path='C:/OSSW4/Img/block.png'),
        Block(0, 200, image_path='C:/OSSW4/Img/block.png'),
        MovingBlock(400, 100, move_range=200, speed=4, image_path='C:/OSSW4/Img/block.png')
    ]
