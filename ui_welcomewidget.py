from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_welcome_widget(object):
    def setupUi(self, welcome_widget):
        if not welcome_widget.objectName():
            welcome_widget.setObjectName(u"welcome_widget")
        welcome_widget.resize(739, 843)
        self.verticalLayout_3 = QVBoxLayout(welcome_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_1 = QLabel(welcome_widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)

        self.verticalLayout_3.addWidget(self.label_1)

        self.label_2 = QLabel(welcome_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.create_project_button = QPushButton(welcome_widget)
        self.create_project_button.setObjectName(u"create_project_button")
        font2 = QFont()
        font2.setPointSize(11)
        self.create_project_button.setFont(font2)

        self.verticalLayout_2.addWidget(self.create_project_button)

        self.open_project_button = QPushButton(welcome_widget)
        self.open_project_button.setObjectName(u"open_project_button")
        self.open_project_button.setMinimumSize(QSize(150, 0))
        self.open_project_button.setFont(font2)

        self.verticalLayout_2.addWidget(self.open_project_button)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 266, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(welcome_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setFont(font2)

        self.verticalLayout.addWidget(self.label_3)

        self.recent_projects_list_view = QListView(welcome_widget)
        self.recent_projects_list_view.setObjectName(u"recent_projects_list_view")
        self.recent_projects_list_view.setMinimumSize(QSize(0, 200))
        self.recent_projects_list_view.setMaximumSize(QSize(16777215, 700))
        self.recent_projects_list_view.setFont(font2)
        self.recent_projects_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout.addWidget(self.recent_projects_list_view)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(welcome_widget)

        QMetaObject.connectSlotsByName(welcome_widget)
    # setupUi

    def retranslateUi(self, welcome_widget):
        welcome_widget.setWindowTitle(QCoreApplication.translate("welcome_widget", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("welcome_widget", u"Project Schedulling Program", None))
        self.label_2.setText(QCoreApplication.translate("welcome_widget", u"Welcome:", None))
        self.create_project_button.setText(QCoreApplication.translate("welcome_widget", u"Create New Project", None))
        self.open_project_button.setText(QCoreApplication.translate("welcome_widget", u"Open Project", None))
        self.label_3.setText(QCoreApplication.translate("welcome_widget", u"Recent Projects:", None))
    # retranslateUi

