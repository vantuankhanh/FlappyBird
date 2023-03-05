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
tree_distance = 150
tree_min_y = screen_y*1//5
tree_max_y = (screen_y-ground_y-ground_top_y)*3.8//7
tree_speed = 3.5
tree_time = 1500

score_font_size = 40
score_color = 'orange'