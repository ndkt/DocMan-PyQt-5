# Should print 1: Date | Document Number | Quantity
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5 import *

qtCreatorFile = "/home/ohm/Desktop/Programming/DocMan/v3/ui_files/documentManager.ui"
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

         #Find the sum of the total quantity.
         #Convert all elements in the list into an integer.
        #listOfQuantity = [int(qty) for qty in listOfQuantity]
        #sumOfQuantity = str((sum(listOfQuantity)))
        #self.ui.totalquantityLabel.setText("Total Quantity: " + sumOfQuantity)

        # Text Formatting for Output. Get values from inside the no duplicate list. 
        noDuplicatesListOfNumberKeys = [key + ": \n" for key in noDuplicatesListOfNumberKeys]
        noDuplicatesStringOfNumberKeys = ''.join(noDuplicatesListOfNumberKeys)
        
        # Text Formatting for Output. Get values from inside the no duplicate list. 
        #listOfDates = ["Dates: " + date + "\n" for date in listOfDates]
        #stringOfDates = ''.join(listOfDates)
        
        # Text Formatting for Output. Get values from inside the no duplicate list. 
        #listOfDocumentNumbers = [" | Document Number: " + docnum + "\n" for docnum in listOfDocumentNumbers]
        #stringOfDocumentNumbers = ''.join(listOfDocumentNumbers)
		
        # Text Formatting for Output. Get values from inside the no duplicate list. 
        # Convert all elements in the list back into a string.
        #listOfQuantity = [ str(qty) for qty in listOfQuantity ]
        #listOfQuantity = [" | Quantity: "+ qty + "\n" for qty in listOfQuantity]
        #stringOfQuantity = ''
        #stringOfQuantity = ''.join(stringOfQuantity)
	
 
        # Show Results
        self.ui.historyLabelNumbers.setText(noDuplicatesStringOfNumberKeys)
        #self.ui.historyLabelDates.setText(stringOfDates)
        #self.ui.historyLabelDocumentNumbers.setText(stringOfDocumentNumbers)
        #self.ui.historyLabelQuantity.setText(stringOfQuantity)

    def restartResetButton(self):
        pass

    def aboutButton(self):
        pass

    def editOldEntry(self):
        pass

    def deleteoldEntry(self):
        pass

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

