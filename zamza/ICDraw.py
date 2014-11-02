#!coding:utf-8

class ICdraw:
    topmargin = 20
    bottommargin = 20
    leftmargin = 40
    rightmargin = 40
    pinmargin = 10
    fontsize = 10

    def __init__(self):
        pass

    def ICname(self, name):
        self.icname[name] = {"width": self.width, "height": self.height, "toppin": self.topictext, "leftpin": self.leftictext, "rightpin": self.rightictext, "bottompin": self.bottomictext, "toppinpos": self.toppinpos, "leftpinpos": self.leftpinpos, "rightpinpos": self.rightpinpos, "bottompinpos": self.bottompinpos}

    def __contour(self, x, y, width, height, color='black'):
        self.drawline.line(((x, y), (x, y+height), (x+width, y+height), (x+width, y), (x, y)), fill=color, width=2)

    def ICpin(self, top=0, left=0, bottom=0, right=0):
        self.width = max(top, bottom) * self.pinmargin + max(top, bottom) * self.fontsize + self.widthmargin
        self.height = max(left, right) * self.pinmargin + max(left, right) * self.fontsize + self.heightmargin

    def ICdraw(self, x, y):
        fontsize = self.fontsize
        self.__contour(x=x, y=y, width=self.width, height=self.height)
        for i, text in enumerate(self.topictext):
            pos = (x+(i*self.pinmargin)+(i*fontsize)+self.widthmargin//2, y)
            self.drawline.text(pos, str(text), font=self.font)
            self.toppinpos.append(pos)
        for i, text in enumerate(self.leftictext):
            pos = (x, y+(i*self.pinmargin)+(i*fontsize)+self.heightmargin//2)
            self.drawline.text(pos, str(text), font=self.font)
            self.leftpinpos.append(pos)
        for i, text in enumerate(self.bottomictext):
            pos = (x+(i*self.pinmargin)+(i*fontsize)+self.widthmargin//2, y+self.height-self.bottommargin//2)
            self.drawline.text(pos, str(text), font=self.font)
            self.bottompinpos.append(pos)
        for i, text in enumerate(self.rightictext):
            pos = (x+self.width-self.rightmargin//2, y+(i*self.pinmargin)+(i*fontsize)+self.heightmargin//2)
            self.drawline.text(pos, str(text), font=self.font)
            self.rightpinpos.append(pos)

    def ICgetpinpos(self, icname, pinname):
        if pinname in self.icname[icname]["toppin"]:
            for i, name in enumerate(self.icname[icname]["toppin"]):
                if pinname == name:
                    return ("top", i, self.icname[icname]["toppinpos"][i])
        if pinname in self.icname[icname]["leftpin"]:
            for i, name in enumerate(self.icname[icname]["leftpin"]):
                if pinname == name:
                    return ("left", i, self.icname[icname]["leftpinpos"][i])
        if pinname in self.icname[icname]["bottompin"]:
            for i, name in enumerate(self.icname[icname]["bottompin"]):
                if pinname == name:
                    return ("bottom", i, self.icname[icname]["bottompinpos"][i])
        if pinname in self.icname[icname]["rightpin"]:
            for i, name in enumerate(self.icname[icname]["rightpin"]):
                if pinname == name:
                    return ("right", i, self.icname[icname]["rightpinpos"][i])

    def ICtext(self, top, left, bottom, right):
        self.topictext = top
        self.leftictext = left
        self.bottomictext = bottom
        self.rightictext = right
