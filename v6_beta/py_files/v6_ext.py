#!/usr/bin/python
# -*- coding: utf-8 -*-


def eraseDataandShowResult(self):
    del d[int(user_input_datanumber)]
    new_d = d
    del listOfNumberKeys[int(user_input_datanumber) - 1]
    del listOfDocumentNumbers[int(user_input_datanumber) - 1]
    del listOfDates[int(user_input_datanumber) - 1]
    del listOfQuantity[int(user_input_datanumber) - 1]

    # Create a list of number keys removing duplicate values.

    noDuplicatesListOfNumberKeys = list(dict.fromkeys(listOfNumberKeys))

    # Create a list of date removing duplicate values.

    newListOfDates = listOfDates

    # Create a list of document number removing duplicate values.

    newListOfDocumentNumbers = listOfDocumentNumbers

    # Create a list of quantity keys removing duplicate values.

    newListOfQuantity = listOfQuantity

    # Find the sum of the total quantity.
    # Convert all elements in the list into an integer.
    # listOfQuantity = [int(qty) for qty in listOfQuantity]
    # sumOfQuantity = str((sum(listOfQuantity)))
    # self.ui.totalquantityLabel.setText("Total Quantity: " + sumOfQuantity)

    # Text Formatting for Output. Get values from inside the no duplicate list.

    noDuplicatesListOfNumberKeys = [int(x) for x in noDuplicatesListOfNumberKeys]
    noDuplicatesListOfNumberKeys = [x - 1 for x in noDuplicatesListOfNumberKeys]
    noDuplicatesListOfNumberKeys = [str(x) for x in noDuplicatesListOfNumberKeys]
    noDuplicatesListOfNumberKeys = [
        "Data Number " + key + ": \n" for key in noDuplicatesListOfNumberKeys
    ]
    noDuplicatesStringOfNumberKeys = "".join(noDuplicatesListOfNumberKeys)

    # Text Formatting for Output. Get values from inside the no duplicate list.

    newListOfDates = ["Dates: " + date + "\n" for date in newListOfDates]
    stringOfDates = "".join(newListOfDates)

    # Text Formatting for Output. Get values from inside the no duplicate list.

    newListOfDocumentNumbers = [
        " | Document Number: " + docnum + "\n" for docnum in newListOfDocumentNumbers
    ]
    stringOfDocumentNumbers = "".join(newListOfDocumentNumbers)

    # Text Formatting for Output. Get values from inside the no duplicate list.
    # Convert all elements in the list back into a string.

    newListOfQuantity = [str(qty) for qty in newListOfQuantity]
    newListOfQuantity = [" | Quantity: " + qty + "\n" for qty in newListOfQuantity]
    stringOfQuantity = "".join(newListOfQuantity)

    # Show New Results

    self.ui.historyLabelNumbers.setText(noDuplicatesStringOfNumberKeys)
    self.ui.historyLabelDates.setText(stringOfDates)
    self.ui.historyLabelDocumentNumbers.setText(stringOfDocumentNumbers)
    self.ui.historyLabelQuantity.setText(stringOfQuantity)

    print(new_d)
