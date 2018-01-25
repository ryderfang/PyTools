#! /usr/local/bin/python3
# -*- coding:utf-8 -*-


import os
import sys

import cairosvg

def remove_watermark(src_name, dst_name):
    if (not os.path.exists(src_name)) or (not os.path.splitext(src_name)[1] == '.svg'):
        print('ERR:: "' + src_name + '" NOT EXISTS or NOT A SVG FILE!')
        return
    
    svg_content = ''
    with open(src_name, 'r') as f:
        svg_content = f.read()
        end = svg_content.rfind('</g')
        beg = svg_content.rfind('<g', 0, end)
        svg_content = svg_content[:beg] + svg_content[end:]

    with open('./vp_test_out.svg', 'w') as f:
        f.write(svg_content)

    cairosvg.svg2png(url='./vp_test_out.svg', write_to=dst_name)
    os.remove('./vp_test_out.svg')
    print('Convert success ~> ' + dst_name)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('usage: python vp_remove_watermark.py "source.svg" [-o] ["dst.png"]')
        print("\nvp_remove_watermark - Remove Visual Paradigm's watermark")
        print("\noptional arguments:\n  -o\tout file name, default [source.png]\n")
    else:
        s = sys.argv[1]
        d = ''
        if len(sys.argv) >= 4:
            d = sys.argv[3]
        else:
            (n, ext) = os.path.splitext(s)
            d = n + '.png'
        remove_watermark(s, d)
