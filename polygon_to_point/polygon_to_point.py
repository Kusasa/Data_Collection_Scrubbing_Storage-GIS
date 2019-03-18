"""-----------------------------------------------------------------------------------------------------
Script Name:      Polygon to Point Tool
Version:          1.1
Description:      Converts polygons to points and then numbers them by:
                    - Exploding the multipart polygons,
                    - Adding column for polygon naming,
                    - Populating polygon naming column using numbering with POL code(i.e. POL1, POL2,...),
                    - Converting polygons to points,
                    - Adding column for point naming,
                    - Selecting and adding point number per polygon for each record.  
Created By:       Kusasalethu Sithole
Date:             2019-03-18
Last Revision:    2019-03-18
------------------------------------------------------------------------------------------------------"""

import arcpy

arcpy.env.overwriteOutput = True

# Request input of target shapefile
#polygon_layer = arcpy.GetParameterAsText(0)
polygon_layer = 'D:/Programming/Data/Inputs/District Municipality.shp'
polygon_singlepart_layer = 'C:/Users/Public/Documents/pol_sglpart.shp'
#points_layer = arcpy.GetParameterAsText(1)
points_layer = 'D:/Programming/Data/Outputs/pol_vertices.shp'

#Exploding the multipart polygons
arcpy.MultipartToSinglepart_management(polygon_layer, polygon_singlepart_layer)

#Adding column for polygon naming
arcpy.AddField_management(polygon_singlepart_layer, "POLYGON_NO", "TEXT", "#", "#", 20, "#", "NULLABLE", "NON_REQUIRED", "#")

#Populating polygon naming column using numbering with POL code(i.e. POL1, POL2,...) and Ceating a list of POLYGON_NO values
tblrows = arcpy.SearchCursor(polygon_singlepart_layer)
number = 1
polygon_numbers = []
fid = 0
fields = ("FID","POLYGON_NO")
with arcpy.UpdateCursor(polygon_singlepart_layer, fields) as Cursor:
        for row in Cursor:
            UpdateValue = 'POL' + str(number)
            polygon_numbers.append(UpdateValue)
            UpdateValue = '"' + UpdateValue + '"'
            if row[0]==fid:
                row[1] = UpdateValue
            Cursor.updateRow(row)
            fid += 1
            number += 1

#Converting polygons to points
arcpy.FeatureVerticesToPoints_management(polygon_singlepart_layer,points_layer,"ALL")

#Adding column for point naming
arcpy.AddField_management(points_layer, "POINT_NO", "TEXT", "#", "#", 20, "#", "NULLABLE", "NON_REQUIRED", "#")

#Selecting and adding point number per polygon for each record
point_layer_feature = arcpy.MakeFeatureLayer_management(points_layer,"point_layer_feature")

for index in range(len(polygon_numbers)):
    no = "'" + polygon_numbers[index] + "'"
    where_clause = '"POLYGON_NO"' + '='  + no
    arcpy.SelectLayerByAttribute_management(point_layer_feature, 'NEW_SELECTION', where_clause)
    
    n = 1
    fields = ("POINT_NO")
    with arcpy.UpdateCursor(point_layer_feature, fields) as Cursor:  
        for row in Cursor:
            value = "'" + str(polygon_numbers[index] + str(n)) + "'"
            row[0] = value
            Cursor.updateRow(row)
            n += 1

#delete intermediary polygon_singlepart_layer
arcpy.Delete_management(polygon_singlepart_layer)

