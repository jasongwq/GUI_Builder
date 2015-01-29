#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 
import pprint, pickle
from PyQt4 import QtCore,QtGui

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
def dot_matrix(hz_in):
    truetypefile = 'simsun.ttc'
    font_width = 16
    font_height = 16
    outfilename = 'dot_matrix.font'
    usr_font = ImageFont.truetype(truetypefile, font_height)
    with open(outfilename, 'wb') as outfile:
#        hz_in=u'美的吃喝拉撒美的吃喝拉撒'
        hz_in=list(hz_in)
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
            if len(a)>1:
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
        
        pkl_filename='font_Mat.h'
        file_object = open(pkl_filename, 'w')
        file_object.writelines(str[0])
        file_object.writelines(str[1])
        file_object.writelines(str[2])
        file_object.close()
    
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
Win_list =[[]]
Win_config =[[[]]]
Str_Code=[[]]
FontCode=''
Win_id=[0]
Obj_id=[0]
col = QtGui.QColor(0, 0, 0)

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        widget =QtGui.QWidget();
        self.setCentralWidget(widget);
        Win_list[0].append(QtGui.QPushButton(self));
        Win_list[0][0].setStyleSheet("QWidget { background-color: %s }" 
            % col.name())
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(10)        
#        pprint.pprint(Win_list)
        self.label_0 = QtGui.QLabel(self)
        self.label_1 = QtGui.QLabel(self)
        self.label_2 = QtGui.QLabel(self)
        self.label_3 = QtGui.QLabel(self)
        self.spinBox_0 = QtGui.QSpinBox(self)
        self.spinBox_1 = QtGui.QSpinBox(self)
        self.spinBox_2 = QtGui.QSpinBox(self)
        self.spinBox_3 = QtGui.QSpinBox(self)        
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit_2 = QtGui.QLineEdit(self)
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 7, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 7, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 7, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(_fromUtf8("颜色"), self)
        self.pushButton.clicked.connect(self.showDialog)
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 8, 1, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 6, 2, 1, 1)
        self.listWidget = QtGui.QListWidget(self)
        self.listWidget.setMaximumSize(QtCore.QSize(75, 16777215))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 4, 2, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self)
        self.tableWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.CurrentChanged|QtGui.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.gridLayout.addWidget(self.tableWidget, 5, 1, 1, 2)
        self.tableWidget.setCellWidget(0,0,self.spinBox_0);
        self.tableWidget.setCellWidget(1,0,self.spinBox_1);
        self.tableWidget.setCellWidget(2,0,self.spinBox_2);
        self.tableWidget.setCellWidget(3,0,self.spinBox_3);
        self.tableWidget.setCellWidget(4,0,self.lineEdit_2);
        
        
        
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.onlineEditChanged)
        QtCore.QObject.connect(self.lineEdit_2, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.onlineEdit_2Changed)
        
        QtCore.QObject.connect(self.spinBox_0, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.onspinBox_0Changed)
        QtCore.QObject.connect(self.spinBox_1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.onspinBox_1Changed)
        QtCore.QObject.connect(self.spinBox_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.onspinBox_2Changed)
        QtCore.QObject.connect(self.spinBox_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.onspinBox_3Changed)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onpushButton_2Clicked)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onpushButton_3Clicked)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onpushButton_4Clicked)
#        QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.oncomboBox_2currentIndexChanged)
        QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.oncomboBox_2currentIndexChanged)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), self.onlistWidgetitemClicked)
#        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL(_fromUtf8("cellChanged(int,int)")), self.ontableWidget_0Changed)

        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "x", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "y", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "w", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "h", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "text", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "值", None))

        self.label_0.setText(_translate("Dialog", "X", None))
        self.label_1.setText(_translate("Dialog", "Y", None))
        self.label_2.setText(_translate("Dialog", "W", None))
        self.label_3.setText(_translate("Dialog", "H", None))
        self.pushButton.setText(_translate("Dialog", "颜色", None))
        self.pushButton_2.setText(_translate("Dialog", "新建", None))
        self.pushButton_3.setText(_translate("Dialog", "删除", None))
        self.pushButton_4.setText(_translate("Dialog", "保存", None))
        for i in range(len(Win_list)):
            text="%s"%i
            self.comboBox_2.addItem(_fromUtf8(""))
            self.comboBox_2.setItemText(i, _translate("Dialog", text, None))
        self.comboBox.setItemText(0, _translate("Dialog", "BUTTON", None))
        self.comboBox.setItemText(1, _translate("Dialog", "WINDOW", None))
        self.lineEdit.setText(_translate("Dialog", "000000", None))
        
        Win_list[0][0].setGeometry(10, 100, 100, 100)
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.spinBox_0.setMaximum(999)
        self.spinBox_1.setMaximum(999)
        self.spinBox_2.setMaximum(999)
        self.spinBox_3.setMaximum(999)
        self.gridLayout.addWidget(self.pushButton_2, 7, 1, 1, 1)
        self.gridLayout.addWidget(self.pushButton_3, 7, 2, 1, 1)
        self.gridLayout.addWidget(self.pushButton_4, 8, 2, 1, 1)
        
        
        self.spinBox_0.setValue(0)
        self.spinBox_1.setValue(0)
        self.spinBox_2.setValue(240)
        self.spinBox_3.setValue(320)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        widget.setLayout(self.gridLayout)

        exitAction = QtGui.QAction(QtGui.QIcon('ico\exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        openAction = QtGui.QAction(QtGui.QIcon('ico\open.png'), '&Open', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('open application')
        openAction.triggered.connect(self.openAction)
        saveAction = QtGui.QAction(QtGui.QIcon('ico\save.png'), '&Save', self)        
        saveAction.setShortcut('Ctrl+O')
        saveAction.setStatusTip('save application')
        saveAction.triggered.connect(self.saveAction)
        newAction = QtGui.QAction(QtGui.QIcon('ico\\new.png'), '&New', self)        
        newAction.setShortcut('Ctrl+O')
        newAction.setStatusTip('new application')
        newAction.triggered.connect(self.newAction)
        setAction = QtGui.QAction(QtGui.QIcon('ico\set.png'), '&Set', self)        
        setAction.setShortcut('Ctrl+O')
        setAction.setStatusTip('set application')
        setAction.triggered.connect(self.onsetAction)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        fileMenu.addAction(openAction)

        self.toolbar = self.addToolBar('open')
        self.toolbar.addAction(openAction)
        fileMenu.addAction(saveAction)

        self.toolbar = self.addToolBar('save')
        self.toolbar.addAction(saveAction)
        fileMenu.addAction(newAction)

        self.toolbar = self.addToolBar('new')
        self.toolbar.addAction(newAction)
        fileMenu.addAction(setAction)

        self.toolbar = self.addToolBar('set')
        self.toolbar.addAction(setAction)
       
        self.setGeometry(300, 300, 800, 600)
        self.statusBar().showMessage('Ready')
        self.setWindowTitle(_fromUtf8("窗口编辑"))
        self.setWindowIcon(QtGui.QIcon('ico.png'))
        self.show()
        self.center()
                
    def openAction(self):
        pkl_filename=QtGui.QFileDialog.getOpenFileName(self)
        pprint.pprint(pkl_filename)
        k="%s"%pkl_filename
        k=k[-4:]
        if cmp(k, '.pkl') == 0:
            pkl_file = open(pkl_filename, 'rb')
            Win_config1 = pickle.load(pkl_file)
            pprint.pprint(Win_config1)
            pkl_file.close()
            Win_id[0]=0
            Obj_id[0]=0
            QtCore.QObject.disconnect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.oncomboBox_2currentIndexChanged)
            self.comboBox_2.clear()
            QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.oncomboBox_2currentIndexChanged)
            for j in range(len(Win_list[Win_id[0]])):
                self.listWidget.takeItem(0)
            for win in range(len(Win_list)-1, -1, -1):
                Win_list.pop()
            pprint.pprint(Win_list)
            for win in range(len(Win_config1)):
                Win_list.append([])
                for obj in range(len(Win_config1[win])):
                    Win_list[win].append(QtGui.QPushButton(self))
                    Win_list[win][obj].setGeometry(
                    Win_config1[win][obj][0],
                    Win_config1[win][obj][1], 
                    Win_config1[win][obj][2], 
                    Win_config1[win][obj][3])
                    Win_list[win][obj].setStyleSheet("QWidget { background-color: %s }"% Win_config1[win][obj][4])    
                    Win_list[win][obj].setText(_translate("Dialog","%s"%Win_config1[win][obj][5], None))
            for i in range(len(Win_list[Win_id[0]])-1):
                    item = QtGui.QListWidgetItem()
                    self.listWidget.addItem(item)
                    item = self.listWidget.item(i)
                    item.setText(_translate("Dialog", "Button%s"%(i), None))
            for i in range(len(Win_list)):
                text="%s"%i
                self.comboBox_2.addItem(_fromUtf8(""))
                self.comboBox_2.setItemText(i, _translate("Dialog", text, None))
    def saveAction(self):
        pkl_filename=QtGui.QFileDialog.getSaveFileName(self)
        k="%s"%pkl_filename
        k=k[-4:]
        if cmp(k, '.pkl') == 0:
            pprint.pprint(Win_config)
            for win in range(len(Win_config)-1, -1, -1):
                Win_config.pop()
            pprint.pprint(Win_config)
            for win in range(len(Win_list)):
                    Win_config.append([])
                    for obj in range(len(Win_list[win])):
                        Win_config[win].append([])
                        Win_config[win][obj].append(Win_list[win][obj].x())
                        Win_config[win][obj].append(Win_list[win][obj].y())
                        Win_config[win][obj].append(Win_list[win][obj].width())
                        Win_config[win][obj].append(Win_list[win][obj].height())
                        Win_config[win][obj].append("%s"%Win_list[win][obj].palette().color(QtGui.QPalette.Background).name())
                        Win_config[win][obj].append("%s"%Win_list[win][obj].text())
            output = open(pkl_filename, 'wb')
            pickle.dump(Win_config, output)
            output.close()
    def newAction(self):
        a=[]
    def onsetAction(self):
        b=[]
    def onlistWidgetitemClicked(self, QListWidgetItem):
        self.spinBox_0.setValue(Win_list[Win_id[0]][Obj_id[0]].x()-10)
        self.spinBox_1.setValue(Win_list[Win_id[0]][Obj_id[0]].y()-100)
        self.spinBox_2.setValue(Win_list[Win_id[0]][Obj_id[0]].width())
        self.spinBox_3.setValue(Win_list[Win_id[0]][Obj_id[0]].height())
        Obj_id[0]=self.listWidget.row(QListWidgetItem)+1
        
    def oncomboBox_2currentIndexChanged(self, int):
        for Obj in Win_list[Win_id[0]]:
            Obj.setVisible(0)
        for j in range(len(Win_list[Win_id[0]])):
            self.listWidget.takeItem(0)
        Win_id[0]=self.comboBox_2.currentIndex()
        Obj_id[0]=0
        self.spinBox_0.setValue(Win_list[Win_id[0]][Obj_id[0]].x()-10)
        self.spinBox_1.setValue(Win_list[Win_id[0]][Obj_id[0]].y()-100)
        self.spinBox_2.setValue(Win_list[Win_id[0]][Obj_id[0]].width())
        self.spinBox_3.setValue(Win_list[Win_id[0]][Obj_id[0]].height())
        for i in range(len(Win_list[Win_id[0]])-1):
            item = QtGui.QListWidgetItem()
            self.listWidget.addItem(item)
            item = self.listWidget.item(i)
            item.setText(_translate("Dialog", "Button%s"%(i), None))
        for Obj in Win_list[Win_id[0]]:
            Obj.setVisible(1)
    def onpushButton_3Clicked(self):
        if self.comboBox.currentIndex()==0:
            Win_list[Win_id[0]][Obj_id[0]].pop()
        elif self.comboBox.currentIndex()==1:
            Win_list[Win_id[0]].pop()
            
            
    def onpushButton_2Clicked(self):
        if self.comboBox.currentIndex()==0:
            for j in range(len(Win_list[Win_id[0]])):
                self.listWidget.takeItem(0)
            Win_list[Win_id[0]].append(QtGui.QPushButton(self))
            Obj_id[0]=(len(Win_list[Win_id[0]])-1)
            Win_list[Win_id[0]][Obj_id[0]].setStyleSheet("QWidget { background-color: %s }"% col.name())
            if Obj_id[0]>1:
                Win_list[Win_id[0]][Obj_id[0]].setGeometry(
                    Win_list[Win_id[0]][Obj_id[0]-1].x(), 
                    Win_list[Win_id[0]][Obj_id[0]-1].y(), 
                    Win_list[Win_id[0]][Obj_id[0]-1].width(), 
                    Win_list[Win_id[0]][Obj_id[0]-1].height()
                )
            else:
                Win_list[Win_id[0]][Obj_id[0]].setGeometry(100, 200, 100, 100)
            self.spinBox_0.setValue(Win_list[Win_id[0]][Obj_id[0]].x()-10)
            self.spinBox_1.setValue(Win_list[Win_id[0]][Obj_id[0]].y()-100)
            self.spinBox_2.setValue(Win_list[Win_id[0]][Obj_id[0]].width())
            self.spinBox_3.setValue(Win_list[Win_id[0]][Obj_id[0]].height())
            for i in range(len(Win_list[Win_id[0]])-1):
                item = QtGui.QListWidgetItem()
                self.listWidget.addItem(item)
                item = self.listWidget.item(i)
                item.setText(_translate("Dialog", "Button%s"%(i), None))
            Win_list[Win_id[0]][Obj_id[0]].setVisible(1)
        elif self.comboBox.currentIndex()==1:
            for j in range(len(Win_list[Win_id[0]])):
                self.listWidget.takeItem(0)
            Win_list.append([])
            for Obj in Win_list[Win_id[0]]:
                Obj.setVisible(0)
            Win_id[0]=(len(Win_list)-1)
            Obj_id[0]=0
            Win_list[Win_id[0]].append(QtGui.QPushButton(self))
            Win_list[Win_id[0]][Obj_id[0]].setStyleSheet("QWidget { background-color: %s }"% col.name())
            Win_list[Win_id[0]][Obj_id[0]].setGeometry(10, 100, 240, 320)
            self.spinBox_0.setValue(Win_list[Win_id[0]][Obj_id[0]].x()-10)
            self.spinBox_1.setValue(Win_list[Win_id[0]][Obj_id[0]].y()-100)
            self.spinBox_2.setValue(Win_list[Win_id[0]][Obj_id[0]].width())
            self.spinBox_3.setValue(Win_list[Win_id[0]][Obj_id[0]].height())
            Win_list[Win_id[0]][Obj_id[0]].setVisible(1)
            self.comboBox_2.addItem(_fromUtf8(""))
            self.comboBox_2.setItemText(Win_id[0], _translate("Dialog", "%s"%Win_id[0], None))
            self.comboBox_2.setCurrentIndex(Win_id[0])
            for i in range(len(Win_list[Win_id[0]])-1):
                item = QtGui.QListWidgetItem()
                self.listWidget.addItem(item)
                item = self.listWidget.item(i)
                item.setText(_translate("Dialog", "Button%s"%(i), None))
    def onlineEdit_2Changed(self):
        Win_list[Win_id[0]][Obj_id[0]].setText(_translate("Dialog","%s"% (unicode(self.lineEdit_2.text())), None))
    def onspinBox_0Changed(self,int):    
        Win_list[Win_id[0]][Obj_id[0]].move(int+10, Win_list[Win_id[0]][Obj_id[0]].y())
    def onspinBox_1Changed(self, int):
        Win_list[Win_id[0]][Obj_id[0]].move(Win_list[Win_id[0]][Obj_id[0]].x(),int+100)
    def onspinBox_2Changed(self, int):
        Win_list[Win_id[0]][Obj_id[0]].resize(int, Win_list[Win_id[0]][Obj_id[0]].height())
    def onspinBox_3Changed(self, int):
        Win_list[Win_id[0]][Obj_id[0]].resize(Win_list[Win_id[0]][Obj_id[0]].width(), int)
    def onlineEditChanged(self):
        Win_list[Win_id[0]][Obj_id[0]].setStyleSheet("QWidget { background-color: #%s }"
                % (unicode(self.lineEdit.text())))
        
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        
    def showDialog(self):
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            Win_list[Win_id[0]][Obj_id[0]].setStyleSheet("QWidget { background-color: %s }"
                % col.name())
            text=_translate("Dialog", col.name(), None)
            self.lineEdit.setText("%s"%text[1:])
    def onpushButton_4Clicked(self):
        pkl_filename=QtGui.QFileDialog.getSaveFileName(self)
        k="%s"%pkl_filename
#        k=k[-4:]
        k=k[-11:]
        if cmp(k, 'UI_User.cpp') == 0:
            for i in range(len(Str_Code)):
                Str_Code.pop()
            FontCode=''
            
            Str_Code.append([])
            Str_Code.append([])
            Str_Code.append([])
            Str_Code[0].append("#include \"UI.h\"\n")
            Str_Code[2].append("void UI_Init(void){\n")
            for win in range(len(Win_list)):
                Str_Code[2].append("ui.add_window(&window%s);\n"%win)
                strcolor="%s"%(Win_list[win][0].palette().color(QtGui.QPalette.Background).name())
                numcolor=(int(strcolor[1:3], 16))/8*2048+(int(strcolor[3:5], 16))/4*32+(int(strcolor[5:7], 16))/8
                Str_Code[2].append("window%s.Set_BackColor(%s);\n"%(
                    win,
                    hex(numcolor)
                    ))
                Str_Code[2].append("window%s.Set_Rect(%s,%s,%s,%s);\n"%(
                    win,
                    (Win_list[win][0].x()-10),
                    (Win_list[win][0].y()-100),
                    Win_list[win][0].width(),
                    Win_list[win][0].height()
                    ))
                Str_Code[0].append("Window window%s(%s);\n"%(
                    win,
                    win))
                for obj in range(1, (len(Win_list[win]))):
                    Str_Code[2].append("window%s.add_button(&Button%s_%s);\n"%(
                        win,win,
                        obj
                        ))
                    Str_Code[2].append("Button%s_%s.rect.Set_Rect(%s,%s,%s,%s);\n"%(
                        win,obj,
                        (Win_list[win][obj].x()-10),
                        (Win_list[win][obj].y()-100),
                        Win_list[win][obj].width(),
                        Win_list[win][obj].height()
                        ))
                    strcolor="%s"%(Win_list[win][obj].palette().color(QtGui.QPalette.Background).name())
                    numcolor=(int(strcolor[1:3], 16))/8*2048+(int(strcolor[3:5], 16))/4*32+(int(strcolor[5:7], 16))/8
                    Str_Code[2].append("Button%s_%s.rect.Set_BackColor(%s);\n"%(
                        win,obj,
                        hex(numcolor)
                        ))
                    Str_Code[2].append("Button%s_%s.text.Set_Text((char *)\"%s\");\n"%(
                        win,obj,
                        unicode(Win_list[win][obj].text()).encode('gbk')
                        ))
                    pprint.pprint(unicode(Win_list[win][obj].text()).encode('gbk'))
                    print(unicode(Win_list[win][obj].text()).encode('utf-8'))
                    Str_Code[2].append("Button%s_%s.Set_Event(&Button%s_%s_Event);\n"%(
                        win,obj,win,obj))
                    Str_Code[0].append("Button Button%s_%s;\n"%(win,obj))
                    Str_Code[1].append("int Button%s_%s_Event(Event event){"%(win,obj))
                    Str_Code[1].append("if (event == release){window%s.Refresh();}return 0;}\n"%(win+1))
                    FontCode+=(unicode(Win_list[win][obj].text()))
            Str_Code[2].append("window0.Refresh();\n")
            Str_Code[2].append("}\n")
            
            file_object = open(pkl_filename, 'w')
            file_object.writelines(Str_Code[0])
            file_object.writelines(Str_Code[1])
            file_object.writelines(Str_Code[2])
            file_object.close()
            dot_matrix(FontCode)
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes: 
            event.accept()
        else:
            event.ignore()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
