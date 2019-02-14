# Program populates the centroids' x and y values of the geometric objects of a target shapefile
import arcpy


# Request input of target shapefile
layer = arcpy.GetParameterAsText(0)

#calculate CENT_X field
arcpy.CalculateField_management(layer, "CENT_X", "!SHAPE.CENTROID.X!", "PYTHON_9.3")

#calculate CENT_Y field
arcpy.CalculateField_management(layer, "CENT_Y", "!SHAPE.CENTROID.Y!", "PYTHON_9.3")

print("Process Complete: CENT X and Y fields populated in the target shapefile")
