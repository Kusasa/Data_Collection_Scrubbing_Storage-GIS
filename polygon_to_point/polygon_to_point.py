"""--------------------------------------------------------------------------
Script Name:      Polygon to Point Tool
Version:          1.1
Description:      Converts polygons to points and gives them ordered and 
                  unique identifiers by:
                    - Exploding its multipart polygons,
                    - Creating unique polygon names(i.e. POL1, POL2,...),
                    - Converting the polygons to points,
                    - And creating unique and ordered point names within each 
                      corresponding polygon (i.e. POL21, POL22, POL23...).  
Created By:       Kusasalethu Sithole
Date:             2019-03-18
Last Revision:    2019-07-05
-----------------------------------------------------------------------------"""

import bk_logger

#Set environment
arcpy.env.overwriteOutput = True

#Request input of target shapefile
polygon_layer = arcpy.GetParameterAsText(0)
polygon_singlepart_layer = polygon_layer[:-4] + "_sglprt" + polygon_layer[-4:]
points_layer = arcpy.GetParameterAsText(1)
logger_directory = arcpy.GetParameterAsText(2)

#Define logger
logger = bk_logger.defineLogger(logger_directory)

try:
    startTime = bk_logger.currentSecondsTime()

    #Exploding the multipart polygons
    bk_logger.log("\t \t Step 1: Exploding the multipart polygons \n")
    arcpy.MultipartToSinglepart_management(polygon_layer, polygon_singlepart_layer)

    #Adding column for polygon naming
    bk_logger.log("\t \t Step 2: Adding column for polygon naming \n")
    arcpy.AddField_management(polygon_singlepart_layer, "POLYGON_NO", "TEXT", "#", "#", 20, "#", "NULLABLE", "NON_REQUIRED", "#")

    #Populating polygon naming column using numbering with POL code(i.e. POL1, POL2,...) and Ceating a list of POLYGON_NO values
    bk_logger.log("\t \t Step 3: Populating polygon naming column using numbering with POL code(i.e. POL1, POL2,...) and Ceating a list of POLYGON_NO values \n")

    number = 1
    polygon_numbers = []
    fid = 0
    fields = ("FID","POLYGON_NO")
    with arcpy.da.UpdateCursor(polygon_singlepart_layer, fields) as Cursor:   #@UndefinedVariable
            for row in Cursor:
                UpdateValue = "POL" + str(number)
                polygon_numbers.append(UpdateValue)
                if row[0]==fid:
                    row[1] = UpdateValue
                Cursor.updateRow(row)
                fid += 1
                number += 1

    del Cursor

    #Converting polygons to points
    bk_logger.log("\t \t Step 4: Converting polygons to points \n")
    arcpy.FeatureVerticesToPoints_management(polygon_singlepart_layer,points_layer,"ALL")

    #Adding column for point naming
    bk_logger.log("\t \t Step 5: Adding column for point naming \n")
    arcpy.AddField_management(points_layer, "POINT_NO", "TEXT", "#", "#", 20, "#", "NULLABLE", "NON_REQUIRED", "#")

    #Selecting and adding point number per polygon for each record
    bk_logger.log("\t \t Step 6: Selecting and adding point number per polygon for each record \n")

    for index in range(len(polygon_numbers)):
        n = 1
        columns = ("POLYGON_NO","POINT_NO")
        with arcpy.da.UpdateCursor(points_layer, columns) as Cursor:   #@UndefinedVariable
            for record in Cursor:
                if record[0] == polygon_numbers[index]:
                    record[1] = record[0] + str(n)
                    Cursor.updateRow(record)
                    n += 1

    del Cursor

    #Deleting intermediary polygon_singlepart_layer
    bk_logger.log("\t \t Step 7: Deleting intermediary polygon_singlepart_layer \n")
    arcpy.Delete_management(polygon_singlepart_layer)

    endTime = bk_logger.currentSecondsTime()

    print("Process Complete")
    bk_logger.log("\t \t Process Completed. It took {} to run \n".format(str(bk_logger.timeTaken(startTime,endTime))))

except:
    bk_logger.handleExcept(logger)