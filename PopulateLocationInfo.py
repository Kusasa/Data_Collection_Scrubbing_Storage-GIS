# Program populates the locational references of the geometric objects of a target shapefile

import arcpy


# Request input of target layer and declare its shp and dbf files
print("Enter absolute path of target layer (NB: exclude extension of file)")
target_layer = raw_input()
target_shp = target_layer + ".shp"
target_dbf = target_layer + ".dbf"

#Request name of the field that needs to be populated in the target layer
print("Enter name of the field that needs to be populated in the target layer")
target_fieldname = raw_input()
target_field = "!" + target_fieldname + "!"

# Request input of source layer and declare its dbf files
print("Enter absolute path of source layer (NB: exclude extension of file)")
source_layer = raw_input()
source_dbf = source_layer + ".dbf"

# Set local variables
target_feat_lyr = arcpy.MakeFeatureLayer_management(target_dbf, "target_feat_lyr")
source_feat_lyr = arcpy.MakeFeatureLayer_management(source_dbf,"source_feat_lyr")
tblrow = arcpy.SearchCursor(source_feat_lyr,'PROVINCE')  


# Populate the target field of the target layer
try:
    for row in tblrow:
        #select source by attribute using search cursor
        arcpy.SelectLayerByAttribute_management (source_feat_lyr, "NEW_SELECTION")
    
        #select target by location using intersection
        arcpy.SelectLayerByLocation_management (target_feat_lyr, "HAVE_THEIR_CENTER_IN", source_feat_lyr, "#", "NEW_SELECTION", "NOT_INVERT")

        #Declare value to be copied accross
        UpdateValue = row['PROVINCE']

        #Copy value into selection
        arcpy.CalculateField_management(target_dbf, target_field, UpdateValue, "PYTHON")


    print("Process Complete: target field populated in the target shapefile")

except:
    print(arcpy.GetMessages())
