#Tristan Scott and Jimmy Sejas
#vqf8xt and bfp5tq

import uvage
import time
camera = uvage.Camera(960,540)
game_on = False
start = True
intro = False
loading = False
#screens + graphics
start_screen = uvage.from_image(480,270,'start_screen.png')
loading_images = uvage.load_sprite_sheet('planet_express_sprite.png', 1, 2)
planet_express_load = uvage.from_image(480,270,loading_images[-1])
loading_frame = 0
dialogue = []
read_dialogue = False
skip = False
n = 0

#Sprite movements
walker_images = uvage.load_sprite_sheet('walk_stand.png', 1, 6)
walker = uvage.from_image(480,270,walker_images[-1])
bender_images = uvage.load_sprite_sheet('bender_sheet.png', 1, 6)
bender = uvage.from_image(480,270,bender_images[-1])
walker_x = 480
walker_y = 270
walking_frame = 0
facing_right = True
walker_velocity = 10

#starting screen [IN WORKING CONDITION]
def game_start():
    global game_on, start, intro
    if start:
        welcome = uvage.from_text(480, 150, "top text", 60, "red", bold=True)
        press_e_to_start = uvage.from_text(480, 200, "Press E to start", 30, "red", bold=True)
        camera.draw(start_screen)
        camera.draw(welcome)
        camera.draw(press_e_to_start)
        if uvage.is_pressing('e'):
            start = False
            intro = True

#function for reading dialogue at certain points of the story and interacting with certain characters
def read_text(dn):
    global game_on, skip, dialogue, read_dialogue, n, intro
    if read_dialogue:
        game_on = False
        text_box = uvage.from_color(480, 420, "light blue", 860, 200)
        camera.draw(text_box)
        text = uvage.from_text(230, 360, dialogue[n], 60, "black")
        #this text variable does something bad, when you have text that is long, it will start floating out of the
        #text box. Fix this at some point
        camera.draw(text)
        if uvage.is_pressing('e'):
            skip = True
            if n < len(dialogue)-1:
                n += 1
            if n == len(dialogue) - 1:
                intro = False
                read_dialogue = False
                game_on = True
'''
Figure out how to read text one letter at a time across the screen to fit into the text box
'''

#introduction scene to the game where prof. farnsworth is explaing what you will be doing, right after this
#it should go to a loading screen. The player should be able to skip text, sections at a time. Loading screen cannot be skipped
def introduction():
    global game_on, read_dialogue, dialogue, intro, n
    sprite = uvage.from_image(815, 200, 'talking_sprite.png')
    sprite.scale_by(0.5)
    camera.draw(sprite)
    camera.draw(walker)
    read_dialogue = True
    dialogue = ["part 1", "second one", "1", "2", "3", "4", "5", "6", "7", ""] #make last dialogue "" to avoid skipping on next line

'''
Figure out how to get dialogue to update and the sprites to change depending on what is said + who is speaking

-draw in each dialogue box and hard code it into game, have key press change out image when it is queued 
'''

def loading_screen():
    global loading_frame
    is_loading = True
    loading = uvage.from_text(480, 180, "Loading...", 60, "white")
    loading_screen = uvage.from_color(480, 270, "black", 960, 540)
    camera.draw(loading_screen)
    camera.draw(planet_express_load)
    camera.draw(loading)
    if is_loading:
        loading_frame += 0.05
        loading_frame %= 2
        planet_express_load.image = loading_images[int(loading_frame)]


#main character walking controls [IN WORKING CONDITION]
def fry_walk():
    global walking_frame, facing_right, game_on, walker_x
    if game_on:
        camera.draw(walker)
        is_walking = False
        if uvage.is_pressing('left arrow') or uvage.is_pressing('a'):
            if facing_right:
                walker.flip()
                facing_right = False
            walker.x -= walker_velocity
            is_walking = True
        if uvage.is_pressing('right arrow') or uvage.is_pressing('d'):
            if not facing_right:
                walker.flip()
                facing_right = True
            walker.x += walker_velocity
            is_walking = True
        if is_walking:
            walking_frame += 0.3
            if walking_frame >= 5:
                walking_frame = 0
            walker.image = walker_images[int(walking_frame)]
        else:
            walker.image = walker_images[-1]
        if walker.x > 960:
            walker.x = 0
            walker_x = walker.x
        if walker.x < 0:
            walker.x = 960
            walker_x = walker.x

    '''
    Figure out how to get camera to follow Fry ONLY when the edge of the screen has NOT been met, the camera 
    should not be able to go more than the screen boarders
    '''

def bender_walk():
    pass

def tick():
    #draw methods
    camera.clear('white')
    game_start()
    if intro:
        introduction()
    if not loading: #get rid of "not" to have normal game start up
        loading_screen()
    if not intro or loading:
        fry_walk()
    read_text(n)
    camera.display()
    #camera.move(walker.x,walker.y)

uvage.timer_loop(30,tick)



