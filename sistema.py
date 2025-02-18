# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sistema.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from configparser import Interpolation
from PyQt5 import QtCore, QtGui, QtWidgets

# Imports
import cv2
import numpy as np
from PIL import Image
from PyQt5.QtGui import QPixmap, QImage


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 696)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_Iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Iniciar.setGeometry(QtCore.QRect(0, 0, 191, 101))
        self.bt_Iniciar.setObjectName("bt_Iniciar")
        self.bt_botao2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_botao2.setGeometry(QtCore.QRect(190, 0, 191, 101))
        self.bt_botao2.setObjectName("bt_botao2")
        self.bt_sair = QtWidgets.QPushButton(self.centralwidget)
        self.bt_sair.setGeometry(QtCore.QRect(760, 0, 191, 101))
        self.bt_sair.setObjectName("bt_sair")
        self.lb_video1 = QtWidgets.QLabel(self.centralwidget)
        self.lb_video1.setGeometry(QtCore.QRect(50, 220, 400, 400))
        self.lb_video1.setText("")
        self.lb_video1.setObjectName("lb_video1")
        self.lb_video2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_video2.setGeometry(QtCore.QRect(490, 220, 400, 400))
        self.lb_video2.setText("")
        self.lb_video2.setObjectName("lb_video2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(460, 210, 21, 421))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lb_txtVideoOriginal = QtWidgets.QLabel(self.centralwidget)
        self.lb_txtVideoOriginal.setGeometry(QtCore.QRect(180, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lb_txtVideoOriginal.setFont(font)
        self.lb_txtVideoOriginal.setObjectName("lb_txtVideoOriginal")
        self.lb_txtVideoEfeito = QtWidgets.QLabel(self.centralwidget)
        self.lb_txtVideoEfeito.setGeometry(QtCore.QRect(640, 180, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lb_txtVideoEfeito.setFont(font)
        self.lb_txtVideoEfeito.setObjectName("lb_txtVideoEfeito")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 130, 871, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rb_semEfeito = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_semEfeito.setObjectName("rb_semEfeito")
        self.horizontalLayout.addWidget(self.rb_semEfeito)
        self.rb_bilateral = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_bilateral.setObjectName("rb_bilateral")
        self.horizontalLayout.addWidget(self.rb_bilateral)
        self.rb_oil = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_oil.setObjectName("rb_oil")
        self.horizontalLayout.addWidget(self.rb_oil)
        self.rb_cartoom = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_cartoom.setObjectName("rb_cartoom")
        self.horizontalLayout.addWidget(self.rb_cartoom)
        self.rb_colored = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_colored.setObjectName("rb_colored")
        self.horizontalLayout.addWidget(self.rb_colored)
        self.rb_onlyBlue = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_onlyBlue.setObjectName("rb_onlyBlue")
        self.horizontalLayout.addWidget(self.rb_onlyBlue)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_Iniciar.setText(_translate("MainWindow", "Iniciar reprodução"))
        self.bt_botao2.setText(_translate("MainWindow", "botão2"))
        self.bt_sair.setText(_translate("MainWindow", "Sair"))
        self.lb_txtVideoOriginal.setText(_translate("MainWindow", "Vídeo original"))
        self.lb_txtVideoEfeito.setText(_translate("MainWindow", "Vídeo com efeito"))
        self.rb_semEfeito.setText(_translate("MainWindow", "Sem Efeito"))
        self.rb_bilateral.setText(_translate("MainWindow", "Bilateral"))
        self.rb_oil.setText(_translate("MainWindow", "Oil"))
        self.rb_cartoom.setText(_translate("MainWindow", "Cartoom"))
        self.rb_colored.setText(_translate("MainWindow", "Colored"))
        self.rb_onlyBlue.setText(_translate("MainWindow", "onlyBlue"))


        ### Botões do Sistema ###
        self.bt_sair.clicked.connect(self.sair)
        self.bt_Iniciar.clicked.connect(self.camera)


    ### Funções do Sistema ###
    ## Sair do sistema ##
    def sair(self):
        sys.exit()

    ## Conexão e filtros com a webcam ##
    def camera(self):
        cap = cv2.VideoCapture(0)
        contArea = 0
        while(True):
            ret, frame = cap.read()
            print('Original dimension: ', frame.shape)
            # Redimensionamento de imagem 400 x 400
            scale_percent_height = 83.35 # percent of original size
            scale_percent_width = 62.5 # percent of original size
            height = int(frame.shape[0] * scale_percent_height / 100)
            width = int(frame.shape[1] * scale_percent_width / 100)
            dim = (height, width)
            resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
            # Transform frame to qImg
            height, width, channel = resized.shape
            bytesPerLine = 3 * width
            qImg = QImage(resized.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            # loading image
            self.pixmap = QPixmap(qImg)
            # Mostrar frames
            print('Resized dimension: ', resized.shape)
            self.lb_video1.setPixmap(self.pixmap)
            cv2.imshow('frame', frame)

            # Recupera botão pressionado
            key = cv2.waitKey(1)
            # Close loop
            if key == ord('c'):
                break
        # Fechar o serviço da webcam e "destroi" o sistema
        cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
