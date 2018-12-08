# Program populates the centroids' x and y values of the geometric objects of a target shapefile
import arcpy


# Request input of target shapefile and direct python to its dbf file
print("Enter absolute path of shapefile (NB: exclude extension of file)")
layer = raw_input()
layer = layer + ".dbf"

#calculate CENT_X field
arcpy.CalculateField_management(layer, "CENT_X", "!SHAPE.CENTROID.X!", "PYTHON_9.3")

#calculate CENT_Y field
arcpy.CalculateField_management(layer, "CENT_Y", "!SHAPE.CENTROID.Y!", "PYTHON_9.3")

print("Process Complete: CENT X and Y fields populated in the target shapefile")
