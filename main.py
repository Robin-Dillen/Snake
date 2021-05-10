import pygame
import random

pygame.init()


class Snake:
    def __init__(self, width, height):
        self.x = random.randrange(20, width - 20, 10)
        self.y = random.randrange(20, height - 20, 10)
        self.move_x = -10
        self.move_y = 0
        self.width, self.height = width, height
        self.length = 1
        self.body = []
        self.alive = True

    def draw(self, win):
        """
        draws the snake on the screen
        :param win: the screen to be draw on
        :return: None
        """
        self.update()

        self.body.append((self.x, self.y, 10, 10))
        self.body = self.body[-self.length:]

        for rect in reversed(self.body):
            pygame.draw.rect(win, (0, 0, 0), rect)

    def update(self):
        """
        updates the position of the snake
        :return: None
        """
        self.x += self.move_x
        self.y += self.move_y
        self.collision_check()

    def collision_check(self):
        """
        checks if the snakes collides with itself or the walls
        :return: none
        """
        if not (0 <= self.x < self.width) or not (0 <= self.y < self.height):
            self.alive = False

        if (self.x, self.y, 10, 10) in self.body:
            self.alive = False


class Food:
    def __init__(self, width, height):
        self.x = random.randrange(0, width, 10)
        self.y = random.randrange(0, height, 10)
        self.w, self.h = width, height

    def draw(self, win):
        """
        draws food on the screen
        :param win: screen
        :return: none
        """
        pygame.draw.rect(win, (0, 255, 255), (self.x, self.y, 10, 10))


class Main:
    def __init__(self):
        self.win_dim = (800, 600)
        self.win = pygame.display.set_mode(self.win_dim)
        pygame.display.set_caption('The Snake Game')
        self.clock = pygame.time.Clock()

        self.snake = Snake(self.win_dim[0], self.win_dim[1])
        self.food = Food(self.win_dim[0], self.win_dim[1])

        self.score = 0

    def run(self):
        """
        main game loop
        :return: none
        """
        while self.snake.alive:

            self.clock.tick(10)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.snake.alive = False
                    break

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_z:
                        self.snake.move_y = -10
                        self.snake.move_x = 0

                    elif event.key == pygame.K_s:
                        self.snake.move_y = 10
                        self.snake.move_x = 0

                    if event.key == pygame.K_q:
                        self.snake.move_x = -10
                        self.snake.move_y = 0

                    elif event.key == pygame.K_d:
                        self.snake.move_x = 10
                        self.snake.move_y = 0

            self.draw()

    def draw(self):
        """
        draws everything on the screen
        :return: none
        """
        self.win.fill((255, 255, 255))

        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.snake.length += 1
            self.score += 1
            self.food = Food(self.win_dim[0], self.win_dim[1])

        self.snake.draw(self.win)
        self.food.draw(self.win)

        pygame.display.update()


m = Main()
m.run()
