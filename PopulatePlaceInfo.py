# Program populates the political location references of the geometric objects of a target shapefile

import arcpy
arcpy.env.overwriteOutput = True


# Request input of target layer and declare its shp and dbf files
#print("Enter workspace path")
#workspace = raw_input()
#arcpy.env.workspace = workspace
arcpy.env.workspace = "C:/Users/User/Documents/Programming/Data/Outputs"

# Declare target and source shapefile names
target_shp = "TargetFile.shp"
target_dbf = "TargetFile.dbf"

source_shp = "PolBounds.shp"
source_dbf = "PolBounds.dbf"

# Declare the field names that need to be copied from the source layer to the target layer
target_fields = ["LOCAL_MUNI", "DISTR_MUNI", "PROVINCE", "COUNTRY"]
source_fields = target_fields

# Set the local variables
target_feat_lyr = arcpy.MakeFeatureLayer_management(target_shp,"target_feat_lyr")
source_feat_lyr = arcpy.MakeFeatureLayer_management(source_shp,"source_feat_lyr")
tblrows = arcpy.SearchCursor(source_feat_lyr)

# Perfom selections and corresponding copying of values across respective fields of source and target layers
try:
    n = 0
    for places in source_fields:

        for row in tblrows:
            #Declare value to be copied from source layer
            UpdateValue = row.getValue(source_fields[n])
            UpdateValue = str(UpdateValue)
            UpdateValue = '"' + UpdateValue + '"'
            print (UpdateValue)

            #select source by attribute using search cursor
            where_clause = "'" + '"' + target_fields[n] + '"' + '==' + UpdateValue + "'"
            print(where_clause)
            arcpy.SelectLayerByAttribute_management (source_feat_lyr, "NEW_SELECTION", where_clause)

            #select target by location using intersection with source selection
            arcpy.SelectLayerByLocation_management (target_feat_lyr, "HAVE_THEIR_CENTER_IN", source_feat_lyr, "#", "REMOVE_FROM_SELECTION","NOT_INVERT")

            #Copy value into selection
            print(target_dbf)
            arcpy.CalculateField_management(target_feat_lyr, target_fields[n], UpdateValue, "PYTHON", "#")
            

        n += 1
    arcpy.CopyFeatures_management(target_feat_lyr, target_shp)

except:
    print(arcpy.GetMessages())

print("Process Complete: target fields populated in the target shapefile")


