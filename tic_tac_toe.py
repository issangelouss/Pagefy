import pygame
import sys


def check(field, sign):
    zeros = 0
    for row in field:
        zeros += row.count(0)
        if row.count(sign) == 3:
            return f'{sign} wins'
    for col in range(3):
        if field[0][col] == sign and field[1][col] == sign and field[2][col] == sign:
            return f'{sign} wins'
    if field[0][0] == sign and field[1][1] == sign and field[2][2] == sign:
        return f'{sign} wins'
    if field[0][2] == sign and field[1][1] == sign and field[2][0] == sign:
        return f'{sign} wins'
    if zeros == 0:
        return 'Piece'
    return False


pygame.init()
block_size = 100
border = 15
field = [[0] * 3 for i in range(3)]
query = 0
game_over = False
width = height = block_size * 3 + border * 4

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Крестики-нолики')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (block_size + border)
            row = y_mouse // (block_size + border)
            if field[row][col] == 0:
                if query % 2 == 0:
                    field[row][col] = 'x'
                else:
                    field[row][col] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            field = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill((0, 0, 0))

    if not game_over:
        for row in range(3):
            for col in range(3):
                if field[row][col] == 'x':
                    color = (255, 0, 0)
                elif field[row][col] == 'o':
                    color = (0, 255, 0)
                else:
                    color = (255, 255, 255)
                x = col * block_size + border * (col + 1)
                y = row * block_size + border * (row + 1)
                pygame.draw.rect(screen, color, (x, y, block_size, block_size))
                if color == (255, 0, 0):
                    pygame.draw.line(screen, (255, 255, 255), (x + 5, y + 5), (x + block_size - 5, y + block_size - 5), 3)
                    pygame.draw.line(screen, (255, 255, 255), (x + block_size - 5, y + 5), (x + 5, y + block_size - 5), 3)
                elif color == (0, 255, 0):
                    pygame.draw.circle(screen, (255, 255, 255), (x + block_size // 2, y + block_size // 2), block_size // 2 - 3, 3)
        if (query - 1) % 2 == 0:
            game_over = check(field, 'x')
        else:
            game_over = check(field, 'o')

    if game_over:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('stxingkai', 80)
        text1 = font.render(game_over, True, (255, 255, 255))
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, (text_x, text_y))

    pygame.display.update()
