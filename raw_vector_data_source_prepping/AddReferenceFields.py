"""----------------------------------------------------------------------------------
Script Name:      Adds Reference Fields
Version:          1.1
Description:      This tool adds reference fields into the target shapefile.
Created By:       Kusasalethu Sithole
Date:             2018-11-27
Last Revision:    2019-01-27
----------------------------------------------------------------------------------"""

import arcpy


# Request input of target shapefile
target_layer = arcpy.GetParameterAsText(0)

#Add field - suburb
arcpy.AddField_management(target_layer, "FEATURE", "TEXT", "#", "#", 10, "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - suburb
arcpy.AddField_management(target_layer, "SUBURB", "TEXT", "#", "#", 40, "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - local municipality
arcpy.AddField_management(target_layer, "LOCAL_MUNI", "TEXT", "#", "#", 40, "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - district municipality
arcpy.AddField_management(target_layer, "DISTR_MUNI", "TEXT", "#", "#", 40, "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - province
arcpy.AddField_management(target_layer, "PROVINCE", "TEXT", "#", "#", 40, "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - country
arcpy.AddField_management(target_layer, "COUNTRY", "TEXT", "#", "#", 40, "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - cent_x
arcpy.AddField_management(target_layer, "CENT_X", "DOUBLE", 30, 15, "#", "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - cent_y
arcpy.AddField_management(target_layer, "CENT_Y", "DOUBLE", 30, 15, "#", "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - recno
arcpy.AddField_management(target_layer, "RECNO", "TEXT", "#", "#", 40, "#", "NULLABLE", "NON_REQUIRED", "#")

print("Process Complete: reference fields added into the target shapefile")
