import pygame # 파이게임 모듈 임포트
from setting import * # 게임 설정 파일 임포트
from screen import Screen # 화면 설정 클래스 임포트
from block import Block # 블록 클래스 임포트
from obstacle import Obstacle # 장애물 클래스 임포트
from portal import Portal # 포털 클래스 임포트
from item import * # 아이템 클래스 임포트

# character 클래스 정의
class Character:
    def __init__(self, blocks, obstacles, portal, items):
        # 캐릭터 초기값 설정
        self.width = 20
        print(self.width)
        self.height = 20
        print(self.height)
        self.speed = 6
        print(self.speed)
        self.jump_speed = 20
        print(self.jump_speed)
        self.gravity = 1.4
        print(self.gravity)
        self.x = SCREEN_WIDTH // 2
        print(self.x)
        self.y = SCREEN_HEIGHT - self.height * 2
        print(self.y)
        self.vertical_momentum = 0
        print(self.vertical_momentum)
        self.is_on_ground = True
        print(self.is_on_ground)
        self.space_pressed = False
        print(self.space_pressed)
        self.life = 3
        print(self.life)
        self.game_over = False
        print(self.game_over)
        self.game_clear = False
        print(self.game_clear)
        self.blocks = blocks
        print(self.blocks)
        self.obstacles = obstacles
        print(self.obstacles)
        self.portal = portal
        print(self.portal)
        self.items = items
        print(self.items)
        self.colors = [RED, ORANGE, YELLOW] # 생명력 표시에 사용될 색상 리스트
        print(self.colors)
        self.current_color_index = 0 # 현재 색상 인덱스
        print(self.current_color_index)
        self.show_life = False # 생명력 표시 여부
        print(self.show_life)
        self.life_counter = 0 # 생명력 표시 카운터
        print(self.life_counter)
        self.invincible = False # 무적 상태 여부
        print(self.invincible)
        self.invincible_timer = 0 # 무적 지속 시간 타이머
        print(self.invincible_timer)
        self.speed_boost_timer = 0 # 속도 증가 지속 시간 타이머
        print(self.speed_boost_timer)
        self.invincible_remaining_time = 0 # 무적 지속 시간
        print(self.invincible_remaining_time)
        self.speed_boost_remaining_time = 0 # 속도 증가 지속 시간
        print(self.speed_boost_remaining_time)
        self.heart_item_eaten = False # 하트 아이템 먹었나
        print(self.heart_item_eaten)
        
        # 캐릭터 이미지 로드 및 크기 조절
        self.image = pygame.image.load('hyunyoolim\character.png').convert_alpha()
        print(self.image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        print(self.image)
    
    # 캐릭터 초기 위치 설정
    def set_initial_position(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - self.height * 2

    def update_game_state(self):
        current_time = pygame.time.get_ticks()
        
        if self.space_pressed and self.is_on_ground:
            self.vertical_momentum = -self.jump_speed
            self.is_on_ground = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x = max(LEFT_EDGE, self.x - self.speed)
        if keys[pygame.K_RIGHT]:
            self.x = min(RIGHT_EDGE, self.x + self.speed)

        self.x = max(0, min(SCREEN_WIDTH - self.width, self.x))
        self.vertical_momentum += self.gravity
        self.y += self.vertical_momentum
        self.y = min(self.y, floor_y - self.height)

        if self.y >= floor_y - self.height:
            self.y = floor_y - self.height
            self.vertical_momentum = 0
            self.is_on_ground = True

        block_collided = Block.check_collision(self.x, self.y, self.width, self.height, self.blocks)
        obstacle_collided = Obstacle.check_collision(self.x, self.y, self.width, self.height, self.obstacles)
        if block_collided:
            if self.vertical_momentum > 0:
                self.y = block_collided.y - self.height
                self.vertical_momentum = 0
                self.is_on_ground = True

        if obstacle_collided and not self.invincible:
            self.life -= 1
            self.show_life = True
            self.life_counter = current_time
            if self.life == 0:
                self.game_over = True
            else:
                self.current_color_index = min(len(self.colors) - 1, self.current_color_index + 1)
                self.set_initial_position()
                self.vertical_momentum = 0
                self.is_on_ground = True
        
        if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(self.portal.rect):
            self.game_clear = True

        # 무적 효과가 끝나면 무적 해제
        if self.invincible and current_time - self.invincible_timer > 5000:
            self.invincible = False

        # 스피드 효과가 끝나면 장애물 속도 복원
        if self.speed_boost_timer and current_time - self.speed_boost_timer > 5000:
            for obstacle in self.obstacles:
                obstacle.speed *= 2
            self.speed_boost_timer = 0
            
        self.check_item_collision()

    def draw_game_elements(self, screen, blocks, obstacles, portal):
        screen.blit(self.image, (self.x, self.y))
        for block in blocks:
            block.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)
        
        portal.draw(screen)

        if self.show_life:
            font = pygame.font.Font(None, 36)
            text = font.render(f"life : {self.life}", True, BLACK)
            current_time = pygame.time.get_ticks()
            if current_time - self.life_counter >= 1000:  # 1초 동안만 표시
                self.show_life = False

        # 남은 시간 표시
        if self.invincible:
            remaining_time = 5 - (pygame.time.get_ticks() - self.invincible_timer) // 1000
            font = pygame.font.Font(None, 36)
            text = font.render(f"Invincible: {remaining_time}", True, BLACK)
            screen.blit(text, (10, 50))

        if self.speed_boost_timer:
            remaining_time = 5 - (pygame.time.get_ticks() - self.speed_boost_timer) // 1000
            font = pygame.font.Font(None, 36)
            text = font.render(f"Speed Boost: {remaining_time}", True, BLACK)
            screen.blit(text, (10, 80))

    def check_item_collision(self):
        character_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        for item in self.items:
            if character_rect.colliderect(item.rect):
                self.handle_item_collision(item)

    def handle_item_collision(self, item):
        if isinstance(item, HeartItem):
            if not self.heart_item_eaten:
                self.life += 1
                self.heart_item_eaten = True
                item.x = -100  # Move off-screen
        elif isinstance(item, SpeedItem):
            for obstacle in self.obstacles:
                obstacle.speed /= 2  # Halve speed
            self.speed_boost_timer = pygame.time.get_ticks()  # Start timer
            item.x = -100  # Move off-screen
        elif isinstance(item, InvincibilityItem):
            self.invincible = True
            self.invincible_timer = pygame.time.get_ticks()  # Start timer
            item.x = -100  # Move off-screen
