# Program adds reference fields into the target shapefile
import arcpy


# Request input of target shapefile and direct python to its dbf file
print("Enter absolute path of shapefile (NB: exclude extension of file)")
layer = raw_input()
layer = layer + ".dbf"

#Add field - suburb
arcpy.AddField_management(layer, "SUBURB", "TEXT", "#", "#", 40, "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - local municipality
arcpy.AddField_management(layer, "LOCAL_MUNI", "TEXT", "#", "#", 40, "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - district municipality
arcpy.AddField_management(layer, "DISTR_MUNI", "TEXT", "#", "#", 40, "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - province
arcpy.AddField_management(layer, "PROVINCE", "TEXT", "#", "#", 40, "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - country
arcpy.AddField_management(layer, "COUNTRY", "TEXT", "#", "#", 40, "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - cent_x
arcpy.AddField_management(layer, "CENT_X", "DOUBLE", 30, 15, "#", "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - cent_y
arcpy.AddField_management(layer, "CENT_Y", "DOUBLE", 30, 15, "#", "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - recno
arcpy.AddField_management(layer, "RECNO", "TEXT", "#", "#", 40, "#", "NULLABLE", "NON_REQUIRED", "#")

#Add field - ekhayaID
arcpy.AddField_management(layer, "EKHAYA_ID", "TEXT", "#", "#", 40, "#", "NULLABLE", "NON_REQUIRED", "#")

print("Process Complete: reference fields added into the target shapefile")
