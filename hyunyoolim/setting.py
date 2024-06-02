import pygame
import sys
from setting import *
from obstacle import Obstacle
from block import Block
from portal import Portal

class Screen:
    def __init__(self):
        pass
    
    
    

    @staticmethod
    def show_start_screen(screen):
        """게임 시작 화면 표시"""
        screen.fill(WHITE)
        font = pygame.font.Font(None, 64)
        text = font.render("Press SPACE to Start", True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        Screen.wait_for_space()

    @staticmethod
    def wait_for_space():
        """SPACE 키 입력을 대기"""
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False

    @staticmethod
    def show_clear_screen(screen):
        """게임 클리어 화면 표시"""
        screen.fill(WHITE)
        font = pygame.font.Font(None, 64)
        text = font.render("Game Clear!", True, GREEN)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)

    @staticmethod
    def show_game_over_screen(screen, game_manager):
        """게임 오버 화면 표시 및 재시작/종료 선택"""
        screen.fill(WHITE)
        font = pygame.font.Font(None, 64)
        text = font.render("Game Over", True, RED)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)

        try_again_button = pygame.Rect(250, 400, 300, 50)
        pygame.draw.rect(screen, GREEN, try_again_button)
        font = pygame.font.Font(None, 36)
        text = font.render("Try Again", True, BLACK)
        text_rect = text.get_rect(center=try_again_button.center)
        screen.blit(text, text_rect)

        exit_button = pygame.Rect(250, 475, 300, 50)
        pygame.draw.rect(screen, RED, exit_button)
        text = font.render("Exit", True, WHITE)
        text_rect = text.get_rect(center=exit_button.center)
        screen.blit(text, text_rect)

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if try_again_button.collidepoint(event.pos):
                        print("한 번 더 !!")
                        game_manager.reset_game()
                        return  # 메인 루프로 돌아가기 위해 반환
                    elif exit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

    @staticmethod
    def draw_game_elements(screen, character, blocks, obstacles, portal):
        """게임 요소를 화면에 그림"""
        pygame.draw.rect(screen, RED, pygame.Rect(character.x, character.y, character.width, character.height))
        for block in blocks:
            block.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)
        if portal:
            portal.draw(screen)
