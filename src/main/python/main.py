from fbs_runtime.application_context.PySide2 import ApplicationContext
import sys
# from package.main_window import MainWindow
from package.main_window import Window, MainWindow

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    # window = MainWindow()
    window = Window(ctx=appctxt)
    # window.resize(650, 550)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)