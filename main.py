import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from layout import Ui_Form

class ProgramNama(Ui_Form):
	def __init__(self, dialog):
		Ui_Form.__init__(self)
		self.setupUi(dialog)
		self.pushButtonSimpan.clicked.connect(self.UpdateProfile)
		
	def UpdateProfile(self):
		valuenama = self.lineEditNama.text()
		self.labelNama.setText(valuenama)
		self.lineEditNama.clear()
		
		valueriset = self.lineEditRiset.text()
		self.lineEditRiset.clear()
		self.labelRiset.setText(valueriset)
		
		valuealamat = self.lineEditAlamat.text()
		self.lineEditAlamat.clear()
		self.labelAlamat.setText(valuealamat)

		
if __name__=='__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()
	
	prog = ProgramNama(dialog)
	
	dialog.show()
	sys.exit(app.exec_())