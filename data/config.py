screen_x = 500
screen_y = 600
fps = 60

title_ratio = 375//96
title_w = screen_x*2//3
title_h = title_w//title_ratio
title_x = screen_x//2
title_y = 150

bird_menu_w = 100
bird_menu_h = 100
bird_menu_x = screen_x//2
bird_menu_y = screen_y//2 - 5

space_menu_x = screen_x//2
space_menu_y = screen_y*4//5 - 20

space_button_ratio = 455//208
space_button_w = screen_x//2
space_button_h = screen_y//2
space_button_x = 10
space_button_y = 10

ground_speed = 1
ground_x = screen_x + 20
ground_y = 80
ground_top_y = 100 - ground_y

bird_x = screen_x//3
bird_y = screen_y//2
bird_scale_x = 55
bird_scale_y = 55
bird_danger = screen_y*(2.6//5)
bird_time_rotate = 380
bird_rotate = 70

gravity_increase = 0.7 #gravity increase per frame
gravity_jump = 9 #pixel of bird fly up

tree_weight = 60
tree_height = screen_y*3//4
tree_start_x = screen_x
tree_min_y = screen_y*1//9 #min tree up lengths
tree_max_y = (screen_y-ground_y-ground_top_y)*6//10 #max tree up lengths
tree_speed = 3.5 #tree movement speed
tree_time = 1500 #time to next tree
tree_distance = 150 #distance from tree up to tree down

menu_font_size = 28
score_font_size = 40
scoreboard_font_size = 40
game_over_font_size = 40
play_again_font_size = 22

score_color = '#EB0A0A'
scoreboard_ratio = 534//467
scoreboard_weight = screen_x*2//3
scoreboard_height = scoreboard_weight//scoreboard_ratio
scoreboard_color = '#B75317'

medal_x = 55
medal_y = 55

play_again_ratio = 215//82
play_again_x = screen_x*4//5
play_again_y = ground_y - 35
play_again_color = '#000000'

game_over_ratio = 353//185
game_over_x = screen_x*4//7
game_over_y = 170
game_over_color = '#04570E'