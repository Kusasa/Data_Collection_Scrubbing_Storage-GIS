# Program populates the centroids' x and y values of the geometric objects of a target shapefile
import arcpy


# Request input of target shapefile and direct python to its dbf file
print("Enter absolute path of shapefile (NB: exclude extension of file)")
layer = raw_input()
layer = layer + ".dbf"

# Expression
express = """IfBlock(!NAME!,!SUFFIX!)"""

# Codeblock
code = """def IfBlock(roadprefix, roadsuffix):
    if roadprefix[0].isdigit():
        return roadprefix.lower() + " " + roadsuffix.title()
    else:
        return roadprefix.title() + " " + roadsuffix.title()"""

# Populate field
arcpy.CalculateField_management(layer, "SUBURB", express, "PYTHON_9.3", 
                                code)
