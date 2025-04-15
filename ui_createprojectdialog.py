from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_create_project_dialog(object):
    def setupUi(self, create_project_dialog):
        if not create_project_dialog.objectName():
            create_project_dialog.setObjectName(u"create_project_dialog")
        create_project_dialog.resize(549, 131)
        self.verticalLayout = QVBoxLayout(create_project_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(create_project_dialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.label)

        self.directory_line_edit = QLineEdit(create_project_dialog)
        self.directory_line_edit.setObjectName(u"directory_line_edit")

        self.horizontalLayout.addWidget(self.directory_line_edit)

        self.directory_button = QPushButton(create_project_dialog)
        self.directory_button.setObjectName(u"directory_button")

        self.horizontalLayout.addWidget(self.directory_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(create_project_dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.project_name_line_edit = QLineEdit(create_project_dialog)
        self.project_name_line_edit.setObjectName(u"project_name_line_edit")

        self.horizontalLayout_2.addWidget(self.project_name_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.confirm_button = QPushButton(create_project_dialog)
        self.confirm_button.setObjectName(u"confirm_button")

        self.horizontalLayout_3.addWidget(self.confirm_button)

        self.cancel_button = QPushButton(create_project_dialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_3.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(create_project_dialog)

        QMetaObject.connectSlotsByName(create_project_dialog)
    # setupUi

    def retranslateUi(self, create_project_dialog):
        create_project_dialog.setWindowTitle(QCoreApplication.translate("create_project_dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("create_project_dialog", u"Directory:", None))
        self.directory_button.setText(QCoreApplication.translate("create_project_dialog", u"Choose Directory", None))
        self.label_2.setText(QCoreApplication.translate("create_project_dialog", u"Project Name:", None))
        self.confirm_button.setText(QCoreApplication.translate("create_project_dialog", u"Confirm", None))
        self.cancel_button.setText(QCoreApplication.translate("create_project_dialog", u"Cancel", None))
    # retranslateUi

