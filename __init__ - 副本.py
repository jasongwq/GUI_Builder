#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 
import pprint, pickle
from PyQt4 import QtCore,QtGui


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
        self.pushButton = QtGui.QPushButton(_fromUtf8("颜色"), self)
        self.pushButton.clicked.connect(self.showDialog)
        self.frame = QtGui.QFrame(self)
#        kk=QtGui.QFileDialog.getOpenFileName(self)
#        pprint.pprint(kk)
        
        Win_list[0].append(self.frame);
        self.frame.setStyleSheet("QWidget { background-color: %s }" 
            % col.name())
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(10)        
       
        self.label_0 = QtGui.QLabel(self)
        self.label_1 = QtGui.QLabel(self)
        self.label_2 = QtGui.QLabel(self)
        self.label_3 = QtGui.QLabel(self)
        
        self.spinBox_0 = QtGui.QSpinBox(self)
        self.spinBox_1 = QtGui.QSpinBox(self)
        self.spinBox_2 = QtGui.QSpinBox(self)
        self.spinBox_3 = QtGui.QSpinBox(self)
        
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
#        self.validator = QtGui.QIntValidator( 0,0xffffff,self);
        #// 只允许 edit 输入整数 100 到 999
        #self.lineEdit.setValidator(self.validator);
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 7, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 7, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 7, 2, 1, 1)
        
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
        self.gridLayout.addWidget(self.listWidget, 5, 2, 1, 1)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.onlineEditChanged)
        QtCore.QObject.connect(self.spinBox_0, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.onspinBox_0Changed)
        QtCore.QObject.connect(self.spinBox_1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.onspinBox_1Changed)
        QtCore.QObject.connect(self.spinBox_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.onspinBox_2Changed)
        QtCore.QObject.connect(self.spinBox_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.onspinBox_3Changed)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onpushButton_2Clicked)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onpushButton_4Clicked)
#        QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.oncomboBox_2currentIndexChanged)
        QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.oncomboBox_2currentIndexChanged)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), self.onlistWidgetitemClicked)
        
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
        
        self.frame.setGeometry(10, 100, 100, 100)
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.label_0, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.label_1, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.spinBox_0, 1, 2, 1, 1)
        self.spinBox_0.setMaximum(999)
        self.gridLayout.addWidget(self.spinBox_1, 2, 2, 1, 1)
        self.spinBox_1.setMaximum(999)
        self.gridLayout.addWidget(self.spinBox_2, 3, 2, 1, 1)
        self.spinBox_2.setMaximum(999)
        self.gridLayout.addWidget(self.spinBox_3, 4, 2, 1, 1)
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
        if pkl_filename != '':
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
                for obj in range(len(Win_list[win])):
                    Win_list[win].pop()
                Win_list.pop()
            for win in range(len(Win_config1)):
                Win_list.append([])
                for obj in range(len(Win_config1[win])):
                    Win_list[win].append(QtGui.QFrame(self))
                    Win_list[win][obj].setGeometry(
                    Win_config1[win][obj][0],
                    Win_config1[win][obj][1], 
                    Win_config1[win][obj][2], 
                    Win_config1[win][obj][3])
                    Win_list[win][obj].setStyleSheet("QWidget { background-color: %s }"% Win_config1[win][obj][4])    
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
        if pkl_filename != '':
            for win in range(len(Win_list)):
                    if win>0:
                        Win_config.append([])
                    for obj in range(len(Win_list[win])):
                        if obj>0 or win>0:
                            Win_config[win].append([])
                        Win_config[win][obj].append(Win_list[win][obj].x())
                        Win_config[win][obj].append(Win_list[win][obj].y())
                        Win_config[win][obj].append(Win_list[win][obj].width())
                        Win_config[win][obj].append(Win_list[win][obj].height())
                        Win_config[win][obj].append("%s"%Win_list[win][obj].palette().color(QtGui.QPalette.Background).name())
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
    def onpushButton_2Clicked(self):
        if self.comboBox.currentIndex()==0:
            for j in range(len(Win_list[Win_id[0]])):
                self.listWidget.takeItem(0)
            Win_list[Win_id[0]].append(QtGui.QFrame(self))
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
            Win_list[Win_id[0]].append(QtGui.QFrame(self))
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
    def onspinBox_0Changed(self, int):
        Win_list[Win_id[0]][Obj_id[0]].move(int+10, Win_list[Win_id[0]][Obj_id[0]].y())
    def onspinBox_1Changed(self, int):
        Win_list[Win_id[0]][Obj_id[0]].move(Win_list[Win_id[0]][Obj_id[0]].x(),int+100)
    def onspinBox_2Changed(self, int):
        Win_list[Win_id[0]][Obj_id[0]].resize(int, Win_list[Win_id[0]][Obj_id[0]].height())
    def onspinBox_3Changed(self, int):
        Win_list[Win_id[0]][Obj_id[0]].resize(Win_list[Win_id[0]][Obj_id[0]].width(), int)
    def onlineEditChanged(self):
        self.frame.setStyleSheet("QWidget { background-color: #%s }"
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
        if pkl_filename != '':
            Str_Code.append([])
            Str_Code.append([])
            Str_Code[0].append("#include \"UI.h\"\n")
            Str_Code[2].append("void UI_Init(void){\n")
            for win in range(len(Win_list)):
                Str_Code[2].append("ui.add_window(&window%s);\n"%win)
                strcolor="%s"%(Win_list[win][0].palette().color(QtGui.QPalette.Background).name())
                numcolor=(int(strcolor[1:3], 16))/4*2048+(int(strcolor[3:5], 16))/8*32+(int(strcolor[5:7], 16))/4
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
                    Str_Code[2].append("Button%s_%s.text.Set_Text((char *)\"%s\");\n"%(
                        win,obj,
                        "ceshi"
                        ))
                    Str_Code[2].append("Button%s_%s.Set_Event(&Button%s_%s_Event);\n"%(
                        win,obj,win,obj))
                    Str_Code[0].append("Button Button%s_%s;\n"%(win,obj))
                    Str_Code[1].append("int Button%s_%s_Event(Event event){\n"%(win,obj))
                    Str_Code[1].append("if (event == press){window%s.Refresh();}return 0;}\n"%win)
            Str_Code[2].append("}\n")
            file_object = open(pkl_filename, 'w')
            file_object.writelines(Str_Code[0])
            file_object.writelines(Str_Code[1])
            file_object.writelines(Str_Code[2])
            file_object.close()
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
