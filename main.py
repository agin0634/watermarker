from PIL import Image, ImageFont, ImageDraw, ImageQt
import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from mainUI import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QColorDialog

class App():
    def previewImg(self, imgfile):
        try:
            img = Image.open(imgfile)
            return img
        except Exception as e:
            print(e)
            return None

    def drawText(self, img, loc, text, color, font, fontsize):
        draw = ImageDraw.Draw(img)
        fontpath = 'Fonts/'  + font
        fontpath = ImageFont.truetype(fontpath,fontsize)
        draw.text(xy=loc,text=text,fill=color,font=fontpath,align='center')
        img.show()

    def fontsBrowser(self):
        fonts = os.listdir("./fonts")
        return fonts

class AppWindow(QMainWindow, Ui_MainWindow):
    # parameter
    img_path = ''
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
        self.addFontstoComboBox()

    def addFontstoComboBox(self):
        fonts = App.fontsBrowser(App)
        for i in range(len(fonts)):
            f = fonts[i]
            f = f.replace('.ttf','')
            self.ui.comboBox_font.addItem(f)

            #TODO font style preview
            '''
            item = self.ui.comboBox_font.model().item(i)
            font = item.font() 
            font.setPointSize(10) 
            font.setFamily("Onthehill.ttf")
            item.setFont(font)
            '''
    
    def eventColorPicker(self):
        color = QColorDialog.getColor()
        self.ui.colorButton.setStyleSheet('QWidget {background-color:%s}'%color.name())
        r = color.red()
        g = color.green()
        b = color.blue()
        self.color = (r,g,b)

    def eventBrowseImg(self):
        App.fontsBrowser(App)
        imgfile = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',os.getcwd(),"All Files(*jpg *png)")
        if imgfile:
            print(imgfile)
            self.img_path = imgfile[0]
            self.pre_img = App.previewImg(App,self.img_path)
        else:
            pass
            
    def eventSaveImg(self):
        if self.pre_img != None:
            try:
                filename = 'wm_' + os.path.basename(self.img_path)
                out = self.pre_img
                out = out.convert("RGB")
                out.save(filename, quality=90, subsampling=0)
                print('save')
            except Exception as e:
                print(e)
                pass
        else:
            pass

    def eventPreview(self):
        if self.ui.lineEdit.text():
            self.text = self.ui.lineEdit.text()

        if self.pre_img != None:
            i = App.previewImg(App,self.img_path)
            self.text_font = self.fontStyle()
            self.text_size = int(self.ui.comboBox_fontsize.currentText())
            currenttext_loc = self.addOffset(self.text_loc)
            try:
                App.drawText(App,i,currenttext_loc,self.text,self.color,self.text_font,self.text_size)
                self.pre_img = i
            except Exception as e:
                print(e)
                pass
        else:
            pass

    def addOffset(self, text_loc):
        w, h = text_loc
        up = self.ui.spinBox_up.text()
        down = self.ui.spinBox_down.text()
        left = self.ui.spinBox_left.text()
        right = self.ui.spinBox_right.text()
        x = int(right) - int(left)
        y = int(down) - int(up)
        text_loc = (w + x, h + y)
        return text_loc

    def fontStyle(self):
        font = self.ui.comboBox_font.currentText() +'.ttf'
        return font

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