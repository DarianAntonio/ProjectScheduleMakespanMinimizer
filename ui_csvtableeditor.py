from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QToolBar,
    QVBoxLayout, QWidget)

class Ui_TableEditorMainWindow(object):
    def setupUi(self, TableEditorMainWindow):
        if not TableEditorMainWindow.objectName():
            TableEditorMainWindow.setObjectName(u"TableEditorMainWindow")
        TableEditorMainWindow.resize(1213, 795)
        TableEditorMainWindow.setAutoFillBackground(True)
        TableEditorMainWindow.setAnimated(False)
        TableEditorMainWindow.setDocumentMode(False)
        self.actionRedo = QAction(TableEditorMainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionUndo = QAction(TableEditorMainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionAddRow = QAction(TableEditorMainWindow)
        self.actionAddRow.setObjectName(u"actionAddRow")
        self.actionDelete_Row = QAction(TableEditorMainWindow)
        self.actionDelete_Row.setObjectName(u"actionDelete_Row")
        self.centralwidget = QWidget(TableEditorMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 0))
        self.label_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.label_2)

        self.RowLineEdit = QLineEdit(self.centralwidget)
        self.RowLineEdit.setObjectName(u"RowLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RowLineEdit.sizePolicy().hasHeightForWidth())
        self.RowLineEdit.setSizePolicy(sizePolicy)
        self.RowLineEdit.setMinimumSize(QSize(100, 0))
        self.RowLineEdit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.RowLineEdit)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 0))
        self.label_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.ColumnLineEdit = QLineEdit(self.centralwidget)
        self.ColumnLineEdit.setObjectName(u"ColumnLineEdit")
        sizePolicy.setHeightForWidth(self.ColumnLineEdit.sizePolicy().hasHeightForWidth())
        self.ColumnLineEdit.setSizePolicy(sizePolicy)
        self.ColumnLineEdit.setMinimumSize(QSize(100, 0))
        self.ColumnLineEdit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.ColumnLineEdit)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(120, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_3.addWidget(self.label)

        self.CSVsourceLineEdit = QLineEdit(self.centralwidget)
        self.CSVsourceLineEdit.setObjectName(u"CSVsourceLineEdit")
        sizePolicy.setHeightForWidth(self.CSVsourceLineEdit.sizePolicy().hasHeightForWidth())
        self.CSVsourceLineEdit.setSizePolicy(sizePolicy)
        self.CSVsourceLineEdit.setMinimumSize(QSize(150, 0))
        self.CSVsourceLineEdit.setMaximumSize(QSize(150, 16777215))
        self.CSVsourceLineEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.CSVsourceLineEdit)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.ChooseFileButton = QPushButton(self.centralwidget)
        self.ChooseFileButton.setObjectName(u"ChooseFileButton")
        self.ChooseFileButton.setMinimumSize(QSize(140, 0))
        self.ChooseFileButton.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_4.addWidget(self.ChooseFileButton)

        self.NewFileButton = QPushButton(self.centralwidget)
        self.NewFileButton.setObjectName(u"NewFileButton")
        self.NewFileButton.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_4.addWidget(self.NewFileButton)

        self.SaveFileButton = QPushButton(self.centralwidget)
        self.SaveFileButton.setObjectName(u"SaveFileButton")
        self.SaveFileButton.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_4.addWidget(self.SaveFileButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.CSVtableView = QTableView(self.centralwidget)
        self.CSVtableView.setObjectName(u"CSVtableView")
        self.CSVtableView.setAutoFillBackground(True)
        self.CSVtableView.setFrameShape(QFrame.WinPanel)
        self.CSVtableView.setAlternatingRowColors(False)
        self.CSVtableView.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.CSVtableView)

        TableEditorMainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(TableEditorMainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(True)
        self.toolBar.setFloatable(False)
        TableEditorMainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAddRow)
        self.toolBar.addAction(self.actionDelete_Row)
        self.toolBar.addSeparator()

        self.retranslateUi(TableEditorMainWindow)

        QMetaObject.connectSlotsByName(TableEditorMainWindow)
    # setupUi

    def retranslateUi(self, TableEditorMainWindow):
        TableEditorMainWindow.setWindowTitle(QCoreApplication.translate("TableEditorMainWindow", u"MainWindow", None))
        self.actionRedo.setText(QCoreApplication.translate("TableEditorMainWindow", u"Redo", None))
#if QT_CONFIG(tooltip)
        self.actionRedo.setToolTip(QCoreApplication.translate("TableEditorMainWindow", u"Redo", None))
#endif // QT_CONFIG(tooltip)
        self.actionUndo.setText(QCoreApplication.translate("TableEditorMainWindow", u"Undo", None))
#if QT_CONFIG(tooltip)
        self.actionUndo.setToolTip(QCoreApplication.translate("TableEditorMainWindow", u"Undo", None))
#endif // QT_CONFIG(tooltip)
        self.actionAddRow.setText(QCoreApplication.translate("TableEditorMainWindow", u"Add Row", None))
        self.actionDelete_Row.setText(QCoreApplication.translate("TableEditorMainWindow", u"Delete Row", None))
#if QT_CONFIG(tooltip)
        self.actionDelete_Row.setToolTip(QCoreApplication.translate("TableEditorMainWindow", u"Delete Row", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("TableEditorMainWindow", u"Row:", None))
        self.label_3.setText(QCoreApplication.translate("TableEditorMainWindow", u"Column:", None))
        self.label.setText(QCoreApplication.translate("TableEditorMainWindow", u"CSV Source:", None))
        self.ChooseFileButton.setText(QCoreApplication.translate("TableEditorMainWindow", u"Choose File", None))
        self.NewFileButton.setText(QCoreApplication.translate("TableEditorMainWindow", u"New File", None))
        self.SaveFileButton.setText(QCoreApplication.translate("TableEditorMainWindow", u"Save File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("TableEditorMainWindow", u"toolBar", None))
    # retranslateUi

