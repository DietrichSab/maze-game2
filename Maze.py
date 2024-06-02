import pygame
import sys

MAZE_WIDTH = 800
MAZE_HEIGHT = 600


class Player:
    def __init__(self):
        self.pos = [0, MAZE_HEIGHT // 2]  # Initialize player at the bottom of the maze
        self.speed = 5

    def move(self, dx, dy):
        if self.pos[0] + dx >= 0 and self.pos[0] + dx < MAZE_WIDTH - 1:
            self.pos[0] += dx
        if self.pos[1] + dy >= 0 and self.pos[1] + dy < MAZE_HEIGHT - 2:
            self.pos[1] += dy


class Enemy:
    def __init__(self):
        self.pos = [MAZE_WIDTH - 1, MAZE_HEIGHT // 2]  # Initialize enemy at the top right corner of the maze
        self.speed = 3

    def move(self, player_pos):
        dx = player_pos[0] - self.pos[0]
        dy = player_pos[1] - self.pos[1]

        if abs(dx) > abs(dy):
            if dx > 0:
                self.pos[0] += self.speed
            else:
                self.pos[0] -= self.speed
        elif dy != 0:
            if dy > 0:
                self.pos[1] += self.speed
            else:
                self.pos[1] -= self.speed


class Maze:
    def __init__(self):
        self.player = Player()
        self.enemy = Enemy()

    def update_maze(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move(0, -1)
                    moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.player.move(0, 1)
                    moving_down = True
                elif event.key == pygame.K_LEFT:
                    self.player.move(-1, 0)
                    moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.player.move(1, 0)
                    moving_right = True

        if moving_up and not moving_down:
            self.player.pos[1] -= self.player.speed
        elif moving_down and not moving_up:
            self.player.pos[1] += self.player.speed
        elif moving_left and not moving_right:
            self.player.pos[0] -= self.player.speed
        elif moving_right and not moving_left:
            self.player.pos[0] += self.player.speed

        if abs(self.enemy.pos[0] - self.player.pos[0]) < 10 and abs(self.enemy.pos[1] - self.player.pos[1]) < 10:
            print("Game Over")
            pygame.quit()
            sys.exit()

    def draw_maze(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, MAZE_WIDTH, MAZE_HEIGHT))
        pygame.draw.circle(screen, (255, 0, 0), tuple(self.player.pos), 5)  # Draw player
        pygame.draw.circle(screen, (0, 0, 255), tuple(self.enemy.pos), 5)  # Draw enemy


def main():
    pygame.init()
    screen = pygame.display.set_mode((MAZE_WIDTH, MAZE_HEIGHT))
    clock = pygame.time.Clock()

    maze = Maze()

    player = maze.player
    enemy = maze.enemy

    moving_up = False
    moving_down = False
    moving_left = False
    moving_right = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    moving_up = True
                elif event.key == pygame.K_DOWN:
                    moving_down = True
                elif event.key == pygame.K_LEFT:
                    moving_left = True
                elif event.key == pygame.K_RIGHT:
                    moving_right = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move(0, -5)
            moving_up = True
        elif keys[pygame.K_DOWN]:
            player.move(0, 5)
            moving_down = True
        elif keys[pygame.K_LEFT]:
            player.move(-5, 0)
            moving_left = True
        elif keys[pygame.K_RIGHT]:
            player.move(5, 0)
            moving_right = True

        if not keys[pygame.K_UP] and moving_up:
            moving_up = False
        if not keys[pygame.K_DOWN] and moving_down:
            moving_down = False
        if not keys[pygame.K_LEFT] and moving_left:
            moving_left = False
        if not keys[pygame.K_RIGHT] and moving_right:
            moving_right = False

        enemy.move(player.pos)

        screen.fill((0, 0, 0))  # Clear the screen
        maze.draw_maze(screen)
        pygame.display.flip()
        clock.tick(60)

        if abs(enemy.pos[0] - player.pos[0]) < 10 and abs(enemy.pos[1] - player.pos[1]) < 10:
            print("Game Over")
            pygame.quit()

            sys.exit()


if __name__ == "__main__":
    main()