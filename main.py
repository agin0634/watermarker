from PIL import Image, ImageFont, ImageDraw, ImageQt
import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from mainUI import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

class App():
    def previewImg(self, imgfile):
        try:
            img = Image.open(imgfile)
            
            '''draw = ImageDraw.Draw(img)
            draw.text(xy=(100,100),text="Hello World",fill=(255,69,0))
            img.show()'''
            #img.show()
            return img
        except Exception as e:
            print(e)
            return None
        

    def drawText(self, img, loc, text, color, font, fontsize):
        draw = ImageDraw.Draw(img)
        cfont = 'C:/Windows/Fonts/'  + font
        # TODO get font
        print(cfont)
        cfont = ImageFont.truetype(cfont,fontsize)
        draw.text(xy=loc,text=text,fill=color,font=cfont,align='center')
        img.show()

class AppWindow(QMainWindow, Ui_MainWindow):
    # parameter
    pre_img = None
    text_loc = (100,0)
    text = ''
    color = (255,255,255)
    text_font = ''
    text_size = 8

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def eventBrowseImg(self):
        imgfile = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',os.getcwd(),"All Files(*jpg *png)")
        if imgfile:
            print(imgfile[0])
            self.pre_img = App.previewImg(App, imgfile[0])
            #color
            '''
            graphicscene = QtWidgets.QGraphicsScene()
            graphicscene.addWidget(pre_img)
            self.ui.graphicsView.setScene(graphicscene)
            self.ui.graphicsView.show()
            '''
            
    def eventSaveImg(self):
        out = self.pre_img
        out = out.convert("RGB")
        out.save('img.jpg', quality=90, subsampling=0)
        print('save')

    def eventPreview(self):
        if self.ui.lineEdit.text():
            self.text = self.ui.lineEdit.text()
        self.text_font = self.fontStyle()
        self.text_size = int(self.ui.comboBox_fontsize.currentText())

        App.drawText(App,self.pre_img,self.text_loc,self.text,self.color,self.text_font,self.text_size)

    def addOffset(self):
        up = self.ui.spinBox_up.text()
        down = self.ui.spinBox_down.text()
        left = self.ui.spinBox_left.text()
        right = self.ui.spinBox_right.text()
        x = int(right) - int(left)
        y = int(down) - int(up)
        pass

    # -- fonts style events
    bisBold = False

    def fontStyle(self):
        font = self.ui.ComboBox_font.currentText() +'.ttf'
        print(font)
        return font

    def eventBold(self):
        self.fontStyle()
        if self.bisBold:
            self.bisBold = False
            self.ui.boldButton.setStyleSheet('color: rgb(220, 220, 220);\nbackground-color: rgb(98, 98, 115);')
        else:
            self.bisBold = True
            self.ui.boldButton.setStyleSheet('color: rgb(0, 0, 0);\nbackground-color: rgb(249, 201, 91);')


        

    # -- align events
    def eventAlign00(self):
        if self.pre_img:
            w,h = self.pre_img.size
            self.text_loc = (w/6,h/6)
        else:
            pass
    
    def eventAlign01(self):
        if self.pre_img:
            w,h = self.pre_img.size
            self.text_loc = (w/6*3,h/6)
        else:
            pass

    def eventAlign02(self):
        if self.pre_img:
            w,h = self.pre_img.size
            self.text_loc = (w/6*5,h/6)
        else:
            pass

    def eventAlign10(self):
        if self.pre_img:
            w,h = self.pre_img.size
            self.text_loc = (w/6,h/6*3)
        else:
            pass

    def eventAlign11(self):
        if self.pre_img:
            w,h = self.pre_img.size
            self.text_loc = (w/6*3,h/6*3)
        else:
            pass

    def eventAlign12(self):
        if self.pre_img:
            w,h = self.pre_img.size
            self.text_loc = (w/6*5,h/6*3)
        else:
            pass

    def eventAlign20(self):
        if self.pre_img:
            w,h = self.pre_img.size
            self.text_loc = (w/6,h/6*5)
        else:
            pass

    def eventAlign21(self):
        if self.pre_img:
            w,h = self.pre_img.size
            self.text_loc = (w/6*3,h/6*5)
        else:
            pass

    def eventAlign22(self):
        if self.pre_img:
            w,h = self.pre_img.size
            self.text_loc = (w/6*5,h/6*5)
        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AppWindow()
    win.show()
    sys.exit(app.exec_())