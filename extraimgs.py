#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     22/05/2022
# Copyright:   (c) User 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from PIL import ImageGrab
import win32com.client as win32
import os
def main():
    excel = win32.Dispatch("Excel.Application")
    workbook = excel.Workbooks.Open(r'C:\Excel\REGPARTIES.xlsx')

    wb_folder = workbook.Path
    wb_name = workbook.Name
    wb_path = os.path.join(wb_folder, wb_name)

    #print "Extracting images from %s" % wb_path
    print("Extracting images from", wb_path)

    image_no = 0

    for sheet in workbook.Worksheets:

        for n, shape in enumerate(sheet.Shapes):
            ##print(dir(shape.TopLeftCell))
            row, col = shape.TopLeftCell.Row, shape.TopLeftCell.Column
            imgname = sheet.Cells(row,4).Value

            ##print(shape.TopLeftCell.Cell)
            if shape.Name.startswith("image"):
                # Some debug output for console
                image_no += 1
                print("---- Image No. %07i ----", image_no)

                # Sequence number the pictures, if there's more than one
                num = "" if n == 0 else "_%03i" % n

                filename = imgname +".png"
                file_path = os.path.join (wb_folder, filename)

                #print "Saving as %s" % file_path    # Debug output
                print('Saving as ', file_path)

                shape.Copy() # Copies from Excel to Windows clipboard

                # Use PIL (python imaging library) to save from Windows clipboard
                # to a file
                image = ImageGrab.grabclipboard()
                image.save(file_path,'png')
            else:
                print("Nothing found >><<"+shape.Name)
if __name__ == '__main__':
    main()
