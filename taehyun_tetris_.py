#이태현_ 테트리스_ 과제제출 8.16(금)
#1. 키보드 ↑ 로 블록 바꾸기 
#2  고스트 블럭 만들기 (블럭이 내려갈 위치 보여준다)
#3. 스페이스 누를 시 블럭이 빠르게 내려가기
#4. 1000점 단위로 1 레벨업/ 레벨업시 블록 내려오는 속도 빨라진다. 
#5 가독성을 위해 블록 색상, 스코어판 변경
import sys
from math import sqrt
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN, \
    K_LEFT, K_RIGHT, K_DOWN, K_SPACE, K_UP

BLOCK_DATA = (
    (
        (0, 0, 1, \
         1, 1, 1, \
         0, 0, 0),
        (0, 1, 0, \
         0, 1, 0, \
         0, 1, 1),
        (0, 0, 0, \
         1, 1, 1, \
         1, 0, 0),
        (1, 1, 0, \
         0, 1, 0, \
         0, 1, 0),
    ), (
        (2, 0, 0, \
         2, 2, 2, \
         0, 0, 0),
        (0, 2, 2, \
         0, 2, 0, \
         0, 2, 0),
        (0, 0, 0, \
         2, 2, 2, \
         0, 0, 2),
        (0, 2, 0, \
         0, 2, 0, \
         2, 2, 0)
    ), (
        (0, 3, 0, \
         3, 3, 3, \
         0, 0, 0),
        (0, 3, 0, \
         0, 3, 3, \
         0, 3, 0),
        (0, 0, 0, \
         3, 3, 3, \
         0, 3, 0),
        (0, 3, 0, \
         3, 3, 0, \
         0, 3, 0)
    ), (
        (4, 4, 0, \
         0, 4, 4, \
         0, 0, 0),
        (0, 0, 4, \
         0, 4, 4, \
         0, 4, 0),
        (0, 0, 0, \
         4, 4, 0, \
         0, 4, 4),
        (0, 4, 0, \
         4, 4, 0, \
         4, 0, 0)
    ), (
        (0, 5, 5, \
         5, 5, 0, \
         0, 0, 0),
        (0, 5, 0, \
         0, 5, 5, \
         0, 0, 5),
        (0, 0, 0, \
         0, 5, 5, \
         5, 5, 0),
        (5, 0, 0, \
         5, 5, 0, \
         0, 5, 0)
    ), (
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6)
    ), (
        (0, 7, 0, 0, \
         0, 7, 0, 0, \
         0, 7, 0, 0, \
         0, 7, 0, 0),
        (0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0, \
         0, 0, 0, 0),
        (0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0),
        (0, 0, 0, 0, \
         0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0)
    )
)

class Block:
    
    def __init__(self, count):
        self.turn = randint(0, 3)
        self.type = BLOCK_DATA[randint(0, 6)]
        self.data = self.type[self.turn]
        self.size = int(sqrt(len(self.data)))
        self.xpos = randint(2, 8 - self.size)
        self.ypos = 1 - self.size
        self.fire = count + INTERVAL

    def update(self, count):
        
    
        erased = 0
        if is_overlapped(self.xpos, self.ypos + 1, self.turn):
            for y_offset in range(BLOCK.size):
                for x_offset in range(BLOCK.size):
                    if 0 <= self.xpos+x_offset < WIDTH and \
                        0 <= self.ypos+y_offset < HEIGHT:
                        val = BLOCK.data[y_offset*BLOCK.size \
                                            + x_offset]
                        if val != 0:
                            FIELD[self.ypos+y_offset]\
                                 [self.xpos+x_offset] = val

            erased = erase_line()
            go_next_block(count)

        if self.fire < count:
            self.fire = count + INTERVAL
            self.ypos += 1
        return erased

    def draw(self):

        for index in range(len(self.data)):
            xpos = index % self.size
            ypos = index // self.size
            val = self.data[index]
            if 0 <= ypos + self.ypos < HEIGHT and \
               0 <= xpos + self.xpos < WIDTH and val != 0:
                x_pos = 25 + (xpos + self.xpos) * 25
                y_pos = 25 + (ypos + self.ypos) * 25
                pygame.draw.rect(SURFACE, COLORS[val],
                                 (x_pos, y_pos, 24, 24))

def erase_line():
    erased = 0
    ypos = 20
    while ypos >= 0:
        if all(FIELD[ypos]):
            erased += 1
            LINE_ERASE_ANIMATION = (ypos, 0)
            del FIELD[ypos]
            FIELD.insert(0, [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8])
        else:
            ypos -= 1
    return erased

def is_game_over():
    
    filled = 0
    for cell in FIELD[0]:
        if cell != 0:
            filled += 1
    return filled > 2   

def go_next_block(count):
    
    global BLOCK, NEXT_BLOCK
    BLOCK = NEXT_BLOCK if NEXT_BLOCK != None else Block(count)
    NEXT_BLOCK = Block(count)

def is_overlapped(xpos, ypos, turn):
    
    data = BLOCK.type[turn]
    for y_offset in range(BLOCK.size):
        for x_offset in range(BLOCK.size):
            if 0 <= xpos+x_offset < WIDTH and \
                0 <= ypos+y_offset < HEIGHT:
                if data[y_offset*BLOCK.size + x_offset] != 0 and \
                    FIELD[ypos+y_offset][xpos+x_offset] != 0:
                    return True
    return False

def get_fall_distance(block):
    fall_distance = 0
    while not is_overlapped(block.xpos, block.ypos + fall_distance + 1, block.turn):
        fall_distance += 1
    return fall_distance - 1

def get_ghost_position(block):
    ghost_ypos = block.ypos
    while not is_overlapped(block.xpos, ghost_ypos + 1, block.turn):
        ghost_ypos += 1
    return ghost_ypos

def draw_ghost_block(ghost_ypos, block):
    for index in range(len(block.data)):
        xpos = index % block.size
        ypos = index // block.size
        val = block.data[index]
        if 0 <= ghost_ypos + ypos < HEIGHT and \
           0 <= block.xpos + xpos < WIDTH and val != 0:
            x_pos = 25 + (block.xpos + xpos) * 25
            y_pos = 25 + (ghost_ypos + ypos) * 25
            pygame.draw.rect(SURFACE, COLORS[val], 
                             (x_pos, y_pos, 24, 24), 1)  # Outline for ghost block
    
pygame.init()
#pygame.key.set_repeat(30, 30)
SURFACE = pygame.display.set_mode([600, 600])
FPSCLOCK = pygame.time.Clock()
WIDTH = 12
HEIGHT = 22
INTERVAL = 40
FIELD = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
COLORS = ((220, 220, 220), (255, 120, 120), (120, 255, 120), (120, 120, 255), \
          (255, 255, 120), (255, 120, 255), (120, 255, 255), (75, 0, 130), (128, 128, 128))
BLOCK = None
NEXT_BLOCK = None

def main():
    
    global INTERVAL
    count = 0
    score = 0
    level = 1
    game_over = False
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_over = largefont.render("GAME OVER!!", True, (180, 0, 0))  # 좀 더 부드러운 색상
    message_rect = message_over.get_rect()
    message_rect.center = (300, 300)

    go_next_block(INTERVAL)

    for ypos in range(HEIGHT):
        for xpos in range(WIDTH):
            FIELD[ypos][xpos] = 8 if xpos == 0 or \
                xpos == WIDTH - 1 else 0
    for index in range(WIDTH):
        FIELD[HEIGHT-1][index] = 8

    while True:
        key = None
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key

        game_over = is_game_over()
        if not game_over:
            count += 5
            if count % 1000 == 0:
                INTERVAL = max(1, INTERVAL - 2)
            erased = BLOCK.update(count)

            if erased > 0:
                score += (2 ** erased) * 100

   				# 레벨 업 조건: 1000점마다 레벨 업
                new_level = score // 1000 + 1
                if new_level > level:
                    level = new_level
                    INTERVAL = max(1, INTERVAL - 5)  # 레벨 업 시 속도 증가
            
            next_x, next_y, next_t = \
                BLOCK.xpos, BLOCK.ypos, BLOCK.turn
            if key == K_UP: # Rotate
                pygame.key.set_repeat()
                next_t = (next_t + 1) % 4
            elif key == K_RIGHT:
                next_x += 1
            elif key == K_LEFT:
                next_x -= 1
            elif key == K_DOWN:
                next_y += 1
            elif key == K_SPACE:  # 키보드 스페이스 누를 시 빠르게 내려간다
                fall_distance = get_fall_distance(BLOCK)
                next_y += fall_distance

            if not is_overlapped(next_x, next_y, next_t):
                BLOCK.xpos = next_x
                BLOCK.ypos = next_y
                BLOCK.turn = next_t
                BLOCK.data = BLOCK.type[BLOCK.turn]

        
        SURFACE.fill((245, 245, 245)) # 배경색 밝은 회색
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                val = FIELD[ypos][xpos]
                pygame.draw.rect(SURFACE, COLORS[val],
                                 (xpos*25 + 25, ypos*25 + 25, 24, 24))
        BLOCK.draw()

		# Draw ghost block
        ghost_ypos = get_ghost_position(BLOCK)
        draw_ghost_block(ghost_ypos, BLOCK)

        
        for ypos in range(NEXT_BLOCK.size):
            for xpos in range(NEXT_BLOCK.size):
                val = NEXT_BLOCK.data[xpos + ypos*NEXT_BLOCK.size]
                pygame.draw.rect(SURFACE, COLORS[val],
                                 (xpos*25 + 460, ypos*25 + 100, 24, 24))
        
        score_message = smallfont.render(f'Score: {score}', True, (80, 80, 80))
        level_message = smallfont.render(f'Level: {level}', True, (80, 80, 80))
        SURFACE.blit(score_message, (450, 30))
        SURFACE.blit(level_message, (450, 60))
        
        if game_over:
            SURFACE.blit(message_over, message_rect)

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()
