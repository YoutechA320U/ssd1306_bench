#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time

# Raspberry Pi pin configuration:
RST = None

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Get display width and height.
width = disp.width
height = disp.height

# Clear display.
disp.clear()
disp.display()
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

t_start = time.time()
count=0
while True:
    count =count+1
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((54,22), str(count), font=font, fill=1)
    disp.image(image)
    disp.display()
    if count == 100:
      result=time.time() - t_start
      time.sleep(2)
      draw.rectangle((0,0,width,height), outline=0, fill=0)
      draw.text((16,22), str("time:%1ds"% result),font=font, fill=1)
      disp.image(image)
      disp.display()
      break
