"""----------------------------------------------------------------------------------
Script Name:      Generate Centroid X and Y
Version:          1.1
Description:      This tool generates the centroids' x and y values of the geometric
                  objects of a target shapefile.
Created By:       Kusasalethu Sithole
Date:             2018-12-03
Last Revision:    2019-01-27
----------------------------------------------------------------------------------"""
 
import arcpy


# Request input of target shapefile
layer = arcpy.GetParameterAsText(0)

#calculate CENT_X field
arcpy.CalculateField_management(layer, "CENT_X", "!SHAPE.CENTROID.X!", "PYTHON_9.3")

#calculate CENT_Y field
arcpy.CalculateField_management(layer, "CENT_Y", "!SHAPE.CENTROID.Y!", "PYTHON_9.3")

print("Process Complete: CENT X and Y fields populated in the target shapefile")
