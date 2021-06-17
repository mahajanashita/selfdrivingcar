import pygame
pygame.init()
window=pygame.display.set_mode((1200, 400))
track=pygame.image.load('C:/Users/ashit/Downloads/track6.png')
car=pygame.image.load('C:/Users/ashit/Downloads/tesla.png')
car=pygame.transform.scale(car,(30, 60))     #dimensions of car
car_x=155
car_y=300
focal_dis =25
cam_x_offset =0
cam_y_offset =0
direction ='up'
drive=True
clock =pygame.time.Clock()
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive=False                     #to stop the game by clicking on cross
    clock.tick(60)                                                      # speed of car being controlled
    cam_x =car_x+ cam_x_offset+15                                                       #get camera infront so add 15 and y
    cam_y =car_y +cam_y_offset+15
    up_px =window.get_at((cam_x, cam_y-focal_dis))[0]
    down_px =window.get_at((cam_x, cam_y+focal_dis))[0]
    right_px =window.get_at((cam_x +focal_dis, cam_y))[0]

    # till road is white move car ie 255
    print((up_px,right_px,down_px))

    # take turn ,rotate and chnage direction
    if direction=='up' and up_px != 255 and right_px==255:
        direction = 'right'
        cam_x_offset=30
        #- for clockwise and also move camera to detect by usimg offset
        car =pygame.transform.rotate(car,-90)
    elif direction =='down' and down_px!=255 and right_px ==255:
        direction ='right'
        car_y=car_y +30
        cam_y_offset=0
        cam_x_offset=30
        car =pygame.transform.rotate(car, 90)

    elif direction =='right' and right_px!=255 and down_px ==255:
        direction ='down'
        # as off track so increase x
        car_x=car_x +30
        #camera position as it goes behind we need to y offset
        cam_x_offset =0
        cam_y_offset =30
        car =pygame.transform.rotate(car,90)
    elif direction=='right' and right_px!=255 and up_px ==255:
        direction= 'up'
        car_x= car_x+ 30
        cam_x_offset=0
        car =pygame.transform.rotate(car,90)




     # drive the car
    if direction =='up' and up_px==255:
        # moving car by reducing it
        car_y = car_y -2
    elif direction =='right' and right_px ==255:
        car_x= car_x+2
    elif direction =='down' and down_px ==255:
        car_y=car_y+2

    window.blit(track,(0,0))                                                   #blit stands for block image transfer
    window.blit(car,(car_x, car_y))                                            #car position
    pygame.draw.circle(window,(0, 255, 0),(cam_x,cam_y),5, 5)                  #camera looks with circle
    pygame.display.update()
