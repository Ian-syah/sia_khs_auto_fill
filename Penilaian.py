# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Penilaianui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import rc.logounmul_rc


class Ui_Dialog(object):
    
    def __init__(self):
        
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(537, 280)
        self.closeBtn = QtWidgets.QDialogButtonBox(self.Dialog)
        self.closeBtn.setGeometry(QtCore.QRect(450, 240, 81, 32))
        self.closeBtn.setMouseTracking(True)
        self.closeBtn.setTabletTracking(True)
        self.closeBtn.setOrientation(QtCore.Qt.Horizontal)
        self.closeBtn.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.closeBtn.setCenterButtons(False)
        self.closeBtn.setObjectName("closeBtn")
        self.imgUnmul = QtWidgets.QLabel(self.Dialog)
        self.imgUnmul.setGeometry(QtCore.QRect(10, 30, 191, 191))
        self.imgUnmul.setText("")
        self.imgUnmul.setTextFormat(QtCore.Qt.AutoText)
        self.imgUnmul.setPixmap(QtGui.QPixmap(":/logoUnmul/assets/logoUnmul.png"))
        self.imgUnmul.setScaledContents(True)
        self.imgUnmul.setObjectName("imgUnmul")
        self.title = QtWidgets.QLabel(self.Dialog)
        self.title.setGeometry(QtCore.QRect(210, 30, 111, 31))
        self.title.setObjectName("title")
        self.label_1 = QtWidgets.QLabel(self.Dialog)
        self.label_1.setGeometry(QtCore.QRect(180, 60, 331, 51))
        self.label_1.setWordWrap(True)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 120, 341, 51))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 180, 331, 51))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi()
        self.closeBtn.accepted.connect(self.Dialog.accept)
        self.closeBtn.rejected.connect(self.Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Penilaian</span></p></body></html>"))
        self.label_1.setText(_translate("Dialog", "<html><head/><body><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Penilaian pada kuesioner bisa dipilih lebih dari satu</span></li></ul></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Nilai-nilai yang dipilih akan diacak saat pengisian kuesioner</span></li></ul></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Bagian saran pada kuesioner akan dikosongkan</span></li></ul></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.Dialog.show()
    sys.exit(app.exec_())
