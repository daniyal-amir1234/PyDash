import time
import pygame

pygame.init()

vsync = 0
window = pygame.display.set_mode((900, 550), flags=pygame.SCALED, vsync=vsync) # this IS NOT a 16:9 ratio
pygame.display.set_caption("PyDash Wave Level Prototype")

# x and y coordinates of the player
x = 108
y = 0

# t = trail; these are ADDED to x and y values
xt = 0
yt = 0

width = 20 # width of the wave's hitbox
length = 20 # length of the wave's hitbox

prog = 0 # progress bar horizontal length
attempt = 0
percentage = -1 # fixes frame bug that occurs at the beginning where it does not start at 0

# vel = speed of up/down movement of wave
# vel2 = speed of obstacles moving left
# vel == vel2 must be true at all times.
vel = 21.213
vel2 = 21.213

# width/height of cube = 50
# width/height of wave = 20

# a = x-cordinate of obstacles
a = 900
b = 530
c = 900

d = 1
e = 1
z = 0

obw = 20 #obstacle width
obh = 400 #obstacle height

diff = 0
# points of polygons
# points should go like: (x=increments of 50) and (y=alternates between 50 and 0)

points2 = [(0, 0), (50, 50), (100, 0), (150, 50), (200, 0), (250, 50), (300, 0), (350, 50), (a, 0), (a, 50), (a, 0)]

# print(points[0])

# class ed(pygame.sprite.Sprite):
# ed = pygame.draw.rect(window, (255, 0, 0), (x, y, width, length))

# class de(pygame.sprite.Sprite):
# de = pygame.draw.rect(window, (255, 0, 0), (a + 300, 250, 50, 50))

clock = pygame.time.Clock()
FPS_CLOCK = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("game_music_trimmed.mp3")
pygame.mixer.music.set_volume(0.2)

waveup = False

# dimensions of original image:
wavew = 102
waveh = 82

wavew = wavew / 2.5
waveh = waveh / 2.5

mwavew = 68
mwaveh = 55

waveimg = pygame.image.load("normal_wave.png")
waveimg = pygame.transform.scale(waveimg, (wavew, waveh))
waveimg = pygame.transform.rotate(waveimg, -45)
waverect = waveimg.get_rect()

up_mini_wave_img = pygame.image.load("up_mini_wave.png")
up_mini_wave_img = pygame.transform.scale(up_mini_wave_img, (102 * 0.3, 82 * 0.3))
up_mini_wave_img = pygame.transform.rotate(up_mini_wave_img, -67.5)
up_mini_wave_rect = up_mini_wave_img.get_rect()

down_mini_wave_img = pygame.image.load("down_mini_wave.png")
down_mini_wave_img = pygame.transform.scale(down_mini_wave_img, (102 * 0.3, 82 * 0.3))
down_mini_wave_img = pygame.transform.rotate(down_mini_wave_img, 67.5)
down_mini_wave_rect = down_mini_wave_img.get_rect()

minicheck = False

mini = False

tcheck = False

sleepcheck = False

noclip = True

a2 = 0

miniclick = False

class trailblock:
    def __init__(self, x_pos_trailblock1, y_pos_trailblock1):
        self.x_pos_trailblock1 = x
        self.y_pos_trailblock1 = y

    def drawtrailblock(self, x_pos_trailblock1, y):
        self.x_pos_trailblock1 = self.x_pos_trailblock1 - 3.5
        if waveup:
            pygame.draw.rect(window, (255, 255, 255), (self.x_pos_trailblock1+8, self.y_pos_trailblock1+8, 4, 16))
            pygame.draw.rect(window, (255, 255, 255), (self.x_pos_trailblock1, self.y_pos_trailblock1+16, 4, 16))

        if not waveup:
            pygame.draw.rect(window, (255, 255, 255), (self.x_pos_trailblock1, self.y_pos_trailblock1-16, 4, 16))
            pygame.draw.rect(window, (255, 255, 255), (self.x_pos_trailblock1+8, self.y_pos_trailblock1-8, 4, 16))



y_pos_trailblock2 = 0

trailblockslist = []
trailblocksy_poslist = []

run = True
while run:
    # speed of player going up/down
    y += vel
    # points += vel
    # points = [(a, 0), (a, 50), (a, 0), (a, 50), (a, 0), (a, 50), (a, 0), (a + 200, 50), (a, 0), (a, 50), (a, 0)]
    # speed of obstacles (all supposed to be the same since game is at one speed)
    a -= vel2
    y_pos_trailblock2 -= vel2
    # a2 -= vel
    # top and bottom barriers
    if y > 550:
        y -= vel
    if y < 40:
        y += vel

    pygame.time.delay(0) # what's the point of this line
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_n]:
        noclip = True

    if keys[pygame.K_m]:
        noclip = False

    # while keys[pygame.K_ESCAPE] and not sleepcheck:
    # time.sleep(0.1)
    # if keys[pygame.K_q]:
    # sleepcheck = True
    # time.unsleep()

    window.fill((0, 0, 0))
    #b2 = 0  # b = y
    #for row in game_map:
        #a2 = 0  # a = x
        #for tile in row:
            #if tile == '1':
                # window.blit(rblock, (a2 * 50, b2 * 50))
                #pass
            #a2 += 1
        #b2 += 1

    # a2 -= vel

    # file = 'game_music_trimmed.mp3'
    # pygame.mixer.init()
    # pygame.mixer.music.load("game_music_trimmed.mp3")
    # pygame.mixer.music.set_volume(0.7)
    # pygame.mixer.music.play()


    if keys[pygame.K_UP]:
        click_indicator = pygame.draw.rect(window, (0, 255, 0), (2, 25, width - 5, length - 5))
        #trail = pygame.draw.rect(window, (0, 255, 255), (x - 5, y - 37, width - 5, length - 5)) #constant one block that stays there
        y -= vel * 2

    if keys[pygame.K_a]:
        obw = obw + 1
    if keys[pygame.K_s]:
        obw = obw - 1

    if keys[pygame.K_q]:
        diff = diff + 1
    if keys[pygame.K_w]:
        diff = diff - 1

    #if not keys[pygame.K_UP]:
        #trail = pygame.draw.rect(window, (0, 255, 255), (x - 5, y - 5, width - 5, length - 5)) #constant one block that stays there

        #trail1 = pygame.draw.rect(window, (0, 255, 255), (x - 15 + xt, y - 15 + yt, width - 5, length - 5))
        #trail2 = pygame.draw.rect(window, (0, 255, 255), (x - 30 + xt, y - 30 + yt, width - 5, length - 5))
        #trail3 = pygame.draw.rect(window, (0, 255, 255), (x - 45 + xt, y - 45 + yt, width - 5, length - 5))
        #trail4 = pygame.draw.rect(window, (0, 255, 255), (x - 60 + xt, y - 60 + yt, width - 5, length - 5))
        #trail5 = pygame.draw.rect(window, (0, 255, 255), (x - 75 + xt, y - 75 + yt, width - 5, length - 5))
        #trail6 = pygame.draw.rect(window, (0, 255, 255), (x - 90 + xt, y - 90 + yt, width - 5, length - 5))
        #trail7 = pygame.draw.rect(window, (0, 255, 255), (x - 105 + xt, y - 105 + yt, width - 5, length - 5))
        #trail8 = pygame.draw.rect(window, (0, 255, 255), (x - 120 + xt, y - 120 + yt, width - 5, length - 5))

        #a -= vel2
        #xt -= vel2
        #xt = xt - 1
        #yt = yt - 1


    if event.type == pygame.MOUSEBUTTONDOWN:
        y -= vel * 2

    if keys[pygame.K_l]:
        y -= vel * 2

    o44 = pygame.draw.rect(window, (0, 0, 0), (a + 5600, (0), 900, 230))   #top
    o45 = pygame.draw.rect(window, (0, 0, 0), (a + 5700, 320, 1000, (obh))) #bot #l-bot to r-top diag #big pink structure; D-blocks
    

    if event.type == pygame.KEYDOWN:
        if vsync:
            vsync = 0
        else:
            vsync = 1

        if (event.key == pygame.K_UP or event.key == pygame.K_l or event.type == pygame.MOUSEBUTTONDOWN) and y > vel and not waveup:
            miniclick = True
            # print("UP pressed down.")
            waveimg = pygame.transform.rotate(waveimg, 90)
            #print("1")

            if miniclick:
                #print("11")
                miniclick = False

            waveup = True


    elif event.type == pygame.KEYUP:
        if (event.key == pygame.K_UP or event.key == pygame.K_l or event.type == pygame.MOUSEBUTTONUP) and waveup:
            minic = False
            # print("UP released.")
            waveimg = pygame.transform.rotate(waveimg, -90)
            # minic = minic + 1
            #print("3")
            if not miniclick:
               #print("11")
                miniclick = True

            waveup = False

    if mini and not minicheck:
        vel = 42.426
        minicheck = True

    if mini:  # opposite waveup/not waveup for some reason - but it works so don't reverse it, even if it seems like it's meant to go the other way around
        wavehitbox = pygame.draw.rect(window, (0, 0, 0), (x, y, width - 10, length - 10))  # DO NOT ADD/SUBTRACT ANY NUMBERS FROM THESE VALUES - there's a black hitbox there but i think i wanna leave that? lemme think. i can render, in this order: the black hitbox, the trail and then the player? - yeah i'll do that actually

        # TRAILBLOCKS
        # y is current y-value of the player
        new_object = trailblock(x, y)
        trailblockslist.append(new_object)
        trailblocksy_poslist.append(y)
        
        if len(trailblocksy_poslist) > 5: # a maximum of 5 objects allowed on screen at a time
            trailblocksy_poslist.pop(0)
        # print(trailblocksy_poslist)

            
        for i in range(len(trailblocksy_poslist)):
            for object in trailblockslist:
                object.drawtrailblock(x, trailblocksy_poslist[i]) # every 10 pixels all the obstacles have moved (variable 'a'), a new object will be drawn at the current x and y positions of the player
        
        if waveup:
            player = window.blit(down_mini_wave_img, (x - 5, y - 25))

        if not waveup:
            player = window.blit(up_mini_wave_img, (x - 5, y - 5))
        #print("454")

    if not mini:
        #PLACE 'wavehitbox =...' HERE
        # print("NOT MINI")
        if waveup:

            wavehitbox = pygame.draw.rect(window, (0, 0, 0), (x, y, width - 5, length - 5))

            # TRAILBLOCKS
            # y is current y-value of the player
            new_object = trailblock(x, y)
            trailblockslist.append(new_object)
            trailblocksy_poslist.append(y)
            
            if len(trailblocksy_poslist) > 5: # a maximum of 5 objects allowed on screen at a time
                trailblocksy_poslist.pop(0)
            # print(trailblocksy_poslist)

                
            for i in range(len(trailblocksy_poslist)):
                for object in trailblockslist:
                    object.drawtrailblock(x, trailblocksy_poslist[i]) # every 10 pixels all the obstacles have moved (variable 'a'), a new object will be drawn at the current x and y positions of the player



            player = window.blit(waveimg, (x - 11, y - 25))
        if not waveup:
            wavehitbox = pygame.draw.rect(window, (0, 0, 0), (x, y, width - 5, length - 5))


            # TRAILBLOCKS
            # y is current y-value of the player
            new_object = trailblock(x, y)
            trailblockslist.append(new_object)
            trailblocksy_poslist.append(y)
            
            if len(trailblocksy_poslist) > 5: # a maximum of 5 objects allowed on screen at a time
                trailblocksy_poslist.pop(0)
            # print(trailblocksy_poslist)

                
            for i in range(len(trailblocksy_poslist)):
                for object in trailblockslist:
                    object.drawtrailblock(x, trailblocksy_poslist[i]) # every 10 pixels all the obstacles have moved (variable 'a'), a new object will be drawn at the current x and y positions of the player


            player = window.blit(waveimg, (x - 11, y - 12))


        # -11 and -12 before


    if ((tcheck or keys[pygame.K_RIGHT]) and not noclip) or (keys[pygame.K_RIGHT] and noclip): #K_RIGHT = instakill with 0.0 seconds respawn time
        pygame.mixer.music.stop()
        print("Player died!")

        if tcheck and not noclip:
            time.sleep(0.5)
            print("Spawn time complete (0.5 secs).")
        if not keys[pygame.K_LEFT]:
            pygame.mixer.music.play()

            # reset player
            attempt = attempt + 1
            prog = 0
            percentage = -1
            vel = 21.213
            vel2 = 21.213
            minicheck = False
            mini = False

            # reset horizontal position of player
            a = c
        else:
            pass
        tcheck = False

    # o1 = pygame.draw.rect(window, (255, 0, 0), (a + 200, 100, 100, 100))
    # o2 = pygame.draw.rect(window, (255, 0, 0), (a + 500, 0, 400, 100))
    # o3 = pygame.draw.rect(window, (255, 0, 0), (a + 500, 300, 400, 500))
    # o4 = pygame.draw.rect(window, (255, 0, 0), (a + 1000, 0, 200, 100))
    # o5 = pygame.draw.rect(window, (0, 255, 0), (a + 1000, 300, 200, 500))

    #generalised obstacle = pygame.draw.rect(window, (R, G, B), (x-pos, y-pos, width, length))

    miniportal = pygame.draw.rect(window, (140, 20, 240), (a + 5100, 100, 20, 200))
    normalsizeportal2 = pygame.draw.rect(window, (0, 0, 0), (a + 6600, -100, 100, (800))) #bot #l-bot to r-top diag
    normalsizeportal = pygame.draw.rect(window, (0, 255, 0), (a + 6500, 100, 200, 20))
    points3 = [(a + 500, 550), (a + 250, 550), (a + 500, 300)]


    # DRAW EACH OBSTACLE INDIVIDUALLY
    o0 = pygame.draw.rect(window, (0, 255, 0), (a - 325, 0, 5, 550))

    o1 = pygame.draw.rect(window, (255, 0, 0), (a + 300, 275 - diff, obw, obh))
    o2 = pygame.draw.rect(window, (255, 0, 0), (a + 375, 0, obw, 175 + diff))

    o3 = pygame.draw.rect(window, (255, 0, 0), (a + 450, 260 - diff, obw, obh))
    o4 = pygame.draw.rect(window, (255, 0, 0), (a + 525, 0, obw, 190 + diff))

    o5 = pygame.draw.rect(window, (255, 0, 0), (a + 600, 260 - diff, obw, obh))
    o6 = pygame.draw.rect(window, (255, 0, 0), (a + 675, 0, obw, 190 + diff))

    o7 = pygame.draw.rect(window, (255, 0, 0), (a + 850, 360 - diff, obw, obh))
    o8 = pygame.draw.rect(window, (255, 0, 0), (a + 800, 0, obw, 250 + diff))

    o10 = pygame.draw.rect(window, (255, 0, 0), (a + 1075, 200 - diff, obw, obh))
    o11 = pygame.draw.rect(window, (255, 0, 0), (a + 1125, 0, obw, 100 + diff))

    o12 = pygame.draw.rect(window, (255, 0, 0), (a + 1300, 300 - diff, obw, obh))
    o13 = pygame.draw.rect(window, (255, 0, 0), (a + 1250, 0, obw, 200 + diff))

    o14 = pygame.draw.rect(window, (255, 0, 0), (a + 1450, 300 - diff, obw, obh))
    o15 = pygame.draw.rect(window, (255, 0, 0), (a + 1400, 0, obw, 200 + diff))

    o16 = pygame.draw.rect(window, (255, 0, 0), (a + 1550, (0), obw, 200 + diff))   #top
    o17 = pygame.draw.rect(window, (255, 0, 0), (a + 1600, 300 - diff, obw, (obh))) #bottom #left-bottom to right-top diagonal

    o18 = pygame.draw.rect(window, (255, 0, 0), (a + 1800, (0), obw, 50 + diff))   #top
    o19 = pygame.draw.rect(window, (255, 0, 0), (a + 1750, 150 - diff, obw, (obh))) #bottom #right-top to left-bottom diagonal

    o20 = pygame.draw.rect(window, (255, 0, 0), (a + 2000, (0), obw, 150 + diff))   #top
    o21 = pygame.draw.rect(window, (255, 0, 0), (a + 2050, 250 - diff, obw, (obh))) #bottom #left-bottom to right-top diagonal

    o22 = pygame.draw.rect(window, (255, 0, 0), (a + 2200, (0), obw, 150 + diff))   #top
    o23 = pygame.draw.rect(window, (255, 0, 0), (a + 2250, 250 - diff, obw, (obh))) #bottom #left-bottom to right-top diagonal

    o24 = pygame.draw.rect(window, (255, 0, 0), (a + 2550, (0), obw, 225 + diff))   #top
    o25 = pygame.draw.rect(window, (255, 0, 0), (a + 2600, 350 - diff, obw, (obh))) #bottom #left-bottom to right-top diagonal

    o26 = pygame.draw.rect(window, (255, 0, 0), (a + 2625, (0), obw, 125 + diff))   #top
    o27 = pygame.draw.rect(window, (255, 0, 0), (a + 2675, 250 - diff, obw, (obh))) #bottom #left-bottom to right-top diagonal

    o28 = pygame.draw.rect(window, (255, 0, 0), (a + 3025, (0), obw, 175 + diff))   #top
    o29 = pygame.draw.rect(window, (255, 0, 0), (a + 3175, (0), obw, 200 + diff))   #top
    o30 = pygame.draw.rect(window, (255, 0, 0), (a + 3100, 300 - diff, obw, (obh))) #bottom #left-bottom to right-top diagonal

    o31 = pygame.draw.rect(window, (255, 0, 0), (a + 3350, (0), obw, 250 + diff))   #top
    o32 = pygame.draw.rect(window, (255, 0, 0), (a + 3250, 350 - diff, obw, (obh))) #bot #l-bot to r-top diag
    o33 = pygame.draw.rect(window, (255, 0, 0), (a + 3450, 350 - diff, obw, (obh))) #bot #l-bot to r-top diag

    o34 = pygame.draw.rect(window, (255, 0, 0), (a + 3750, (0), obw, 200 + diff))   #top
    o35 = pygame.draw.rect(window, (255, 0, 0), (a + 3650, 250 - diff, obw, (obh))) #bot #l-bot to r-top diag

    o36 = pygame.draw.rect(window, (255, 0, 0), (a + 4100, (0), obw, 250 + diff))   #top
    o37 = pygame.draw.rect(window, (255, 0, 0), (a + 4000, 275 - diff, obw, (obh))) #bot #l-bot to r-top diag

    o38 = pygame.draw.rect(window, (255, 0, 0), (a + 4450, (0), obw, 250 + diff))   #top
    o39 = pygame.draw.rect(window, (255, 0, 0), (a + 4350, 275 - diff, obw, (obh))) #bot #l-bot to r-top diag

    o38 = pygame.draw.rect(window, (255, 0, 0), (a + 4800, (0), obw, 250 + diff))   #top
    o39 = pygame.draw.rect(window, (255, 0, 0), (a + 4700, 275 - diff, obw, (obh))) #bot #l-bot to r-top diag

    o38 = pygame.draw.rect(window, (255, 0, 0), (a + 5150, (0), obw, 250 + diff))   #top
    o39 = pygame.draw.rect(window, (255, 0, 0), (a + 5050, 275 - diff, obw, (obh))) #bot #l-bot to r-top diag

    o40 = pygame.draw.rect(window, (255, 0, 0), (a + 5500, (0), obw, 250 + diff))   #top
    o41 = pygame.draw.rect(window, (255, 0, 0), (a + 5400, 275 - diff, obw, (obh))) #bot #l-bot to r-top diag



    o42 = pygame.draw.rect(window, (0, 0, 255), (a + 5600, (0), 925, 200))   #top
    o43 = pygame.draw.rect(window, (0, 0, 255), (a + 5700, 350, 1000, (obh))) #bot #l-bot to r-top diag #big blue structure; D-blocks


    if wavehitbox.colliderect(o44): #D-blocks (top platform)
        #y = y + 10
        y += vel
    if wavehitbox.colliderect(o45): #D-blocks (bottom platform)
        #y = y - 10
        y -= vel

    o46 = pygame.draw.rect(window, (255, 0, 0), (a + 5800, (0), 25, 220))   #top
    o47 = pygame.draw.rect(window, (255, 0, 0), (a + 5875, 330, 25, (obh))) #bot #l-bot to r-top diag

    o48 = pygame.draw.rect(window, (255, 0, 0), (a + 5950, (0), 25, 220))   #top
    o49 = pygame.draw.rect(window, (255, 0, 0), (a + 6025, 330, 25, (obh))) #bot #l-bot to r-top diag

    o50 = pygame.draw.rect(window, (255, 0, 0), (a + 6100, (0), 25, 220))   #top
    o51 = pygame.draw.rect(window, (255, 0, 0), (a + 6175, 330, 25, (obh))) #bot #l-bot to r-top diag

    o52 = pygame.draw.rect(window, (255, 0, 0), (a + 6250, (0), 25, 220))   #top
    o53 = pygame.draw.rect(window, (255, 0, 0), (a + 6325, 330, 25, (obh))) #bot #l-bot to r-top diag

    o54 = pygame.draw.rect(window, (255, 0, 0), (a + 6400, (0), 125, 220))   #top

    o57 = pygame.draw.rect(window, (255, 0, 0), (a + 6600, 230, 25, (obh + 100))) #bot #l-bot to r-top diag

    #o9 = pygame.draw.polygon(window, (0, 255, 0), (points3))

    if wavehitbox.colliderect(o0):
        y = 0

    # DO NOT INCLUDE 42-45 INCLUSIVE
    obstacles = [
        o1, o2, o3, o4, o5, o6, o7, o8,
        o10, o11, o12, o13, o14, o15, o16, o17,
        o18, o19, o20, o21, o22, o23, o24, o25,
        o26, o27, o28, o29, o30, o31, o32, o33,
        o34, o35, o36, o37, o38, o39, o40, o41,
        o46, o47, o48, o49, o50, o51, o52, o53, o54
    ]
    if any(wavehitbox.colliderect(o) for o in obstacles):
        tcheck = True


    if wavehitbox.colliderect(miniportal):
        mini = True
    if wavehitbox.colliderect(normalsizeportal) or wavehitbox.colliderect(normalsizeportal2):
        vel = 21.213
        vel2 = 21.213
        minicheck = False
        mini = False

    # pygame.draw.polygon(window, (255,0,0), points)

    # pygame.draw.polygon(window, (255,0,0), points2)
    # if a < 1:
    # a = c

    # b = 2 #b = y
    # for row in game_map:
    # a = 0.048 #a = x
    # for tile in row:
    # if tile == '0':
    # window.blit(unmarked, (a * 45, b * 45))
    # again = button(a * 45, b * 45, '')
    # if tile == '1':
    # window.blit(grass, (a * 45, b * 45))

    # a += 1
    # b += 1

    # ATTEMPT TEXT
    font = pygame.font.Font('freesansbold.ttf', 45)
    attempt_text = font.render("Attempt " + str(attempt), True, (255, 255, 255))
    window.blit(attempt_text, (a - 100, 75))

    font = pygame.font.Font('freesansbold.ttf', 16)

    if percentage < 100:
        percentage = percentage + 0.2801 # 0.2801 pixels per frame - this rate is as close as possible
    percentage_text = font.render(str(int(percentage)) + "%", True, (255, 255, 255))
    window.blit(percentage_text, (155, 3))

    # NOCLIP TEXT
    font = pygame.font.Font('freesansbold.ttf', 14)
    if noclip:
        noclip_text = font.render("NOCLIP: ON", True, (255, 0, 0))
    else:
        noclip_text = font.render("NOCLIP: OFF", True, (255, 0, 0))
    window.blit(noclip_text, (50, 4))

    # PROGRESS BAR
    if prog < 498:
        prog = prog + 1.4
    progress_bar_fill = pygame.draw.rect(window, (255, 255, 255), (200, 5, prog, 10 ))
    progress_bar_empty = pygame.draw.rect(window, (255, 255, 255), (200, 5, 500, 10 ), 2)

    # FPS COUNTER:
    font = pygame.font.SysFont("Arial", 20)
    def update_fps():
        fps = str(int(FPS_CLOCK.get_fps()))
        fps_text = font.render(fps, 1, pygame.Color("red")) #it was 'Coral' before
        return fps_text
    window.blit(update_fps(), (3, 0))

    if not keys[pygame.K_LEFT]:
        pygame.display.flip()
        FPS_CLOCK.tick(60)

pygame.quit()