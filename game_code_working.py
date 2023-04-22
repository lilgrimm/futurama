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
walls = []
loading_frame = 0
dialogue = []
read_dialogue = False
has_advanced = False
skip = False
n = 0
#characters
amy = uvage.from_image(1980,400,'amy.png')
amy.scale_by(0.8)
#events
talk_kip = False
talk_amy = False
got_hat = False
got_boots = False
got_saddle = False
#Sprite movements
walker_images = uvage.load_sprite_sheet('walk_stand.png', 1, 6)
walker = uvage.from_image(200,400,walker_images[-1])
walker.scale_by(0.5)
bender_dist = 115
bender_images = uvage.load_sprite_sheet('bender_sheet.png', 1, 6)
bender = uvage.from_image(85,400,bender_images[-1])
bender.scale_by(0.5)
walker_x = 200
walker_velocity = 13
walking_frame = 0
facing_right = True
bender_face_r = True
fry_walk_r = True
#talking sprites
fry_talk = uvage.load_sprite_sheet('fry_test.png', 1, 3)
fry_dia = uvage.from_image(1300, 350 ,fry_talk[0])

fry_dia.scale_by(2.25)
talking_frame = 0
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
    global game_on, walker_x, walls, talk_kip, talk_amy, read_dialogue
    walls = [
        uvage.from_color(0, 270, "black", 30, 270),
        uvage.from_color(2000, 270, "black", 10, 270)
    ]
    for i in walls:
        camera.draw(i)
    if game_on:
        camera.draw(walker)
        camera.draw(bender)
        camera.draw(main_map)
        camera.draw(amy)
    #interaction points
    prompt = uvage.from_text(walker_x, 480, "Press E to Talk", 30, "black", bold=True)
    if 1200 <= walker_x <= 1350:
        camera.draw(prompt)
        if uvage.is_pressing('e'):
            talk_kip = True
    if 1800 <= walker_x <= 2000:
        camera.draw(prompt)
        if uvage.is_pressing('e'):
            talk_amy = True
    if 1500 <= walker_x <= 1560:
        prompt2 = uvage.from_text(walker_x, 480, "Press E to Interact", 30, "black", bold=True)
        camera.draw(prompt2)
    #events
    if talk_kip:
        read_dialogue = True
    if talk_amy:
        pass


def collision():
    global walls
    walker.move_to_stop_overlapping(amy)
    bender.move_to_stop_overlapping(amy)
    for wall in walls:
        walker.move_to_stop_overlapping(wall)
        bender.move_to_stop_overlapping(wall)


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
    global walking_frame, facing_right, walker_x, fry_flip, is_walking, bender_face_r, fry_walk_r, bender_dist
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
                bender.x = walker.x - bender_dist
            if not fry_walk_r:
                bender.x = walker.x + bender_dist
        else:
            if facing_right:
                bender.x = walker_x - 115
            if not facing_right:
                bender.x = walker_x + 115
            bender.image = bender_images[-1]

'''
have bender follow after fry, flip when he does and run behind him, and only move when fry is moving
'''

#function for reading dialogue at certain points of the story and interacting with certain characters
def read_text():
    global game_on, skip, dialogue, read_dialogue, intro, has_advanced, talk_kip, talking_frame, walker_x
    game_on = False
    camera.draw(main_map)
    camera.draw(walker)
    camera.draw(bender)
    camera.draw(amy)
    camera.draw(foreground)
    if talk_kip:
        camera.draw(fry_dia)
        if uvage.is_pressing('space'):
            talking_frame += 0.25
            fry_dia.image = fry_talk[int(talking_frame - 0.5)]
        if talking_frame >= 3: #however long the sprite sheet is without starting at an index of 1 (uvage indexs at 1, python at 0 and this causes issues)
            talk_kip = False
            read_dialogue = False
            game_on = True
            talking_frame = 0
            fry_dia.image = fry_talk[int(talking_frame)]

'''
Figure out how to read text one letter at a time across the screen to fit into the text box [for flavor, not important right now]
'''


#draw methods
def tick():
    camera.clear('white')
    game_start()
    if intro:
        introduction()
    if loading:
        loading_screen()
    if read_dialogue:
        read_text()
    if not intro and not loading and not start and not read_dialogue:
        main_game()
        fry_walk()
        bender_walk()
        collision()
        camera.draw(foreground)
    camera.display()

uvage.timer_loop(30,tick)



