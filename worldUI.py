from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPixmap


class Form(QGraphicsItem):
    def __init__(self):
        super(Form,self).__init__()
        self.karel=None
        self.size = 50 # size of rec
        self.count=11 # # of recs in the row and col of karel world
        self.bound=550

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None):
        QPainter.setPen(Qt.black)
        for i in range(1, self.count+1):
            QPainter.drawLine(0, self.size * i, self.bound , self.size * i)
            QPainter.drawLine(self.size * i, 0, self.size * i, self.bound)

        self.karel=QPixmap("karel.png")
        QPainter.drawPixmap(5,505,40,40,self.karel) # load karel image

    def boundingRect(self):
        return QRectF(0,0,self.bound,self.bound)

class MainWindow(QGraphicsView):
    def __init__(self):
        super(MainWindow, self).__init__()
        scene = QGraphicsScene(self)
        self.form = Form()
        scene.addItem(self.form)
        scene.setSceneRect(0, 0, 550,550)
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setWindowTitle("Karel World")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
