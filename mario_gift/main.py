#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import pygame
import player
import level
import camera

# Объявляем переменные
# TODO: продумать необходимые константы
TITLE = "САША"

BG_DIR = "levels/bg.gif"

def main():
    # TODO: реализовать работу приложения
    pygame.init()
    screen = pygame.display.set_mode(camera.DISPLAY)
    pygame.display.set_caption(TITLE)
    bg = pygame.image.load(BG_DIR)
    level1 = level.Level()
    level1.getPlatform()
    main_camera = camera.Camera(len(level1.lines_of_level[0]),
                                len(level1.lines_of_level))
    entities = pygame.sprite.Group()
    for pf in level1.platforms:
        entities.add(pf)
    hero = player.Player(55, 55)
    timer = pygame.time.Clock()
    entities.add(hero)
    while True:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit(1)
            hero.move((event))

        screen.blit(bg, (0, 0))
        #entities.draw(screen)
        hero.update(level1.platforms)
        main_camera.update(hero)
        for e in entities:
            screen.blit(e.image, main_camera.apply(e))

        pygame.display.update()

if __name__ == "__main__":
    main()
