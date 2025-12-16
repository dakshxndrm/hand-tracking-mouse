import pygame
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hand-Controlled Tic Tac Toe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 80)

board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

def draw_board():
    screen.fill(WHITE)

    # Grid
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 2)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 2)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 2)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 2)

    # Draw symbols
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, BLACK)
                screen.blit(text, (col * 100 + 30, row * 100 + 20))

def check_winner():
    lines = []

    lines.extend(board)
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if line[0] != "" and all(cell == line[0] for cell in line):
            return line[0]
    return None

while True:
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // 100
            col = x // 100

            if board[row][col] == "":
                board[row][col] = current_player
                current_player = "O" if current_player == "X" else "X"

    winner = check_winner()
    if winner:
        pygame.display.set_caption(f"{winner} Wins! Restart app")

    pygame.display.update()
