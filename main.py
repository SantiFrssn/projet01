# Librairie   : https://github.com/kholm777/maqueen/tree/main
from maqueen import Maqueen
from microbit import * 
import utime
import music
# Constantes
WHITE = 1
BLACK = 0

robot = Maqueen()
display.show(Image.HAPPY)


while True:
   if robot.line_left()== BLACK and robot.line_right()== BLACK:
       robot.motor_left(255)
       robot.motor_right(170)
       pin8.write_digital(1)
       pin12.write_digital(1)
       robot.rgb_front_left(0,255,0)
       robot.rgb_rear_left(0,255,0)
       robot.rgb_front_right(0,255,0)
       robot.rgb_rear_right(0,255,0)
       
       
   elif robot.line_left() == BLACK and robot.line_right()== WHITE:
       robot.motor_left(0)
       robot.motor_right(255)
       pin8.write_digital(0)
       pin12.write_digital(1)
       robot.rgb_front_left(0,0,0)
       robot.rgb_rear_left(0,0,0)
       robot.rgb_front_right(0,0,255)
       robot.rgb_rear_right(0,0,255)
       
       
   elif robot.line_left() == WHITE and robot.line_right()== BLACK:
       robot.motor_left(255)
       robot.motor_right(0)
       pin8.write_digital(1)
       pin12.write_digital(0)
       robot.rgb_front_left(255,0,0)
       robot.rgb_rear_left(255,0,0)
       robot.rgb_front_right(0,0,0)
       robot.rgb_rear_right(0,0,0)
       
   elif robot.line_left() == WHITE and robot.line_right()== WHITE:
       robot.motor_left(255)
       robot.motor_right(170)
       pin8.write_digital(0)
       pin12.write_digital(0)
       robot.rgb_front_left(255,255,255)
       robot.rgb_rear_left(255,255,255)
       robot.rgb_front_right(255,255,255)
       robot.rgb_rear_right(255,255,255)
      
       
       
    

        
        
       
      