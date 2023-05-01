import uvage
camera = uvage.Camera(960,540)
game_on = False
start = True
intro = False
opening = False
outro = False
loading = False
fry_flip = False
is_walking = False
mini_start = False
end_mini = False
win = False
end = False
close_out = False
package_ready = False
counter = 0
points = 0
time = 0
#screens + graphics
start_screen = uvage.from_image(480, 270, 'start_screen.png')
loading_images = uvage.load_sprite_sheet('planet_express_sprite.png', 1, 2)
planet_express_load = uvage.from_image(0, 270, loading_images[-1])
main_map = uvage.from_image(1010, 240, 'main_map.png')
main_map.scale_by(1.45)
foreground = uvage.from_image(1010, 240, 'foreground.png')
foreground.scale_by(1.45)
intro_bg = uvage.from_image(480, 270, 'intro_bg.png')
out_talk = uvage.load_sprite_sheet('out_dia.png', 1, 3)
out_dia = uvage.from_image(480, 270, out_talk[0])
end_card = uvage.from_image(480, 270, 'end_card.png')
walls = []
loading_frame = 0
read_dialogue = False
has_advanced = False
#bender mini-game graphics
bender_mini_screen = uvage.load_sprite_sheet('mini_game.png', 1, 7)
bend_mini_game = uvage.from_image(960, 270, bender_mini_screen[1])
game_box = uvage.from_color(960, 270, "black", 1200, 540)
mini = False
#characters
amy = uvage.from_image(1980,400,'amy.png')
amy.scale_by(0.8)
leela = uvage.from_image(850,380,'leela.png')
leela.scale_by(0.8)
#events
talk_kip = False
kip_progress = 0
talk_amy = False
amy_progress = 0
talk_leela = False
leela_progress = 0
talk_betsy = False
talk_bender = False
got_hat = False
got_boots = False
got_saddle = False
got_straw = False
got_purse = False
got_package = False
finished_package_talk = uvage.load_sprite_sheet('finished_package_dia.png', 1, 3)
finished_package_dia = uvage.from_image(480, 320, finished_package_talk[0])
deliver_package_talk = uvage.load_sprite_sheet('deliver_package_dia.png', 1, 5)
deliver_package_dia = uvage.from_image(1600, 320, deliver_package_talk[0])
#Sprite movements
walker_images = uvage.load_sprite_sheet('walk_stand.png', 1, 9)
walker = uvage.from_image(200,400,walker_images[-1])
walker.scale_by(0.5)
bender_dist = 115
bender_images = uvage.load_sprite_sheet('bender_sheet.png', 1, 9)
bender = uvage.from_image(85,380,bender_images[-1])
bender.scale_by(0.5)
walker_x = 200
walker_velocity = 15
walking_frame = 0
facing_right = True
bender_face_r = True
fry_walk_r = True
#talking sprites
intro_talk = uvage.load_sprite_sheet('introduction.png', 1, 7)
intro_dia = uvage.from_image(480, 310, intro_talk[0])
opening_talk = uvage.load_sprite_sheet('opening.png', 1, 5)
opening_dia = uvage.from_image(480, 310, opening_talk[0])
#kip
kip_talk_one = uvage.load_sprite_sheet('kip_dia_one.png', 1, 10)
kip_dia_one = uvage.from_image(1300, 320, kip_talk_one[0])
kip_talk_two = uvage.load_sprite_sheet('kip_dia_two.png', 1, 2)
kip_dia_two = uvage.from_image(1300, 320, kip_talk_two[0])
kip_talk_three = uvage.load_sprite_sheet('kip_dia_three.png', 1, 3)
kip_dia_three = uvage.from_image(1300, 320, kip_talk_three[0])
kip_dia_four = uvage.from_image(1300, 320, 'kip_dia_four.png')
#leela
leela_talk_one = uvage.load_sprite_sheet('leela_dia_one.png', 1, 9)
leela_dia_one = uvage.from_image(800, 320, leela_talk_one[0])
leela_talk_two = uvage.load_sprite_sheet('leela_dia_two.png', 1, 5)
leela_dia_two = uvage.from_image(800, 320, leela_talk_two[0])
#amy
amy_talk_one = uvage.load_sprite_sheet('amy_dia_one.png', 1, 6)
amy_dia_one = uvage.from_image(1600, 320, amy_talk_one[0])
amy_talk_two = uvage.load_sprite_sheet('amy_dia_two.png', 1, 3)
amy_dia_two = uvage.from_image(1600, 320, amy_talk_two[0])
#betsy
betsy_one = uvage.from_image(1530, 320, 'betsy_one.png')
betsy_talk_two = uvage.load_sprite_sheet('betsy_two.png', 1, 3)
betsy_dia_two = uvage.from_image(1530, 320, betsy_talk_two[0])
#bender
bender_talk_one = uvage.load_sprite_sheet('bender_dia_one.png', 1, 7)
bender_dia_one = uvage.from_image(480, 320, bender_talk_one[0])
talking_frame = 0


#starting screen [IN WORKING CONDITION]
def game_start():
    global game_on, start, intro, loading
    if start:
        camera.draw(start_screen)
        if uvage.is_pressing('f'):
            start = False
            loading = True
            intro = True


def introduction():
    global game_on, read_dialogue, intro, talking_frame, loading, opening
    game_on = False
    camera.draw(intro_bg)
    camera.draw(intro_dia)
    if camera.mouseclick:
        talking_frame += 0.25
        intro_dia.image = intro_talk[int(talking_frame - 0.5)]
    if talking_frame >= 7:
        intro = False
        opening = True
        loading = True
        talking_frame = 0


#loading screen [IN WORKING CONDITION]
def loading_screen():
    global loading_frame, counter, loading, game_on, walker_x, package_ready, opening, close_out
    camera.left = -480
    game_on = False
    is_loading = True
    load = uvage.from_text(0, 180, "Loading...", 60, "white")
    loading_screen = uvage.from_color(0, 270, "black", 960, 540)
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
        game_on = True
        counter = 0
        if close_out:
            walker_shift = walker_x - 20
            camera.center = [walker_shift, 270]
            close_out = False
        if package_ready or opening or intro:
            walker_x = 200
            walker.center = [200, 400]
            bender.center = [85, 400]
            camera.center = [480, 270]

def main_game():
    global game_on, walker_x, walls, talk_kip, talk_amy, talk_leela, talk_betsy, talk_bender, read_dialogue, leela_progress, package_ready, loading, got_saddle, got_package
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
        camera.draw(leela)
    #interaction points
    prompt = uvage.from_text(walker_x, 480, "Press E to Talk", 30, "black", bold=True)
    if 800 <= walker_x <= 900 and not got_package:
        camera.draw(prompt)
        if uvage.is_pressing('e'):
            talk_leela = True
    if 1200 <= walker_x <= 1350 and not got_package:
        camera.draw(prompt)
        if uvage.is_pressing('e'):
            talk_kip = True
    if 1800 <= walker_x <= 2000:
        camera.draw(prompt)
        if uvage.is_pressing('e'):
            talk_amy = True
    if 1500 <= walker_x <= 1560 and not got_package:
        prompt2 = uvage.from_text(walker_x, 480, "Press E to Interact", 30, "black", bold=True)
        camera.draw(prompt2)
        if uvage.is_pressing('e'):
            talk_betsy = True
    #events
    if talk_kip and not got_package:
        read_dialogue = True
    if talk_amy:
        read_dialogue = True
    if talk_leela and not got_package:
        read_dialogue = True
    if talk_betsy and not got_package:
        read_dialogue = True
    if talk_bender:
        read_dialogue = True
    if leela_progress == 0 and got_straw:
        if 90 <= walker_x <= 200:
            prompt3 = uvage.from_text(walker_x, 480, "Press E to... talk to Bender?", 30, "black", bold=True)
            camera.draw(prompt3)
            if uvage.is_pressing('e'):
                talk_bender = True
    if got_hat and got_boots and got_saddle and not got_package:
        package_ready = True
        read_dialogue = True


#function for reading dialogue at certain points of the story and interacting with certain characters
def read_text():
    global game_on, read_dialogue, opening, has_advanced, talking_frame, walker_x, kip_progress, amy_progress, leela_progress, talk_leela, talk_amy, talk_kip, talk_bender
    global talk_betsy, mini, loading, got_saddle, got_straw, got_hat, got_purse, got_boots, package_ready, got_package, outro
    game_on = False
    camera.draw(main_map)
    camera.draw(walker)
    camera.draw(bender)
    camera.draw(amy)
    camera.draw(leela)
    camera.draw(foreground)
    if opening:
        camera.draw(opening_dia)
        if camera.mouseclick:
            talking_frame += 0.25
            opening_dia.image = opening_talk[int(talking_frame - 0.5)]
        if talking_frame >= 5:
            read_dialogue = False
            opening = False
            game_on = True
            talking_frame = 0
    #kip is working!
    if talk_kip:
        if kip_progress == 0:
            camera.draw(kip_dia_one)
            if camera.mouseclick:
                talking_frame += 0.25
                kip_dia_one.image = kip_talk_one[int(talking_frame - 0.5)]
            if talking_frame >= 10: #however long the sprite sheet is without starting at an index of 1 (uvage indexs at 1, python at 0 and this causes issues)
                kip_progress = 1
                mini = True
                talk_kip = False
                read_dialogue = False
                talking_frame = 0
        if kip_progress == 1:
            camera.draw(kip_dia_two)
            if camera.mouseclick:
                talking_frame += 0.25
                kip_dia_two.image = kip_talk_two[int(talking_frame - 0.5)]
                if talking_frame >= 2:
                    mini = True
                    talk_kip = False
                    read_dialogue = False
                    talking_frame = 0
                    kip_dia_two.image = kip_talk_two[int(talking_frame)]
        if mini:
            loading = True
        if kip_progress == 2:
            camera.draw(kip_dia_three)
            if camera.mouseclick:
                talking_frame += 0.25
                kip_dia_three.image = kip_talk_three[int(talking_frame - 0.5)]
                if talking_frame >= 3:
                    kip_progress = 3
                    talk_kip = False
                    read_dialogue = False
                    got_saddle = True
                    talking_frame = 0
                    game_on = True
        if kip_progress == 3:
            camera.draw(kip_dia_four)
            if camera.mouseclick:
                talking_frame += 0.25
                if talking_frame >= 1:
                    talk_kip = False
                    read_dialogue = False
                    talking_frame = 0
                    game_on = True
    #leela is working!
    if talk_leela:
        if leela_progress == 0:
            camera.draw(leela_dia_one)
            if camera.mouseclick:
                talking_frame += 0.25
                leela_dia_one.image = leela_talk_one[int(talking_frame - 0.5)]
            if talking_frame >= 9:
                amy_progress = 1
                talk_leela = False
                read_dialogue = False
                game_on = True
                talking_frame = 0
                leela_dia_one.image = leela_talk_one[int(talking_frame)]
        if leela_progress == 1:
            camera.draw(leela_dia_two)
            if camera.mouseclick:
                talking_frame += 0.25
                leela_dia_two.image = leela_talk_two[int(talking_frame - 0.5)]
            if talking_frame >= 5:
                leela_progress = 2
                got_boots = True
                talk_leela = False
                read_dialogue = False
                game_on = True
                talking_frame = 0
        if leela_progress == 2:
            read_dialogue = False
            talk_leela = False
            game_on = True


    if talk_amy:
        if amy_progress == 0:
            camera.draw(amy_dia_one)
            if camera.mouseclick:
                talking_frame += 0.25
                amy_dia_one.image = amy_talk_one[int(talking_frame - 0.5)]
            if talking_frame >= 6:
                talk_amy = False
                read_dialogue = False
                game_on = True
                talking_frame = 0
                amy_dia_one.image = amy_talk_one[int(talking_frame)]
        if amy_progress == 1:
            camera.draw(amy_dia_two)
            if camera.mouseclick:
                talking_frame += 0.25
                amy_dia_two.image = amy_talk_two[int(talking_frame - 0.5)]
            if talking_frame >= 3:
                amy_progress = 2
                got_straw = True
                talk_amy = False
                read_dialogue = False
                game_on = True
                talking_frame = 0
                amy_dia_two.image = amy_talk_two[int(talking_frame)]
        if amy_progress == 2:
            talk_amy = False
            read_dialogue = False
            game_on = True
        if amy_progress == 3:
            camera.draw(deliver_package_dia)
            if camera.mouseclick:
                talking_frame += 0.25
                deliver_package_dia.image = deliver_package_talk[int(talking_frame - 0.5)]
            if talking_frame >= 5:
                loading = True
                outro = True
                talk_amy = False
                talking_frame = 0

    if talk_betsy:
        if not got_straw:
            camera.draw(betsy_one)
            if camera.mouseclick:
                talking_frame += 0.25
            if talking_frame >= 1:
                talk_betsy = False
                read_dialogue = False
                game_on = True
                talking_frame = 0
        if got_straw:
            camera.draw(betsy_dia_two)
            if camera.mouseclick:
                talking_frame += 0.25
                betsy_dia_two.image = betsy_talk_two[int(talking_frame - 0.5)]
            if talking_frame >= 3:
                got_hat = True
                talk_betsy = False
                read_dialogue = False
                game_on = True
                talking_frame = 0
        if got_hat:
            talk_betsy = False
            read_dialogue = False
            game_on = True

    if talk_bender:
        camera.draw(bender_dia_one)
        if camera.mouseclick:
            talking_frame += 0.25
            bender_dia_one.image = bender_talk_one[int(talking_frame - 0.5)]
        if talking_frame >= 7:
            got_purse = True
            talk_bender = False
            read_dialogue = False
            game_on = True
            leela_progress = 1
            talking_frame = 0

    if package_ready:
        loading = True
        if walker_x == 200:
            loading = False
            camera.draw(finished_package_dia)
            if camera.mouseclick:
                talking_frame += 0.25
                finished_package_dia.image = finished_package_talk[int(talking_frame - 0.5)]
            if talking_frame >= 3:
                amy_progress = 3
                package_ready = False
                got_package = True
                read_dialogue = False
                game_on = True
                talking_frame = 0



def mini_game():
    global game_on, mini, mini_start, points, kip_progress, time, talk_kip, read_dialogue, win, end_mini, loading, close_out
    game_on = False
    read_dialogue = False
    camera.left = 480
    camera.draw(game_box)
    camera.draw(bend_mini_game)
    if not mini_start and not end_mini:
        time += 0.03
        if 0 <= time < 4:
            bend_mini_game.image = bender_mini_screen[1]
        if time >= 4:
            time = 0
            mini_start = True
            bend_mini_game.image = bender_mini_screen[2]
    if mini_start and not end_mini:
        time += 0.05
        print(time)
        if camera.mouseclick:
            points += 1
            if points == 35:
                bend_mini_game.image = bender_mini_screen[3]
            if points == 70:
                bend_mini_game.image = bender_mini_screen[4]
            if points == 105:
                bend_mini_game.image = bender_mini_screen[5]
            if points == 140:
                bend_mini_game.image = bender_mini_screen[6]
                win = True
                end_mini = True
        if time >= 15:
            win = False
            end_mini = True

    if end_mini and not win:
        time = 0
        bend_mini_game.image = bender_mini_screen[0]
        if uvage.is_pressing('f'):
            points = 0
            close_out = True
            loading = True
            mini = False
            mini_start = False
            end_mini = False
            game_on = True
            bend_mini_game.image = bender_mini_screen[1]
    if end_mini and win:
        time = 0
        print("Press f to exit")
        if uvage.is_pressing('f'):
            kip_progress = 2
            close_out = True
            loading = True
            mini = False
            mini_start = False
            end_mini = False
            read_dialogue = True
            talk_kip = True

def outro_scene():
    global game_on, read_dialogue, intro, talking_frame, loading, outro, end
    camera.center = [480, 270]
    game_on = False
    camera.draw(game_box)
    camera.draw(out_dia)
    if camera.mouseclick:
        talking_frame += 0.25
        out_dia.image = out_talk[int(talking_frame - 0.5)]
    if talking_frame >= 3:
        outro = False
        end = True
        talking_frame = 0

def the_end():
    camera.draw(end_card)


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
            if walker.x >= 1553:
                camera.move(-walker_velocity, 0)
        if is_walking:
            walking_frame += 0.05
            if walking_frame >= 8:
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
            if walking_frame >= 8:
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

#draw methods
def tick():
    global read_dialogue, opening, loading, intro, mini, outro, start
    camera.clear('white')
    if start:
        game_start()
    if intro:
        introduction()
    if read_dialogue:
        read_text()
    if game_on:
        if opening:
            read_dialogue = True
        main_game()
        fry_walk()
        bender_walk()
        collision()
        camera.draw(foreground)
    if mini and not loading:
        mini_game()
    if outro:
        outro_scene()
    if loading:
        loading_screen()
    if end:
        the_end()
    camera.display()

uvage.timer_loop(30,tick)



