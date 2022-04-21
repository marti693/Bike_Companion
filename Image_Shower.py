import sys

import pygame
import time
from pygame.locals import *
from threading import Thread
#import RPi.GPIO as GPIO


speed_value = 0;
max_speed = 0
anim_count = 0;
miles_value = 0;
avg_arrow_value = 0
avg_value = 0;

run = True;

def run_game():
    boot_time = time.time()
    pygame.init()
    size = [320, 240]
    speed = [2, 2]
    win = pygame.display.set_mode(size)
    white = (255, 255, 255)
    eat_timer = 0;
    drink_timer = 0;
    sleep_timer = 0;
    #Load sleep
    sleep = {}
    for i in range(3):
        filename = 'images/sleeping_' + str(i) + '.png'
        sleep[i] = pygame.image.load(filename)
    sleep_rect = sleep[0].get_rect()

    Font = pygame.font.SysFont("Trebuchet MS", 18)

    #Load eating
    eat = {}
    filename = 'images/eating.png'
    eat[0] = pygame.image.load(filename)
    eat_rect = eat[0].get_rect()

    #Load drinking
    drink = {}
    filename = 'images/drinking.png'
    drink[0] = pygame.image.load(filename)
    drink_rect = drink[0].get_rect()

    #Load cry_eating
    cry_eat = {}
    filename = 'images/cry_eating.png'
    cry_eat[0] = pygame.image.load(filename)
    cry_eat_rect = cry_eat[0].get_rect()

    #Load cry_drinking
    cry_drink = {}
    filename = 'images/cry_drinking.png'
    cry_drink[0] = pygame.image.load(filename)
    cry_drink_rect = cry_drink[0].get_rect()

    #Load stop
    stop = {}
    filename = 'images/stop.png'
    stop[0] = pygame.image.load(filename)
    stop_rect = stop[0].get_rect()

    #Load walk
    walk = {}
    for i in range(16):
        if i < 10:
            filename = 'images/walk_0' + str(i) + '.png'
        else:
            filename = 'images/walk_' + str(i) + '.png'
        walk[i] = pygame.image.load(filename)
    walk_rect = walk[0].get_rect()

    #Load run_slow
    run_slow = {}
    for i in range(10):
        filename = 'images/run_slow_0' + str(i) + '.png'
        run_slow[i] = pygame.image.load(filename)
    run_slow_rect = run_slow[0].get_rect()

    #Load run_mid
    run_mid = {}
    for i in {0, 1, 2, 3, 4, 5, 6, 7}:
        filename = 'images/run_mid_' + str(i) + '.png'
        run_mid[i] = pygame.image.load(filename)
    run_mid_rect = run_mid[0].get_rect()

    #Load run_fast
    run_fast = {}
    for i in {0, 1, 2, 3, 4, 5, 6, 7}:
        filename = 'images/run_fast_' + str(i) + '.png'
        run_fast[i] = pygame.image.load(filename)
    run_fast_rect = run_fast[0].get_rect()

    #Load fastest
    fastest = {}
    for i in range(3):
        filename = 'images/fastest_' + str(i) + '.png'
        fastest[i] = pygame.image.load(filename)
    fastest_rect = fastest[0].get_rect()

    #Load food
    food = {}
    for i in {0, 1, 2, 3, 4}:
        filename = 'images/food_' + str(i) + '.png'
        food[i] = pygame.image.load(filename)
    food_rect = food[0].get_rect()

    #Load water
    water = {}
    for i in {0, 1, 2, 3, 4, 5}:
        filename = 'images/water_' + str(i) + '.png'
        water[i] = pygame.image.load(filename)
    water_rect = water[0].get_rect()

    #Load speed
    speed = {}
    for i in range(40):
        if i < 10:
            filename = 'images/speed_0' + str(i) + '.png'
        else:
            filename = 'images/speed_' + str(i) + '.png'
        speed[i] = pygame.image.load(filename)
    speed_rect = speed[0].get_rect()

    #Load avg
    avg = {}
    for i in range(26):
        if i < 10:
            filename = 'images/avg_0' + str(i) + '.png'
        else:
            filename = 'images/avg_' + str(i) + '.png'
        avg[i] = pygame.image.load(filename)
    avg_rect = avg[0].get_rect()

    #Load avg_arrow
    avg_arrow = {}
    for i in range(2):
        filename = 'images/avg_arrow_' + str(i) + '.png'
        avg_arrow[i] = pygame.image.load(filename)
    avg_arrow_rect = avg[0].get_rect()

    # Load max
    max_s = {}
    for i in range(40):
        if i < 10:
            filename = 'images/max_0' + str(i) + '.png'
        else:
            filename = 'images/max_' + str(i) + '.png'
        max_s[i] = pygame.image.load(filename)
    max_s_rect = max_s[0].get_rect()

    # Load miles_base
    miles_base = {}
    for i in range(10):
        filename = 'images/mi_base_0' + str(i) + '.png'
        miles_base[i] = pygame.image.load(filename)
    miles_base_rect = miles_base[0].get_rect()

    # Load miles_1st place
    miles_1 = {}
    for i in range(10):
        filename = 'images/mil_2_0' + str(i) + '.png'
        miles_1[i] = pygame.image.load(filename)
    miles_1_rect = miles_1[0].get_rect()

    # Load miles_2nd place
    miles_2 = {}
    for i in range(10):
        filename = 'images/mil_3_0' + str(i) + '.png'
        miles_2[i] = pygame.image.load(filename)
    miles_2_rect = miles_2[0].get_rect()

    clock = pygame.time.Clock()

    #text = pygame.image.load('images/text.png')
    #text_rect = text.get_rect()
    global speed_value
    global max_speed
    global miles_value
    global avg_arrow_value
    current_animation = ""
    #speed_value = 20
    food_value = 0
    water_value = 0
    #disp_modes = {"avg", "dist", "max"}
    disp_modes = {}
    disp_modes[0] = "avg"
    disp_modes[1] = "dist"
    disp_modes[2] = "max"
    disp_mode = "dist"
    disp_index = 0

    def redrawGameWindow():

        global anim_count
        if current_animation == "stop":
            if anim_count >= 1:
                anim_count = 0
            win.blit(stop[anim_count], stop_rect)
            anim_count += 1
        elif current_animation == "walk":
            if anim_count >= 16:
                anim_count = 0
            win.blit(walk[anim_count], walk_rect)
            anim_count += 1
        elif current_animation == "run_slow":
            if anim_count >= 10:
                anim_count = 0
            win.blit(run_slow[anim_count], run_slow_rect)
            anim_count += 1
        elif current_animation == "run_mid":
            if anim_count >= 8:
                anim_count = 0
            win.blit(run_mid[anim_count], run_mid_rect)
            anim_count += 1
        elif current_animation == "run_fast":
            if anim_count >= 8:
                anim_count = 0
            win.blit(run_fast[anim_count], run_fast_rect)
            anim_count += 1
        elif current_animation == "fastest":
            if anim_count >= 3:
                anim_count = 0
            win.blit(fastest[anim_count], fastest_rect)
            anim_count += 1
        elif current_animation == "drinking":
            if anim_count >= 1:
                anim_count = 0
            win.blit(drink[anim_count], drink_rect)
            anim_count += 1
        elif current_animation == "eating":
            if anim_count >= 1:
                anim_count = 0
            win.blit(eat[anim_count], eat_rect)
            anim_count += 1
        elif current_animation == "cry_drinking":
            if anim_count >= 1:
                anim_count = 0
            win.blit(cry_drink[anim_count], cry_drink_rect)
            anim_count += 1
        elif current_animation == "cry_eating":
            if anim_count >= 1:
                anim_count = 0
            win.blit(cry_eat[anim_count], cry_eat_rect)
            anim_count += 1
        else: #animation = sleep

            if anim_count >= 3:
                anim_count = 0
            win.blit(sleep[anim_count], sleep_rect)
            time.sleep(.4);
            anim_count += 1



        if speed_value < 40:
            win.blit(speed[speed_value], speed_rect)

        win.blit(avg_arrow[avg_arrow_value], avg_arrow_rect)

        if disp_mode == "dist":
            if miles_value < 99:
                win.blit(miles_base[int((miles_value * 10) % 10)], miles_base_rect)
                win.blit(miles_1[int(miles_value % 10)], miles_1_rect)
                win.blit(miles_2[int((miles_value / 10) % 10)], miles_2_rect)
        elif disp_mode == "avg":
            if avg_value < 26:
                win.blit(avg[int(avg_value)], avg_rect)
        elif disp_mode == "max":
            if avg_value < 26:
                win.blit(max_s[max_speed], max_s_rect)

        win.blit(food[food_value], food_rect)
        win.blit(water[water_value], water_rect)

        # Hour
        HourFont = Font.render(str(int(((time.time() - boot_time) / 3600)) % 24).zfill(2) + ":", 1, (0,0,0))
        HourFontR = HourFont.get_rect()
        HourFontR.center = (260, 230)
        # Minute
        MinuteFont = Font.render(str(int(((time.time() - boot_time) / 60)) % 60).zfill(2) + ".", 1, (0,0,0))
        MinuteFontR = MinuteFont.get_rect()
        MinuteFontR.center = (284, 230)
        # Day
        SecondFont = Font.render(str(int((time.time() - boot_time) % 60)).zfill(2), 1, (0,0,0))
        SecondFontR = SecondFont.get_rect()
        SecondFontR.center = (305, 230)

        win.blit(MinuteFont, MinuteFontR)
        win.blit(HourFont, HourFontR)
        win.blit(SecondFont, SecondFontR)

        pygame.display.update()

    global run
    running = True
    eating = False
    drinking = False
    sleeping = False
    cry_drinking = False
    cry_eating = False
    speed_sum = 0
    speed_counter = 1
    global avg_value

    last_time = time.time()
    while run:
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                #print(event.key)
                if event.key == 27:
                    run = False
                elif event.key == 1073741903:
                    if disp_index == 2:
                        disp_index = 0
                    else:
                        disp_index += 1

        if speed_sum > sys.maxsize - 1000:
            speed_sum = 0
            speed_counter = 1
        speed_sum += speed_value
        speed_counter += 1
        avg_value = speed_sum / speed_counter
        miles_value += ((time.time() - last_time) / 3600) * speed_value
        last_time = time.time()
        if speed_value > max_speed:
            max_speed = speed_value
        if speed_value > avg_value:
            avg_arrow_value = 0
        else:
            avg_arrow_value = 1
        eat_timer += 1;
        drink_timer += 1;
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # print(event.key)
                if event.key == 27:
                    run = False
        #print(speed)

        disp_mode = disp_modes[disp_index]

        if cry_eating:
            running = False
            drinking = False
            eat_timer -= 40
            current_animation = "cry_eating"
        elif cry_drinking:
            running = False
            drink_timer -= 32
            current_animation = "cry_drinking"
        elif eating:
            running = False
            drinking = False
            eat_timer -= 40
            current_animation = "eating"
        elif drinking:
            running = False
            drink_timer -= 32
            current_animation = "drinking"
        elif sleeping:
            running = False
            current_animation = "sleeping"
        else:
            running = True;

        if running:
            if speed_value <= 1:
                current_animation = "stop"
            if 1 < speed_value < 7:
                current_animation = "walk"
            elif 7 <= speed_value < 14:
                current_animation = "run_slow"
            elif 14 <= speed_value < 21:
                current_animation = "run_mid"
            elif 21 <= speed_value < 30:
                current_animation = "run_fast"
            elif speed_value >= 30:
                current_animation = "fastest"

        if eat_timer > 4000:
            if food_value == 4:
                cry_eating = True
            else:
                eating = True
                food_value += 1
        elif drink_timer > 3200:
            if water_value == 5:
                cry_drinking = True
            else:
                drinking = True
                water_value += 1
        if speed_value <= 1:
            sleep_timer += 1
        else:
            sleep_timer = 0
        if sleep_timer > 50:
            sleeping = True
        else:
            sleeping = False

        if eat_timer <= 0:
            eating = False
            cry_eating = False
        if drink_timer <= 0:
            drinking = False
            cry_drinking = False
        if sleep_timer == 0:
            sleeping = False

        redrawGameWindow()

def get_speed():
    pygame.init()
    clock = pygame.time.Clock()
    i = 0

    global speed_value
    global run
    while run:
        #print("getting speed")
        #start = time.time()
        #GPIO.wait_for_edge(31, GPIO.RISING)
        #end = time.time()
        #t_passed = start - end
        #speed_value = 0.00043496 / (t_passed * 2.7778e-7) #miles/rotation / hours/rotation = miles / hour
        clock.tick(5)
        if i == 40:
            i = 0
        speed_vector = range(40)
        speed_value = speed_vector[i]
        #speed_value = 15
        i += 1

if __name__ == '__main__':
    Thread(target = run_game).start()
    Thread(target = get_speed).start()
