#!/usr/bin/env python3
import random
import os
#version 2

r = lambda: random.randint(0,255)
rclr='#%02X%02X%02X' % (r(),r(),r())


os.system('clear')#change if incompatible with your system

inf = input('Where to save image?(relative)')
l = int(input('Enter image length: '))
w=int(input('Enter image width: '))


file = open(inf,"w+")
f=file.read()
exec(f)
line=0
pix=[]
ipix=iter(pix)
clr="0"
step=0

while line < l * w:#put the dimensions of the desired output image, this default is pretty large. for slow computers use smaller.
    pix.append(rclr)#also, the dimensions must be equal to each other, aka create a square
    r = lambda: random.randint(0,255)
    rclr='#%02X%02X%02X' % (r(),r(),r())
    print(rclr)
    line=line+1

#while step < len(pix):
 #   file.write(clr)
  #  clr=next(ipix)
   # step=step+1

with open(inf, 'w+') as file:
    sw=str(w)
    file.write('w=')
    file.write(sw)
    file.write('\npix=[')
    for item in pix:#it should be a plaintext document, that's the fastest to edit. of course change extension to .pgf
        file.write('"{}",'.format(item))#after it's finished writing, you have to open the file and add the list brackets "[]" like:
        #pix=[whatever was generated]. also, above pix, add w=x. x is whatever dimensions you chose. if you chose 1000 * 1000,
        #you would do w=1000. you only put width because pgexec assumes that the image is square and square width = square height
        #if you want to make anything nonsquare, you have to "draw" the hex values yourself and add a square background of alpha to
        #your image. I'm working on an image converter.
    file.write(']')
