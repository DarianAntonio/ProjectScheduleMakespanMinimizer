from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTimeEdit, QVBoxLayout, QWidget)

class Ui_AlgorithmControlWidget(object):
    def setupUi(self, AlgorithmControlWidget):
        if not AlgorithmControlWidget.objectName():
            AlgorithmControlWidget.setObjectName(u"AlgorithmControlWidget")
        AlgorithmControlWidget.resize(751, 870)
        self.verticalLayout_4 = QVBoxLayout(AlgorithmControlWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.line = QFrame(AlgorithmControlWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)

        self.label = QLabel(AlgorithmControlWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_13.addWidget(self.label)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.label_2 = QLabel(AlgorithmControlWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_11.addWidget(self.label_2)

        self.PopulationSizeLineEdit = QLineEdit(AlgorithmControlWidget)
        self.PopulationSizeLineEdit.setObjectName(u"PopulationSizeLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PopulationSizeLineEdit.sizePolicy().hasHeightForWidth())
        self.PopulationSizeLineEdit.setSizePolicy(sizePolicy)
        self.PopulationSizeLineEdit.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_11.addWidget(self.PopulationSizeLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.label_3 = QLabel(AlgorithmControlWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.label_3)

        self.MutationRateLineEdit = QLineEdit(AlgorithmControlWidget)
        self.MutationRateLineEdit.setObjectName(u"MutationRateLineEdit")
        sizePolicy.setHeightForWidth(self.MutationRateLineEdit.sizePolicy().hasHeightForWidth())
        self.MutationRateLineEdit.setSizePolicy(sizePolicy)
        self.MutationRateLineEdit.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_6.addWidget(self.MutationRateLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_4 = QLabel(AlgorithmControlWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.CrossoverRateLineEdit = QLineEdit(AlgorithmControlWidget)
        self.CrossoverRateLineEdit.setObjectName(u"CrossoverRateLineEdit")
        sizePolicy.setHeightForWidth(self.CrossoverRateLineEdit.sizePolicy().hasHeightForWidth())
        self.CrossoverRateLineEdit.setSizePolicy(sizePolicy)
        self.CrossoverRateLineEdit.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_5.addWidget(self.CrossoverRateLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.ResetButton = QPushButton(AlgorithmControlWidget)
        self.ResetButton.setObjectName(u"ResetButton")

        self.horizontalLayout_3.addWidget(self.ResetButton)

        self.StartButton = QPushButton(AlgorithmControlWidget)
        self.StartButton.setObjectName(u"StartButton")

        self.horizontalLayout_3.addWidget(self.StartButton)

        self.PauseButton = QPushButton(AlgorithmControlWidget)
        self.PauseButton.setObjectName(u"PauseButton")

        self.horizontalLayout_3.addWidget(self.PauseButton)

        self.StopButton = QPushButton(AlgorithmControlWidget)
        self.StopButton.setObjectName(u"StopButton")

        self.horizontalLayout_3.addWidget(self.StopButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_7 = QLabel(AlgorithmControlWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.label_7)

        self.MakespanLineEdit = QLineEdit(AlgorithmControlWidget)
        self.MakespanLineEdit.setObjectName(u"MakespanLineEdit")
        sizePolicy.setHeightForWidth(self.MakespanLineEdit.sizePolicy().hasHeightForWidth())
        self.MakespanLineEdit.setSizePolicy(sizePolicy)
        self.MakespanLineEdit.setMinimumSize(QSize(180, 0))
        self.MakespanLineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.MakespanLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_6 = QLabel(AlgorithmControlWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.label_6)

        self.GenerationLineEdit = QLineEdit(AlgorithmControlWidget)
        self.GenerationLineEdit.setObjectName(u"GenerationLineEdit")
        sizePolicy.setHeightForWidth(self.GenerationLineEdit.sizePolicy().hasHeightForWidth())
        self.GenerationLineEdit.setSizePolicy(sizePolicy)
        self.GenerationLineEdit.setMinimumSize(QSize(180, 0))
        self.GenerationLineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.GenerationLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_14.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.label_8 = QLabel(AlgorithmControlWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.label_8)

        self.WorkersConfigFileLineEdit = QLineEdit(AlgorithmControlWidget)
        self.WorkersConfigFileLineEdit.setObjectName(u"WorkersConfigFileLineEdit")
        sizePolicy.setHeightForWidth(self.WorkersConfigFileLineEdit.sizePolicy().hasHeightForWidth())
        self.WorkersConfigFileLineEdit.setSizePolicy(sizePolicy)
        self.WorkersConfigFileLineEdit.setMinimumSize(QSize(180, 0))
        self.WorkersConfigFileLineEdit.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.WorkersConfigFileLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.label_9 = QLabel(AlgorithmControlWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.label_9)

        self.JobsConfigFileLineEdit = QLineEdit(AlgorithmControlWidget)
        self.JobsConfigFileLineEdit.setObjectName(u"JobsConfigFileLineEdit")
        sizePolicy.setHeightForWidth(self.JobsConfigFileLineEdit.sizePolicy().hasHeightForWidth())
        self.JobsConfigFileLineEdit.setSizePolicy(sizePolicy)
        self.JobsConfigFileLineEdit.setMinimumSize(QSize(180, 0))
        self.JobsConfigFileLineEdit.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.JobsConfigFileLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.label_10 = QLabel(AlgorithmControlWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.label_10)

        self.TaskDurationConfigFileLineEdit = QLineEdit(AlgorithmControlWidget)
        self.TaskDurationConfigFileLineEdit.setObjectName(u"TaskDurationConfigFileLineEdit")
        sizePolicy.setHeightForWidth(self.TaskDurationConfigFileLineEdit.sizePolicy().hasHeightForWidth())
        self.TaskDurationConfigFileLineEdit.setSizePolicy(sizePolicy)
        self.TaskDurationConfigFileLineEdit.setMinimumSize(QSize(180, 0))
        self.TaskDurationConfigFileLineEdit.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.TaskDurationConfigFileLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_5 = QLabel(AlgorithmControlWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.label_5)

        self.ConvergenceCriteriaComboBox = QComboBox(AlgorithmControlWidget)
        self.ConvergenceCriteriaComboBox.addItem("")
        self.ConvergenceCriteriaComboBox.addItem("")
        self.ConvergenceCriteriaComboBox.addItem("")
        self.ConvergenceCriteriaComboBox.addItem("")
        self.ConvergenceCriteriaComboBox.setObjectName(u"ConvergenceCriteriaComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ConvergenceCriteriaComboBox.sizePolicy().hasHeightForWidth())
        self.ConvergenceCriteriaComboBox.setSizePolicy(sizePolicy1)
        self.ConvergenceCriteriaComboBox.setMinimumSize(QSize(180, 0))
        self.ConvergenceCriteriaComboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_4.addWidget(self.ConvergenceCriteriaComboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)

        self.currentCriteriaLabel = QLabel(AlgorithmControlWidget)
        self.currentCriteriaLabel.setObjectName(u"currentCriteriaLabel")

        self.horizontalLayout_10.addWidget(self.currentCriteriaLabel)

        self.currentCriteriaLineEdit = QLineEdit(AlgorithmControlWidget)
        self.currentCriteriaLineEdit.setObjectName(u"currentCriteriaLineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.currentCriteriaLineEdit.sizePolicy().hasHeightForWidth())
        self.currentCriteriaLineEdit.setSizePolicy(sizePolicy2)
        self.currentCriteriaLineEdit.setMinimumSize(QSize(0, 0))
        self.currentCriteriaLineEdit.setReadOnly(False)

        self.horizontalLayout_10.addWidget(self.currentCriteriaLineEdit)

        self.currentCriteriaTimeEdit = QTimeEdit(AlgorithmControlWidget)
        self.currentCriteriaTimeEdit.setObjectName(u"currentCriteriaTimeEdit")

        self.horizontalLayout_10.addWidget(self.currentCriteriaTimeEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_14.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)


        self.retranslateUi(AlgorithmControlWidget)

        QMetaObject.connectSlotsByName(AlgorithmControlWidget)
    # setupUi

    def retranslateUi(self, AlgorithmControlWidget):
        AlgorithmControlWidget.setWindowTitle(QCoreApplication.translate("AlgorithmControlWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Parameters:", None))
        self.label_2.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Population Size:", None))
        self.label_3.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Mutation Rate:", None))
        self.label_4.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Crossover Rate:", None))
        self.ResetButton.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Reset", None))
        self.StartButton.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Start", None))
        self.PauseButton.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Pause", None))
        self.StopButton.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Stop", None))
        self.label_7.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Minimized Makespan:", None))
        self.label_6.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Generation:", None))
        self.label_8.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Workers Configuration File:", None))
        self.label_9.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Jobs Configuration File:", None))
        self.label_10.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Tasks Duration Configuration File:", None))
        self.label_5.setText(QCoreApplication.translate("AlgorithmControlWidget", u"Convergence Criteria:", None))
        self.ConvergenceCriteriaComboBox.setItemText(0, QCoreApplication.translate("AlgorithmControlWidget", u"None", None))
        self.ConvergenceCriteriaComboBox.setItemText(1, QCoreApplication.translate("AlgorithmControlWidget", u"Maximum Number of Iterations", None))
        self.ConvergenceCriteriaComboBox.setItemText(2, QCoreApplication.translate("AlgorithmControlWidget", u"Time Limit", None))
        self.ConvergenceCriteriaComboBox.setItemText(3, QCoreApplication.translate("AlgorithmControlWidget", u"Target Objective Function Value", None))

        self.currentCriteriaLabel.setText(QCoreApplication.translate("AlgorithmControlWidget", u"TextLabel", None))
        self.currentCriteriaTimeEdit.setDisplayFormat(QCoreApplication.translate("AlgorithmControlWidget", u"hh:mm:ss", None))
    # retranslateUi

