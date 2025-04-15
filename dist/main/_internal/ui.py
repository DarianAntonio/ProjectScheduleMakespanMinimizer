import csv
import configparser
import random
import re

import pyqtgraph

from PySide6.QtWidgets import QLabel,QMainWindow,QWidget, QDialog, QFileDialog, QMessageBox
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsTextItem, QGraphicsRectItem,QGraphicsLineItem
from PySide6.QtGui import QCursor, QUndoCommand, QUndoStack, QColor
from PySide6.QtCore import QTime,QObject, QThread,QTimer, QDir, QFile, QStringListModel, Qt, Signal, QAbstractTableModel,QModelIndex, QItemSelectionModel

#UI files for widgets
from EvolutionaryAlgorithm import SchedulingEvolutionaryAlgorithm
from ui_mainwindow import Ui_MainWindow
from ui_welcomewidget import Ui_welcome_widget
from ui_createprojectdialog import Ui_create_project_dialog
from ui_viewtabs import Ui_viewtabs_widget
from ui_scheduleconfiguration import Ui_ScheduleConfigWidget
from ui_csvtableeditor import Ui_TableEditorMainWindow
from ui_aglorithmcontrol import Ui_AlgorithmControlWidget
from ui_ganttchartwidget import Ui_GanttChartWidget

current_project = ""
WelcomeWidgetHidden = False
workerCSVfileName = ""
workerCSVfilePath = ""
jobCSVfileName = ""
jobCSVfilePath = ""
taskDurationCSVfileName = ""
taskDurationCSVfilePath = ""

class scheduleConfigCSVfile():
    def __init__(self,header):
        self.filePath = ""
        self.header = header
    def chooseFile(self,path):
        self.filePath = path
        try:
            if self.checkHeader(path):
                pass
            else:
                raise Exception("Wrong header format")
        except FileNotFoundError:
            self.create_csv_file(path)

    def create_csv_file(self,path):
        self.filePath = path
        with open(self.filePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.header)

    def checkHeader(self,path):
        try:
            with open(path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                fileHeader = next(reader)
            if self.header == fileHeader:
                return True
        except:
            return False
        return False
    
workerCSVfile = scheduleConfigCSVfile(['ID', 'Name', 'Role'])
jobCSVfile = scheduleConfigCSVfile(['ID','Name','Predecessor'])
taskDurationCSVfile = scheduleConfigCSVfile(['JobID','WorkersID','EstimatedTime'])

class ProjectINIfile():
    
    def __init__(self) -> None:
        self.IniFile = 'project.ini'
        self.IniPath = './'

    def create_ini_file(self):
        global current_project
        self.IniPath = current_project + '/' + self.IniFile
        config = configparser.ConfigParser()
        
        config['ProjectConfig'] = {
            'workerconfigfilepath': "",
            'jobconfigfilepath': "",
            'taskdurationconfigfilepath': "",
        }
        
        with open(self.IniPath, 'w') as configfile:
            config.write(configfile)

    def read_ini_file(self):
        self.IniPath = current_project + '/' + self.IniFile
        config = configparser.ConfigParser()
        
        config.read(self.IniPath)
        #Test if keys have values
        config.get('ProjectConfig', 'workerconfigfilepath')
        config.get('ProjectConfig', 'jobconfigfilepath')
        config.get('ProjectConfig', 'taskdurationconfigfilepath')

        return config

    def write_to_ini_file(self,key, value):
        self.IniPath = current_project + '/' + self.IniFile
        config = configparser.ConfigParser()

        config.read(self.IniPath)
        
        config.set('ProjectConfig', key, value)
        
        with open(self.IniPath, 'w') as configfile:
            config.write(configfile)

projectINI = ProjectINIfile()

class RecentProjects():
    def __init__(self):
        self.list = []

    def read_file(self):
        #filePath = QCoreApplication.applicationDirPath()+"/"+"recentProjects.txt" 
        filePath = ".\\recentProjects.csv" 
        
        if filePath:
            with open(filePath, 'r') as file:
                
                self.list = []
                _list = []

                csvreader = csv.reader(file)
                for row in csvreader:
                    if row != []:
                        _list.append(row)
                for row in _list:
                    if QDir(row[1]+'/'+row[0]).exists():
                        self.list.append(row)

    def add_to_recent_projects(self,dir_path, name):
        self.read_file()
        
        if [name,dir_path] in self.list:
            self.list.remove([name,dir_path])
        self.list.insert(0,[name,dir_path])
        while len(self.list)>8:
            self.list.pop()
        filePath = ".\\recentProjects.csv" 
        if filePath:
            with open(filePath, 'w') as file:
                writer = csv.writer(file)
                writer.writerows(self.list)
        
recent_projects = RecentProjects()

#Undo Command for editing values in cells in the custom table model
class cellEditedUndoCommand(QUndoCommand):
    def __init__(self,model,index,oldValue,newValue):
        super().__init__()
        self._model = model
        self._oldValue = oldValue
        self._newValue = newValue
        self._index = index
    def redo(self):
        self._model._data[ self._index.row()][ self._index.column()] =  self._newValue
        self._model.dataChanged.emit(self._index, self._index)
    def undo(self):
        self._model._data[ self._index.row()][ self._index.column()] = self._oldValue
        self._model.dataChanged.emit(self._index, self._index)

#Unused, was undo command for adding rows
"""
class rowAddedUndoCommand(QUndoCommand):
    def __init__(self,model,row):
        super().__init__()
        self._model = model
        self._row = row

    def undo(self):
        #self._model.removeRow(len(self._model._data))
        self._model.beginRemoveRows(QModelIndex(), self._row, self._row)
        self._model.endRemoveRows()
        self._model.dataChanged.emit(self._model.index(self._row,0), self._model.index(self._row,len(self._model.header)))
    def redo(self):
        self._model.beginInsertRows(QModelIndex(), self._row, self._row)
        self._model._data.append([""]*len(self._model.header))
        self._model.endInsertRows()
        self._model.dataChanged.emit(self._model.index(self._row,0), self._model.index(self._row,len(self._model.header)))
"""
#Unused, was undo command for deleting rows
"""
class rowDeletedUndoCommand(QUndoCommand):
    def __init__(self,model,row):
        super().__init__()
        self._model = model
        self._row= row
        self._rowData = self._model._data[self._row]
    def undo(self):
        self._model.beginInsertRows(QModelIndex(), self._row, self._row)
        self._model._data.insert(self._row,[""]*len(self._model.header))
        self._model.endInsertRows()
        self._model._data[self._row] = self._rowData
        self._model.dataChanged.emit(self._model.index(self._row,0), self._model.index(self._row,len(self._model.header)))
    def redo(self):
        #self._model.removeRow(len(self._model._data))
        self._model.beginRemoveRows(QModelIndex(), len(self._model._data), len(self._model._data))
        #del self._data[row]
        self._model.endRemoveRows()
        self._model.dataChanged.emit(self._model.index(self._row,0), self._model.index(self._row,len(self._model.header)))
"""
#Undo command for insert / remove row in the custom table view model
class insertDeleteRowUndoCommand(QUndoCommand):
    def __init__(self,model,oldModel,newModel):
        super().__init__()
        self._model = model
        self._oldModel = oldModel
        self._newModel = newModel
    def undo(self):
        self._model._data = self._oldModel[0]
        self._model.header = self._oldModel[1]
        self._model.layoutChanged.emit()
    def redo(self):
        self._model._data = self._newModel[0]
        self._model.header = self._newModel[1]
        self._model.layoutChanged.emit()
        
#Custom table model for displaying Schedule Config CSV files
class CSVtableModel(QAbstractTableModel):
    #Initialize model
    def __init__(self, data, header):
        super().__init__()
        self._data = data
        self.header = header
        self.undoStack = QUndoStack(self)
    #Required rowCount function
    def rowCount(self, parent=QModelIndex()):
        return len(self._data)
    #Required columnCount function
    def columnCount(self, parent=QModelIndex()):
        return len(self.header)
    #Required data function
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
    #Required setData function
    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            #Add changes to undo stack
            _oldValue = self._data[index.row()][index.column()]
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            self.undoStack.push(cellEditedUndoCommand(self,index,_oldValue,value))
            return True
        return False
    #Required flags function
    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled
    #headerData function to show the headers of the CSV files
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header[section]
        return super().headerData(section, orientation, role)
    #add row function
    def insertRow(self):
        _oldModel = (list(self._data),list(self.header))
        self.beginInsertRows(QModelIndex(), len(self._data), len(self._data))
        self._data.append([""]*len(self.header))
        self.endInsertRows()
        _newModel = (list(self._data),list(self.header))
        self.undoStack.push(insertDeleteRowUndoCommand(self,_oldModel,_newModel))
        #self.undoStack.push(rowAddedUndoCommand(self,len(self._data)))
    #add row function with index
    def insertRowIndex(self,row):
        _oldModel = (list(self._data),list(self.header))
        self.beginInsertRows(QModelIndex(), row, row)
        self._model._data.insert(row,[""]*len(self._model.header))
        self.endInsertRows()
        _newModel = (list(self._data),list(self.header))
        self.undoStack.push(insertDeleteRowUndoCommand(self,_oldModel,_newModel))
        #self.undoStack.push(rowAddedUndoCommand(self,row))
    #Remove row function
    def removeRow(self, row):
        _oldModel = (list(self._data),list(self.header))
        self.beginRemoveRows(QModelIndex(), row, row)
        del self._data[row]
        self.endRemoveRows()
        _newModel = (list(self._data),list(self.header))
        self.undoStack.push(insertDeleteRowUndoCommand(self,_oldModel,_newModel))
    #Undo function
    def undo(self):
        if self.undoStack.canUndo():
            self.undoStack.undo()
    #Redo function
    def redo(self):
        if self.undoStack.canRedo():
            self.undoStack.redo()

#Widget for the tabs in the Schedule Configuration
class CSVtableEditorMainWindow(QMainWindow, Ui_TableEditorMainWindow):
    changed_files = Signal()
    #Keep track of the last selected row / column for the actions
    row = 0
    column = 0
    model = None
    #File info
    filePath = ""
    #Header format
    headerFormat = []
    #Initialize widget
    def __init__(self,key,value):
        super().__init__()
        self.setupUi(self)
        #Remember the key and value to be able to modify them
        self.key = key
        self.value = value
        #Load the model from the project.ini file
        global projectINI
        _config = projectINI.read_ini_file()
        self.filePath = _config.get(key,value)
        #Load model from CSV File
        self.loadCSVfile(self.filePath)
        #Save header format to be able to check for valid files later
        self.headerFormat = [self.model.headerData(col, Qt.Horizontal) for col in range(self.model.columnCount())]
        #Show file name in CSV source line edit
        self.CSVsourceLineEdit.setText(self.filePath.split('/')[-1])
        if self.value == "workerconfigfilepath":
            global workerCSVfileName
            workerCSVfileName = self.filePath.split('/')[-1]
            global workerCSVfilePath
            workerCSVfilePath = self.filePath
        if self.value == "jobconfigfilepath":
            global jobCSVfileName
            jobCSVfileName = self.filePath.split('/')[-1]
            global jobCSVfilePath
            jobCSVfilePath = self.filePath
        if self.value == "taskdurationconfigfilepath":
            global taskDurationCSVfileName
            taskDurationCSVfileName = self.filePath.split('/')[-1]
            global taskDurationCSVfilePath
            taskDurationCSVfilePath = self.filePath

        #Attach model to table view
        self.CSVtableView.setModel(self.model)

        #Change the header/ index color
        #self.CSVtableView.setStyleSheet("QHeaderView::section { background-color: #ebf5ff; }")
        
        #Select the first cell to show on which cell the actions would have effect when table is first shown
        if self.model.index(0, 0).isValid():
            self.CSVtableView.selectionModel().setCurrentIndex(self.model.index(0, 0), QItemSelectionModel.SelectCurrent)
        self.RowLineEdit.setText(str(self.row+1))
        self.ColumnLineEdit.setText(str(self.column+1))

        #Connect functions to triggers / actions
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionAddRow.triggered.connect(self.addRow)
        self.actionDelete_Row.triggered.connect(self.delRow)
        self.CSVtableView.clicked.connect(self.cellClickedDragged)
        self.CSVtableView.entered.connect(self.cellClickedDragged)
        self.CSVtableView.selectionModel().currentChanged.connect(self.cellSelected)
        self.RowLineEdit.returnPressed.connect(self.selectRowColumnLineEdit)
        self.ColumnLineEdit.returnPressed.connect(self.selectRowColumnLineEdit)
        self.SaveFileButton.clicked.connect(self.saveCSVfile)
        self.ChooseFileButton.clicked.connect(self.chooseCSVfile)
        self.NewFileButton.clicked.connect(self.newCSVfile)
        #self.model.dataChanged.connect()

    def undo(self):
        self.model.undo()
        
    def redo(self):
        self.model.redo()
        
    #Update the row / index values when a cell is clicked / dragged over
    def cellClickedDragged(self, index):
        self.row = index.row()
        self.column = index.column()
        self.RowLineEdit.setText(str(self.row+1))
        self.ColumnLineEdit.setText(str(self.column+1))

    #Update the row / index values when a cell is selected
    def cellSelected(self, current, previous):
        if current.isValid():
            self.row = current.row()
            self.column = current.column()
            self.RowLineEdit.setText(str(self.row+1))
            self.ColumnLineEdit.setText(str(self.column+1))
    
    #Select the row, column chosen in the line edits
    def selectRowColumnLineEdit(self):
        #Try to select the specified row/column
        try:
            #Check if the values in the row / column line edits can be converted to int
            _row = int(self.RowLineEdit.text()) - 1
            _column = int(self.ColumnLineEdit.text()) - 1
            #If the values for the row and column are valid, select the specified cell
            if _row >= 0 and _row < self.model.rowCount():
                if _column >= 0 and _column < self.model.columnCount():
                    self.CSVtableView.selectionModel().setCurrentIndex(self.model.index(_row, _column), QItemSelectionModel.SelectCurrent)
        #If not possible, do nothing     
        except:
            pass
    
    #Add a row to the table view's model
    def addRow(self):
        self.model.insertRow()

    #Delete row to the table view's model
    def delRow(self):
        _row = self.row
        #If the model has no rows, do nothing
        if self.model.rowCount() == 0:
            return
        #Remove the row
        self.model.removeRow(_row)
        #Select the previous row if possible
        """
        self.row-=1
        self.column -= 1
        if self.row < 0:
            self.row = 0
        if self.column < 0:
            self.column = 0
        #If the table has no rows, add 1 more row
        if self.model.rowCount() == 0:
            self.addRow()
        #Select a cell in a row
        if self.model.index(self.row, self.column).isValid():
            self.CSVtableView.selectionModel().setCurrentIndex(self.model.index(self.row, self.column), QItemSelectionModel.SelectCurrent)
        """
        #Update the line edits
        self.RowLineEdit.setText(str(self.row+1))
        self.ColumnLineEdit.setText(str(self.column+1))

    #Create new empty CSV file
    def newCSVfile(self):
        _fileDialog = QFileDialog()
        _fileDialog.setNameFilter("CSV Files (*.csv)")
        _fileDialog.setViewMode(QFileDialog.List)
        _fileDialog.setFileMode(QFileDialog.AnyFile)
        _fileDialog.setAcceptMode(QFileDialog.AcceptSave)
        global current_project
        _fileDialog.setDirectory(current_project)

        if _fileDialog.exec():
            _filePath = _fileDialog.selectedFiles()[0]
        else:
            return
        try:
            with open(_filePath, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                # Write the header of the model to the CSV file
                header = [self.model.headerData(col, Qt.Horizontal) for col in range(self.model.columnCount())]
                writer.writerow(header)
        except:
            pass
        data = [[""]*len(header)]
        #Create new model
        self.model = CSVtableModel(data, header)
        #Show file name in CSV source line edit and set new file path
        self.filePath = _filePath
        self.CSVsourceLineEdit.setText(self.filePath.split('/')[-1])
        if self.value == "workerconfigfilepath":
            global workerCSVfileName
            workerCSVfileName = self.filePath.split('/')[-1]
            global workerCSVfilePath
            workerCSVfilePath = self.filePath
        if self.value == "jobconfigfilepath":
            global jobCSVfileName
            jobCSVfileName = self.filePath.split('/')[-1]
            global jobCSVfilePath
            jobCSVfilePath = self.filePath
        if self.value == "taskdurationconfigfilepath":
            global taskDurationCSVfileName
            taskDurationCSVfileName = self.filePath.split('/')[-1]
            global taskDurationCSVfilePath
            taskDurationCSVfilePath = self.filePath

        #Reset the selected row/column positions
        self.row = 0
        self.column = 0
        if self.model.index(0, 0).isValid():
            self.CSVtableView.selectionModel().setCurrentIndex(self.model.index(0, 0), QItemSelectionModel.SelectCurrent)
        self.RowLineEdit.setText(str(self.row+1))
        self.ColumnLineEdit.setText(str(self.column+1))
        #Update the project.ini
        config = configparser.ConfigParser()
        config.read(current_project + '/project.ini')
        # Modify the value
        config.set(self.key, self.value, self.filePath)
        # Write changes back to the file
        with open(current_project + '/project.ini', 'w') as configFile:
            config.write(configFile)
        self.model.undoStack.setClean()
        self.changed_files.emit()
        

    #Choose CSV file
    def chooseCSVfile(self):
        global current_project
        _filePath,_ = QFileDialog.getOpenFileName(self, "Open File",
                                 current_project,
                                 "CSV files(*.csv);;All files(*.*)")
        #If no file is chosen to nothing
        if((_filePath == "")):
            return
        data = []
        header = []
        with open(_filePath, "r", newline="") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            #If the CSV file does not has the right header then do not accept this file
            if header != self.headerFormat:
                QMessageBox.warning(self,"Warning!",
                                        "The file is invalid.",
                                        QMessageBox.Ok)
                return
            for row in csv_reader:
                data.append(row)
        if data == []:
            data = [[""]*len(header)]

        self.filePath = _filePath
        #Create a new model
        self.model = CSVtableModel(data, header)
        #Set the table view to the new model
        self.CSVtableView.setModel(self.model)
        #Show file name in CSV source line edit
        self.CSVsourceLineEdit.setText(self.filePath.split('/')[-1])
        if self.value == "workerconfigfilepath":
            global workerCSVfileName
            workerCSVfileName = self.filePath.split('/')[-1]
            global workerCSVfilePath
            workerCSVfilePath = self.filePath
        if self.value == "jobconfigfilepath":
            global jobCSVfileName
            jobCSVfileName = self.filePath.split('/')[-1]
            global jobCSVfilePath
            jobCSVfilePath = self.filePath
        if self.value == "taskdurationconfigfilepath":
            global taskDurationCSVfileName
            taskDurationCSVfileName = self.filePath.split('/')[-1]
            global taskDurationCSVfilePath
            taskDurationCSVfilePath = self.filePath
        #Reset the selected row/column positions
        self.row = 0
        self.column = 0
        if self.model.index(0, 0).isValid():
            self.CSVtableView.selectionModel().setCurrentIndex(self.model.index(0, 0), QItemSelectionModel.SelectCurrent)
        self.RowLineEdit.setText(str(self.row+1))
        self.ColumnLineEdit.setText(str(self.column+1))
        #Update the project.ini
        config = configparser.ConfigParser()
        config.read(current_project + '/project.ini')
        # Modify the value
        config.set(self.key, self.value, self.filePath)
        # Write changes back to the file
        with open(current_project + '/project.ini', 'w') as configFile:
            config.write(configFile)
        self.model.undoStack.setClean()
        self.changed_files.emit()

    #Load the data from a CSV file in the CSV table view's model, this function is used for the first loaded file from project.ini
    def loadCSVfile(self,path):
        #Read the data and header for the model from a csv file.
        data = []
        header = []
        with open(path, "r", newline="") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            for row in csv_reader:
                data.append(row)
        if data == []:
            data = [[""]*len(header)]
        #Create a new model
        self.model = CSVtableModel(data, header)
        #Set the table view to the new model
        self.CSVtableView.setModel(self.model)
        #Reset the selected row/column positions
        self.row = 0
        self.column = 0
        if self.model.index(0, 0).isValid():
            self.CSVtableView.selectionModel().setCurrentIndex(self.model.index(0, 0), QItemSelectionModel.SelectCurrent)
        self.RowLineEdit.setText(str(self.row+1))
        self.ColumnLineEdit.setText(str(self.column+1))
        self.model.undoStack.setClean()
        self.changed_files.emit()

    #Save the model to a CSV file
    def saveCSVfile(self):
        with open(self.filePath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write the header of the model to the CSV file
            header = [self.model.headerData(col, Qt.Horizontal) for col in range(self.model.columnCount())]
            writer.writerow(header)
            # Write the data of the model to the CSV file
            for row in range(self.model.rowCount()):
                row_data = [self.model.data(self.model.index(row, col),Qt.DisplayRole) for col in range(self.model.columnCount())]
                writer.writerow(row_data)
        self.model.undoStack.setClean()
        self.changed_files.emit()

class ScheduleConfigurationWidget(QWidget, Ui_ScheduleConfigWidget):
    changed_files = Signal()
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.workerCSVeditor = CSVtableEditorMainWindow("ProjectConfig","workerconfigfilepath")
        self.jobCSVeditor = CSVtableEditorMainWindow("ProjectConfig","jobconfigfilepath")
        self.timeDurationCSVeditor = CSVtableEditorMainWindow("ProjectConfig","taskdurationconfigfilepath")

        self.tabWidget.insertTab(0, self.workerCSVeditor, "Workers Configuration")
        self.tabWidget.insertTab(1, self.jobCSVeditor, "Jobs Configuration")
        self.tabWidget.insertTab(2, self.timeDurationCSVeditor, "Task Duration Configuration")
        self.workerCSVeditor.changed_files.connect(self.changed_files.emit)
        self.jobCSVeditor.changed_files.connect(self.changed_files.emit)
        self.timeDurationCSVeditor.changed_files.connect(self.changed_files.emit)

#The QObject that I will use for threading
#It allows the use of the evolutionary algorithm within the program
class AlgorithmThread(QObject):
    #result_ready = Signal(dict)
    algorithm_stopped = Signal()
    generation_finished = Signal()
    _running = False
    def __init__(self):
        super().__init__()
        self._running = False
        global workerCSVfilePath
        global jobCSVfilePath
        global taskDurationCSVfilePath
        self.evoAlg = SchedulingEvolutionaryAlgorithm(workerCSVfilePath,jobCSVfilePath,taskDurationCSVfilePath)

    def start_running(self):
        self._running = True
        if self.evoAlg.generation == -1:
            self.evoAlg.initialize_population()
        while self._running:
            # Replace this with your actual calculation algorithm
            self.evoAlg.evolve()
            self.generation_finished.emit()
    
    def reset(self):
        self.stop_running()
        global workerCSVfilePath
        global jobCSVfilePath
        global taskDurationCSVfilePath
        self.evoAlg = SchedulingEvolutionaryAlgorithm(workerCSVfilePath,jobCSVfilePath,taskDurationCSVfilePath)
        self.evoAlg.generation = -1

    def setParameters(self, popSize, crossoverChance, mutationChance):
        self.reset()
        self.evoAlg.setParameters(popSize,crossoverChance,mutationChance)
        self.evoAlg.generation = -1

    def stop_running(self):
        self._running = False
        self.algorithm_stopped.emit()
        
class AlgorithmControlWidget(QWidget,Ui_AlgorithmControlWidget):
    #Signal to emit for the gantt chart
    algorithmResults = Signal(list)
    currentConvergenceCriteria = None
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        global workerCSVfileName
        global jobCSVfileName
        global taskDurationCSVfileName
        self.WorkersConfigFileLineEdit.setText(workerCSVfileName)
        self.JobsConfigFileLineEdit.setText(jobCSVfileName)
        self.TaskDurationConfigFileLineEdit.setText(taskDurationCSVfileName)

        self.ResetButton.setText("Start")
        self.StartButton.hide()
        self.StopButton.hide()
        self.PauseButton.hide()

        self.plot_widget = pyqtgraph.PlotWidget()
        self.plot_widget.setLabel('left', 'Makespan')
        self.plot_widget.setLabel('bottom', 'Generation')
        self.plot_widget.showGrid(x=True, y=True)
        self.curve = self.plot_widget.plot(pen='g')
        self.plot_widget.setBackground('w')
        #self.plot_widget.setMouseEnabled(False, False)

        self.verticalLayout_3.addWidget(self.plot_widget)

        
        try:
            self.thread = QThread()
            self.evoThread = AlgorithmThread()
            self.evoThread.moveToThread(self.thread)
            # Initialize data
            self.generations = []
            self.fitness_values = []
            self.current_generation = 0

            self.thread.started.connect(self.evoThread.start_running)
            self.thread.destroyed.connect(self.pauseAlgorithm)

            self.evoThread.algorithm_stopped.connect(self.thread.quit)

            self.ResetButton.clicked.connect(self.resetAlgorithm)
            self.StartButton.clicked.connect(self.startAlgorithm)
            self.PauseButton.clicked.connect(self.pauseAlgorithm)
            self.StopButton.clicked.connect(self.stopAlgorithm)
            # Update plot every couple miliseconds
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_plot)
            self.timer.start(15)  

            #Trigger the function for updating the convergence criteria widgets
            self.convergenceCriteriaChanged(self.ConvergenceCriteriaComboBox.currentIndex())

            #Check if convergence criteria was met
            self.timer2 = QTimer()
            self.timer2.timeout.connect(self.convergenceCriteriaMet)
            self.timer2.start(15)  
            
            self.check_algorithm_parameters()

            self.PopulationSizeLineEdit.returnPressed.connect(self.check_algorithm_parameters)
            self.MutationRateLineEdit.returnPressed.connect(self.check_algorithm_parameters)
            self.CrossoverRateLineEdit.returnPressed.connect(self.check_algorithm_parameters)
            self.ConvergenceCriteriaComboBox.currentIndexChanged.connect(self.convergenceCriteriaChanged)
            self.evoThread.generation_finished.connect(self.check_convergence_criteria)
            
            
            self.criteriaTimer = QTimer()
            self.criteriaTimer.timeout.connect(self.updateConvergenceCriteriaTimeEdit)
            self.criteriaTimer.start(1000)

        except:
            self.ResetButton.setEnabled(False)
            self.PopulationSizeLineEdit.setReadOnly(True)
            self.MutationRateLineEdit.setReadOnly(True)
            self.CrossoverRateLineEdit.setReadOnly(True)
            self.currentCriteriaLineEdit.setReadOnly(True)
            self.currentCriteriaTimeEdit.setReadOnly(True)
            self.ConvergenceCriteriaComboBox.setEnabled(False)
            pass
        
    def updateConvergenceCriteriaTimeEdit(self):
        
        if(self.currentCriteriaTimeEdit.time()<= QTime(0, 0, 0)):
            self.currentCriteriaTimeEdit.setTime(QTime(0, 0, 0))
            return
        if self.evoThread._running:
            self.currentCriteriaTimeEdit.setTime(self.currentCriteriaTimeEdit.time().addSecs(-1))
        

    def check_convergence_criteria(self):
        if self.ConvergenceCriteriaComboBox.currentText() == "None":
            return
        if self.ConvergenceCriteriaComboBox.currentText() == "Maximum Number of Iterations":
            if int(self.currentCriteriaLineEdit.text())<= self.evoThread.evoAlg.generation:
                self.timer2.stop()
                self.stopAlgorithm()
                self.GenerationLineEdit.setText(self.currentCriteriaLineEdit.text())
            return
        if self.ConvergenceCriteriaComboBox.currentText() == "Target Objective Function Value":
            if int(self.currentCriteriaLineEdit.text())>= -self.evoThread.evoAlg.bestChromosome["fitness"]:
                self.stopAlgorithm()
            return
        if self.ConvergenceCriteriaComboBox.currentText() == "Time Limit":
            if self.currentCriteriaTimeEdit.time()<= QTime(0, 0, 0):
                self.stopAlgorithm()
        
    def startAlgorithm(self):
        self.timer2.start(15)
        if self.evoThread._running == False:
            self.thread.start()
            self.StartButton.setEnabled(False)
            self.PauseButton.setEnabled(True)

    def pauseAlgorithm(self):
        self.timer2.stop()
        if self.evoThread._running == True:
            self.evoThread.stop_running()
            self.StartButton.setEnabled(True)
            self.PauseButton.setEnabled(False)

    def resetAlgorithm(self):
        self.timer2.start(15)
        #Disable Config Lines
        #Will re-enable them in the stop function
        self.PopulationSizeLineEdit.setReadOnly(True)
        self.MutationRateLineEdit.setReadOnly(True)
        self.CrossoverRateLineEdit.setReadOnly(True)
        self.currentCriteriaLineEdit.setReadOnly(True)
        self.currentCriteriaTimeEdit.setReadOnly(True)
        self.ConvergenceCriteriaComboBox.setEnabled(False)

        self.ResetButton.setText("Reset")
        self.StartButton.show()
        self.StopButton.show()
        self.PauseButton.show()
        self.StartButton.setEnabled(False)
        self.PauseButton.setEnabled(True)

        self.generations=[]
        self.fitness_values=[]
        self.curve.setData(self.generations, self.fitness_values)
        
        self.check_algorithm_parameters()
        self.pauseAlgorithm()

        try:
            self.evoThread.setParameters(int(self.PopulationSizeLineEdit.text()),
                                     float(re.sub(r'[^\d.]', '', self.CrossoverRateLineEdit.text()))/100,
                                     float(re.sub(r'[^\d.]', '', self.MutationRateLineEdit.text()))/100)
            self.thread.start()
        except:
            pass
        #self.evoThread.start_running()
    def stopAlgorithm(self):
        self.timer2.stop()
        #Disable Config Lines
        #Will re-enable them in the stop function
        self.PopulationSizeLineEdit.setReadOnly(False)
        self.MutationRateLineEdit.setReadOnly(False)
        self.CrossoverRateLineEdit.setReadOnly(False)
        self.currentCriteriaLineEdit.setReadOnly(False)
        self.currentCriteriaTimeEdit.setReadOnly(False)
        self.ConvergenceCriteriaComboBox.setEnabled(True)

        self.ResetButton.setText("Start")
        self.StartButton.hide()
        self.StopButton.hide()
        self.PauseButton.hide()

        self.pauseAlgorithm()
        self.algorithmResults.emit([self.evoThread.evoAlg.bestChromosome,self.evoThread.evoAlg.workers_dict,self.evoThread.evoAlg.jobs_dict,self.evoThread.evoAlg.jobs_graph])
        """
        print(self.evoThread.evoAlg.bestChromosome)
        print()
        print(self.evoThread.evoAlg.workers_dict)
        print()
        print(self.evoThread.evoAlg.jobs_dict)
        print()
        print(self.evoThread.evoAlg.jobs_graph)
        """


    def check_algorithm_parameters(self):
            try:
                self.PopulationSizeLineEdit.setText(re.sub(r'[^0-9]', '', self.PopulationSizeLineEdit.text()))
                float(self.PopulationSizeLineEdit.text())
                self.PopulationSizeLineEdit.setText(str(int(self.PopulationSizeLineEdit.text())))
            except:
                self.PopulationSizeLineEdit.setText("1000")
            try:
                self.MutationRateLineEdit.setText(re.sub(r'[^\d.]', '', self.MutationRateLineEdit.text()))
                if(float(self.MutationRateLineEdit.text())<0):
                    self.MutationRateLineEdit.setText("0%")
                    print(1)
                elif(float(self.MutationRateLineEdit.text())>100):
                    self.MutationRateLineEdit.setText("100.0%")
                else:
                    self.MutationRateLineEdit.setText(str(float(self.MutationRateLineEdit.text()))+"%")
            except:
                self.MutationRateLineEdit.setText("5.0%")
            try:
                self.CrossoverRateLineEdit.setText(re.sub(r'[^\d.]', '', self.CrossoverRateLineEdit.text()))
                if(float(self.CrossoverRateLineEdit.text())<0):
                    self.CrossoverRateLineEdit.setText("0%")
                    print(1)
                elif(float(self.CrossoverRateLineEdit.text())>100):
                    self.CrossoverRateLineEdit.setText("100.0%")
                else:
                    self.CrossoverRateLineEdit.setText(str(float(self.CrossoverRateLineEdit.text()))+"%")
            except:
                self.CrossoverRateLineEdit.setText("75.0%")
           
    def update_plot(self):
        #Get the fitness values from the evoThread
        if self.evoThread.evoAlg.bestChromosome == None:
            return
        fitness = -self.evoThread.evoAlg.bestChromosome["fitness"]

        self.MakespanLineEdit.setText(str(fitness))
        self.GenerationLineEdit.setText(str(self.evoThread.evoAlg.generation))
        if self.ConvergenceCriteriaComboBox.currentText() == "Maximum Number of Iterations":
            if int(self.currentCriteriaLineEdit.text())<= self.evoThread.evoAlg.generation:
                self.GenerationLineEdit.setText(self.currentCriteriaLineEdit.text())
        # Append data to lists
        self.generations.append(self.evoThread.evoAlg.generation)
        self.fitness_values.append(fitness)

        # Update the plot with the new data
        self.curve.setData(self.generations, self.fitness_values)

    def convergenceCriteriaChanged(self,index):
        if self.ConvergenceCriteriaComboBox.currentText() == "None":
            self.currentCriteriaLabel.hide()
            self.currentCriteriaTimeEdit.hide()
            self.currentCriteriaLineEdit.hide()
            return
        else:
            self.currentCriteriaLabel.show()

        #Show the setting widget for number of iteration limit
        if self.ConvergenceCriteriaComboBox.currentText() == "Maximum Number of Iterations":
            self.currentCriteriaLabel.setText("Max Iterations:")
            self.currentCriteriaLineEdit.setText("1000")
            self.currentCriteriaTimeEdit.hide()
            self.currentCriteriaLineEdit.show()
            return
        #Show the setting widget for time limit
        elif self.ConvergenceCriteriaComboBox.currentText() == "Time Limit":
            self.currentCriteriaLabel.setText("Time Limit:")
            self.currentCriteriaTimeEdit.setTime(QTime.fromString("00:05:00", "hh:mm:ss"))
            self.currentCriteriaTimeEdit.show()
            self.currentCriteriaLineEdit.hide()
            return

        #Show the setting widget for Target Objective Function Value
        elif self.ConvergenceCriteriaComboBox.currentText() == "Target Objective Function Value":
            self.currentCriteriaTimeEdit.hide()
            self.currentCriteriaLineEdit.show()
            self.currentCriteriaLabel.setText("Minimum Makespan:")
            self.currentCriteriaLineEdit.setText("10")

    def convergenceCriteriaMet(self):
        pass


class HoverRectItem(QGraphicsRectItem):
    def __init__(self, x, y, width, height,task,names,start,finish,parent1, parent=None):
        super().__init__(x, y, width, height, parent)
        self.setAcceptHoverEvents(True)
        self.parent1 = parent1
        self.hover_label = QLabel(self.parent1)
        self.hover_label.setText(f"Task: {task}\nWorkers: {(',').join(names)}\nStartTime: {start}\nFinishTime: {finish}")
        self.hover_label.setStyleSheet("background-color: white; border: 1px solid black; padding: 5px;")
        self.hover_label.hide()

    def hoverEnterEvent(self, event):
        self.hover_label.show()
        self.hover_label.move(self.parent1.mapFromGlobal(QCursor.pos()).x()+2,self.parent1.mapFromGlobal(QCursor.pos()).y()+2)
        event.accept()

    def hoverLeaveEvent(self, event):
        self.hover_label.hide()
        event.accept()


class GanttChart(QGraphicsView):
    def __init__(self,worker_dict,jobs_dict, data,mode):
        super().__init__()
        self.data = data
        self.worker_dict = worker_dict
        self.jobs_dict = jobs_dict
        self.mode = mode[:-len(" View")]
        self.modeWorker = None
        if self.mode != "Overall":
            self.modeWorker = [key for key, value in worker_dict.items() if value.get('Name') == self.mode][0]
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.draw_gantt_chart()

    def draw_gantt_chart(self):
        # Constants
        top_padding = 25
        task_height = 50
        task_spacing = 10
        # Calculate total time range
        start_time = min(task['StartTime'] for task in self.data)
        end_time = max(task['FinishTime'] for task in self.data)
        total_time = end_time - start_time
        # Draw tasks
        if self.mode == "Overall":
            newData = self.data
        else:
            newData = [d for d in self.data if self.modeWorker in d.get('WorkersID')]
        for i, task in enumerate(sorted(newData, key=lambda x: (x['StartTime'], x['FinishTime']))):
            # Calculate task position and dimensions
            task_x = (task['StartTime'] - start_time) / total_time * self.width()
            task_width = (task['FinishTime'] - task['StartTime']) / total_time * self.width()
            # Draw task rectangle
            rect = HoverRectItem(task_x, i * (task_height + task_spacing) + top_padding, task_width, task_height,self.jobs_dict[task["JobID"]]["Name"],[self.worker_dict[i]["Name"] for i in task["WorkersID"]],task["StartTime"],task["FinishTime"],self)
            rect.setBrush(QColor(random.randint(120,255),random.randint(120,255),random.randint(120,255)))
            self.scene.addItem(rect)
            #Draw labels
            label = QGraphicsTextItem(self.jobs_dict[task['JobID']]["Name"])
            label.setPos(-5-label.boundingRect().width(), i * (task_height + task_spacing) + top_padding + task_height/2 - label.boundingRect().height()/2)
            self.scene.addItem(label)
        # Draw bottom axis
        ticks_line_y = self.scene.sceneRect().height()+ top_padding
        bottom_axis = QGraphicsLineItem(-30, self.scene.sceneRect().height()+ top_padding, self.width()+30, self.scene.sceneRect().height()+top_padding)
        self.scene.addItem(bottom_axis)
        left_axis = QGraphicsLineItem(0, 0, 0, self.scene.sceneRect().height()+30 + top_padding)
        self.scene.addItem(left_axis)
        #Add time label
        label = QGraphicsTextItem("Time")
        label.setPos(self.width()/2-label.boundingRect().width()/2,ticks_line_y+25)
        self.scene.addItem(label)
        #Add time ticksmin((self.width()/30),total_time))
        no_of_ticks = int(min((self.width()/30),total_time))
        for i in range(no_of_ticks+1):
            tick_line = QGraphicsLineItem(int(i*self.width()/no_of_ticks), ticks_line_y, int(i*self.width()/no_of_ticks), ticks_line_y+5)
            self.scene.addItem(tick_line)
            if i != 0:
                label = QGraphicsTextItem(str(int(total_time*i/no_of_ticks)))
                label.setPos(int(i*self.width()/no_of_ticks)-label.boundingRect().width()/2,ticks_line_y+5)
                self.scene.addItem(label)
        # Resize the scene
        self.setSceneRect(0, 0, self.width(), len(self.data) * (task_height + task_spacing)+60 + top_padding)

class GanttChartData():
    def __init__(self, genes_dict,worker_dict,jobs_dict,jobs_graph):
        self.genes_dict = genes_dict
        self.worker_dict = worker_dict
        self.jobs_dict = jobs_dict
        self.jobs_graph = jobs_graph

    def barData(self):
        bar_dict = {}
        bar_dict["Start"] = {"JobID":None,"WorkersID":None,"StartTime":0,"FinishTime":0}
        workers_finish_time = {}
        for key,value in self.worker_dict.items():
            workers_finish_time[key] = 0
        for i in self.genes_dict["priority"]:
            _job_id = i
            _workers_id = self.genes_dict["genes"][i]["WorkersID"]
            _start_time = max(max([bar_dict[j]["FinishTime"] for j in self.jobs_graph[i]["parents"]]),max([workers_finish_time[j] for j in _workers_id]))
            _finish_time = _start_time + self.genes_dict["genes"][i]["EstimatedTime"]
            for j in _workers_id:
                workers_finish_time[j] = _finish_time
            bar_dict[i] = {"JobID":_job_id,"WorkersID":_workers_id,"StartTime":_start_time,"FinishTime":_finish_time}
        bar_dict.pop("Start")
        return bar_dict


class GanttChartWidget(QWidget,Ui_GanttChartWidget):
    ViewChanged = Signal()
    data = []
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.ViewComboBox.activated.connect(self.option_chosen)
    def option_chosen(self,index):
        self.create_graph()
    def create_graph(self):
        self.barsData = GanttChartData(self.data[0],self.data[1],self.data[2],self.data[3])
        self.gantt_chart_graphics = GanttChart(self.data[1],self.data[2],self.barsData.barData().values(),self.ViewComboBox.currentText())

        while self.GraphLayout.count():
            item = self.GraphLayout.takeAt(0)
            self.layout().removeItem(item)
            del item
        self.GraphLayout.addWidget(self.gantt_chart_graphics)
        pass
    def setData(self,data):
        self.data = data
        for key,value in sorted(self.data[1].items(),key=lambda x:x[1]["Name"]):
            self.ViewComboBox.addItem(value["Name"]+" View")
        


class ViewTabsWidget(QWidget,Ui_viewtabs_widget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.schedule_config_widget = ScheduleConfigurationWidget()
        self.schedule_config_tab = self.tabWidget.insertTab(0,self.schedule_config_widget,"Project Configuration")

        self.algorithm_control_widget = AlgorithmControlWidget()
        self.algorithm_control_tab = self.tabWidget.insertTab(1, self.algorithm_control_widget,"Algorithm Control")

        self.gantt_chart_widget = GanttChartWidget()
        self.gantt_chart_tab = self.tabWidget.insertTab(2,self.gantt_chart_widget,"Gantt Chart")
        self.tabWidget.setTabEnabled(2, False)

        self.algorithm_control_widget.algorithmResults.connect(self.resultsReady)
        self.schedule_config_widget.changed_files.connect(self.filesChanged)

    def close_project(self):
        self.tabWidget.removeTab(2)
        self.tabWidget.removeTab(1)
        self.tabWidget.removeTab(0)
        del self.algorithm_control_widget
        del self.gantt_chart_widget
        del self.schedule_config_widget

    def filesChanged(self):
        self.tabWidget.removeTab(2)
        self.tabWidget.removeTab(1)
        del self.algorithm_control_widget
        self.algorithm_control_widget = AlgorithmControlWidget()
        del self.gantt_chart_widget
        self.gantt_chart_widget = GanttChartWidget()
        self.algorithm_control_tab = self.tabWidget.insertTab(1, self.algorithm_control_widget,"Algorithm Control")
        self.gantt_chart_tab = self.tabWidget.insertTab(2,self.gantt_chart_widget,"Gantt Chart")   
        self.algorithm_control_widget.algorithmResults.connect(self.resultsReady)
        self.tabWidget.setTabEnabled(2, False)
        
        
    def resultsReady(self,data):
        del self.gantt_chart_widget
        self.tabWidget.removeTab(2)
        self.gantt_chart_widget = GanttChartWidget()
        self.gantt_chart_tab = self.tabWidget.insertTab(2,self.gantt_chart_widget,"Gantt Chart")   
        self.gantt_chart_widget.setData(data)
        self.gantt_chart_widget.create_graph()
        self.tabWidget.setTabEnabled(2, True)
        

class CreateProjectDialog(QDialog, Ui_create_project_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Create New Project")

        self.dir_path = ""

        self.confirm_button.clicked.connect(self.confirm)
        self.cancel_button.clicked.connect(self.cancel)
        self.directory_button.clicked.connect(self.get_directory)

    def get_directory(self):
        directory_name= QFileDialog.getExistingDirectory(self, "Choose Folder")
        if((directory_name =="")):
            return
        self.directory_line_edit.setText(directory_name)

    def cancel(self):
        self.reject()

    def confirm(self):
        self.dir_path = self.directory_line_edit.text() + "/" + self.project_name_line_edit.text()
        if((self.directory_line_edit.text()== "")):
            QMessageBox.warning(self,"Warning!",
                                        "The directory is not valid.",
                                        QMessageBox.Ok)
            return
        if((self.project_name_line_edit.text()== "")):
            QMessageBox.warning(self,"Warning!",
                                        "The project name is not valid.",
                                        QMessageBox.Ok)
            return
        
        dir = QDir(self.dir_path)
        if( dir.exists()):
            #Add Warning
            QMessageBox.warning(self,"Warning!",
                                        "The project folder already exists.",
                                        QMessageBox.Ok)
            pass
        else:
            if(dir.mkpath(self.dir_path)):
                #Add the project folder to the recent files
                recent_projects.add_to_recent_projects(self.directory_line_edit.text(),self.project_name_line_edit.text())
                self.accept()
            else:
                QMessageBox.warning(self,"Warning!",
                                        "The project name or the directory is not valid.",
                                        QMessageBox.Ok)

#Welcome page widget
class WelcomeWidget(QWidget,Ui_welcome_widget):
    #Signal to emit when welcome page gets hidden
    hidden_signal = Signal()
    #Initialize function
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.directory= ""
        #Initialize create project dialog to be used
        self.create_project_dialog = CreateProjectDialog()
        
        #Load and show recent project list
        global recent_projects
        recent_projects.read_file()

        self.model = QStringListModel()
        self.model.setStringList([', '.join(i) for i in recent_projects.list])
        self.recent_projects_list_view.setModel(self.model)

        self.create_project_button.clicked.connect(self.create_project)
        self.open_project_button.clicked.connect(self.open_project)
        self.recent_projects_list_view.doubleClicked.connect(self.open_recent_project)

    def create_project(self):
        self.create_project_dialog.exec()
        self.directory = self.create_project_dialog.dir_path
        if self.directory == "":
            return
        global current_project
        current_project = str(self.directory)

        global recent_projects
        recent_projects.add_to_recent_projects('/'.join(current_project.split('/')[:-1]),current_project.split('/')[-1])
        
        global WelcomeWidgetHidden
        WelcomeWidgetHidden = True
        self.hide()
    
    def open_project(self):
        self.directory= QFileDialog.getExistingDirectory(self, "Choose Folder")
        if self.directory == "":
            return
        global current_project
        current_project = str(self.directory)
        global recent_projects
        recent_projects.add_to_recent_projects('/'.join(current_project.split('/')[:-1]),current_project.split('/')[-1])
        
        global WelcomeWidgetHidden
        WelcomeWidgetHidden = True
        self.hide()

    def open_recent_project(self, index):
        global recent_projects
        item_text = self.model.data(index)
        self.directory = item_text.split(", ")[1]+"/"+item_text.split(", ")[0]
        if not QDir(self.directory).exists():
            QMessageBox.warning(self,"Warning!",
                                        "The project no longer exists.",
                                        QMessageBox.Ok)
            recent_projects.read_file()
            self.model = QStringListModel()
            self.model.setStringList([', '.join(i) for i in recent_projects.list])
            self.recent_projects_list_view.setModel(self.model)
            return     
        global current_project
        current_project = str(self.directory)

        recent_projects.add_to_recent_projects('/'.join(current_project.split('/')[:-1]),current_project.split('/')[-1])
        
        
        global WelcomeWidgetHidden
        WelcomeWidgetHidden = True
        self.hide()

        

    def hideEvent(self, event):
        super().hideEvent(event)
        self.hidden_signal.emit()

#The main window of the program
class MainWindow(QMainWindow,Ui_MainWindow):
    #Intialize function
    def __init__(self,app) -> None:
        super().__init__()
        self.setupUi(self)
        #Window title
        self.setWindowTitle("Project Schedulling Program")
        self.app = app
        
        #Directory of the chosen project
        self.directory= ""
        
        #Initialize create project dialog to be used
        self.create_project_dialog = CreateProjectDialog()
        
        #Initialize the welcome page to be used
        self.welcomePage = WelcomeWidget()
        
        #Initialize the main window with the welcome page widget
        self.setCentralWidget(self.welcomePage)

        #Connect functions to triggers / actions
        #Create project button from menu
        self.actionNew_Project.triggered.connect(self.create_project)
        #Open project button from menu
        self.actionOpen_Project.triggered.connect(self.open_project)
        #Exit program button from menu
        self.actionExit.triggered.connect(self.quit_app)
        #When welcome page gets hidden(because project was chosen), show the project page
        self.welcomePage.hidden_signal.connect(self.projectPage)


    def quit_app(self):
        self.app.quit()

    #Create a project folder
    def create_project(self):
        #Start the dialog for picking the location and the name of the folder
        self.create_project_dialog.exec()
        #Save the chosen directory
        self.directory = self.create_project_dialog.dir_path
        #If the directory was not chosen, do nothing
        if self.directory == "":
            return
        #Else
        #Save the current directory location
        global current_project
        current_project = str(self.directory)
        #Add project to recent list
        global recent_projects
        recent_projects.add_to_recent_projects('/'.join(current_project.split('/')[:-1]),current_project.split('/')[-1])
        
        #Hide welcome page
        try:
            self.welcomePage.hide()
            global WelcomeWidgetHidden
            WelcomeWidgetHidden = True
        except:
            pass
    
    #Choose project directory
    def open_project(self):
        #Choose folder
        self.directory= QFileDialog.getExistingDirectory(self, "Choose Folder")
        #If no folder was chosen, do nothing
        if self.directory == "":
            return
        try:
            self.viewTabsPage.close_project()
            self.setCentralWidget(QWidget())
            del self.viewTabsPage
        except:
            pass
        #Else save the project directory
        global current_project
        current_project = str(self.directory)
        #Add project to recent list
        global recent_projects
        recent_projects.add_to_recent_projects('/'.join(current_project.split('/')[:-1]),current_project.split('/')[-1])
        #Hide welcome page
        try:
            self.welcomePage.hide()
            global WelcomeWidgetHidden
            WelcomeWidgetHidden = True
        except:
            pass
        self.projectPage()
        

    #Display the project page.
    def projectPage(self):
        self.menuFile.setEnabled(False)
        global WelcomeWidgetHidden
        if WelcomeWidgetHidden == False:
            return
        #Read the settings from the project.ini file
        global projectINI
        global current_project
        #Open project.ini file
        try:
            projectINI.read_ini_file()
        #Create project.ini file if it does not exists
        except:
            projectINI.create_ini_file()
        #Check if the worker, jobs and task duration config files exist or are valid
        global workerCSVfile
        global jobCSVfile
        global taskDurationCSVfile
        config = []
        correct_settings = False
        while correct_settings == False:
            correct_settings = True
            config = projectINI.read_ini_file()
            if not (QFile(config.get('ProjectConfig', 'workerconfigfilepath')).exists) or config.get('ProjectConfig', 'workerconfigfilepath') == "":
                _config = configparser.ConfigParser()
                _config.read(current_project + '/' +'project.ini')

                # Change the value of 'key1' in 'Section1'
                _config['ProjectConfig']['workerconfigfilepath'] = current_project + '/' + "workerConfig.csv"

                # Write the updated configuration back to the file
                with open(current_project + '/' +'project.ini', 'w') as _configfile:
                    _config.write(_configfile)
                if _config.get('ProjectConfig', 'workerconfigfilepath') != "":
                    _file = QFile(_config.get('ProjectConfig', 'workerconfigfilepath'))
                    if not (_file.exists()):
                        workerCSVfile.create_csv_file(_config.get('ProjectConfig', 'workerconfigfilepath'))

            if not(QFile(config.get('ProjectConfig', 'jobconfigfilepath')).exists) or config.get('ProjectConfig', 'jobconfigfilepath') == "":
                _config = configparser.ConfigParser()
                _config.read(current_project + '/' +'project.ini')

                # Change the value of 'key1' in 'Section1'
                _config['ProjectConfig']['jobconfigfilepath'] = current_project + '/' + "jobsConfig.csv"

                # Write the updated configuration back to the file
                with open(current_project + '/' +'project.ini', 'w') as _configfile:
                    _config.write(_configfile)
                if _config.get('ProjectConfig', 'jobconfigfilepath') != "":
                    _file = QFile(_config.get('ProjectConfig', 'jobconfigfilepath'))
                    if not (_file.exists()):
                        jobCSVfile.create_csv_file(_config.get('ProjectConfig', 'jobconfigfilepath'))

            if not(QFile(config.get('ProjectConfig', 'taskdurationconfigfilepath')).exists) or config.get('ProjectConfig', 'taskdurationconfigfilepath') == "":
                _config = configparser.ConfigParser()
                _config.read(current_project + '/' +'project.ini')

                # Change the value of 'key1' in 'Section1'
                _config['ProjectConfig']['taskdurationconfigfilepath'] = current_project + '/' + "taskDurationConfig.csv"

                # Write the updated configuration back to the file
                with open(current_project + '/' +'project.ini', 'w') as _configfile:
                    _config.write(_configfile)
                if _config.get('ProjectConfig', 'taskdurationconfigfilepath') != "":
                    _file = QFile(_config.get('ProjectConfig', 'taskdurationconfigfilepath'))
                    if not (_file.exists()):
                        taskDurationCSVfile.create_csv_file(_config.get('ProjectConfig', 'taskdurationconfigfilepath'))
            
            config = projectINI.read_ini_file()
            
            try:
                workerCSVfile.chooseFile(config.get('ProjectConfig', 'workerconfigfilepath'))
            except:
                correct_settings = False
                QMessageBox.warning(self,"Warning!",
                                            "The file "+ config.get('ProjectConfig', 'workerconfigfilepath') + " does not has a valid format for the workers configuration. Please create a new file.",
                                            QMessageBox.Ok)
                
                _file_path, _ = QFileDialog.getSaveFileName(self, "Save CSV File", "", "CSV Files (*.csv)")
                if _file_path:
                    workerCSVfile.create_csv_file(_file_path)
                    
                    _config = configparser.ConfigParser()
                    _config.read(current_project + '/' +'project.ini')

                    # Change the value of 'key1' in 'Section1'
                    _config['ProjectConfig']['workerconfigfilepath'] = _file_path

                    # Write the updated configuration back to the file
                    with open(current_project + '/' +'project.ini', 'w') as _configfile:
                        _config.write(_configfile)
                else:
                    QMessageBox.warning(self,"Warning!",
                                            "The project requires a file for the workers configuration, the program will now close.",
                                            QMessageBox.Ok)
                    self.quit_app()
                    return
            try:
                jobCSVfile.chooseFile(config.get('ProjectConfig', 'jobconfigfilepath'))
            except:
                correct_settings = False
                QMessageBox.warning(self,"Warning!",
                                            "The file "+ config.get('ProjectConfig', 'jobconfigfilepath') + " does not has a valid format for the jobs configuration. Please create a new file.",
                                            QMessageBox.Ok)
                _file_path, _ = QFileDialog.getSaveFileName(self, "Save CSV File", "", "CSV Files (*.csv)")
                if _file_path:
                    jobCSVfile.create_csv_file(_file_path)
                    _config = configparser.ConfigParser()
                    _config.read(current_project + '/' +'project.ini')

                    # Change the value of 'key1' in 'Section1'
                    _config['ProjectConfig']['jobconfigfilepath'] = _file_path

                    # Write the updated configuration back to the file
                    with open(current_project + '/' +'project.ini', 'w') as _configfile:
                        _config.write(_configfile)
                else:
                    QMessageBox.warning(self,"Warning!",
                                            "The project requires a file for the jobs configuration, the program will now close.",
                                            QMessageBox.Ok)
                    self.quit_app()
                    return
                
            try:
                taskDurationCSVfile.chooseFile(config.get('ProjectConfig', 'taskdurationconfigfilepath'))
            except:
                correct_settings = False
                QMessageBox.warning(self,"Warning!",
                                            "The file "+ config.get('ProjectConfig', 'taskdurationconfigfilepath') + " does not has a valid format for the time duration configuration. Please create a new file.",
                                            QMessageBox.Ok)
                _file_path, _ = QFileDialog.getSaveFileName(self, "Save CSV File", "", "CSV Files (*.csv)")
                if _file_path:
                    taskDurationCSVfile.create_csv_file(_file_path)
                    _config = configparser.ConfigParser()
                    _config.read(current_project + '/' +'project.ini')

                    # Change the value of 'key1' in 'Section1'
                    _config['ProjectConfig']['taskdurationconfigfilepath'] = _file_path

                    # Write the updated configuration back to the file
                    with open(current_project + '/' +'project.ini', 'w') as _configfile:
                        _config.write(_configfile)
                else:
                    QMessageBox.warning(self,"Warning!",
                                            "The project requires a file for the time duration configuration, the program will now close.",
                                            QMessageBox.Ok)
                    self.quit_app()
                    return
        #Show the tabs for the different functions of the project page.
        self.viewTabsPage = ViewTabsWidget()
        self.setCentralWidget(self.viewTabsPage)