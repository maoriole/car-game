import pygame, time, random
from cars import car
from things import thing
from shooting_thing import shoot


pygame.init()





display_width = 800
display_height = 600



black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

random_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('fun_run_car')

clock = pygame.time.Clock()

car_img = pygame.image.load('car.png')
dack = pygame.image.load('dack.png')

def overall_music():#open music
    global pause
    pygame.mixer.music.load('Raining Bits.ogg')
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()

def things_dodged(count): #counter for dodges
    font = pygame.font.SysFont(None, 30)
    text = font.render("Dodge: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


#massages
def text_object(text, font):
    TextSurface = font.render(text, True, red)
    return TextSurface, TextSurface.get_rect()


def message_display(text, game_type):
    LargeText = pygame.font.Font('freesansbold.ttf', 120)
    TextSurf, TextRect = text_object(text, LargeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3)
    stop_music()
    #pygame.mixer.music.stop()
    game_loop(game_type)

def crash_sound():
    pygame.mixer.music.load('Aargh7.ogg')
    pygame.mixer.music.play(1)



def crash(game_type):#when the car crashes
    stop_music()
    crash_sound()
    message_display('you Crashed', game_type)



def game_start():
    message_display('time to play')



def button(msg,x,y,w,h,ic,ac,action=None):#buttons
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:#checking if the mouse press any button
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            if msg == 'quit':
                action()
            else:
                action(msg)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_object(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def quit_game():
    pygame.quit()
    quit()



def game_intro():#game intro screen
    pygame.mixer.music.load('intro_music.wav')#music
    pygame.mixer.music.play(-1)
    intro =True
    while intro:
        events = pygame.event.get()
        for event in events:  # event per frame per sec
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(dack, (0, 0))
        LargeText = pygame.font.Font('freesansbold.ttf', 120)
        TextSurf, TextRect = text_object("fun run car", LargeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        #add difficulty
        button("normal", display_width * 0.1875, display_height * 0.85, display_width*0.125, display_height*0.085, green, white,
               game_loop)  # first and sec x,y sec rectangle boundaries
        button("shooting", display_width * 0.1875, display_height * 0.65, display_width*0.125,  display_height*0.085, green, white, game_loop)
        button("quit", display_width * 0.6875, display_height * 0.75, display_width*0.125,  display_height*0.085, blue, white, quit_game)
        #button("register", display_width * 0.4, display_height * 0.85, display_width * 0.125, display_height * 0.085,
         #      black, white, reg_log)  # first and sec x,y sec rectangle boundaries
        #calls the buttons function

        pygame.display.update()
        clock.tick(15)


def destroy_thing(things_list, shot):#when obstacles get destroy
    for thingss in things_list:
        if shot.y < thingss.thing_starty + thingss.thing_height and shot.y > thingss.thing_starty or \
                                        shot.y + shot.height < thingss.thing_starty + thingss.thing_height and shot.y + shot.height > thingss.thing_starty:  # checking his back of the car
            # print ('y crossover')
            if shot.x > thingss.thing_startx and shot.x < thingss.thing_startx + thingss.thing_width or \
                                            shot.x + shot.width > thingss.thing_startx and shot.x + shot.width < thingss.thing_startx + thingss.thing_width:

                return thingss
    return 0

def reset_things(things,list_thing, dodged):#reset obstacles
    things.change_thing_starty_reset()
    things.change_thing_startx(display_width)
    things.change_thing_speed()
    things.change_thing_width()
    new_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    things.change_thing_color(new_color)
    if dodged % 7 == 0:
        list_thing.append(thing(random.randrange(0, display_width), -600, 4, 20, 100, random_color, 1, 1.2))


#normal gamee loop
def game_loop(game_type):#main game
    overall_music()
    shoot.shooting_counter = 0

    shoot_speed = -5.0
    #__init__(self, car_width, car_height, x, y, car_img)
    list_cars = [] #cars list of objects
    list_cars.append(car(33, 55, (display_width * 0.45), (display_height * 0.8), car_img))#x,y,car_width,car_height,car_img creating car object
    x_change = 0
    y_change = 0
    #__init__(self,thing_startx, thing_starty, thing_speed, thing_width, thing_height, color, thing_increase_speed, thing_increase_width):
    list_thing = [] #obstacles list of objects
    list_thing.append(thing(random.randrange(0, display_width), -600, 4, 20, 100, random_color, 0.1, 0.5))#x_start,y_start,thing_speed, thing_width,thing height, color, speed_after dodge, width_increase_after_dodge

    shooting_list = []
    y_dack = 0

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():  # event per frame per sec, checking every event that occur in game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # moving x
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5.0
                elif event.key == pygame.K_RIGHT:
                    x_change = +5.0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0.0

            # moving y
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5.0
                elif event.key == pygame.K_DOWN:
                    y_change = +5.0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0.0

            #shooting
            if game_type == 'shooting':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        #def __init__(self, x, y, speed, width, height, color):
                        for cars in list_cars:
                            shooting_list.append(shoot(cars.x,cars.y, red))






        # event endler
        for cars in list_cars:
            cars.move_car(x_change,y_change)#moving car

        gameDisplay.blit(dack, (0, 0))  # background highway drawing


        things_dodged(dodged)

        # gameDisplay.fill(black)
        for things in list_thing: #draw obstacles
            things.draw_thing(gameDisplay)
            things.change_thing_starty_speed()#change the y with speed

        for cars in list_cars:
            cars.draw_car(gameDisplay)  # drawing the car

        #
            if cars.x > display_width -cars.car_width or cars.x < 0:#checking ends of screen
                crash(game_type)

            if cars.y > display_height - cars.car_height or cars.y < 0:#checking ends of screen
                crash(game_type)

        for things in list_thing:
            if things.thing_starty > display_height: #reseting after obstacles out of screen + counter
                reset_things(things,list_thing, dodged)
                dodged += 1

        for cars in list_cars:
            for things in list_thing:#checking crash with obstacles
                if cars.y < things.thing_starty + things.thing_height and cars.y > things.thing_starty or \
                                        cars.y + cars.car_height < things.thing_starty + things.thing_height and cars.y + cars.car_height > things.thing_starty: #checking his back of the car
                    #print ('y crossover')
                    if cars.x > things.thing_startx and cars.x < things.thing_startx + things.thing_width or \
                                                    cars.x +cars.car_width > things.thing_startx and cars.x +cars.car_width < things.thing_startx + things.thing_width:
                        #print (cars.x)
                        #print ("sx: " + str(things.thing_startx) + "tw: " + str(things.thing_startx + things.thing_width))
                        crash(game_type)

        #shooting
        if shoot.shooting_counter > 0:#checking shooting hit with obstacles and counted as dodged
            for shooting in shooting_list:
                shooting.move_shoot()
                shooting.draw_shoot(gameDisplay)
                destroy = destroy_thing(list_thing, shooting)
                if (destroy > 0):
                    shooting_list.remove(shooting)

                    list_thing.append(thing(random.randrange(0, display_width), -600, destroy.thing_speed, 20, 100, random_color, 0.1,
                                            0.5))  # x_start,y_start,thing_speed, thing_width,thing height, color, speed_after dodge, width_increase_after_dodge
                    list_thing.remove(destroy)

                    dodged += 1

        pygame.display.update()
        clock.tick(60) #fps

#main
game_intro()
