from PySide2 import QtWidgets
import sys
from package.main_window import Window

if __name__ == '__main__':
    appctxt = QtWidgets.QApplication(sys.argv)     # 1. Instantiate ApplicationContext
    window = Window(ctx=appctxt)
    window.show()
    exit_code = appctxt.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
