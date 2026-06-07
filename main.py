import pygame
pygame.init() # Run before importing from assets
pygame.mixer.init()

import random
import assets
import classes
import functions

#-----Title Screen-----
# Initializing screen dimensions among other variables
info = pygame.display.Info() # 2560, 1440
swidth = info.current_w
sheight = info.current_h
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks() # Time in ms since pygame initializes
dt = 0

# Load title background music
pygame.mixer.music.load(assets.titlescreen_audio)
pygame.mixer.music.play(-1) # -1 = Loops forever

# Change images and screens according to user's screen scale through transform.scale()
assets.title_png
title_background = pygame.transform.scale(assets.ironbackground_png, (swidth, (sheight * 2))) # Also for settings menu

# Scrolling title background bounds (from 0 to the height of image) in william terms y spawn point of image
title_bg_y1 = 0
title_bg_y2 = title_background.get_height()

# 0.60 represents the scale factor of the image (its a square, so same proportions)
title = pygame.transform.scale(assets.title_png, (int(sheight * 0.60), int(sheight * 0.60)))

# Initializes screen with window caption
screen = pygame.display.set_mode((swidth, sheight))
pygame.display.set_icon(assets.title_png)
pygame.display.set_caption("Exodus_666")

# Create instances of buttons and centering
title_playbutton = classes.Button(swidth // 2 - swidth // 4, sheight // 2 + sheight // 6, screen, assets.playbutton_png, swidth * 0.0015)
title_quitbutton = classes.Button(swidth // 2 + swidth // 25, sheight // 2  + sheight // 6, screen, assets.quitbutton_png, swidth * 0.0015)
scaledhealthbar = pygame.transform.scale((assets.healthbar_png), (swidth * (800 / 1920), sheight * (56 / 1080)))
scaledfullheatlbar = pygame.transform.scale((assets.fullhealthbar_png), (swidth * (800 / 1920), sheight * (56 / 1080)))

run = True # On/Off
title_menu = True
settings_menu = False
startbutton_appear = False

#-----Settings Screen-----
# PNG Images
settings = pygame.transform.scale(assets.playbutton_png, (int(sheight * 0.60), int(sheight * 0.60)))

# Instances of buttons
backarrow_button = classes.Button(0, 0, screen, assets.backarrow_png, swidth * 0.00075)
start_button = classes.Button(swidth // 3, sheight // 50, screen, assets.startbutton_png, swidth * 0.0008)

# Instances of difficulty buttons and descriptions
serene_button = classes.Button(swidth // 20, sheight // 2 + sheight // 6, screen, assets.serene_png, swidth * 0.001)
serene_button_desc = pygame.transform.scale(assets.serene_desc_png, (swidth * (240 / 1920), sheight * (60 / 1080)))
easy_button = classes.Button(swidth // 4, sheight // 2 + sheight // 6, screen, assets.easy_png, swidth * 0.001)
easy_button_desc = pygame.transform.scale(assets.easy_desc_png, (swidth * (180 / 1920), sheight * (60 / 1080)))
moderate_button = classes.Button(swidth // 2 - swidth // 10, sheight // 2 + sheight // 6, screen, assets.moderate_png, swidth * 0.001)
moderate_button_desc = pygame.transform.scale(assets.moderate_desc_png, (swidth * (180 / 1920), sheight * (60 / 1080)))
nightmare_button = classes.Button(swidth // 2 + swidth // 6, sheight // 2 + sheight // 6, screen, assets.nightmare_png, swidth * 0.001)
nightmare_button_desc = pygame.transform.scale(assets.nightmare_desc_png, (swidth * (150 / 1920), sheight * (60 / 1080)))

# Player variables
lives = 0
iframe_duration = 2000  # 2 seconds in milliseconds
last_hit_time = -iframe_duration  # Initialize to allow immediate hit at game start

#-----Tutorial Screen-----
# Player movement and sprite
player = pygame.transform.scale(assets.player_png, (swidth * (32 / 1920), sheight * (56 / 1080)))
player_pos = player.get_rect(center = (swidth // 5, sheight // 2))  # Calculates the rectangle for player, or "hitbox"

# Rooms
tutorial_room = pygame.transform.scale(assets.tutorialroom_png, (swidth, sheight))

# Animation Sheets
ghostsheet = assets.playeranimation_png
watergunsheet = assets.watergunanimation_png
heartattacksheet = assets.succubus_heartattackanimation_png
bigpinksheet = assets.animatedpink_png
ghost_list = functions.animation_processer(ghostsheet, [4], 16, 28, 32, 56)
watergun_list = functions.animation_processer(watergunsheet, [1, 2], 39, 17, 40, 17)
heartattack_list = functions.animation_processer(heartattacksheet, [9], 32, 32, 64, 64)
bigpink_list = functions.animation_processer(bigpinksheet, [2], 35, 35, 350, 350)

# Animation Objects (list, ms delay per frame)
heartattackfinale = classes.Animation(heartattack_list, 100)
ghostfinale = classes.Animation(ghost_list, 100)
watergunfinale = classes.Animation(watergun_list, 500)
bigpinkfinale = classes.Animation(bigpink_list, 300)

# Directions in which player will look
playerstate = {
    ("up"): pygame.transform.scale((assets.playerback_png), (swidth * (32 / 1920), sheight * (56 / 1080))),
    ("down"): pygame.transform.scale(assets.player_png, (swidth * (32 / 1920), sheight * (56 / 1080))),
    ("left"): pygame.transform.flip(pygame.transform.scale(assets.playerside_png, (swidth * (32 / 1920), sheight * (56 / 1080))), True, False),
    ("right"): pygame.transform.scale((assets.playerside_png), (swidth * (32 / 1920), sheight * (56 / 1080))),
    ("upright"): pygame.transform.flip(pygame.transform.scale(assets.playervertical_png, (swidth * (32 / 1920), sheight * (56 / 1080))), True, False),
    ("upleft"): pygame.transform.scale(assets.playervertical_png, (swidth * (32 / 1920), sheight * (56 / 1080))) ,
    ("downright"): pygame.transform.scale(assets.playervertical_png, (swidth * (32 / 1920), sheight * (56 / 1080))) ,
    ("downleft"): pygame.transform.flip(pygame.transform.scale(assets.playervertical_png, (swidth * (32 / 1920), sheight * (56 / 1080))), True, False)
}

# Weapon instance
watergun_list = (
    assets.watergun_empty_png,
    assets.watergun_semi_png,
    assets.watergun_full_png
)
watergun = watergunfinale.final_product()
watergun_pos = watergun.get_rect(center = (player_pos.x + 25, player_pos.y + 25))

# Bullets and iframes
bullets = []
can_shoot = True
last_shot_time, last_dash_time = 0, 0
bullet_damage, bullet_firerate, bullet_speed = 0, 0, 0
iframes, dashiframes = False, False
dashmovement = 6000

#-----Boss Menu------
# Succubus variables
succubus_hp = 5000
succubus = pygame.transform.scale(assets.succubus_png, (swidth * (80 / 1920), sheight * (140 / 1080)))
succubus_pos = succubus.get_rect(center = (swidth - (swidth // 10), (sheight // 2)))
succubus_bullets = []
succubus_can_shoot = True
succubus_last_shot_time = 0
succubus_bullet_damage, succubus_bullet_firerate, succubus_bullet_speed = 0, 0, 0

# Initializes game
while run:
    current_time = pygame.time.get_ticks()

    # Displays buttons and checks if pressed
    if title_menu:
        # Does the scrolling animation, continuously keeps track of the y coordinates of the background that is being scrolled.
        title_bg_y1, title_bg_y2 = functions.scroll_background(screen, title_background, 4, swidth, sheight, title_bg_y1, title_bg_y2, title)

        if title_quitbutton.draw(): # Made as else if to prevent it from re-popping up once transitioning
            pygame.mixer.Sound.play(assets.button_audio)
            run = False

        if title_playbutton.draw():
            pygame.mixer.Sound.play(assets.button_audio)

            # Ensures that the scrolling transition carries over to settings menu
            settings_bg_y1, settings_bg_y2 = title_bg_y1, title_bg_y2

            pygame.display.update()
            settings_menu = True
            title_menu = False
            startbutton_appear = False

            pygame.display.update()
            pygame.time.wait(100) # Delay for buttons to not play

    elif settings_menu:
        settings_bg_y1, settings_bg_y2 = functions.scroll_background(screen, title_background, -4, swidth, sheight, settings_bg_y1, settings_bg_y2)
        # Loading in difficulty descriptions.
        screen.blit(serene_button_desc, (swidth // 12, sheight // 2 + sheight // 3.5))
        screen.blit(easy_button_desc, (swidth // 12 + sheight // 3.5, sheight // 2 + sheight // 3.5))
        screen.blit(moderate_button_desc, (swidth // 12 + (swidth // 2 - swidth // 8), sheight // 2 + sheight // 3.5))
        screen.blit(nightmare_button_desc, (swidth // 12 + (swidth // 2 + swidth // 6), sheight // 2 + sheight // 3.5))
        
        if serene_button.draw():
            pygame.mixer.Sound.play(assets.button_audio)
            lives = -1 # Indicates infinite lives
            startbutton_appear = True
            difficulty_firerate, difficulty_movement = 500, 2


        if easy_button.draw():
            pygame.mixer.Sound.play(assets.button_audio)
            lives = 3
            startbutton_appear = True
            difficulty_firerate, difficulty_movement = 4000, 20


        if moderate_button.draw():
            pygame.mixer.Sound.play(assets.button_audio)
            lives = 2
            startbutton_appear = True
            difficulty_firerate, difficulty_movement = 2000, 10


        if nightmare_button.draw():
            pygame.mixer.Sound.play(assets.button_audio)
            lives = 1
            startbutton_appear = True
            difficulty_firerate, difficulty_movement = 500, 2

        if backarrow_button.draw():
            pygame.mixer.Sound.play(assets.button_audio)
            title_bg_y1, title_bg_y2 = settings_bg_y1, settings_bg_y2

            # Switch to title screen
            pygame.display.update()
            title_menu = True
            settings_menu = False
            pygame.display.update()

        if startbutton_appear == True:
            if start_button.draw():
                # Reposition/replenish Succubus and Player
                succubus_hp  = 5000
                succubus_direction = 1
                succubus_pos = succubus.get_rect(center = (swidth - (swidth // 10), (sheight // 2)))
                player_pos = player.get_rect(center = (swidth // 5, sheight // 2))  # Calculates the rectangle for player, or "hitbox"
                enemyhealthbar = classes.Healthbar(((swidth * 0.5) - (scaledhealthbar.get_width() * 0.5)), 0, scaledhealthbar, scaledfullheatlbar, 5000)
                functions.fade(screen, swidth, sheight, "out")

                # Transition into tutorial and game
                pygame.mixer.music.stop()
                pygame.time.wait(1000)
                pygame.mixer.Sound.play(assets.drum_audio)
                functions.fade(screen, swidth, sheight, "in")
                pygame.time.wait(int(assets.drum_audio.get_length() * 1000)) # Waits the length (in ms) of the drum_audio
                pygame.mixer.music.load(assets.succubus_audio)
                pygame.mixer.music.play(-1)
                
                # Clear all bullets before spawning
                succubus_bullets.clear(), bullets.clear()
                player_has_moved = False
                settings_menu = False
                tutorial_menu = True

    elif tutorial_menu:
        ghostfinale.update_animation()
        #-----TEMPORARY------
        if backarrow_button.draw():
            pygame.mixer.Sound.play(assets.button_audio)
            pygame.mixer.music.stop()
            title_bg_y1, title_bg_y2 = settings_bg_y1, settings_bg_y2

            # Switch to title screen
            pygame.display.update()
            title_menu = True
            settings_menu = False
            pygame.display.update()
            pygame.mixer.music.load(assets.titlescreen_audio)
            pygame.mixer.music.play(-1)

        # Load in the background and player

        screen.blit(tutorial_room, (0, 0))
        enemyhealthbar.draw(screen)


        # Check to see if invisibility period is over
        if iframes and current_time - last_hit_time >= iframe_duration:
            iframes = False

        # Blinking effect during iframes
        if not iframes or (current_time // 200) % 2 == 0:
            # Places player onto a rectangle, enabled as its hitbox
            screen.blit(player, player_pos)
            screen.blit(watergun, watergun_pos)

        screen.blit(succubus, succubus_pos)

        keys = pygame.key.get_pressed()

        current_weapons = ['watergun', 'steelsoul'] # Later for inventory use
        succubus_attacks = ['heartattack', 'pinkattack', 'diamondattack'] 

        player = ghostfinale.final_product()
        watergun = watergunfinale.final_product()
        bullet_state, bullet_pos = False, (watergun_pos.x, watergun_pos.y)

        # Succubus logic
        if current_time - succubus_last_shot_time >= difficulty_firerate and player_has_moved == True:
            succubus_random = random.randint(0, 100)
            succubus_last_shot_time = current_time

            # Pick random attack
            succubus_choice = random.choice(succubus_attacks)

            if succubus_choice == 'heartattack':
                succubus_bullet = classes.Bullet(
                    screen, 
                    'heartattack',
                    heartattackfinale, 
                    (succubus_pos.centerx, succubus_pos.centery), 
                    (-1, 0), # Represents bullet direction 
                    swidth * 0.0015, 
                    player_pos,
                    assets.succubus_heart_bullet9_png,
                    animation = True
                )
                # Makes the bullet an entity
                succubus_bullets.append(succubus_bullet)
            
            elif succubus_choice == 'diamondattack':
                # Will shoot twice; once up and once down
                for bullet_direction in [-1, 1]:
                    succubus_bullet = classes.Bullet(
                        screen,
                        'diamondattack',
                        assets.succubus_diamond1_png,
                        (succubus_pos.centerx, succubus_pos.centery),
                        (0, bullet_direction),
                        swidth * 0.001,
                        player_pos,
                        assets.succubus_diamond2_png
                    )
                    succubus_bullets.append(succubus_bullet)
        
            elif succubus_choice == 'pinkattack':
                succubus_bullet = classes.Bullet(
                    screen,
                    'pinkattack',
                    bigpinkfinale,
                    (succubus_pos.centerx, succubus_pos.centery),
                    (-1, 0),
                    swidth * 0.005,
                    player_pos,
                    animation = True
                )
                succubus_bullets.append(succubus_bullet)
    
            # Difficulty movement changes by difficulty, determines how often boss moves
            if succubus_random % difficulty_movement == 0:
                succubus_direction = functions.movement(screen, succubus_pos, succubus_direction)
                

        for succubus_bullet in succubus_bullets[:]:
            if succubus_bullet.weapon == 'diamondattack' and not succubus_bullet.exploded:
                # Handle heart attack explosion
                new_mini_bullet = succubus_bullet.spawn_mini_diamond()
                if new_mini_bullet:
                    succubus_bullets.append(new_mini_bullet)

            if succubus_bullet.should_explode():
                if succubus_bullet.weapon == 'heartattack' and not succubus_bullet.exploded:
                    succubus_bullet.exploded = True
                    mini_bullets = succubus_bullet.explode()
                    succubus_bullets.extend(mini_bullets)

                    # Avoid crashing error
                    if succubus_bullet in succubus_bullets:
                        succubus_bullets.remove(succubus_bullet)

            if succubus_bullet.update(dt) and (iframes == False or dashiframes == False):
                lives -= 1
                last_hit_time = current_time  # Start the invincibility period
                iframes = 1

                if lives == 0:
                    pygame.mixer.music.stop()
                    title_bg_y1, title_bg_y2 = settings_bg_y1, settings_bg_y2

                    # Switch to title screen
                    pygame.display.update()
                    title_menu = True
                    settings_menu = False
                    pygame.display.update()
                    pygame.mixer.music.load(assets.titlescreen_audio)
                    pygame.mixer.music.play(-1)

            if succubus_bullet.alive:
                succubus_bullet.animatebullet()
                succubus_bullet.draw()
            else:
                succubus_bullets.remove(succubus_bullet)

        # Detect movement - W (Up) A (Left) S (Down) D (Right)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player_has_moved = True
            player_pos.y -= 300 * dt
            watergun_pos.y -= 300 * dt

            if keys[pygame.K_e] and (current_time - last_dash_time >= 500):
                last_dash_time = current_time
                player_pos.y -= dashmovement * dt
                watergun_pos.y -= dashmovement * dt
                dashiframes = True
 

            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player = playerstate.get("upright")
            elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player = playerstate.get("upleft")
            else:
                player = playerstate.get("up")

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player_has_moved = True
            player_pos.y += 300 * dt
            watergun_pos.y += 300 * dt
            
            if keys[pygame.K_e] and (current_time - last_dash_time >= 500):
                last_dash_time = current_time
                player_pos.y += dashmovement * dt
                watergun_pos.y += dashmovement * dt 
                dashiframes = True


            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player = playerstate.get("downright")
            elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player = playerstate.get("downleft")
            else:
                player = playerstate.get("down")

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_has_moved = True
            player_pos.x -= 300 * dt
            watergun_pos.x -= 300 * dt

            if keys[pygame.K_e] and (current_time - last_dash_time >= 500):
                last_dash_time = current_time
                player_pos.x -= dashmovement * dt
                watergun_pos.x -= dashmovement * dt 
                dashiframes = True


            if keys[pygame.K_w] or keys[pygame.K_UP]:
                pass
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                pass
            else:
                player = playerstate.get("left")

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_has_moved = True
            player_pos.x += 300 * dt
            watergun_pos.x += 300 * dt

            if keys[pygame.K_e] and (current_time - last_dash_time >= 500):
                last_dash_time = current_time
                player_pos.x += dashmovement * dt
                watergun_pos.x += dashmovement * dt 
                dashiframes = True

            if keys[pygame.K_w] or keys[pygame.K_UP]:
                pass
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                pass
            else:
                player = playerstate.get("right")

        # Handle shooting
        if (keys[pygame.K_o] or pygame.mouse.get_pressed()[0]) and can_shoot:
            player_has_moved = True
            can_shoot = False
            last_shot_time = current_time

            # Determine the direction of the bullet based on player's facing direction
            # Note: Since the gun is directionless, it will only travel to the right, you are able to change this!!
            bullet_direction = (1, 0) 

            # Create instance of bullet object
            bullet = classes.Bullet(
                screen, 
                current_weapons[0], 
                assets.watergun_bullet_png, 
                (watergun_pos.centerx, watergun_pos.centery), 
                bullet_direction, 
                swidth * 0.0001, 
                succubus_pos    
            )
            # The get_attributes() method is only for later use (once we have more than 1 weapon)
            bullet_damage, bullet_firerate, bullet_speed = bullet.get_attributes()
            bullets.append(bullet)

            # Watergun animation
            watergunfinale.update_animation()
            watergunfinale.action = 1
        else:
            watergunfinale.action = 0

        tuple = (123, False, True)
        # Cooldown check
        if not can_shoot and current_time - last_shot_time >= bullet_firerate:
            can_shoot = True

        # Update and draw bullets
        for bullet in bullets[:]:

            if bullet.update(dt):
                enemyhealthbar.current_hp -= bullet_damage
                succubus_hp -= bullet_damage
                if succubus_hp <= 0:
                    pygame.mixer.music.stop()
                    title_bg_y1, title_bg_y2 = settings_bg_y1, settings_bg_y2

                    # Switch to title screen
                    pygame.display.update()
                    title_menu = True
                    settings_menu = False
                    pygame.display.update()
                    pygame.mixer.music.load(assets.titlescreen_audio)
                    pygame.mixer.music.play(-1)
                
            if bullet.alive:
                bullet.draw()

            else:
                bullets.remove(bullet)
        
        # Check to disable offscreen movement
        player_pos = functions.check_player_bounds(player_pos, swidth, sheight)
        watergun_pos.center = (player_pos.x + 25, player_pos.y + 25) # Ensure gun follows player
        
        # If user dies, never happens for lives = -1
        if lives == 0:
            pygame.mixer.music.stop()
            title_bg_y1, title_bg_y2 = settings_bg_y1, settings_bg_y2

            # Switch to title screen
            pygame.display.update()
            title_menu = True
            settings_menu = False
            pygame.display.update()
            pygame.mixer.music.load(assets.titlescreen_audio)
            pygame.mixer.music.play(-1)

    # Checks if the user quits by closing window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # Breaks the forever loop

    pygame.display.update()

    # Limits FPS to 60 and dt is delta time in seconds since last frame, used for framerate-independent physics
    dt = clock.tick(60) / 1000

pygame.quit()