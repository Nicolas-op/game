import sys

import pygame
from pygame import Font, Surface, Rect
from pygame.examples.aliens import Score

from code.Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH, COLOR_ORANGE, MENU_OPTION
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Obstacle import Obstacle


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode  # mode de jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.player = EntityFactory.get_entity('Player1')
        self.entity_list.append(self.player)
        self.cactus = EntityFactory.get_entity('Cactus')
        self.entity_list.append(self.cactus)
        self.timeout = 20000  # 20 segundos
        self.spawn_timer = 0
        self.score  = 0
        self.last_score_update = pygame.time.get_ticks()
        self.next_difficulty = 50
        self.game_speed = 5
        self.game_over = False
        self.high_score = self.load_high_score()




    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            if self.handle_events():
               return

            self.update()
            self.draw(clock)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_SPACE:
                    self.player.jump()

                if self.game_over and event.key == pygame.K_RETURN:
                        return True

        return False

    def update(self):
        if self.game_over:
            return

        for ent in self.entity_list:
            ent.update()


        self.update_score()
        self.update_difficulty()
        self.check_collision()
        self.spawn_obstacles()




    def check_collision(self):
        for ent in self.entity_list:
            if isinstance(ent, Obstacle):
                if not ent.active:

                    continue

                if self.player.rect.colliderect(ent.rect):
                    self.game_over = True


    def spawn_obstacles(self):

        if self.cactus.active:
            return

        self.spawn_timer += 1
        if self.spawn_timer >= 120:

            self.cactus.rect.left = WIN_WIDTH +50
            self.cactus.active = True
            self.spawn_timer = 0


    def update_score(self):
        current_time = pygame.time.get_ticks()

        if current_time -  self.last_score_update >= 100:
            self.score += 1
            self.last_score_update = current_time


    def update_difficulty(self):

        if self.score >= self.next_difficulty:
            self.game_speed += 1

            for ent in self.entity_list:
                if isinstance(ent, Obstacle):
                   ent.speed = self.game_speed

            self.next_difficulty +=50


    def load_high_score(self):
        return










    def draw(self, clock):

        self.window.fill((0, 0, 0))

        for ent in self.entity_list:
            if hasattr(ent, 'active') and not ent.active:
                continue
            self.window.blit(source=ent.surf, dest=ent.rect)


        self.level_text(14, f'Score: {self.score}', COLOR_WHITE, (450, 10))
        self.level_text(14, f' {self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
        self.level_text(14, f'{clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
        self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))


        if self.game_over:
            self.level_text(30,'GAME OVER', COLOR_WHITE,(200,120))
            self.level_text(30, f'Score Final: {self.score}', COLOR_ORANGE, (200, 150))
            self.level_text(20, 'Pressione ENTER para voltar ao menu', COLOR_ORANGE, (200, 180))
        pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="LucidaSans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)


