import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5 import *

qtCreatorFile = "/home/ohm/Desktop/Programming/DocMan/v1/ui_files/documentManager.ui"
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
        # Add value of dateFormatted into list value of the number key.
        d[i].append(dateFormatted)
        # Get document number information and converting the document number into a string
        # Add # in front of output.
        userInputDocumentNumber = "#" + str(self.ui.documentNumberBox.text())
        # Add value of userInputDocumentNumber into list value of the number
        # key.
        d[i].append(userInputDocumentNumber)
        # Get quantity information and converting the quantity into a string.
        userInputQuantity = str(self.ui.qtyBox.text())
        # Add value of userInputQuantity into list value of the number key.
        d[i].append(userInputQuantity)

        #Print Dictionary to Terminal
        print(d)

        # For each key value pairs inside dictionary. Append the values into a new list.
        for k, v in d.items():
            listOfDates.append(str(v[0]))
            listOfDocumentNumbers.append(str(v[1]))
            listOfQuantity.append(str(v[2]))
            listOfNumberKeys.append(str(k))

        # Create a list of number keys removing duplicate values.
        noDuplicatesListOfNumberKeys = list(dict.fromkeys(listOfNumberKeys))
        
        # Create a list of date removing duplicate values.
        noDuplicatesListOfDates = list(dict.fromkeys(listOfDates))
       
        # Create a list of document number removing duplicate values.
        noDuplicatesListOfDocumentNumbers = list(dict.fromkeys(listOfDocumentNumbers))
       
        # Create a list of quantity keys removing duplicate values.
        noDuplicatesListOfQuantity = list(dict.fromkeys(listOfQuantity))  

        # Find the sum of the total quantity.
        # Convert all elements in the list into an integer.
        noDuplicatesListOfQuantity = [int(qty) for qty in noDuplicatesListOfQuantity]
        sumOfQuantity = str((sum(noDuplicatesListOfQuantity)))
        self.ui.totalquantityLabel.setText("Total Quantity: " + sumOfQuantity)
        

        # Text Formatting for Output. Get values from inside the no duplicate list. 
        noDuplicatesListOfNumberKeys = [key + ": \n" for key in noDuplicatesListOfNumberKeys]
        noDuplicatesStringOfNumberKeys = ''.join(noDuplicatesListOfNumberKeys)

        # Text Formatting for Output. Get values from inside the no duplicate list. 
        noDuplicatesListOfDates = ["Date: " + date + "\n" for date in noDuplicatesListOfDates]
        noDuplicatesStringOfDates = ''.join(noDuplicatesListOfDates)
        
        # Text Formatting for Output. Get values from inside the no duplicate list. 
        noDuplicatesListOfDocumentNumbers = [" | Document Number: " + docnum + "\n" for docnum in noDuplicatesListOfDocumentNumbers]
        noDuplicatesStringOfDocumentNumbers = ''.join(noDuplicatesListOfDocumentNumbers)

        # Text Formatting for Output. Get values from inside the no duplicate list. 
        # Convert all elements in the list back into a string.
        noDuplicatesListOfQuantity = [ str(qty) for qty in noDuplicatesListOfQuantity ]
        noDuplicatesListOfQuantity = [" | Quantity: "+ qty + "\n" for qty in noDuplicatesListOfQuantity]
        noDuplicatesStringOfQuantity = ''.join(noDuplicatesListOfQuantity)

        # Show Results
        self.ui.historyLabelNumbers.setText(noDuplicatesStringOfNumberKeys)
        self.ui.historyLabelDates.setText(noDuplicatesStringOfDates)
        self.ui.historyLabelDocumentNumbers.setText(noDuplicatesStringOfDocumentNumbers)
        self.ui.historyLabelQuantity.setText(noDuplicatesStringOfQuantity)
        
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



# Test Values:
"""
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