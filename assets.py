import os
import pygame

# Automatically finds the directory for .py file
directory = os.path.dirname(__file__)
assets_directory = os.path.join(directory, "assets")

# Title - PNG Images
ironbackground_png = pygame.image.load(os.path.join(assets_directory, "ironbackground.png"))
playbutton_png = pygame.image.load(os.path.join(assets_directory, "playbutton.png"))
quitbutton_png = pygame.image.load(os.path.join(assets_directory, "quitbutton.png"))
title_png = pygame.image.load(os.path.join(assets_directory, "title.png"))

# Settings - PNG Images
backarrow_png = pygame.image.load(os.path.join(assets_directory, "backarrow.png"))
startbutton_png = pygame.image.load(os.path.join(assets_directory, "startbutton.png"))
serene_png = pygame.image.load(os.path.join(assets_directory, "serene.png"))
easy_png = pygame.image.load(os.path.join(assets_directory, "easy.png"))
moderate_png = pygame.image.load(os.path.join(assets_directory, "moderate.png"))
nightmare_png = pygame.image.load(os.path.join(assets_directory, "nightmare.png"))
serene_desc_png = pygame.image.load(os.path.join(assets_directory, "serene_desc.png"))
easy_desc_png = pygame.image.load(os.path.join(assets_directory, "easy_desc.png"))
moderate_desc_png = pygame.image.load(os.path.join(assets_directory, "moderate_desc.png"))
nightmare_desc_png = pygame.image.load(os.path.join(assets_directory, "nightmare_desc.png"))

# Main Game - PNG Images
player_png = pygame.image.load(os.path.join(assets_directory, "player.png"))
playerback_png = pygame.image.load(os.path.join(assets_directory, "ghostback.png"))
playerside_png = pygame.image.load(os.path.join(assets_directory, "ghostside.png"))
tutorialroom_png = pygame.image.load(os.path.join(assets_directory, "tutorialroom.png"))
playeranimation_png = pygame.image.load(os.path.join(assets_directory, "playeranimation.png"))
playerhorizontal_png = pygame.image.load(os.path.join(assets_directory, "playerhorizontal.png"))
playervertical_png = pygame.image.load(os.path.join(assets_directory, "playervertical.png"))

# Succubus - PNG Images
succubus_png = pygame.image.load(os.path.join(assets_directory, "succubus.png")) 
succubus_heartattackanimation_png = pygame.image.load(os.path.join(assets_directory, "succubus_heartattackanimation.png"))
succubus_heart_bullet1_png = pygame.image.load(os.path.join(assets_directory, "succubus_heart_bullet1.png"))
succubus_heart_bullet9_png = pygame.image.load(os.path.join(assets_directory, "succubus_heart_bullet9.png"))
succubus_pink_bullet_png = pygame.image.load(os.path.join(assets_directory, "succubus_pink_bullet.png"))
succubus_diamond1_png = pygame.image.load(os.path.join(assets_directory, "succubus_diamond1.png"))
succubus_diamond2_png = pygame.image.load(os.path.join(assets_directory, "succubus_diamond2.png"))
succubus_pyramid_attack1_png = pygame.image.load(os.path.join(assets_directory, "succubus_pyramid_attack1.png"))
succubus_pyramid_attack2_png = pygame.image.load(os.path.join(assets_directory, "succubus_pyramid_attack2.png"))
succubus_pyramid_attack3_png = pygame.image.load(os.path.join(assets_directory, "succubus_pyramid_attack3.png"))
succubus_pyramid_attack4_png = pygame.image.load(os.path.join(assets_directory, "succubus_pyramid_attack4.png"))
succubus_pyramid_attack5_png = pygame.image.load(os.path.join(assets_directory, "succubus_pyramid_attack5.png"))
succubus_pyramid_attack6_png = pygame.image.load(os.path.join(assets_directory, "succubus_pyramid_attack6.png"))
succubus_tail_png = pygame.image.load(os.path.join(assets_directory, "succubus_tail_short.png"))
succubus_tail_png = pygame.image.load(os.path.join(assets_directory, "succubus_tail.png"))
animatedpink_png = pygame.image.load(os.path.join(assets_directory, "animatedbigballs.png"))
healthbar_png = pygame.image.load(os.path.join(assets_directory, "healthbar.png"))
fullhealthbar_png = pygame.image.load(os.path.join(assets_directory, "fullhealthbar.png"))

# Weapons
watergun_empty_png = pygame.image.load(os.path.join(assets_directory, "watergun_empty.png"))
watergun_semi_png = pygame.image.load(os.path.join(assets_directory, "watergun_semi.png"))
watergun_full_png = pygame.image.load(os.path.join(assets_directory, "watergun_full.png"))
watergunanimation_png = pygame.image.load(os.path.join(assets_directory, "watergunanimation.png"))

# Weapon Bullets
watergun_bullet_png = pygame.image.load(os.path.join(assets_directory, "watergun_bullet.png"))
steelsoul_bullet_png = pygame.image.load(os.path.join(assets_directory, "steelsoul_bullet.png"))

# Title - Audio Files
titlescreen_audio = os.path.join(assets_directory, "titlescreen_theme.wav") 
button_audio = pygame.mixer.Sound(os.path.join(assets_directory, "button.wav")) # Load as an object

# Main Game - Audio Files
drum_audio = pygame.mixer.Sound(os.path.join(assets_directory, "drum.wav"))
succubus_audio = os.path.join(assets_directory, "succubus_theme.wav") # Only load file path
