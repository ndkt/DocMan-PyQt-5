# Should print 1: Date | Document Number | Quantity
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit, QInputDialog
from PyQt5 import uic
from PyQt5 import *

qtCreatorFile = "/home/ohm/Desktop/Programming/DocMan/v5/ui_files/documentManager.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# Declare all variable.
# i=0 when program start.
i = 0
# Declare a dictionary called "d"
d = {}
global listOfNumberKeys
global listOfDates
global listOfDocumentNumbers
global listOfQuantity
listOfNumberKeys = []
listOfDates = []
listOfDocumentNumbers = []
listOfQuantity = []


class MyApp(QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Connect this button to a function called "selectdatetodelete"
        self.ui.dataNumberDeletionButton.clicked.connect(self.selectdatanumberToDelete)
        # Connect this button to a function called "createNewEntry"
        self.ui.submitButton.clicked.connect(self.createNewEntry)


        # New Row of Values
    def createNewEntry(self):
        # Each time the button is pressed, a new (i) key will be created inside the dictionary.
        # The (i) key will be incremented by one each time the button is pressed.
        global i
        i += 1
        d[i] = []
        # Get date information and converting the date into a string.
        dateUnformatted = self.ui.dateBox.date()
        dateFormatted = str(dateUnformatted.toPyDate())
        # Add recently entered user input date into list of dates.
        #listOfDates = []
        print("LIST OF DATES: " + str(listOfDates))
        listOfDates.append((dateFormatted))
        # Add value of dateFormatted into list value of the number key.
        d[i].append(str(dateFormatted))
        # Get document number information and converting the document number into a string
        # Add # in front of output.
        # Add recently entered user input docnmum into list of docnum.
        listOfDocumentNumbers.append(str(self.ui.documentNumberBox.text()))
        userInputDocumentNumber = "#" + str(self.ui.documentNumberBox.text())
        # Add value of userInputDocumentNumber into list value of the number
        # key.
        d[i].append(userInputDocumentNumber)
        # Add recently entered user input quantity into list of quantity.
        #listOfQuantity = []
        listOfQuantity.append(str(self.ui.qtyBox.text()))
        # Get quantity information and converting the quantity into a string.
        userInputQuantity = str(self.ui.qtyBox.text())
        # Add value of userInputQuantity into list value of the number key.
        d[i].append(userInputQuantity)


        print("Print out the dictionary:  " + str(d))
        print("Printing out user input date:"+ str(listOfDates))
        print("Printing out user input docnum: " + str(listOfDocumentNumbers))
        print("Printing out user input quantity number: " + str(listOfQuantity))
        
        

         # For each key value pairs inside dictionary. Append the values into a new list.
        for k, v in d.items():
            listOfNumberKeys.append(str(k))

        # Create a list of number keys removing duplicate values.
        noDuplicatesListOfNumberKeys = list(dict.fromkeys(listOfNumberKeys))
        
        # Create a list of date removing duplicate values.
        newListOfDates = listOfDates
       
        # Create a list of document number removing duplicate values.
        newListOfDocumentNumbers = listOfDocumentNumbers
      
        # Create a list of quantity keys removing duplicate values.
        newListOfQuantity = listOfQuantity
         

         #Find the sum of the total quantity.
         #Convert all elements in the list into an integer.
        #listOfQuantity = [int(qty) for qty in listOfQuantity]
        #sumOfQuantity = str((sum(listOfQuantity)))
        #self.ui.totalquantityLabel.setText("Total Quantity: " + sumOfQuantity)

        # Text Formatting for Output. Get values from inside the no duplicate list. 
        noDuplicatesListOfNumberKeys = ["Data Number " + key + ": \n" for key in noDuplicatesListOfNumberKeys]
        noDuplicatesStringOfNumberKeys = ''.join(noDuplicatesListOfNumberKeys)
        
        # Text Formatting for Output. Get values from inside the no duplicate list. 
        newListOfDates = ["Dates: " + date + "\n" for date in newListOfDates]
        stringOfDates = ''.join(newListOfDates)
        
        # Text Formatting for Output. Get values from inside the no duplicate list. 
        newListOfDocumentNumbers = [" | Document Number: " + docnum + "\n" for docnum in newListOfDocumentNumbers]
        stringOfDocumentNumbers = ''.join(newListOfDocumentNumbers)
		
        # Text Formatting for Output. Get values from inside the no duplicate list. 
        # Convert all elements in the list back into a string.
        newListOfQuantity = [ str(qty) for qty in newListOfQuantity ]
        newListOfQuantity = [" | Quantity: "+ qty + "\n" for qty in newListOfQuantity]
        stringOfQuantity = ''.join(newListOfQuantity)
	
 
        # Show Results
        self.ui.historyLabelNumbers.setText(noDuplicatesStringOfNumberKeys)
        self.ui.historyLabelDates.setText(stringOfDates)
        self.ui.historyLabelDocumentNumbers.setText(stringOfDocumentNumbers)
        self.ui.historyLabelQuantity.setText(stringOfQuantity)

    def restartResetButton(self):
        pass

    def aboutButton(self):
        pass

    def editOldEntry(self):
        pass

    def selectdatanumberToDelete(self):
        user_input_datanumber, ok = QInputDialog.getText(self, 'Enter data number to Delete', 'Enter data number:\n')


        if len(user_input_datanumber) != 1:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR!")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please enter a 1 digit number!")
            x = msg.exec_()
        if len(user_input_datanumber) == 1:
            del d[int(user_input_datanumber)]
            new_d = d
            del listOfNumberKeys[int(user_input_datanumber)-1]
            del listOfDocumentNumbers[int(user_input_datanumber)-1]
            del listOfDates[int(user_input_datanumber)-1]
            del listOfQuantity[int(user_input_datanumber)-1]
                # Create a list of number keys removing duplicate values.
            noDuplicatesListOfNumberKeys = list(dict.fromkeys(listOfNumberKeys))
            
            # Create a list of date removing duplicate values.
            newListOfDates = listOfDates
           
            # Create a list of document number removing duplicate values.
            newListOfDocumentNumbers = listOfDocumentNumbers
          
            # Create a list of quantity keys removing duplicate values.
            newListOfQuantity = listOfQuantity
             

             #Find the sum of the total quantity.
             #Convert all elements in the list into an integer.
            #listOfQuantity = [int(qty) for qty in listOfQuantity]
            #sumOfQuantity = str((sum(listOfQuantity)))
            #self.ui.totalquantityLabel.setText("Total Quantity: " + sumOfQuantity)

            # Text Formatting for Output. Get values from inside the no duplicate list. 
            noDuplicatesListOfNumberKeys = [int(x) for x in noDuplicatesListOfNumberKeys]
            noDuplicatesListOfNumberKeys = [x-1 for x in noDuplicatesListOfNumberKeys]
            noDuplicatesListOfNumberKeys = [str(x) for x in noDuplicatesListOfNumberKeys]
            noDuplicatesListOfNumberKeys = ["Data Number " + key + ": \n" for key in noDuplicatesListOfNumberKeys]
            noDuplicatesStringOfNumberKeys = ''.join(noDuplicatesListOfNumberKeys)
            
            # Text Formatting for Output. Get values from inside the no duplicate list. 
            newListOfDates = ["Dates: " + date + "\n" for date in newListOfDates]
            stringOfDates = ''.join(newListOfDates)
            
            # Text Formatting for Output. Get values from inside the no duplicate list. 
            newListOfDocumentNumbers = [" | Document Number: " + docnum + "\n" for docnum in newListOfDocumentNumbers]
            stringOfDocumentNumbers = ''.join(newListOfDocumentNumbers)
            
            # Text Formatting for Output. Get values from inside the no duplicate list. 
            # Convert all elements in the list back into a string.
            newListOfQuantity = [ str(qty) for qty in newListOfQuantity ]
            newListOfQuantity = [" | Quantity: "+ qty + "\n" for qty in newListOfQuantity]
            stringOfQuantity = ''.join(newListOfQuantity)

            # Show New Results
            self.ui.historyLabelNumbers.setText(noDuplicatesStringOfNumberKeys)
            self.ui.historyLabelDates.setText(stringOfDates)
            self.ui.historyLabelDocumentNumbers.setText(stringOfDocumentNumbers)
            self.ui.historyLabelQuantity.setText(stringOfQuantity)

            print(new_d)

        


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


"""
# Test Values:

Date: 1/1/2020  Doc 1000    Qty: 10
Date: 2/1/2020  Doc 1001    Qty: 20
Date: 3/1/2020  Doc 1002    Qty: 30
Date: 4/1/2020  Doc 1003  
Date: 5/1/2020  Doc 1004
Date: 6/1/2020
Date: 7/1/2020
Date: 8/1/2020
Date: 9/1/2020 

"""

