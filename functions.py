import pygame, random
import assets
info = pygame.display.Info()
swidth = info.current_w
sheight = info.current_h

def scroll_background(screen, background, speedofscroll, width, height, bg_y1, bg_y2, image = None):
    """
    The scroll_background functions continously updates the y-coordinates of an image,
    it receives many inputs, but the important ones are bg_y1 and bg_y2, defining the
    aforementioned y-coordinates. Additionally, it wraps around the background by
    resetting bg_y1 and bg_y2 to -height (opposite direciton) if they exceed the height.
    """
    # Increases bounds by a small increment
    bg_y1 += speedofscroll
    bg_y2 += speedofscroll
    
    # Will make the bounds reset to -height for the wraparound effect
    if speedofscroll > 0:
     if bg_y1 >= background.get_height():
       bg_y1 = -background.get_height() 
     if bg_y2 >= background.get_height():
       bg_y2 = -background.get_height()
    else:
     # Reverse scrolling
     if bg_y1 <= -background.get_height():
       bg_y1 = background.get_height() 
     if bg_y2 <= -background.get_height():
       bg_y2 = background.get_height() 

    
    # Makes the animation of the scrolling
    screen.blit(background, (0, bg_y1))
    screen.blit(background, (0, bg_y2))

    # Positions the image by centering through pre-defined factors
    if image:
      image_x = (width - image.get_width()) * 0.5 
      image_y = (width - image.get_height()) * 0.01

      # Updates the final scrolling animation
      screen.blit(image, (image_x, image_y))

    return bg_y1, bg_y2

def fade(screen, width, height, fade_type):
    """
    The fade function continously fills in a black screen, slightly
    lowering the opaqueness per frame (60 cap). Additionally, it uses
    the arguments width and height to determine what area of your screen
    it is going to fill.
    """
    clock = pygame.time.Clock()

    # Sets temporary screen
    fade_surface = pygame.Surface((width, height))
    fade_surface.fill((0, 0, 0)) # Turns screen black
    if fade_type == 'out':
      # Fade out: from transparent to opaque (screen fades to black)
      for alpha in range(0, 75, 5): # Determines speed
        fade_surface.set_alpha(alpha) # Changes opacity

        # Updates pygame screen
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        clock.tick(60) # So fade doesn't happen instantly 

    elif fade_type == 'in':
      # Ensure screen is black before fading in
      black_surface = pygame.Surface((width, height))
      black_surface.fill((0, 0, 0))
      screen.blit(black_surface, (0,0))
      pygame.display.update()

      # Fade in: from opaque to transparent (screen fades from black)
      for alpha in range(75, -1, -5): # Decrease opacity from 75 to 0
        fade_surface.set_alpha(alpha) 

        # Updates pygame screen
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        clock.tick(60)

def get_image(sheet, frame, width, height, colour):
    """
    The get_image function returns a blank slate of a color that
    is used for animations.
    """
    image = pygame.Surface((width, height))
    image.blit(sheet, (0, 0), (frame * width, 0, width, height))
    image.set_colorkey(colour)
    return image

def movement(screen, boss_pos, direction):
    """
    Function used for the movement of bosses.
    direction - up/down
    x - lower bound
    y - upper bound
    """
    movement_value = 300
    # Directions: 2 = up, 1 = middle, 0 = down
    if direction == 0:
      choice = random.choice([1, 2])
      if choice == 1:
         boss_pos.y -= movement_value
         return choice
      else:
         boss_pos.y -= movement_value * 2
         return choice
      
    elif direction == 1:
      choice = random.choice([0, 2])
      if choice == 0:
        boss_pos.y += movement_value
        return choice
      else:
        boss_pos.y -= movement_value
        return choice
      
    else:
      choice = random.choice([0, 1])
      if choice == 1:
        boss_pos.y += movement_value
        return choice
      else:
        boss_pos.y += movement_value * 2
        return choice

def animation_processer(sheet, ani_steps, width, height, scalewidth, scaleheight):
  """Function that processes an animation"""
  step_counter = 0
  ani_list = []

  for animation in ani_steps:
      temp_img_list = []
      # For each animation step
      for x in range(animation):
          image = get_image(sheet, step_counter, width, height, (127, 146, 255))
          image = pygame.transform.scale(image, (swidth * (scalewidth / 1920), sheight * (scaleheight / 1080)))
          temp_img_list.append(image)
          step_counter += 1
      ani_list.append(temp_img_list)
  return ani_list

def check_player_bounds(player_rect, screen_width, screen_height):
    """
    Checks if the player's rectangle is within the screen bounds.
    If the player tries to move outside, the rectangle's position is adjusted
    to keep it at the edge.
    """
    if player_rect.left < 0: # Left Bound
        player_rect.left = 0

    if player_rect.right > screen_width: # Right Bound
        player_rect.right = screen_width

    if player_rect.top < 0: # Top Bound
        player_rect.top = 0

    if player_rect.bottom > screen_height: # Bottom Bound
        player_rect.bottom = screen_height
        
    return player_rect
