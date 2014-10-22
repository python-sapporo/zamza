#!coding:utf-8
from PIL import ImageDraw, Image, ImageFont
import os


class ICdraw:
    topmargin = 20
    bottommargin = 20
    leftmargin = 40
    rightmargin = 40
    pinmargin = 10
    fontsize = 16

    def __init__(self):
        self.im = Image.new('RGBA', (480, 780), (128, 128, 128, 0))
        self.icname = {}
        self.drawline = ImageDraw.Draw(self.im)
        self.font = ImageFont.truetype(os.path.dirname(__file__) + "/../font/ipaexg.ttf", size=16)
        self.widthmargin = self.leftmargin + self.rightmargin
        self.heightmargin = self.topmargin + self.bottommargin

    def name(self, name):
        self.icname[name] = {"width": self.width, "height": self.height, "toppin": self.topictext, "leftpin": self.leftictext, "rightpin": self.rightictext, "bottompin": self.bottomictext}

    def __contour(self, x, y, width, height, color='black'):
        self.drawline.line(((x, y), (x, y+height), (x+width, y+height), (x+width, y), (x, y)), fill=color, width=2)

    def pin(self, top=0, left=0, bottom=0, right=0):
        self.width = max(top, bottom) * self.pinmargin + max(top, bottom) * self.fontsize + self.widthmargin
        self.height = max(left, right) * self.pinmargin + max(left, right) * self.fontsize + self.heightmargin

    def draw(self, x, y):
        fontsize = self.fontsize
        self.__contour(x=x, y=y, width=self.width, height=self.height)
        for i, text in enumerate(self.topictext):
            self.drawline.text((x+(i*self.pinmargin)+(i*fontsize)+self.widthmargin//2, y), str(text), font=self.font)
        for i, text in enumerate(self.leftictext):
            self.drawline.text((x, y+(i*self.pinmargin)+(i*fontsize)+self.heightmargin//2), str(text), font=self.font)
        for i, text in enumerate(self.bottomictext):
            self.drawline.text((x+(i*self.pinmargin)+(i*fontsize)+self.widthmargin//2, y+self.height-self.bottommargin//2), str(text), font=self.font)
        for i, text in enumerate(self.rightictext):
            self.drawline.text((x+self.width-self.rightmargin//2, y+(i*self.pinmargin)+(i*fontsize)+self.heightmargin//2), str(text), font=self.font)

    def getpinpos(self, icname, pinname):
        if pinname in self.icname[icname]["toppin"]:
            for i, name in enumerate(self.icname[icname]["toppin"]):
                if pinname == name:
                    return ("top", i)
        if pinname in self.icname[icname]["leftpin"]:
            for i, name in enumerate(self.icname[icname]["leftpin"]):
                if pinname == name:
                    return ("left", i)
        if pinname in self.icname[icname]["bottompin"]:
            for i, name in enumerate(self.icname[icname]["bottompin"]):
                if pinname == name:
                    return ("bottom", i)
        if pinname in self.icname[icname]["rightpin"]:
            for i, name in enumerate(self.icname[icname]["rightpin"]):
                if pinname == name:
                    return ("right", i)

    def text(self, top, left, bottom, right):
        self.topictext = top
        self.leftictext = left
        self.bottomictext = bottom
        self.rightictext = right

    def show(self):
        self.im.show()


class Import(object):
    def __init__(self):
        pass
