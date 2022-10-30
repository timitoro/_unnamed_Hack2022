#Perceptron.py
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.colors import ListedColormap
#from Perceptron_Class import Perceptron
import numpy as np
import pandas as pd
import catboost
from catboost import CatBoostClassifier, Pool
from sklearn.model_selection import train_test_split

class DemoGUIPerceptron(QMainWindow):   
    def __init__(self):       
        QMainWindow.__init__(self)
        loadUi("gui_interface.ui",self)

        self.setWindowTitle("_Unnamed_")
        self.setWindowIcon(QIcon('психология.jpg'))
        self.pbLoad.clicked.connect(self.display_data)
    #    self.addToolBar(NavigationToolbar(self.widgetData.canvas, self))
        self.sbLength.valueChanged.connect(self.display_data)


    def load_data(self):
        print(self.input.text())
        df = pd.read_excel(str(self.input.text()))
        df.drop(['Data'], axis=1, inplace=True)

        self.dataLength = self.sbLength.value()
        
        #display data on table
        self.display_table(df[:self.dataLength])
        
        #model
    #    model = CatBoostClassifier()
#
    #    model.load_model("model")
#
    #    results = model.predict(df.drop(['Class_label_FPG'], axis=1))
        
    def display_data(self): 
        self.load_data()

   #     dataHalf = int(self.dataLength/2)

        # plot data

   #     self.widgetData.canvas.axis1.clear()
   #     self.widgetData.canvas.axis1.scatter(self.X[:dataHalf, 0],\
   #         self.X[:dataHalf, 1],
   #         color='red', marker='o', label='setosa')
   #     self.widgetData.canvas.axis1.scatter(\
   #         self.X[dataHalf:self.dataLength, 0], \
   #         self.X[dataHalf:self.dataLength, 1],
   #         color='blue', marker='x', label='versicolor')
   #     self.widgetData.canvas.axis1.set_xlabel('sepal length [cm]')
   #     self.widgetData.canvas.axis1.set_ylabel('petal length [cm]')
   #     self.widgetData.canvas.axis1.legend(loc='upper left')
   #     self.widgetData.canvas.draw()

    def display_table(self,df):
        # show data on table widget

        self.write_df_to_qtable(df,self.tableData)
        self.tableData.setHorizontalHeaderLabels(['Name', 'Test_index', 'Presentation', 'Question', 'Class_label_FPG'])
        self.tableData.setColumnWidth(0, 300)
        self.tableData.setColumnWidth(1, 100)
        self.tableData.setColumnWidth(2, 100)
        self.tableData.setColumnWidth(3, 100)
        self.tableData.setColumnWidth(4, 140)

        
        styleH = "::section {""background-color: red; }"
        self.tableData.horizontalHeader().setStyleSheet(styleH)

        styleV = "::section {""background-color: yellow; }"
        self.tableData.verticalHeader().setStyleSheet(styleV)        

        
    # Takes a df and writes it to a qtable provided. df headers become qtable headers
    @staticmethod
    def write_df_to_qtable(df,table):
        table.setRowCount(df.shape[0])
        table.setColumnCount(df.shape[1])       

        # getting data from df is computationally costly so convert it to array first
        df_array = df.values
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                table.setItem(row, col, \
                    QTableWidgetItem(str(df_array[row,col])))


if __name__ == '__main__':
    import sys

 #   df = pd.read_excel("dataset_train.xls")
 #   X = df.drop(['Obfuscated name', 'Test_index', 'Class_label_FPG', 'Data'], axis=1)
 #   y = df['Class_label_FPG']
#
 #   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
 #   X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, train_size=0.5, random_state=42, stratify=y_test)
 #   cat_features = [0, 1]
 #   train_dataset = Pool(data=X_train,
 #                        label=y_train,
 #                        cat_features=cat_features)
 #   validate_dataset = Pool(data=X_val,
 #                           label=y_val,
 #                           cat_features=cat_features)
 #   test_dataset = Pool(data=X_test,
 #                       label=y_test,
 #                       cat_features=cat_features)
#
#
#
 #   model = CatBoostClassifier()
#
 #   model.load_model("model")
#
 #   results = model.predict(test_dataset)
 #   print(results)

    app = QApplication(sys.argv)
    ex = DemoGUIPerceptron()
    ex.show()
    sys.exit(app.exec_())