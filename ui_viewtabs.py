from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_viewtabs_widget(object):
    def setupUi(self, viewtabs_widget):
        if not viewtabs_widget.objectName():
            viewtabs_widget.setObjectName(u"viewtabs_widget")
        viewtabs_widget.resize(700, 570)
        self.verticalLayout = QVBoxLayout(viewtabs_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(viewtabs_widget)
        self.tabWidget.setObjectName(u"tabWidget")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(viewtabs_widget)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(viewtabs_widget)
    # setupUi

    def retranslateUi(self, viewtabs_widget):
        viewtabs_widget.setWindowTitle(QCoreApplication.translate("viewtabs_widget", u"Form", None))
    # retranslateUi

