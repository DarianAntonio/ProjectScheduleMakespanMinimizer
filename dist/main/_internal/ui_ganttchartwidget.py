from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_GanttChartWidget(object):
    def setupUi(self, GanttChartWidget):
        if not GanttChartWidget.objectName():
            GanttChartWidget.setObjectName(u"GanttChartWidget")
        GanttChartWidget.resize(555, 346)
        self.verticalLayout = QVBoxLayout(GanttChartWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(GanttChartWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.ViewComboBox = QComboBox(GanttChartWidget)
        self.ViewComboBox.addItem("")
        self.ViewComboBox.setObjectName(u"ViewComboBox")

        self.horizontalLayout.addWidget(self.ViewComboBox)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.GraphLayout = QHBoxLayout()
        self.GraphLayout.setObjectName(u"GraphLayout")

        self.verticalLayout.addLayout(self.GraphLayout)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(GanttChartWidget)

        QMetaObject.connectSlotsByName(GanttChartWidget)
    # setupUi

    def retranslateUi(self, GanttChartWidget):
        GanttChartWidget.setWindowTitle(QCoreApplication.translate("GanttChartWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("GanttChartWidget", u"View:", None))
        self.ViewComboBox.setItemText(0, QCoreApplication.translate("GanttChartWidget", u"Overall View", None))

    # retranslateUi

