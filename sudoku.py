import pygame

with open("sudoku_board.txt") as sFile:
    board = [line.split() for line in sFile]

board = [[int(i) for i in line] for line in board]

zeros = []
for i in range(9):
    for j in range(9):
        if(board[i][j] == 0):
            zeros.append((i, j))

def check(n, pair):
    i, j = pair

    if n in board[i]:
        return 0

    for line in board:
        if line[j] == n:
            return 0

    initial_i, initial_j = i // 3 * 3, j // 3 * 3
    
    for x in range(initial_i, initial_i+3):
        for y in range(initial_j, initial_j+3):
            if(board[x][y] == n):
                return 0                
    return 1

def solved():
    for line in board:
        for i in line:
            if i == 0:
                return 0
    return 1

def print_board():
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = ' ')

            if ((j+1) % 3 == 0) and (j != 9):
                print(' ', end='')

        if((i+1) % 3 == 0):
            print('')
        print('')

def solve(i):
    for num in range(1, 10):
        if check(num, zeros[i]):

            board[zeros[i][0]][zeros[i][1]] = num

            if i < len(zeros) - 1:
                solve(i+1)
            else:
                print_board()
                exit()
            board[zeros[i][0]][zeros[i][1]] = 0

def main():
    pygame.init()

    gameDisplay = pygame.display.set_mode((459,459))
    pygame.display.set_caption('Sudoku')

    background = pygame.Surface(gameDisplay.get_size())
    background.fill((255,255,255))
    background = background.convert()
    gameDisplay.blit(background, (0, 0))

    block_size = gameDisplay.get_size()[0] // 9

    for x in range(9):
        for y in range(9):
            pygame.draw.rect(gameDisplay, (0, 0, 0), (x*block_size, y*block_size, block_size, block_size), 1)
    
    myfont = pygame.font.SysFont('Arial', 25)
    print(board)
    for x in range(9):
        for y in range(9):
            if board[x][y] != 0:
                textsurface = myfont.render(str(board[x][y]), False, (0, 0, 0))
                gameDisplay.blit(textsurface, ((y+0.36)*(block_size), (x+0.2)*(block_size)))

    clock = pygame.time.Clock()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                key_event = pygame.event.wait()
                key_event = pygame.event.wait()
                textsurface = myfont.render(str(key_event.key - 48), False, (0, 0, 0))
                y = event.pos[0] // block_size
                x = event.pos[1] // block_size
                pygame.draw.rect(gameDisplay, (255, 255, 255), ((y+0.1)*block_size, (x+0.1)*block_size, block_size-10, block_size-10))
                gameDisplay.blit(textsurface, ((y+0.36)*(block_size), (x+0.2)*(block_size)))
                print(event.pos)
        

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()