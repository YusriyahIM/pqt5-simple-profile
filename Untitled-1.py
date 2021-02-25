        #119
        self.pushButtonSimpan.clicked.connect(self.addItem)
        self.selectImageBtn.clicked.connect(self.setImage)

    #134
    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image","", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.imageLbl.width(), self.ImageLbl.height(), QtCore.Qt.KeepAspectRatio)
            self.ImageLbl.setPixmap(pixmap)
            self.ImageLbl.setAlignment(QtCore.Qt.AlignCenter)

    def addItem(self):
        value = self.lineEditNama.text()
        self.lineEditNama.clear()
        self.labelNama.addItem(value)
        value = self.lineEditRiset.text()
        self.lineEditRiset.clear()
        self.labelRiset.addItem(value)
        value = self.lineEditAlamat.text()
        self.lineEditAlamat.clear()
        self.labelAlamat.addItem(value)


    def setImage(self):
		fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image","", "Image Files (*.png *.jpg *.jpeg *.bmp)")
		if fileName:
			pixmap = QtGui.QPixmap(fileName)
			pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio)
			self.imageLbl.setPixmap(pixmap)
			self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)