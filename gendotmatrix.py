#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import bitarray
from bitarray import bitarray
import getopt
import sys
import re

def get_pix(image):
    pixel = image.load()
    width, height = image.size
    bitmap = bitarray()
    for h in range(height):
        for w in range(width):
            # if int(sum(pixel[w, h])) > (255 * 3 / 2):
            if pixel[w, h] > 0:
                bitmap.append(False)
            else:
                bitmap.append(True)
    return bitmap

def get_gb2312_pix(gb2312_code, w, h, usr_font):
    # image = Image.new("RGB", (w, h), (255, 255, 255))
    image = Image.new("1", (w, h), (1))
    d_usr = ImageDraw.Draw(image)
    try:
        unicode_code = gb2312_code.decode('gb2312')
        # d_usr.text((0, 0), unicode_code, (0,0,0), font=usr_font)
        d_usr.text((0, 0), unicode_code, (0), font=usr_font)
    except:
        # d_usr.text((0, 0), u" ", (0,0,0), font=usr_font)
        d_usr.text((0, 0), u" ", (0), font=usr_font)
    return get_pix(image)

def main():
    truetypefile = 'simsun.ttc'
    font_width = 16
    font_height = 16
    outfilename = 'dot_matrix.font'
    usr_font = ImageFont.truetype(truetypefile, font_height)
    with open(outfilename, 'wb') as outfile:
#        for i in range(0xA1, 0xF8):
#            for j in range(0xA1, 0xFF):
        hz_in=u'美的吃喝拉撒美的吃喝拉撒'
        hz_in=list(set(hz_in))
#        hz_list.sort()
        str=[]
        str.append([])
        str.append([])
        str.append([])
        str[1].append("void *p%s_%sx%s[]={"%(truetypefile[:-4],font_width, font_height))
        str[2].append("u16 GBK_code_%s_%sx%s[]={"%(truetypefile[:-4],font_width, font_height))
        hz_list=[]
        for a in range(len(hz_in)):
            hz_list.append(unicode(hz_in[a]).encode('gbk'))
        hz_list.sort();
        for a in hz_list:
            data = get_gb2312_pix(chr(ord(a[0])) + chr(ord(a[1])), font_width, font_height, usr_font)
            str[0].append("//%s\n"%a)
            str[0].append("char ot_%s[]={"%(hex(ord(a[0])*256+(ord(a[1])))))
            for x in range(0, len(data), 8):
                if x>0:
                    str[0].append(",")
                str[0].append("%s"%(hex(int(data.to01()[x:x+8], 2))))
            str[0].append("};\n")
            if len(str[1])==1:
                str[1].append("\n(void *)ot_%s"%(hex(ord(a[0])*256+(ord(a[1])))))
            else:
                str[1].append(",\n(void *)ot_%s"%(hex(ord(a[0])*256+(ord(a[1])))))
            if len(str[2])==1:
                str[2].append("%s"%(hex(ord(a[0])*256+(ord(a[1])))))
            else:
                str[2].append(",%s"%(hex(ord(a[0])*256+(ord(a[1])))))
        str[1].append("};\n")
        str[2].append("};\n")
        
        str[2].append("Font User_Font_%s_%sx%s={\n"%(truetypefile[:-4],font_width, font_height))
        str[2].append("    GBK_code_%s_%sx%s,\n"%(truetypefile[:-4],font_width, font_height))
        str[2].append("    p%s_%sx%s,\n"%(truetypefile[:-4],font_width, font_height))
        str[2].append("    %s,\n"%font_width)
        str[2].append("    sizeof(GBK_code_%s_%sx%s)\n"%(truetypefile[:-4],font_width, font_height))
        str[2].append("};")
#        
        pkl_filename='dot_matrix.cpp'
        file_object = open(pkl_filename, 'w')
        file_object.writelines(str[0])
        file_object.writelines(str[1])
        file_object.writelines(str[2])
        file_object.close()
        

if __name__ == '__main__':
    main()

