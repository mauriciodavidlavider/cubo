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

r = 18
xof = 64 
yof = 34
radcon = 57.2958

while True:
    val = accelerometer.get_values()
    y = round((val['AcX']*90)/16000)
    x = round((val['AcY']*90)/16000)
    print("{0}  {1}".format(x, y))

    a1_x = (135-x)
    a1_y = (135-y)
    p1_x = math.cos(a1_x/radcon)
    p1_y = math.cos(a1_y/radcon)
    p1_x = int(r*p1_x)
    p1_y = int(r*p1_y)
    
    a2_x = (45-x)
    a2_y = (135-y)
    p2_x = math.cos(a2_x/radcon)
    p2_y = math.cos(a2_y/radcon)
    p2_x = int(r*p2_x)
    p2_y = int(r*p2_y)
    
    a3_x = (135-x)
    a3_y = (45-y)
    p3_x = math.cos(a3_x/radcon)
    p3_y = math.cos(a3_y/radcon)
    p3_x = int(r*p3_x)
    p3_y = int(r*p3_y)
    
    a4_x = (45-x)
    a4_y = (45-y)
    p4_x = math.cos(a4_x/radcon)
    p4_y = math.cos(a4_y/radcon)
    p4_x = int(r*p4_x)
    p4_y = int(r*p4_y)
    
    a5_x = (135+x)
    a5_y = (135+y)
    p5_x = math.cos(a5_x/radcon)
    p5_y = math.cos(a5_y/radcon)
    p5_x = int(r*p5_x)
    p5_y = int(r*p5_y)
    
    a6_x = (45+x)
    a6_y = (135+y)
    p6_x = math.cos(a6_x/radcon)
    p6_y = math.cos(a6_y/radcon)
    p6_x = int(r*p6_x)
    p6_y = int(r*p6_y)
    
    a7_x = (135+x)
    a7_y = (45+y)
    p7_x = math.cos(a7_x/radcon)
    p7_y = math.cos(a7_y/radcon)
    p7_x = int(r*p7_x)
    p7_y = int(r*p7_y)
    
    a8_x = (45+x)
    a8_y = (45+y)
    p8_x = math.cos(a8_x/radcon)
    p8_y = math.cos(a8_y/radcon)
    p8_x = int(r*p8_x)
    p8_y = int(r*p8_y)
    
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