import random
import curses
import time

def show_menu():
    w.clear()
    w.border(0)
    w.addstr(sh // 2 - 2, sw // 2 - 5, "Serpiente")
#    w.addstr(sh // 2, sw // 2 - 8, "1. Nueva partida")
#    w.addstr(sh - 2, sw // 2 - 16, "Presiona 'q' para salir")
    # 
    # option1_text = "1 - Nueva partida"
    # option_espacio = " "
    # option2_text = "2 - Salir"
    #
    # w.addstr(sh // 2 + 2, sw // 2 - len(option1_text) // 2, option1_text)
    # w.addstr(sh // 2 + 3, sw // 2 - len(option1_text) // 2, option_espacio)
    # w.addstr(sh // 2 + 4, sw // 2 - len(option2_text) // 2, option2_text)
    #
    option1_text = "1. Nueva partida"
    option2_text = "2. Salir"

    option1_x = sw // 2 - len(option1_text) // 2
    option2_x = sw // 2 - len(option2_text) // 2

    w.addstr(sh // 2 + 2, option1_x, option1_text)
    w.addstr(sh // 2 + 4, option2_x, option2_text)
    while True:
        key = w.getch()
        if key == ord('1'):
            w.clear()
            break
        elif key == ord('2'):
            curses.endwin()
            quit()

def game_over(score):
    w.clear()
    w.border(0)
    w.addstr(sh // 2 - 2, sw // 2 - 5, "Game Over")
#    w.addstr(sh // 2, sw // 2 - 8, "Puntuación: {}".format(score))
    score_text = "Puntuación: {}".format(score)
    score_x = sw // 2 - len(score_text) // 2
    w.addstr(sh // 2, score_x, score_text)
    # option1_text = "1 - Nueva partida"
    # option2_text = "2 - Salir"
    #
    # w.addstr(sh // 2 + 2, sw // 2 - len(option1_text) // 2, option1_text)
    # w.addstr(sh // 2 + 4, sw // 2 - len(option2_text) // 2, option2_text)
    #
      
    option1_text = "1. Nueva partida"
    option2_text = "2. Salir"

    option1_x = sw // 2 - len(option1_text) // 2
    option2_x = sw // 2 - len(option2_text) // 2

    w.addstr(sh // 2 + 2, option1_x, option1_text)
    w.addstr(sh // 2 + 4, option2_x, option2_text)

    while True:
        key = w.getch()
        if key == ord('1'):
            w.clear()
            break
        elif key == ord('2'):
            curses.endwin()
            quit()

stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

show_menu()

w.border(0)

snake_x = sw // 4 + 1
snake_y = sh // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

direction = curses.KEY_RIGHT

food = [sh // 2, sw // 2]

key = curses.KEY_RIGHT

score = 0
score_text = "Puntuación: {}".format(score)
w.addstr(0, sw // 2 - len(score_text) // 2, score_text)

quit_message = "Presiona 'q' para salir"
w.addstr(sh - 1, sw // 2 - len(quit_message) // 2, quit_message)

delay = 0.1
prev_time = time.time()
apple_counter = 0

while True:
    current_time = time.time()
    elapsed_time = current_time - prev_time

    if curses.KEY_DOWN <= direction <= curses.KEY_RIGHT:
        if elapsed_time >= delay:
            prev_time = current_time

    next_key = w.getch()
    if next_key != -1:
        if next_key == curses.KEY_DOWN and direction != curses.KEY_UP:
            direction = next_key
        elif next_key == curses.KEY_UP and direction != curses.KEY_DOWN:
            direction = next_key
        elif next_key == curses.KEY_LEFT and direction != curses.KEY_RIGHT:
            direction = next_key
        elif next_key == curses.KEY_RIGHT and direction != curses.KEY_LEFT:
            direction = next_key

        if next_key == ord('q') or next_key == ord('Q'):
            game_over(score)

    new_head = [snake[0][0], snake[0][1]]
    if direction == curses.KEY_DOWN:
        new_head[0] += 1
    if direction == curses.KEY_UP:
        new_head[0] -= 1
    if direction == curses.KEY_LEFT:
        new_head[1] -= 1
    if direction == curses.KEY_RIGHT:
        new_head[1] += 1
    
    snake.insert(0, new_head)
    if snake[0][0] == 0:
        snake[0][0] = sh - 2
    elif snake[0][0] == sh - 1:
        snake[0][0] = 1
    if snake[0][1] == 0:
        snake[0][1] = sw - 2
    elif snake[0][1] == sw - 1:
        snake[0][1] = 1
    


    if snake[0][0] in [0, sh - 1] or snake[0][1] in [0, sw - 1] or snake[0] in snake[1:]:
        break
   
    if snake[0] == food:
        score += 1
        score_text = "Puntuación: {}".format(score)
        w.addstr(0, sw // 2 - len(score_text) // 2, score_text)
        
        if apple_counter % 2 == 0:
            delay *= 0.7

        while True:
            new_food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
            if new_food not in snake:
                food = new_food
                break

    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(food[0], food[1], '🍏')
    w.addch(snake[0][0], snake[0][1], curses.ACS_BLOCK)
    time.sleep(delay)

curses.endwin()


game_over(score)
