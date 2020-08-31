from PyQt4 import QtGui


def main():
    
    app = QtGui.QApplication()

    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    exit(app.exec_())


if __name__ == '__main__':
    main()