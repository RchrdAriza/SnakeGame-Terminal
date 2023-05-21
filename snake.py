import random
import curses
import time

def show_menu():
    w.clear()
    w.border(0)
    
    title = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡖⣻⠉⢿⣿⠆⠈⠙⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡚⠒⠊⠙⠂⠀⠀⢆⣱⡘⡷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡟⠛⠳⣖⠒⠒⢙⡤⣿⣷⠃⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢻⠆⠤⠤⡗⣿⢻⣼⢀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠸⣼⣏⡒⢲⠟⡟⣾⡾⣎⢾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⢸⡴⢻⠃⠀⡜⢸⣻⠴⠛⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣰⣰⣷⠏⠀⢰⠃⣿⣷⢳⣰⣤⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠹⣯⣿⣟⠢⢤⣇⣸⣿⡽⣧⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⣭⠓⠌⠉⡛⠉⣿⣼⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⣰⠁⣼⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠐⠁⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⣼⠏⢰⢦⡀⠀⠀⠀⠀⠀⣀⡠⠤⠤⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⡀⠀⠀⣸⡟⠀⠈⢯⡓⠦⢤⡤⠴⠚⠁⠀⠀⠀⠀⠀⢘⠍⠳⡄⠀⠀⠀⠀
⠀⠀⢀⣠⠤⠖⠒⡒⠒⠢⢤⡗⢤⡉⢺⠒⣿⡃⣀⣀⣠⠽⠷⠒⠛⠉⠉⣉⣉⣛⣛⣛⣛⡉⠀⠀⣸⠀⠀⠀⠀
⢀⡴⠋⠀⠀⢠⠊⠀⠀⠀⢸⡇⢄⡈⠛⣏⣿⠉⠁⠀⢀⣠⠤⠖⠚⠉⠉⠀⠀⠀⠓⠦⣄⠉⠙⠚⠯⣄⡀⠀⠀
⡜⠀⠀⠀⠀⢸⣤⡶⠦⢤⣼⣇⠀⠈⢉⣧⢿⣧⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠉⢦⠀
⣇⠀⠀⠀⠀⠈⠳⣄⣀⣀⣈⣿⠑⠢⠤⠼⡞⣿⡄⠀⠀⠀⠀⠀⢀⣀⣠⡤⠴⠶⠶⠒⠒⢿⡇⠀⠀⠀⠀⠸⡆
⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢇⠈⠐⠂⠙⣖⠻⣤⣠⣤⡶⠞⠋⠉⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⢸⠇
⠀⠈⠓⢦⣀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡀⠀⠀⠈⠢⠀⠉⠓⠦⠤⢤⣀⣠⠤⠤⠤⠒⠚⠉⠀⠀⠀⠀⠀⣠⡟⠁
⠀⠀⠀⠀⠈⠙⠓⠲⠶⠶⠶⠶⠞⠛⠓⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⠴⠞⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
   # w.addstr(sh // 2 - 6, sw // 2 - len(title) // 2, title)
    w.addstr(sh // 2 - 6, sw // 2 - len(title.splitlines()[0]) // 2, title)
    # snake_x = sw // 2 - len(title.splitlines()[0]) // 2
    # snake_y = sh // 2 - len(title.splitlines()) - 6
    # 
    # w.addstr(snake_y, snake_x, title)
    #
    option1_text = "1. New Game"
    option2_text = "2. Quit"

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
    title = "Game Over"
    w.addstr(sh // 2 - 6, sw //2 - len(title) // 2, title)
   # w.addstr(sh // 2 - 2, sw // 2 - 5, "Game Over")

    score_text = "Score: {}".format(score)
    score_x = sw // 2 - len(score_text) // 2
    w.addstr(sh // 2, score_x, score_text)


    option2_text = "1. Quit"


    option2_x = sw // 2 - len(option2_text) // 2


    w.addstr(sh // 2 + 4, option2_x, option2_text)

    while True:
        key = w.getch()
        if key == ord('2'):
            w.clear()
            break
        if key == ord('1'):
            curses.endwin()
            quit()

stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)
curses.noecho()

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
score_text = "Score: {}".format(score)
w.addstr(0, sw // 2 - len(score_text) // 2, score_text)

quit_message = "Press 'q' to quit"
w.addstr(sh - 1, sw // 2 - len(quit_message) // 2, quit_message)

delay = 0.1
prev_time = time.time()
apple_counter = 0
pear = None
pear_timer = None
pear_score = 4
pear_duration = 5
pear_chance = 10
bomb = None
bomb_timer = None
bomb_duration = 3
bomb_chance = 20

while True:
   
    current_time = time.time()
    elapsed_time = current_time - prev_time

    if curses.KEY_DOWN <= direction <= curses.KEY_RIGHT:
        if elapsed_time >= delay:
            prev_time = current_time


    next_key = w.getch()
    if next_key != -1:
        if (next_key == curses.KEY_DOWN or next_key == ord('s')) and direction != curses.KEY_UP:
            direction = next_key
        elif (next_key == curses.KEY_UP or next_key == ord('w')) and direction != curses.KEY_DOWN:
            direction = next_key
        elif (next_key == curses.KEY_LEFT or next_key == ord('a')) and direction != curses.KEY_RIGHT:
            direction = next_key
        elif (next_key == curses.KEY_RIGHT or next_key == ord('d')) and direction != curses.KEY_LEFT:
            direction = next_key

    if next_key == ord('q') or next_key == ord('Q'):
        game_over(score)


       
    new_head = [snake[0][0], snake[0][1]]
    if direction == curses.KEY_DOWN or direction == ord("s"):
        new_head[0] += 1
    if direction == curses.KEY_UP or direction == ord("w"):
        new_head[0] -= 1
    if direction == curses.KEY_LEFT or direction == ord("a"):
        new_head[1] -= 1
    if direction == curses.KEY_RIGHT or direction == ord("d"):
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

    if score % 5 == 0 and score > 0 and pear is None and random.randint(1, pear_chance) == 1:
        while True:
            new_pear = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
            if new_pear not in snake and new_pear != food:
                pear = new_pear
                pear_timer = time.time()
                break
    elif pear is not None and time.time() - pear_timer > pear_duration:
        w.addch(pear[0], pear[1], ' ')
        pear = None

    if score % 8 == 0 and score > 0 and bomb is None and random.randint(1, bomb_chance) == 1:
        while True:
            new_bomb = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
            if new_bomb not in snake and new_bomb != food and new_bomb != pear:
                bomb = new_bomb
                bomb_timer = time.time()
                break
    elif bomb is not None and time.time() - bomb_timer > bomb_duration:
        w.addch(bomb[0], bomb[1], ' ')
        bomb = None

    if snake[0] == pear:
        score += pear_score
        score_text = "Score: {}".format(score)
        w.addstr(0, sw // 2 - len(score_text) // 2, score_text)
        pear = None

    if snake[0] == bomb:
        game_over(score)

    if snake[0] == food:
        score += 1
        score_text = "Score: {}".format(score)
        w.addstr(0, sw // 2 - len(score_text) // 2, score_text)

        if apple_counter % 2 == 0:
            delay *= 0.5
    #
        while True:
            new_food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
            
            collision = False
            for segment in snake:
                if new_food == segment:
                    collision = True
                    break

            if collision:
                continue
            
            if new_food not in snake and new_food != pear and new_food != bomb:
                food = new_food
                break

        # new_food = None
        # while new_food is None:
        #     potential_food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
        #
        #     collision = False
        #     for segment in snake:
        #         if potential_food == segment:
        #             collision = True
        #             break
        #
        #     if collision or potential_food == pear or potential_food == bomb:
        #         continue
        #
        # new_food = potential_food
        # food = new_food
        #
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    if pear is not None:
        w.addch(pear[0], pear[1], '🍐')
    if bomb is not None:
        w.addch(bomb[0], bomb[1], '💣')

    w.addch(food[0], food[1], '🍏')
    w.addch(snake[0][0], snake[0][1], "O")
    time.sleep(delay)
game_over(score)

curses.endwin()



