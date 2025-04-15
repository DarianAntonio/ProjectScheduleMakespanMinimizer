from PySide6.QtWidgets import QApplication, QWidget, QTabWidget
import sys
from ui import MainWindow

app = QApplication(sys.argv)
window = MainWindow(app)

try:
    from qt_material import apply_stylesheet
    extra = {
        'density_scale': '-1',
    }
    apply_stylesheet(app, 'default',extra=extra)
except:
    pass

window.show()

app.exec()