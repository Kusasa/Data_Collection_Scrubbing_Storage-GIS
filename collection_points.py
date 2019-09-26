"""------------------------------------------------------------------------------------------------------
Script Name:      Bin Collection Points
Version:          1.1
Description:      This tool generates bin collection points by:
                  1. Delete roads that have nonviable attributes.
                  2. Cut and delete road segments that intersect no-access areas.
                  3. Selecting all roads longer than 20m and then export layer.
                  4. Selecting all roads that are less than 20m from a property and then export layer.
                  5. Generate a bin collection point at the middle of each segment in the exported road.
                  6. Generate a service point for each cad property on the theoretically ideal side.
                  7. Assign service points to their closest bin collection point, leaving out collection 
                  points that have not bins assigned to them.
Created By:       Kusasalethu Sithole
Date:             2019-09-11
Last Revision:    2019-09-12
------------------------------------------------------------------------------------------------------"""
 
import logging
import os

#import modules
import arcpy
import arcpy.cartography as CA
import bk_logger

# User inputs
working_directory = "S:/KUSASA/GIS/Temp/collections_points"
roads = "S:/KUSASA/GIS/Routing/firstRun/TestArea_Roads_Final.shp"
no_access_areas = "S:/KUSASA/GIS/Temp/collections_points/input/no_access.shp"
cad = "S:/KUSASA/GIS/Temp/collections_points/input/sample_cad.shp"

#set environment
arcpy.env.overwriteOutput = True
arcpy.env.parallelProcessingFactor = "100%"
arcpy.env.workspace = working_directory

# initialize the configuration for the logger
bk_logger.defineLogger(working_directory)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s : %(message)s')
file_handler = logging.FileHandler(working_directory + '/log.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

try:
    startTime = bk_logger.currentSecondsTime()
    os.mkdir(working_directory + "/intermediate_layers")
    intermediate_layers = working_directory + "/intermediate_layers"

    #Step 1: Delete roads that have nonviable attributes
    bk_logger.showPyMessage("Step 1: Delete roads that have nonviable attributes ", logger)
    step1_startTime = bk_logger.currentSecondsTime()

    attr_roads = intermediate_layers + "/attr_roads.shp"
    arcpy.MakeFeatureLayer_management (roads, "roadlyr")
    arcpy.SelectLayerByAttribute_management ("roadlyr", "NEW_SELECTION", """ "ROADCLASS" <> 'MAJOR' AND "ROADCLASS" <> 'SECONDARY' """)
    arcpy.CopyFeatures_management("roadlyr",attr_roads)
    
    step1_endTime = bk_logger.currentSecondsTime()
    bk_logger.showPyMessage(" -- Step 1 done. Took {}".format(bk_logger.timeTaken(step1_startTime, step1_endTime)), logger)


    #Step 2: Cut and delete road segments that intersect no-access areas
    bk_logger.showPyMessage("Step 2: Cut and delete road segments that intersect no-access areas ", logger)
    step2_startTime = bk_logger.currentSecondsTime()

    spatial_roads = intermediate_layers + "/spatial_roads.shp"
    arcpy.MakeFeatureLayer_management (attr_roads, "attr_roads")
    arcpy.MakeFeatureLayer_management (no_access_areas, "no_access_areas")
    arcpy.SelectLayerByLocation_management("attr_roads", "INTERSECT", "no_access_areas", "", "NEW_SELECTION", "INVERT")
    arcpy.CopyFeatures_management("attr_roads",spatial_roads)
    
    step2_endTime = bk_logger.currentSecondsTime()
    bk_logger.showPyMessage(" -- Step 2 done. Took {}".format(bk_logger.timeTaken(step2_startTime, step2_endTime)), logger)


    #Step 3: Selecting all roads longer than 20m and then export layer
    bk_logger.showPyMessage("Step 3: Selecting all roads longer than 40m and then cutting them at 20m ", logger)
    step3_startTime = bk_logger.currentSecondsTime()

    spatial_roads_above20m = intermediate_layers + "/spatial_roads_above20m.shp"
    arcpy.AddField_management(spatial_roads, "lengt_road", "DOUBLE", 30, 15, "#", "#", "NULLABLE", "NON_REQUIRED", "#")
    arcpy.CalculateField_management(spatial_roads, "lengt_road", "!shape.geodesicLength@meters!", "PYTHON_9.3")
    arcpy.MakeFeatureLayer_management (spatial_roads, "spatial_roads")
    arcpy.SelectLayerByAttribute_management ("spatial_roads", "NEW_SELECTION", ' "lengt_road" >= 20 ')
    arcpy.CopyFeatures_management("spatial_roads",spatial_roads_above20m)
    
    step3_endTime = bk_logger.currentSecondsTime()
    bk_logger.showPyMessage(" -- Step 3 done. Took {}".format(bk_logger.timeTaken(step3_startTime, step3_endTime)), logger)


    #Step 4: Selecting all roads that are less than 20m from a property and then export layer
    bk_logger.showPyMessage("Step 4: Selecting all roads that are less than 20m from a property and then export layer ", logger)
    step4_startTime = bk_logger.currentSecondsTime()

    cad_proximal_roads = intermediate_layers + "/cad_proximal_roads.shp"
    arcpy.MakeFeatureLayer_management (spatial_roads_above20m, "spatial_roads_above20m")
    arcpy.MakeFeatureLayer_management (cad, "cad")
    arcpy.SelectLayerByLocation_management("spatial_roads_above20m", "WITHIN_A_DISTANCE", "cad", "20 Meters", "NEW_SELECTION", "NOT_INVERT")
    arcpy.CopyFeatures_management("spatial_roads_above20m",cad_proximal_roads)
    
    step4_endTime = bk_logger.currentSecondsTime()
    bk_logger.showPyMessage(" -- Step 4 done. Took {}".format(bk_logger.timeTaken(step4_startTime, step4_endTime)), logger)    
     

    #Step 5: Generate a rough bin collection point at the middle of each segment in the exported road
    bk_logger.showPyMessage("Step 5: Generate a bin collection point at the middle of each segment in the exported road ", logger)
    step5_startTime = bk_logger.currentSecondsTime()

    rough_bin_collection_points = intermediate_layers + "/rough_bin_collection_points.shp"
    arcpy.FeatureToPoint_management(cad_proximal_roads, rough_bin_collection_points, "CENTROID")
    
    step5_endTime = bk_logger.currentSecondsTime()
    bk_logger.showPyMessage(" -- Step 5 done. Took {}".format(bk_logger.timeTaken(step5_startTime, step5_endTime)), logger)


    #Step 6: Generate a service point for each cad property on the theoretically ideal side
    bk_logger.showPyMessage("Step 6: Generate a service point for each cad property on the theoretically ideal side ", logger)
    step6_startTime = bk_logger.currentSecondsTime()

    arcpy.MakeFeatureLayer_management(cad,"cad")
    simplifiedCAD = intermediate_layers + "/simplifiedCAD.shp"
    CA.SimplifyPolygon("cad", simplifiedCAD, "BEND_SIMPLIFY", 1, "", "RESOLVE_ERRORS", "KEEP_COLLAPSED_POINTS")

    arcpy.MakeFeatureLayer_management(simplifiedCAD,"simplifiedCAD")
    polylineCAD = intermediate_layers + "/polylineCAD.shp"
    arcpy.PolygonToLine_management("simplifiedCAD", polylineCAD,"IGNORE_NEIGHBORS")

    arcpy.MakeFeatureLayer_management(polylineCAD,"polylineCAD")
    polygon_fid = 0
    max_polgyon_fid = int(arcpy.GetCount_management("polylineCAD").getOutput(0))
    fields_ = ['FID', 'ID']
    target_polylineCAD = intermediate_layers + "/target_polylineCAD.shp"
    service_points = working_directory + "/service_points.shp"
    arcpy.CopyFeatures_management('polylineCAD',target_polylineCAD)
    arcpy.TruncateTable_management(target_polylineCAD)

    if polygon_fid <= max_polgyon_fid:
        expression = arcpy.AddFieldDelimiters("polylineCAD", "FID") + ' = {}'.format(polygon_fid)
        tblrows = arcpy.SearchCursor("polylineCAD", where_clause=expression)
        current_shortest_side_length = 1000000
        current_shortest_side_id = None
        for row in tblrows:
            if arcpy.SelectLayerByLocation_management('polylineCAD', 'WITHIN_A_DISTANCE', 'polylineCAD', "1 Meters", "#", "#") == None:
                row_length = row['SHAPE@LENGTH']
                if row_length < current_shortest_side_length :
                    current_shortest_side_length = row_length
                    current_shortest_side_id = row['ID']
                else:
                    continue
            else:
                continue
        where = " 'ID' = {}".format(current_shortest_side_id)
        arcpy.SelectLayerByAttribute_management("polylineCAD", "NEW_SELECTION", where)
        arcpy.Append_management('polylineCAD', target_polylineCAD, "TEST", "#")
        polygon_fid =+ 1
    arcpy.GeneratePointsAlongLines_management(target_polylineCAD, service_points, 'PERCENTAGE', Percentage=50, Include_End_Points='No_END_POINTS')

    
    step6_endTime = bk_logger.currentSecondsTime()
    bk_logger.showPyMessage(" -- Step 6 done. Took {}".format(bk_logger.timeTaken(step6_startTime, step6_endTime)), logger)


    #Step 7: Assign service points to their closest bin collection point
    bk_logger.showPyMessage("Step 7: Assign service points to their closest bin collection point ", logger)
    step7_startTime = bk_logger.currentSecondsTime()

    actual_bin_collection_points = working_directory + "/bin_collection_points.shp"
    arcpy.SpatialJoin_analysis(service_points, rough_bin_collection_points, actual_bin_collection_points, "JOIN_ONE_TO_MANY", "KEEP_COMMON", "#", "CLOSEST", "1000 meters", "dist_diff")
    
    step7_endTime = bk_logger.currentSecondsTime()
    bk_logger.showPyMessage(" -- Step 7 done. Took {}".format(bk_logger.timeTaken(step7_startTime, step7_endTime)), logger)


except:
    bk_logger.handleExcept(logger)
