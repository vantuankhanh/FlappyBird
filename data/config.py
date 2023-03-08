screen_x = 500
screen_y = 600
fps = 60

ground_speed = 1
ground_x = screen_x + 20
ground_y = 80
ground_top_y = 100 - ground_y

bird_x = screen_x//3
bird_y = screen_y//2
bird_scale_x = 55
bird_scale_y = 55

bird_danger = int(screen_y*(2.6/5))
bird_time_rotate = 380
bird_rotate = 70

gravity_increase = 0.7
gravity_jump = 9

tree_weight = 70
tree_height = screen_y*3//4
tree_start_x = screen_x
tree_distance = 160
tree_min_y = screen_y*1//5
tree_max_y = (screen_y-ground_y-ground_top_y)*3.8//7
tree_speed = 3.5
tree_time = 1500

score_font_size = 40
scoreboard_font_size = 40
play_again_font_size = 25

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
play_again_color = '#AF1435'