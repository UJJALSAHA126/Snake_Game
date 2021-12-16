import pygame
import random

pygame.init()

# Colors
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

screen_width = 600
screen_height = 600
font = pygame.font.SysFont(None, 35)


def update_display():
    pygame.display.update()


def score_on_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# Creating Window
gameWindow = pygame.display.set_mode(size=(screen_height, screen_height))
pygame.display.set_caption("First Snake Game By 7U")

gameWindow.fill(white)
update_display()


def game_loop():

    # Game Specific variables
    velocity = 7
    diff = 10
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)

    exit_game = False
    game_over = False
    snake_x = 45
    velocity_x = 0
    velocity_y = 0
    snake_y = 45
    snake_size = 10
    fps = 30
    snake_list = []
    snake_length = 1

    clock = pygame.time.Clock()

    # Game Loop
    score = 0
    inc = 10
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            score_on_screen(f"GAME OVER. Your Score is {score}", red, 100, 250)
            update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    game_loop()
                    return

        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT and velocity_x == 0:
                        velocity_x = velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT and velocity_x == 0:
                        velocity_x = -velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP and velocity_y == 0:
                        velocity_y = -velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN and velocity_y == 0:
                        velocity_y = velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x-food_x) < diff and abs(snake_y-food_y) < diff:
                score += inc
                snake_length += 3
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)

            gameWindow.fill(white)

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            score_on_screen(f"Score = {score}", black, 5, 5)

            pygame.draw.rect(gameWindow, red, [
                food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            plot_snake(gameWindow, black, snake_list, snake_size)

            update_display()
            clock.tick(fps)

    pygame.quit()
    quit()

if __name__ == '__main__':
    game_loop()
    
