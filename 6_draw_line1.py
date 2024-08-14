"""
line(Surface, color, start_pos, end_pos, width=1) -> Rect
Surface : 그리는 대상이 되는 화면(Surface 객체)
color : 색
start_pos : 시작점
end_pos : 도착점
width : 선 폭 
"""
""" draw_line1.py """
import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400, 220))
FPSCLOCK = pygame.time.Clock()

def main():
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        SURFACE.fill((255,255,255))

        #빨간색: 가로줄
        pygame.draw.line(SURFACE, (255, 0, 0), (10, 80), (200, 80))

        #빨간색: 가로줄(굵기 15)
        pygame.draw.line(SURFACE, (255, 0,0),(10,150), (200,150), 15)

        #녹색: 세로줄
        pygame.draw.line(SURFACE, (0, 255, 0), (250, 30), (250, 200))

        #녹색: 빗금(굵기 10)
        start_pos = (300, 30)
        end_pos = ( 380, 200)
        pygame.draw.line(SURFACE, (0, 0, 255), start_pos, end_pos, 10)

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()
