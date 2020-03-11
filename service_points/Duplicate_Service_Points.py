"""----------------------------------------------------------------------------------
Script Name:      Duplicate Service Points
Version:          1.1
Description:      This tool duplicates the features by the number of service points
                  in the "Count_F" field on that location.
Created By:       Kusasalethu Sithole
Date:             2020-03-11
Last Revision:    2020-03-11
----------------------------------------------------------------------------------"""
#Import Modules
import arcpy

# Request inputs
ws = arcpy.GetParameterAsText(0)
service_points = arcpy.GetParameterAsText(1)
Service_Count_Field = "Count_F"
duplicant_service_points = "final_service_points.shp"

#Set environment
arcpy.env.workspace = r'%s' % ws
arcpy.env.overwriteOutput = True

# Declare the field name that holds the Count_F value
Service_Count_Field = str(Service_Count_Field)

# Set the local variables
arcpy.CopyFeatures_management(service_points, duplicant_service_points)
duplicant_service_points_lyr = arcpy.MakeFeatureLayer_management(duplicant_service_points,"duplicant_service_points_lyr")

service_points_lyr = arcpy.MakeFeatureLayer_management(service_points,"service_points_lyr")
sourceCursor  = arcpy.SearchCursor(service_points_lyr)
inputCursor = arcpy.InsertCursor(duplicant_service_points_lyr)

# Perfom duplication
try:
    for row in sourceCursor:
        #Capture copy count from service layer
        counter = int(row.getValue(Service_Count_Field))

        #Copy row count number of times
        if counter > 1:
            for count in range(counter - 1):
                inputCursor.insertRow(row)

except:
    print(arcpy.GetMessages())