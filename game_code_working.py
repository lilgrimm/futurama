#Tristan Scott and Jimmy Sejas
#vqf8xt and bfp5tq

import uvage
camera = uvage.Camera(960,540)
game_on = False
start = True
intro = False
loading = False
fry_flip = False
is_walking = False
counter = 0
#screens + graphics
start_screen = uvage.from_image(480,270,'start_screen.png')
loading_images = uvage.load_sprite_sheet('planet_express_sprite.png', 1, 2)
planet_express_load = uvage.from_image(480,270,loading_images[-1])
main_map = uvage.from_image(1010,240,'main_map.png')
main_map.scale_by(1.45)
foreground = uvage.from_image(1010,240,'foreground.png')
foreground.scale_by(1.45)
loading_frame = 0
dialogue = []
read_dialogue = False
has_advanced = False
skip = False
n = 0
#characters
amy = uvage.from_image(1980,400,'amy.png')
amy.scale_by(0.8)

#Sprite movements
walker_images = uvage.load_sprite_sheet('walk_stand.png', 1, 6)
walker = uvage.from_image(200,400,walker_images[-1])
walker.scale_by(0.5)
bender_images = uvage.load_sprite_sheet('bender_sheet.png', 1, 6)
bender = uvage.from_image(85,400,bender_images[-1])
bender.scale_by(0.5)
walker_x = 200
walking_frame = 0
facing_right = True
bender_face_r = True
fry_walk_r = True
walker_velocity = 13

#starting screen [IN WORKING CONDITION]
def game_start():
    global game_on, start, intro, loading
    if start:
        welcome = uvage.from_text(480, 150, "top text", 60, "red", bold=True)
        press_e_to_start = uvage.from_text(480, 200, "Press E to start", 30, "red", bold=True)
        camera.draw(start_screen)
        camera.draw(welcome)
        camera.draw(press_e_to_start)
        if uvage.is_pressing('e'):
            start = False
            loading = False #Make True
            intro = False #Make True to run actual game w/ intro
            game_on = True #remove

#function for reading dialogue at certain points of the story and interacting with certain characters
def read_text(dn):
    global game_on, skip, dialogue, read_dialogue, n, intro, has_advanced
    if read_dialogue:
        game_on = False
        camera.draw(main_map)
        if uvage.is_pressing('e'):
            skip = True
            if n < len(dialogue)-1:
                n += 1
            if n == len(dialogue) - 1:
                intro = False
                read_dialogue = False
                game_on = True
'''
Figure out how to read text one letter at a time across the screen to fit into the text box [for flavor, not important right now]
'''

#introduction scene to the game where prof. farnsworth is explaing what you will be doing, right after this
#it should go to a loading screen. The player should be able to skip text, sections at a time. Loading screen cannot be skipped
def introduction():
    global game_on, read_dialogue, dialogue, intro, n
    sprite = uvage.from_image(815, 200, 'talking_sprite.png')
    sprite.scale_by(0.5)
    camera.draw(sprite)
    read_dialogue = True


'''
Figure out how to get dialogue to update and the sprites to change depending on what is said + who is speaking

-draw in each dialogue box and hard code it into game, have key press change out image when it is queued 
'''

#loading screen [IN WORKING CONDITION]
def loading_screen():
    global loading_frame, counter, loading
    is_loading = True
    load = uvage.from_text(480, 180, "Loading...", 60, "white")
    loading_screen = uvage.from_color(480, 270, "black", 960, 540)
    camera.draw(loading_screen)
    camera.draw(planet_express_load)
    camera.draw(load)
    if is_loading:
        loading_frame += 0.05
        loading_frame %= 2
        planet_express_load.image = loading_images[int(loading_frame)]
        counter += 0.05
    if counter >= 4:
        loading = False

def main_game():
    global game_on
    if game_on:
        camera.draw(walker)
        camera.draw(bender)
        camera.draw(main_map)
        camera.draw(amy)



#main character walking and camera controls [IN WORKING CONDITION]
def fry_walk():
    global walking_frame, facing_right, game_on, walker_x, is_walking, fry_flip, walker_velocity, bender_face_r, fry_walk_r
    if game_on:
        camera.draw(walker)
        is_walking = False
        if uvage.is_pressing('left arrow') or uvage.is_pressing('a'):
            if facing_right:
                walker.flip()
                fry_flip = True
                facing_right = False
                bender_face_r = True
            walker.x -= walker_velocity
            walker_x = walker.x
            camera.move(-walker_velocity, 0)
            fry_walk_r = False
            is_walking = True
            if walker.x <= 490:
                camera.move(walker_velocity, 0)
            if walker.x >= 1540:
                camera.move(walker_velocity, 0)
        if uvage.is_pressing('right arrow') or uvage.is_pressing('d'):
            if not facing_right:
                walker.flip()
                fry_flip = True
                bender_face_r = False
                facing_right = True
            walker.x += walker_velocity
            walker_x = walker.x
            camera.move(walker_velocity, 0)
            fry_walk_r = True
            is_walking = True
            if walker.x <= 500:
                camera.move(-walker_velocity, 0)
            if walker.x >= 1555:
                camera.move(-walker_velocity, 0)
        if is_walking:
            walking_frame += 0.3
            if walking_frame >= 5:
                walking_frame = 0
            walker.image = walker_images[int(walking_frame)]
        else:
            walker.image = walker_images[-1]

def bender_walk():
    global walking_frame, facing_right, walker_x, fry_flip, is_walking, bender_face_r, fry_walk_r
    if game_on:
        camera.draw(bender)
        if bender_face_r and fry_flip:
            bender.flip()
            fry_flip = False
            bender_face_r = False
        if not bender_face_r and fry_flip is True:
            bender.flip()
            fry_flip = False
            bender_face_r = True
        if is_walking:
            walking_frame += 0.3
            if walking_frame >= 5:
                walking_frame = 0
            bender.image = bender_images[int(walking_frame)]
            if fry_walk_r:
                bender.x = walker.x - 115
            if not fry_walk_r:
                bender.x = walker.x + 115
        else:
            if facing_right:
                bender.x = walker_x - 115
            if not facing_right:
                bender.x = walker_x + 115
            bender.image = bender_images[-1]

'''
have bender follow after fry, flip when he does and run behind him, and only move when fry is moving
'''

#draw methods
def tick():
    camera.clear('white')
    game_start()
    if intro:
        introduction()
    if loading:
        loading_screen()
    if not intro and not loading and not start:
        main_game()
        fry_walk()
        bender_walk()
        camera.draw(foreground)
    read_text(n)
    camera.display()

uvage.timer_loop(30,tick)



