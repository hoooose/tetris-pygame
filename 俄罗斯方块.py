# import pygame as py
# from pygame.locals import *
# import sys
# import random
# import pdb
# import time

# SCREEN_SIZE = (640, 480)
# basic_size = 20
# basic_delta = 1
# real_size = basic_size- 2*basic_delta
# MAIN_WINDOW = (basic_size*10, basic_size*20)
# TIP_WINDOW = (1/4*SCREEN_SIZE[0], MAIN_WINDOW[1])

# begin_pos = (MAIN_WINDOW[0]/2, -4*basic_size)
# score_count = 0

# def row_y_switch(row=None, y=None):
#     '''切换行数和y坐标的具体数值'''
#     if not row == None:
#         y = int((20-row)*basic_size)
#         return y
#     elif not y == None:
#         # 最底层为1行,最高层为20行
#         row = int(20 - (y / basic_size ))
#         return row

# def exist_check(clear_rows, exist_dict):
#     global score_count
#     clear_rows.sort(reverse=True)

#     for row in clear_rows:
#         score_count += 1
#         exist_dict[row].clear()

#     for row in clear_rows:
#         for exist_row in exist_dict.keys():
#             if exist_row > row:
#                 exist_dict[exist_row-1] = exist_dict[exist_row][:]

# # 基础写class Block,而所谓基础方块可能不需要
# class LBlock():
#     def __init__(self, color, pos, speed):
#         self.pos = pos
#         self.dot_0 = [[self.pos[0], self.pos[1]+i*basic_size] for i in range(4)]
#         self.dot_1 = [[self.pos[0]+i*basic_size, self.pos[1]] for i in range(4)]

#         self.shape = self.dot_0
#         self.speed = speed
#         self.color = color
#         self.is_move = True
#         self.change = 0

#     def update_pos(self):
#         self.dot_0 = [[self.pos[0], self.pos[1]+i*basic_size] for i in range(4)]
#         self.dot_1 = [[self.pos[0]+i*basic_size, self.pos[1]] for i in range(4)]
#         if self.change == 0:
#             self.shape = self.dot_0
#         elif self.change == 1:
#             self.shape = self.dot_1

#     def check_status(self, dx=None, dy=None, exist_dict=None):
#         # 判断是否超出边界
#         if not dx == None:
#             if self.change == 0:
#                 if self.pos[0] + dx < 0 or self.pos[0] + dx > MAIN_WINDOW[0] - basic_size:
#                     return False
#             elif self.change == 1:
#                 if self.pos[0] + dx < 0 or self.pos[0] + dx > MAIN_WINDOW[0] - 4 * basic_size:
#                     return False
#             return True

#         # 判断是否遇上其他块    
#         if not dy == None:
#             real_y = []
#             for element_x, element_y in self.shape:
#                 row = row_y_switch(y=element_y+dy)
#                 if row == 0:
#                     row = 1

#                 if element_x in exist_dict[row]:
#                     return False
#             return True

#     def draw(self, screen):
#         for element_x, element_y in self.shape:
#             py.draw.rect(screen, self.color, (element_x-basic_delta, element_y-basic_delta, real_size, real_size))

#     def x_move(self, x_distance):
#         temp = self.pos[:]
#         dx = x_distance

#         # x轴方向没有超出边界
#         if self.check_status(dx=dx):
#             self.pos[0] += dx
#             self.update_pos()

#         # 移动后是否遇上其他块
#         if not self.check_status(dy=0, exist_dict=exist_dict):
#             self.pos = temp[:]
#             self.update_pos()

#     def y_move(self, y_time ,exist_dict):
#         dy = self.speed * y_time

#         if not self.check_status(dy=dy, exist_dict=exist_dict):
#             self.is_move = False
#             dy = 0

#         self.pos[1] += dy

#         # 判断是否碰到底框
#         if self.change == 0 and self.pos[1] + 4*basic_size >= MAIN_WINDOW[1]:
#             self.pos[1] = MAIN_WINDOW[1] - 4*basic_size 
#             self.is_move = False
#         elif self.change == 1 and self.pos[1] + basic_size >= MAIN_WINDOW[1]:
#             self.pos[1] = MAIN_WINDOW[1] - basic_size 
#             self.is_move = False

#         self.update_pos()

#     def go_change(self, exist_dict, max_change=1):
#         '''变形'''
#         temp = self.change
#         self.change += 1
#         if self.change > max_change:
#             self.change = 0
#         self.update_pos()

#         if not self.check_status(dx=0) or not self.check_status(dy=0, exist_dict=exist_dict):
#             # 如果超出边界或者碰到其他块
#             self.change = temp
#             self.update_pos()
   
# py.init()
# screen = py.display.set_mode(SCREEN_SIZE)
# my_font = py.font.SysFont('隶书', 30)

# color = {
#     'main':(255,0,56),
#     'tip':(100,100,56),
#     'my_font':(30, 20, 190),
#     'clear':(130, 120, 90),
#     }

# lose = my_font.render('失败了', True, color['my_font'])

# clock = py.time.Clock()

# move_list = []

# # 按行数存放点 初始位置-4放屏幕外
# exist_dict = {x:[] for x in range(1, int(MAIN_WINDOW[1]/basic_size+1)+4)}

# while True:
#     # 元组无法修改,用列表代替
#     # 没有可移动的方块时,新生一个
#     if not move_list:
#         block = LBlock(color['main'], [begin_pos[0], begin_pos[1]], 70)
#         move_list.append(block)

#     for event in py.event.get():
#         if event.type == QUIT:
#             py.quit()
#             sys.exit()

#         elif event.type == KEYDOWN:
#             if event.key == K_LEFT:
#                 block.x_move(-basic_size)
#             elif event.key == K_RIGHT:
#                 block.x_move(basic_size)
#             elif event.key == K_DOWN:
#                 block.speed *= 15
#             elif event.key == K_UP:
#                 # print('上')
#                 block.go_change(exist_dict)

#     screen.fill((255,255,255))
#     # 主窗口
#     py.draw.rect(screen, color['main'], (0, 0, MAIN_WINDOW[0], MAIN_WINDOW[1]), 4)
#     py.draw.rect(screen, color['tip'], (MAIN_WINDOW[0], 0, TIP_WINDOW[0], TIP_WINDOW[1]), 4)

#     # 移动
#     time_passed_seconds = clock.tick() / 1000
#     block.y_move(time_passed_seconds, exist_dict)

#     block.draw(screen)
#     for row in exist_dict.keys():
#         for exist_x in exist_dict[row]:
#             py.draw.rect(screen, color['my_font'], (exist_x-basic_delta, row_y_switch(row=row)-basic_delta, real_size, real_size))

#     # 消除
#     clear_rows = []
#     for row in range(1, int(MAIN_WINDOW[1]/basic_size)+1):
#         if len(exist_dict[row]) == MAIN_WINDOW[0]/basic_size:
#             clear_rows.append(row)

#     if clear_rows:
#         for row in clear_rows:
#             for exist_x in exist_dict[row]:
#                 py.draw.rect(screen, color['clear'], (exist_x-basic_delta, row_y_switch(row=row)-basic_delta, real_size, real_size))
#         exist_check(clear_rows, exist_dict)
#         time.sleep(0.3)

#     if not block.is_move:
#         move_list.remove(block)
#         # 拆开存放
#         for element in block.shape:
#             row = row_y_switch(y=element[1])
#             if row > 20:
#                 screen.blit(lose, (MAIN_WINDOW[0]/2, MAIN_WINDOW[1]/2 - 5))
#                 print(exist_dict)
#                 sys.exit()
#             else:
#                 exist_dict[row].append(element[0])

#     py.display.update()


















# version 2
import pygame as py
from pygame.locals import *
import sys
import random
import pdb
import time

SCREEN_SIZE = (640, 480)

# 块的大小
basic_size = 20
# 块与块之间的白线距离
basic_delta = 1
real_size = basic_size-2*basic_delta

# 主窗口和提示窗的大小
MAIN_WINDOW = (basic_size*10, basic_size*20)
TIP_WINDOW = (1/4*SCREEN_SIZE[0], MAIN_WINDOW[1])

window_off_set = (SCREEN_SIZE[0] - MAIN_WINDOW[0] - TIP_WINDOW[0]) / 2
tip_off_set = 10
tip_pos = (MAIN_WINDOW[0]+window_off_set, MAIN_WINDOW[1]/5)

begin_pos = (MAIN_WINDOW[0]/2+window_off_set, -4*basic_size)
score = 0
# 下降速度
block_speed = 1/30

color = {
    'bg':(1, 158, 193),
    'main':(230, 159, 43),
    'main_panel':(97, 134, 171),
    'tip':(230, 159, 43),
    'my_font':(30, 20, 190),
    'clear':(230, 159, 43),
    'IBlock':(185,63,181),
    'LBlock':(209,143,102),
    'NLBlock':(15,43,207),
    'ZBlock':(0, 120, 0),
    'NZBlock':(120, 120, 125),
    'TBlock':(135,181,24),
    'OBlock':(98,63,186),
    }

def row_y_switch(row=None, y=None):
    '''切换行数和y坐标的具体数值'''
    if not row == None:
        y = int((20-row)*basic_size)
        return y
    elif not y == None:
        # 最底层为1行,最高层为20行
        row = int(20 - (y / basic_size ))
        if row == 0:
            row = 1
        return row

def exist_check(clear_rows, exist_dict):
    global score
    score_count = 0
    clear_rows.sort(reverse=True)

    for row in clear_rows:
        score_count += 1
        exist_dict[row].clear()

    # 得分
    if score_count == 1:
        score += 1000
    elif score_count == 2:
        score += 2500
    elif score_count == 3:
        score += 4000
    elif score_count == 4:
        score += 6000

    for row in clear_rows:
        for exist_row in exist_dict.keys():
            if exist_row > row:
                exist_dict[exist_row-1] = exist_dict[exist_row][:]

def exist_display(exist_dict):
    '''显示已经存在的块'''
    for row in exist_dict.keys():
        for exist_x in exist_dict[row]:
            py.draw.rect(screen, color['my_font'], (exist_x+basic_delta, row_y_switch(row=row)-basic_delta, real_size, real_size))

def in_area(target_pos, target_size, mouse_pos):
    # 判断鼠标是否在范围中
    x_in, y_in = False, False
    if target_pos[0] <= mouse_pos[0] <= target_pos[0]+target_size[0]:
        x_in = True
    if target_pos[1] <= mouse_pos[1] <= target_pos[1]+target_size[1]:
        y_in = True
    return x_in and y_in

def random_block():
    block = random.sample([IBlock(), LBlock(), ZBlock(), TBlock(), OBlock(), NZBlock(), NLBlock()], 1)[0]
    return block

class Block():
    '''基础block'''
    def __init__(self , max_change, color, speed=block_speed):
        # 控制点
        self.control = [begin_pos[0], begin_pos[1]]
        # 下一个提示位置
        self.next = (tip_pos[0]+6*tip_off_set, tip_pos[1]+5*tip_off_set)
        # 形状点组
        self.dot = {}
        # 位置
        self.pos = []

        self.speed = speed
        self.color = color
        self.is_move = True
        self.max_change = max_change
        self.change = random.randint(0, self.max_change)
        
    def update_pos(self, is_next=None):
        if not is_next is None:
            # 直接显示不变形的
            self.pos = [[self.next[0]+x*basic_size, self.next[1]+y*basic_size] for x, y in self.dot[0]]
        else:
            self.pos = [[self.control[0]+x*basic_size, self.control[1]+y*basic_size] for x, y in self.dot[self.change]]

    def check_status(self, dx=None, dy=None, exist_dict=None):
        # 判断是否超出边界
        if not dx == None:
            x_list = [element[0] for element in self.pos]
            if min(x_list) + dx < window_off_set or max(x_list) + dx > MAIN_WINDOW[0] + window_off_set - basic_size:
                return False
            return True

        # 判断是否遇上其他块    
        if not dy == None:
            for x, y in self.pos:
                row = row_y_switch(y=y+dy)
                if row == 0:
                    row = 1
                if x in exist_dict[row]:
                    return False
            return True

    def draw(self, screen):
            for x, y in self.pos:
                py.draw.rect(screen, self.color, (x+basic_delta, y-basic_delta, real_size, real_size))

    def x_move(self, x_distance):
        x_temp = self.control[:]
        dx = x_distance

        # x轴方向没有超出边界
        if self.check_status(dx=dx):
            self.control[0] += dx
            self.update_pos()

        # 移动后是否遇上其他块
        if not self.check_status(dy=0, exist_dict=exist_dict):
            self.control = x_temp[:]
            self.update_pos()

    def y_move(self, exist_dict):
        # dy = self.speed * y_time
        dy = basic_size*self.speed
        # 判断是否碰到其他块
        if not self.check_status(dy=dy, exist_dict=exist_dict):
            self.is_move = False
            dy = 0
        self.control[1] += dy
        self.update_pos()

        # 判断是否碰到底框
        y_list = [element[1] for element in self.pos]
        y_delta = max(y_list) + basic_size - MAIN_WINDOW[1]

        if y_delta >= 0:
            self.is_move = False
            self.control[1] -= y_delta

        self.update_pos()

    def go_change(self, exist_dict):
        '''变形'''
        temp = self.change

        self.change += 1
        if self.change > self.max_change:
            self.change = 0
        self.update_pos()

        if not self.check_status(dx=0) or not self.check_status(dy=0, exist_dict=exist_dict):
            # 如果超出边界或者碰到其他块
            self.change = temp
            self.update_pos()

class IBlock(Block):
    def __init__(self):
        super().__init__(max_change=1,color=color['IBlock'])
        self.dot={  0:[(0, 0),(1, 0),(2, 0),(-1, 0)],
                    1:[(0, 0),(0, 1),(0, -1),(0, -2)],
                    }
        self.update_pos(is_next=1)

class LBlock(Block):
    def __init__(self):
        super().__init__(max_change=3,color=color['LBlock'])
        self.dot={  0:[(0, 0),(0, 1),(0, -1),(-1, 1)],
                    1:[(0, 0),(-1, 0),(1, 0),(1, 1)],
                    2:[(0, 0),(0, 1),(0, -1),(1, -1)],
                    3:[(0, 0),(1, 0),(-1, 0),(-1, -1)],
                    }
        self.update_pos(is_next=1)

class ZBlock(Block):
    def __init__(self):
        super().__init__(max_change=1,color=color['ZBlock'])
        self.dot={  0:[(0, 0),(0, 1),(-1, 0),(-1, -1)],
                    1:[(0, 0),(1, 0),(0, 1),(-1, 1)],
                    }
        self.update_pos(is_next=1)

class TBlock(Block):
    def __init__(self):
        super().__init__(max_change=3,color=color['TBlock'])
        self.dot={  0:[(0, 0),(1, 0),(0, 1),(-1, 0)],
                    1:[(0, 0),(1, 0),(0, 1),(0, -1)],
                    2:[(0, 0),(1, 0),(0, -1),(-1, 0)],
                    3:[(0, 0),(0, -1),(0, 1),(-1, 0)],
                    }
        self.update_pos(is_next=1)

class OBlock(Block):
    def __init__(self):
        super().__init__(max_change=0,color=color['OBlock'])
        self.dot={  0:[(0, 0),(1, 0),(1, 1),(0, 1)],
                    }
        self.update_pos(is_next=1)

class NZBlock(Block):
    def __init__(self):
        super().__init__(max_change=1,color=color['NZBlock'])
        self.dot={  0:[(0, 0),(0, 1),(1, 0),(1, -1)],
                    1:[(0, 0),(-1, 0),(0, 1),(1, 1)],
                    }
        self.update_pos(is_next=1)

class NLBlock(Block):
    def __init__(self):
        super().__init__(max_change=3,color=color['NLBlock'])
        self.dot={  0:[(0, 0),(0, 1),(0, -1),(1, 1)],
                    1:[(0, 0),(-1, 0),(1, 0),(1, -1)],
                    2:[(0, 0),(0, 1),(0, -1),(-1, -1)],
                    3:[(0, 0),(1, 0),(-1, 0),(-1, 1)],
                    }
        self.update_pos(is_next=1)

py.init()
screen = py.display.set_mode(SCREEN_SIZE)
my_font = py.font.SysFont('隶书', 30)

lose_surface = my_font.render('失败了', True, color['my_font'])
replay_surface = my_font.render('重玩', True, color['my_font'])
score_surface = my_font.render('得分', True, color['my_font'])
next_surface = my_font.render('下一个', True, color['my_font'])
pause_surface = my_font.render('暂停', True, color['my_font'])
replay_size = replay_surface.get_size()
pause_size = pause_surface.get_size()

clock = py.time.Clock()
game_run = True
game_pause = False
fps = 120

move_list = []
# 按行数存放点 初始位置-4放屏幕外,然后random.change会超出部分
exist_dict = {x:[] for x in range(1, int(MAIN_WINDOW[1]/basic_size+1)+10)}

next_block = random_block()
x_distance = 0

while True: 
    clock.tick(fps)
    # 元组无法修改,用列表代替
    # 没有可移动的方块时,新生一个
    if not move_list:
        move_block = next_block
        move_block.update_pos()
        move_list.append(move_block)
        next_block = random_block()

    # 设置允许的事件
    # py.event.set_allowed([QUIT, KEYDOWN,KEYUP, MOUSEBUTTONDOWN])
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_a:
                move_block.x_move(-basic_size)
            elif event.key == K_d:
                move_block.x_move(basic_size)
            elif event.key == K_s:
                move_block.speed *= 15
            elif event.key == K_w:
                move_block.go_change(exist_dict)

        elif event.type == KEYUP:
            # 放开则速度恢复
            move_block.speed = block_speed
            x_distance = 0

        elif event.type == MOUSEBUTTONDOWN:
            # 暂停
            if game_run and in_area((tip_pos[0]+3*tip_off_set, tip_pos[1]+20*tip_off_set), pause_size, event.pos):
                game_pause = not game_pause
                time_passed_seconds = clock.tick() / 1000

            # 重玩
            if not game_run and in_area((MAIN_WINDOW[0], MAIN_WINDOW[1]/2+40), pause_size, event.pos):
                game_run = True
                exist_dict = {x:[] for x in range(1, int(MAIN_WINDOW[1]/basic_size+1)+10)}
                move_list.clear()
                score = 0

                move_block = random_block()
                move_block.update_pos()
                move_list.append(move_block)
                next_block = random_block()

    screen.fill(color['bg'])
    # 主窗口
    py.draw.rect(screen, color['main_panel'], (window_off_set, 0, MAIN_WINDOW[0], MAIN_WINDOW[1]))
    py.draw.rect(screen, color['main'], (window_off_set, 0, MAIN_WINDOW[0], MAIN_WINDOW[1]), 1)

    # 提示窗口--绘制窗口
    py.draw.rect(screen, color['tip'], (MAIN_WINDOW[0]+window_off_set, 0, TIP_WINDOW[0], TIP_WINDOW[1]), 1)
    screen.blit(next_surface, (tip_pos[0]+3*tip_off_set, tip_pos[1]))
    # 绘制下一个提示
    next_block.draw(screen)
    # 绘制分数
    screen.blit(score_surface, (tip_pos[0]+3*tip_off_set, tip_pos[1]+10*tip_off_set))
    score_image = my_font.render(str(score), True, color['my_font'])
    screen.blit(score_image, (tip_pos[0]+3*tip_off_set, tip_pos[1]+15*tip_off_set))
    # 暂停键
    screen.blit(pause_surface, (tip_pos[0]+3*tip_off_set, tip_pos[1]+20*tip_off_set))

    if not game_run:
        exist_display(exist_dict)
        py.draw.rect(screen, color['clear'], (MAIN_WINDOW[0], MAIN_WINDOW[1]/2, 100, 80))
        screen.blit(lose_surface, (MAIN_WINDOW[0], MAIN_WINDOW[1]/2))

        screen.blit(replay_surface, (MAIN_WINDOW[0], MAIN_WINDOW[1]/2+40))

    elif game_pause:
        exist_display(exist_dict)
        move_block.draw(screen)

    elif not game_pause and game_run:
        # 移动,用刷新率控制移动速度
        # time_passed_seconds = clock.tick() / 1000
        move_block.y_move(exist_dict)
        move_block.draw(screen)
        exist_display(exist_dict)
        
        # 消除
        clear_rows = []
        for row in range(1, int(MAIN_WINDOW[1]/basic_size)+1):
            if len(exist_dict[row]) == MAIN_WINDOW[0]/basic_size:
                clear_rows.append(row)

        if clear_rows:
            for row in clear_rows:
                for exist_x in exist_dict[row]:
                    py.draw.rect(screen, color['clear'], (exist_x-basic_delta, row_y_switch(row=row)-basic_delta, real_size, real_size))
            exist_check(clear_rows, exist_dict)
            time.sleep(0.3)

        if not move_block.is_move:
            move_list.remove(move_block)
            # 拆开存放
            for element in move_block.pos:
                row = row_y_switch(y=element[1])
                if row > 20:
                    game_run = False

                else:
                    exist_dict[row].append(element[0])

    py.display.update()


