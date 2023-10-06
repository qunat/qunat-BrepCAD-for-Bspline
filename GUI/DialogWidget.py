# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Process_message_word.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QLabel
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget,QTableWidget,QSpinBox,QTableWidgetItem,QDoubleSpinBox,QAbstractSpinBox


class DialogWidget(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(DialogWidget, self).__init__(parent)
		self.parent=parent
		self.setupUi()
		x = parent.geometry().x() + parent.geometry().width() / 4
		y = parent.geometry().y() + parent.geometry().height() / 4
		self.setGeometry(x, y, 150, 40)
		self.setWindowTitle('样条点设置')
		self.qdoubleSpinBox_valuechanged=False
		self.pushbutton_ok.clicked.connect(self.ok)
		self.pushbutton_cancel.clicked.connect(self.cancel)
		
		
	
	def setupUi(self):
		self.widget = QtWidgets.QWidget(self)
		#self.setMovable(False)
		#self.addWidget(self.widget)
		# self.setStyleSheet("background-color: rgb(14, 162, 185);")
		self.setCentralWidget(self.widget)
		HBOX = QVBoxLayout()
		HBOX_X=QVBoxLayout()
		HBOX_Y=QVBoxLayout()
		HBOX_Z=QVBoxLayout()

		HBOX_button = QHBoxLayout()
		self.widget.setLayout(HBOX)

		

		HBOX.addLayout(HBOX_X)
		HBOX.addLayout(HBOX_Y)
		HBOX.addLayout(HBOX_Z)
		HBOX.addLayout(HBOX_button)
		
		lab_x=QLabel("X")
		lab_y=QLabel("Y")
		lab_z=QLabel("Z")

		self.qdoubleSpinBox_x=QDoubleSpinBox()
		self.qdoubleSpinBox_y=QDoubleSpinBox()
		self.qdoubleSpinBox_z=QDoubleSpinBox()

		self.qdoubleSpinBox_x.setRange(-10000, 10000)
		self.qdoubleSpinBox_y.setRange(-10000, 10000)
		self.qdoubleSpinBox_z.setRange(-10000, 10000)

		HBOX_X.addWidget(lab_x,0, QtCore.Qt.AlignTop)
		HBOX_X.addWidget(self.qdoubleSpinBox_x,0, QtCore.Qt.AlignTop)
		HBOX_Y.addWidget(lab_y,0, QtCore.Qt.AlignTop)
		HBOX_Y.addWidget(self.qdoubleSpinBox_y,0, QtCore.Qt.AlignTop)
		HBOX_Z.addWidget(lab_z,0, QtCore.Qt.AlignTop)
		HBOX_Z.addWidget(self.qdoubleSpinBox_z,0, QtCore.Qt.AlignTop)
		
		
		
		
		self.pushbutton_ok=QtWidgets.QPushButton("确定")
		self.pushbutton_cancel = QtWidgets.QPushButton("取消")
		HBOX_button.addWidget(self.pushbutton_ok)
		HBOX_button.addWidget(self.pushbutton_cancel)
		self.parent.statusbar.showMessage("请选择草绘平面")

	def ok(self):
		#self.qdoubleSpinBox_x.valueChanged.disconnect()
		#self.parent.Sketcher.sketch_bspline.dialogWidget=None
		self.parent.Displayshape_core.canva.mouse_move_Signal.trigger.disconnect()
		self.close()
		
	def cancel(self):
		#self.qdoubleSpinBox_x.valueChanged.disconnect()
		#self.parent.Sketcher.sketch_bspline.dialogWidget=None
		self.parent.Displayshape_core.canva.mouse_move_Signal.trigger.disconnect()
		self.close()
		
		
	def Show(self):
		self.show()
