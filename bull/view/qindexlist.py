﻿#!/usr/bin/python  
#-*-coding:utf-8-*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore  
from qlistitem import QListItem

class QIndexList(QtGui.QWidget):
    def __init__(self,parent,title,index_list,image_list):
        super(QIndexList,self).__init__(parent)
        self.title = title
        self.index_list = index_list
        self.image_list = image_list
        self.button_list = []
        self.selected_index = 0
        self.initUI()
        
        
    def initUI(self):
        self.title_label = QtGui.QLabel(self.title,self)
        self.title_label.setStyleSheet('font-weight: bold;padding-bottom: 20px;border-right: 1px solid #ccc;')
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.title_label)
        #init ui
        for i in range(len(self.index_list)):
            print(i)
            list_item = QListItem(self,
                                  self.index_list[i],
                                  self.image_list[i],
                                  i)
            self.connect(list_item,
                         QtCore.SIGNAL('clicked(int)'),
                         self.on_nth_btn_press)
            self.button_list.append(list_item)
            vbox.addWidget(list_item)
        self.setLayout(vbox)
        self.resetStyleSheet()

    def resetStyleSheet(self):
        for i in range(len(self.index_list)):
            if i==self.selected_index:
                self.button_list[i].setStyleSheet("""
                .QListItem{
                    border: 1px solid #ccc;
                    border-right: none;
                    background: #ffffff;
                    border-top-left-radius: 5px;
                    border-bottom-left-radius: 5px;
                    }
                    """)
            else:
                self.button_list[i].setStyleSheet("""
                .QListItem{
                    border-right: 1px solid #ccc;
                    }
                    """)

    def on_nth_btn_press(self,id):
         self.selected_index = id
         self.resetStyleSheet()

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        title = u'条件设置'
        index_list = [u'基本指标',u'我的收藏']
        image_list = [
            QtGui.QImage('../images/icon_menu_stock_filter_1.png'),
            QtGui.QImage('../images/icon_menu_stock_filter_2.png')]
        self.index_list = QIndexList(self,title,index_list,image_list)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.index_list)
        self.setLayout(hbox)
        self.setStyleSheet('font-size:14px')

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()