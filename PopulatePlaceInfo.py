# Program populates the political location references of the geometric objects of a target shapefile

import arcpy, os

# Request input of workspace
ws = raw_input('Enter workspace path (NB use forward slash delineators)\n')
os.chdir(ws.replace("\r", ""))
arcpy.env.workspace = r'%s' % ws

def attributePopulate (target_field):
    arcpy.env.overwriteOutput = True
    
    # Declare target and source shapefile names
    target_shp = "TargetFile.shp"
    target_dbf = "TargetFile.dbf"
    source_shp = "PolBounds.shp"
    source_dbf = "PolBounds.dbf"

    # Declare the field names that need to be copied from the source layer to the target layer
    target_field = str(target_field)
    source_field = target_field

    # Set the local variables
    target_feat_lyr = arcpy.MakeFeatureLayer_management(target_shp,"target_feat_lyr")
    source_feat_lyr = arcpy.MakeFeatureLayer_management(source_shp,"source_feat_lyr")
    tblrows = arcpy.SearchCursor(source_feat_lyr)

    # Perfom selections and corresponding copying of values across respective fields of source and target layers
    try:

        for row in tblrows:
            #Declare value to be copied from source layer
            UpdateValue = row.getValue(source_field)
            UpdateValue = UpdateValue.replace("'", "") 
            UpdateValue = UpdateValue.replace("!", "")
            UpdateValue = "'" + UpdateValue + "'"

            #select source by attribute using search cursor
            where_clause = target_field + " = " + UpdateValue
            arcpy.SelectLayerByAttribute_management (source_feat_lyr, "NEW_SELECTION", where_clause)

            #select target by location using intersection with source selection
            arcpy.SelectLayerByLocation_management (target_feat_lyr, "HAVE_THEIR_CENTER_IN", source_feat_lyr, "#", "NEW_SELECTION","NOT_INVERT")

            #Copy value into selection
            arcpy.CalculateField_management(target_feat_lyr, target_field, UpdateValue, "PYTHON", "#")

    except:
        print(arcpy.GetMessages())
    
targets = ["LOCAL_MUNI", "DISTR_MUNI", "PROVINCE", "COUNTRY"]
for target in targets:
        attributePopulate (target)

print("Process Complete: target fields populated in the target shapefile")