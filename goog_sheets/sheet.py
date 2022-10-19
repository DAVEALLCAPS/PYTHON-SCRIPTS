import ezsheets

ss = ezsheets.createSpreadsheet(title='My New Spreadsheet')
sh = ss.sheets[0]
sh.updateRow(1, ['Name', 'Species', 'Color', 'Weight'])
sh.updateRow(2, ('Zophie', 'Cat', 'Gray', 11))