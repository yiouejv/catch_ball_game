
import pygame as pg
import sys
import random
import time
pg.init()

game_window = pg.display.set_mode((600, 500))  # 设置窗体的大小
pg.display.set_caption('接球小游戏')  # 窗体的名称

window_color = (100, 100, 255)  # 游戏窗口的颜色
ball_color = (255, 165, 0)  # 球的颜色
ball_x = random.randint(20, 580)   # 球心的x起始坐标
ball_y = 20   # 球心的y起始坐标
rect_color = (255, 0, 0)
move_x = 1
move_y = 1
score = 0  # 分数
count = 0
point = 0
t = 0.003
rect_width = 300
font = pg.font.Font(None, 50)
while True:
    game_window.fill(window_color)
    for enent in pg.event.get():  # 循环获取窗口的事件
        if enent.type == pg.QUIT:
            sys.exit()
    mouse_x, mouse_y = pg.mouse.get_pos()
    pg.draw.circle(game_window, ball_color, (ball_x, ball_y), 20)  # 画球
    pg.draw.rect(game_window, rect_color, (mouse_x, 480, rect_width, 10))  # 画板
    ball_x += move_x
    ball_y += move_y
    text = font.render(str(score), True, (255, 255, 255))
    game_window.blit(text, (500, 30))
    if ball_x == 600 - 20 or ball_x == 20:  # 窗口的宽度减去球的半径，弹到窗口的左边或者右边
        move_x = -move_x
    if ball_y + 20 == 480:  # 如果板和球在一水平上
        if mouse_x - 20 <= ball_x <= mouse_x + rect_width + 20:  # 被弹起
            move_y = -move_y
            count += 1
            point += 1
            if count == 3:
                count = 0
                point += point  # 每弹三次分数翻倍，且速度增加
                t /= 2
                rect_width -= 20  # 板的长度缩短
            score += point
        else:
            break
    if ball_y == 20:  # 如果球弹到了窗口的上边
        move_y = -move_y
    pg.display.update()
    time.sleep(t)
