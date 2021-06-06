#Mauricio Estrella
#https://www.instagram.com/mauriciolavider/

from machine import I2C, Pin
import math
import gfx
import ssd1306
import mpu6050

i2c = I2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
graphics = gfx.GFX(oled_width, oled_height, oled.pixel)

accelerometer = mpu6050.accel(i2c)

xof = 64 
yof = 34

while True:
    val = accelerometer.get_values()
    y = round((val['AcX']*10)/16000)
    x = round((val['AcY']*10)/16000)
    print("{0}  {1}".format(x, y))

    p1_x = -10-x
    p1_y = 10-y
    p2_x = 10-x
    p2_y = 10-y    
    p3_x = -10-x
    p3_y = -10-y  
    p4_x = 10-x
    p4_y = -10-y
    
    p5_x = -10+x
    p5_y = 10+y
    p6_x = 10+x
    p6_y = 10+y    
    p7_x = -10+x
    p7_y = -10+y  
    p8_x = 10+x
    p8_y = -10+y
    
    oled.fill(0)
    
    graphics.line(p1_x+xof, p1_y+yof, p2_x+xof, p2_y+yof, 1)
    graphics.line(p3_x+xof, p3_y+yof, p4_x+xof, p4_y+yof, 1)
    graphics.line(p1_x+xof, p1_y+yof, p3_x+xof, p3_y+yof, 1)
    graphics.line(p2_x+xof, p2_y+yof, p4_x+xof, p4_y+yof, 1)
    
    graphics.line(p5_x+xof, p5_y+yof, p6_x+xof, p6_y+yof, 1)
    graphics.line(p7_x+xof, p7_y+yof, p8_x+xof, p8_y+yof, 1)
    graphics.line(p5_x+xof, p5_y+yof, p7_x+xof, p7_y+yof, 1)
    graphics.line(p6_x+xof, p6_y+yof, p8_x+xof, p8_y+yof, 1)
    
    graphics.line(p1_x+xof, p1_y+yof, p5_x+xof, p5_y+yof, 1)
    graphics.line(p2_x+xof, p2_y+yof, p6_x+xof, p6_y+yof, 1)
    graphics.line(p3_x+xof, p3_y+yof, p7_x+xof, p7_y+yof, 1)
    graphics.line(p4_x+xof, p4_y+yof, p8_x+xof, p8_y+yof, 1)
    
    graphics.fill_circle(xof, yof, 2, 1)
    
    oled.show()
