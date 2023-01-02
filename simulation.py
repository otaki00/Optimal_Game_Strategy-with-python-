import pygame
import math
# for initialize the module
pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont("comicsan",22)
FONT_TITLE = pygame.font.SysFont("comicsan", 30)
FONT_RESULT = pygame.font.SysFont("comicsan", 24)
WIDTH, HEIGHT = 1200, 770
WHITE = (255, 255, 255)
# YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
def define_window():
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Algorithm Simulation")
    return WIN



def draw(WIN,fullCoinSet, subCoinSet,table):
    WIN.fill(WHITE)
    title = FONT_TITLE.render("Start Mode", 1, BLACK)
    WIN.blit(title, (480, 20))
    text_for_fullCoinSet = FONT.render("FULL COIN SET :", 1, BLACK)
    WIN.blit(text_for_fullCoinSet, (70, 80))
    text_for_subCoinSet = FONT.render("SUB COIN SET :", 1, BLACK)
    WIN.blit(text_for_subCoinSet, (70, 120))
    start_guid1 = FONT_RESULT.render("1- press F to see final Result", 1, BLACK)
    start_guid2 = FONT_RESULT.render("2- press E to Go Through Process step by step", 1, BLACK)
    start_guid3 = FONT_RESULT.render("3- press s to return to start mode", 1, BLACK)
    WIN.blit(start_guid1, (700, 80))
    WIN.blit(start_guid2, (700, 100))
    WIN.blit(start_guid3, (700, 120))

    # draw coins
    i = 1
    for coin in fullCoinSet:
        coin_text = FONT.render(str(coin), 1, BLACK)
        X_CORD = 70 + text_for_fullCoinSet.get_width() + i*30
        WIN.blit(coin_text, (X_CORD, 80))
        i += 1

    i = 1
    for coin in subCoinSet:
        coin_text = FONT.render(str(coin), 1, BLACK)
        X_CORD = 70 + text_for_subCoinSet.get_width() + i*30
        WIN.blit(coin_text, (X_CORD, 120))
        i += 1

    # draw table
    # Vertical Lines
    for i in range(len(fullCoinSet)):
        left = 270 + i * 40
        top = 200
        height = ((len(fullCoinSet)-1) * 30) + 90
        border = pygame.Rect(left, top, 2, height)
        pygame.draw.rect(WIN, BLACK, border, width=0)

        # draw row
        num_text = FONT.render(str(fullCoinSet[i]), 1, BLACK)
        top_n = 230
        left_n = 285 + i * 40
        WIN.blit(num_text, (left_n, top_n))
    for i in range(1,len(fullCoinSet)):
        num_text = FONT.render(str(fullCoinSet[i]), 1, BLACK)
        top_n = 260 + i * 30
        left_n = 245
        WIN.blit(num_text, (left_n, top_n))

    num_text = FONT.render(str(fullCoinSet[0]), 1, BLACK)
    top_n = 230 + 1 * 30
    left_n = 245
    WIN.blit(num_text, (left_n, top_n))

    # Horizantal Lines
    for i in range(len(fullCoinSet)):
        left = 220
        top = 250 + i * 30
        width = ((len(fullCoinSet)-1) * 40) + 90
        border = pygame.Rect(left, top, width, 2)
        pygame.draw.rect(WIN, BLACK, border, width=0)
    # for i in range(len(fullCoinSet)):
    #     for j in range(len(fullCoinSet)):
    #         num_text = FONT.render(str(table[i][j]), 1, BLACK)
    #         left = 285 + j * 40
    #         top = 260 + i * 30
    #         WIN.blit(num_text, (left, top))
    pygame.display.update()

def draw_final_results(WIN,fullCoinSet, subCoinSet, table):
    WIN.fill(WHITE)
    title = FONT_TITLE.render("Final Result", 1, BLACK)
    WIN.blit(title, (480, 20))
    text_for_fullCoinSet = FONT.render("FULL COIN SET :", 1, BLACK)
    WIN.blit(text_for_fullCoinSet, (70, 80))
    text_for_subCoinSet = FONT.render("SUB COIN SET :", 1, BLACK)
    WIN.blit(text_for_subCoinSet, (70, 120))

    # draw coins
    i = 1
    for coin in fullCoinSet:
        coin_text = FONT.render(str(coin), 1, BLACK)
        X_CORD = 70 + text_for_fullCoinSet.get_width() + i*30
        WIN.blit(coin_text, (X_CORD, 80))
        i += 1

    i = 1
    for coin in subCoinSet:
        coin_text = FONT.render(str(coin), 1, BLACK)
        X_CORD = 70 + text_for_subCoinSet.get_width() + i*30
        WIN.blit(coin_text, (X_CORD, 120))
        i += 1

    # draw table
    # Vertical Lines
    for i in range(len(fullCoinSet)):
        left = 270 + i * 40
        top = 200
        height = ((len(fullCoinSet)-1) * 30) + 90
        border = pygame.Rect(left, top, 2, height)
        pygame.draw.rect(WIN, BLACK, border, width=0)

        # draw row
        num_text = FONT.render(str(fullCoinSet[i]), 1, BLACK)
        top_n = 230
        left_n = 285 + i * 40
        WIN.blit(num_text, (left_n, top_n))
    for i in range(1,len(fullCoinSet)):
        num_text = FONT.render(str(fullCoinSet[i]), 1, BLACK)
        top_n = 260 + i * 30
        left_n = 245
        WIN.blit(num_text, (left_n, top_n))

    num_text = FONT.render(str(fullCoinSet[0]), 1, BLACK)
    top_n = 230 + 1 * 30
    left_n = 245
    WIN.blit(num_text, (left_n, top_n))

    # Horizantal Lines
    for i in range(len(fullCoinSet)):
        left = 220
        top = 250 + i * 30
        width = ((len(fullCoinSet)-1) * 40) + 90
        border = pygame.Rect(left, top, width, 2)
        pygame.draw.rect(WIN, BLACK, border, width=0)
    for i in range(len(fullCoinSet)):
        for j in range(len(fullCoinSet)):
            num_text = FONT.render(str(table[i][j]), 1, BLACK)
            left = 285 + j * 40
            top = 260 + i * 30
            WIN.blit(num_text, (left, top))
    best_score = FONT_RESULT.render("best score : " + str(table[0][len(fullCoinSet)-1]),1, BLACK)
    WIN.blit(best_score, (750, 80))
    wins_set = []
    n = len(fullCoinSet)-1
    flag = True
    i = 0
    while flag:
        if table[i][n-1] >= table[i+1][n-1]:
            value = table[i][n] - (min(table[i][n-1], table[i][n-2]))
            wins_set.append(value)
            n =  table[i].index(min(table[i][n-1], table[i][n-2]))
        elif table[i][n-1] < table[i+1][n-1]:
            value = table[i][n] - (max(table[i+1][n-1], table[i+1][n-2]))
            wins_set.append(value)
            i+=1
            n =  table[i].index(max(table[i][n-1], table[i][n-2]))
        if n == 0:
            wins_set.append(fullCoinSet[0])
            flag = False
        if n == 1:
            wins_set.append(fullCoinSet[1])
            flag = False
        elif table[i][n-1]  == 0 or table[i][n-2] == 0:
            value_1 = max(table[i][n-1], table[i][n-2])
            wins_set.append(value_1)
            flag = False
    wins_score = FONT_RESULT.render("Wins Set : ",1, BLACK)
    WIN.blit(wins_score, (750, 110))
    
    i = 0
    for coin in wins_set:
        coin_text = FONT_RESULT.render(str(wins_set[len(wins_set)-1-i]), 1, BLACK)
        X_CORD = 750 + text_for_fullCoinSet.get_width() + i*30
        WIN.blit(coin_text, (X_CORD, 110))
        i += 1
    # print(wins_set)
    
    pygame.display.update()

def draw_number(number, x, y):
    num_text = FONT.render(str(number), 1, BLACK)
    left = 285 + x * 40
    top = 260 + y * 30
    WIN.blit(num_text, (left, top))
    # pygame.display.update()

def draw_steps(WIN,fullCoinSet, subCoinSet,table, step_num, x,y,z,first_value, last_value, result, i ,j):
    WIN.fill(WHITE)
    title = FONT_TITLE.render("STEP "+str(step_num), 1, BLACK)
    WIN.blit(title, (480, 20))
    text_for_fullCoinSet = FONT.render("FULL COIN SET :", 1, BLACK)
    WIN.blit(text_for_fullCoinSet, (70, 80))
    text_for_subCoinSet = FONT.render("SUB COIN SET :", 1, BLACK)
    WIN.blit(text_for_subCoinSet, (70, 120))

    # draw coins
    i = 1
    for coin in fullCoinSet:
        coin_text = FONT.render(str(coin), 1, BLACK)
        X_CORD = 70 + text_for_fullCoinSet.get_width() + i*30
        WIN.blit(coin_text, (X_CORD, 80))
        i += 1

    i = 1
    for coin in subCoinSet:
        coin_text = FONT.render(str(coin), 1, BLACK)
        X_CORD = 70 + text_for_subCoinSet.get_width() + i*30
        WIN.blit(coin_text, (X_CORD, 120))
        i += 1

    # draw table
    # Vertical Lines
    for i in range(len(fullCoinSet)):
        left = 270 + i * 40
        top = 200
        height = ((len(fullCoinSet)-1) * 30) + 90
        border = pygame.Rect(left, top, 2, height)
        pygame.draw.rect(WIN, BLACK, border, width=0)

        # draw row
        num_text = FONT.render(str(fullCoinSet[i]), 1, BLACK)
        top_n = 230
        left_n = 285 + i * 40
        WIN.blit(num_text, (left_n, top_n))
    for i in range(1,len(fullCoinSet)):
        num_text = FONT.render(str(fullCoinSet[i]), 1, BLACK)
        top_n = 260 + i * 30
        left_n = 245
        WIN.blit(num_text, (left_n, top_n))

    num_text = FONT.render(str(fullCoinSet[0]), 1, BLACK)
    top_n = 230 + 1 * 30
    left_n = 245
    WIN.blit(num_text, (left_n, top_n))

    # Horizantal Lines
    for i in range(len(fullCoinSet)):
        left = 220
        top = 250 + i * 30
        width = ((len(fullCoinSet)-1) * 40) + 90
        border = pygame.Rect(left, top, width, 2)
        pygame.draw.rect(WIN, BLACK, border, width=0)
    for i in range(len(fullCoinSet)):
        for j in range(len(fullCoinSet)):
            num_text = FONT.render(str(table[i][j]), 1, BLACK)
            left = 285 + j * 40
            top = 260 + i * 30
            WIN.blit(num_text, (left, top))
    text = "max( ("+ str(first_value)+ " + min("+str(x)+","+str(y)+")) , ("+str(last_value)+" + min("+str(y)+","+str(z)+")) )"
    relation = FONT_RESULT.render(f"table[{i}][{j}] ="+text, 1, BLACK)
    WIN.blit(relation, (700, 80))
    final_result_text =FONT_RESULT.render("value = " + str(result), 1, BLACK) 
    WIN.blit(final_result_text, (700, 100))
    pygame.display.update()

def main(arr):
    WIN = define_window()
    run = True
    clock = pygame.time.Clock()
    sub_set = []
    n = len(arr)
    print(n)
    table = [[0 for i in range(n)] for i in range(n)]
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap
            x = 0
            if((i + 2) <= j):
                x = table[i+2][j]
            y = 0
            if((i + 1) <= (j - 1)):
                y = table[i + 1][j - 1]
            z = 0
            if(i <= (j - 2)):
                z = table[i][j - 2]
            table[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
    table_steps = [ ]
    start = True
    if start:
        num_of_moves = n * n
        move_num = 0
        gap_moves = n-1 
        j_moves = 0
        table_steps = [[0 for i in range(n)] for i in range(n)]
        # start = False
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if start:
                draw(WIN,arr, sub_set, table)
                start = False
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    draw(WIN,arr, sub_set, table)
                    start = True
                if event.key == pygame.K_f:
                # craete inital table and fill with zeros
                    draw_final_results(WIN,arr, sub_set, table)
                # the step by step simulation
                if event.key == pygame.K_e:
                    if start:
                        draw_steps(WIN,arr, sub_set, table_steps)
                    if move_num == 0:
                        gap = 0
                    else:
                        gap = int((move_num) / (n))
                    if gap < n:
                        j = j_moves
                        if j < n:
                            # gap = int((move_num+1) / (n+1))
                            # j = gap
                            i = j - gap
                            # print(j, gap, i)
                            x = 0
                            if((i + 2) <= j):
                                x = table_steps[i+2][j]
                            y = 0
                            if((i + 1) <= (j - 1)):
                                y = table_steps[i + 1][j - 1]
                            z = 0
                            if(i <= (j - 2)):
                                z = table_steps[i][j - 2]
                            table_steps[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
                            int_i = i
                            int_j = j
                            draw_steps(WIN,arr, arr[i:j], table_steps, move_num, x,y,z,arr[i], arr[j], table[i][j], j_moves-gap , j_moves )
                            j_moves += 1
                            move_num += 1
                            
                        else:
                            # print("last move")
                            j_moves =  gap
        
    pygame.quit()


# main()
