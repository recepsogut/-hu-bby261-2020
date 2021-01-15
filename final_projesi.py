from PyQt4.QtGui import *
from PyQt4.QtCore import *

class yakitHesaplayicisi(QDialog):
    def _init_(self, ebeveyn=None):
        super(yakitHesaplayicisi, self).__init__(ebeveyn)
        
        grid=QGridLayout()
        grid.addWidget(QLabel('Gideceğiniz yol (KM): '),0,0)
        self.gidilenYol=QLineEdit()
        self.gidilenYol.setInputMask('0000000000')
        grid.addWidget(self.gidilenYol,0,1)
        
        grid.addWidget(QLabel('Yakıtın Litre Fiyatı'),1,0)
        self.yakitFiyati=QLineEdit()
        self.yakitFiyati.setInputMask('0.00')
        grid.addWidget(self.yakitFiyati,1,1)
        
        grid.addWidget(QLabel("100 Km'de Tüketilen Yakıt: "),2,0)
        self.yakitTuketimi=QLineEdit()
        self.yakitTuketimi.setInputMask('00.0')
        grid.addWidget(self.yakitTuketimi, 2,1)
        
        grid.addWidget(QLabel('Toplam Tutar: '),3,0)
        self.tutar=QLabel('<i>KM GİRİNİZ</i>')
        grid.addWidget(self.tutar,3,1)
        
        hedaplaDugme=QPushButton('Hesapla')
        self.connect(hedaplaDugme, SIGNAL('pressed()'), self.yakitHesapla)
        grid.addWidget(hedaplaDugme,4,0,1,2)
        
        self.setLayout(grid)
        self.setWindowTitle('Yakıt Hesaplayıcısı')
        
    def yakitHesapla(self):
        yol=0
        try: yol=int(self.gidilenYol.text())
        except: pass
        fiyat=0
        try: fiyat=float(self.yakitFiyati.text())
        except: pass
        tuketim=0
        try: tuketim=float(self.yakitTuketimi.text())
        except: pass
        
        if not yol:
            self.tutar.setText('<font color="red"><i>KM giriniz</i></font>')
            self.gidilenYol.setFocus()
        elif not fiyat:
                self.tutar.setText('<font color="red"><i>Fiyat giriniz</i></font>')
                self.yakitFiyati.setFocus()
        elif not tuketim:
                self.tutar.setText('<font color="red"><i>Tüketim giriniz</i></font>')
                self.yakitTuketimi.setFocus()
        else:
                    tutar=fiyat*(yol*tuketim)/100
                    self.tutar.setText('<font color="blue"><b>%0.2f</b> TL</font>' % tutar)
uyg=QApplication([])
pencere=yakitHesaplayicisi()
pencere.show()
uyg.exec_(