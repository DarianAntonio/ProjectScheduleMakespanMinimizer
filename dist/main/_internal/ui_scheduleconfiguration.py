from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_ScheduleConfigWidget(object):
    def setupUi(self, ScheduleConfigWidget):
        if not ScheduleConfigWidget.objectName():
            ScheduleConfigWidget.setObjectName(u"ScheduleConfigWidget")
        ScheduleConfigWidget.resize(552, 348)
        self.verticalLayout = QVBoxLayout(ScheduleConfigWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(ScheduleConfigWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setUsesScrollButtons(False)

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(ScheduleConfigWidget)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(ScheduleConfigWidget)
    # setupUi

    def retranslateUi(self, ScheduleConfigWidget):
        ScheduleConfigWidget.setWindowTitle(QCoreApplication.translate("ScheduleConfigWidget", u"Form", None))
    # retranslateUi

