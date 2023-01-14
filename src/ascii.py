import curses
import logging
import imageio.v3 as iio
import numpy as np

from PIL import Image


ascii_str     = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_str_len = len(ascii_str)

def main(stdscr):
    stdscr.nodelay(True)

    for frame in iio.imiter("<video0>"):
        key = stdscr.getch()
        if(key == 113):
            break
        elif(key == curses.KEY_RESIZE):
            pass
        
        frame = np.dot(frame,[0.2989, 0.5870, 0.1140])
        frame = np.round(frame).astype(np.uint8)

        rows,cols = stdscr.getmaxyx()
        cols -= 1

        im = Image.fromarray(frame,mode="L")
        im = im.resize((cols,rows))
        
        im = np.interp(np.array(im),[0,255],[0,ascii_str_len-1])
        im = np.rint(im).astype(np.uint8)

        for y in range(rows):
            tmp_str = ""
            for x in range(cols):
                tmp_str+=ascii_str[im[y][x]]
            stdscr.addstr(y,0,tmp_str)
            

curses.wrapper(main)