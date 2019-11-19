"""------------------------------------------------------------------------------------------------------
Script Name:      Bin Collection Points
Version:          1.1
Description:      This tool generates bin collection points by:
                  1. Deleting roads that have nonviable attributes.
                  2. Selecting all roads longer than 20m and then cutting them at 40m intervals.
                  3. Selecting all roads that are less than 40m from a property and then export layer.
                  4. Converting bin collection road strips into bin collection points.
                  5. Assigning service points to their closest bin collection point, leaving out collection 
                  points that have not bins assigned to them.
Created By:       Kusasalethu Sithole
Date:             2019-11-11
Last Revision:    2019-11-19
------------------------------------------------------------------------------------------------------"""
 
import logging
import os

#import modules
import arcpy
import bk_logger
import shutil

# User inputs
working_directory = "S:/KUSASA/GIS/Temp/collections_points"
roads = "S:/KUSASA/GIS/Routing/firstRun/TestArea_Roads_Final.shp"
cad = "S:/KUSASA/GIS/Temp/collections_points/input/sample_cad.shp"
service_points = "S:/KUSASA/GIS/Temp/collections_points/input/service_points.shp"

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


    #Step 2: Select all roads longer than 20m and then cutting them at 40m intervals
    bk_logger.showPyMessage("Step 2: Select all roads longer than 20m and then cutting them at 40m intervals ", logger)
    step2_startTime = bk_logger.currentSecondsTime()

    spatial_roads_above20m = intermediate_layers + "/spatial_roads_above20m.shp"
    arcpy.AddField_management(attr_roads, "lengt_road", "DOUBLE", 30, 15, "#", "#", "NULLABLE", "NON_REQUIRED", "#")
    arcpy.CalculateField_management(attr_roads, "lengt_road", "!shape.geodesicLength@meters!", "PYTHON_9.3")
    arcpy.MakeFeatureLayer_management (attr_roads, "attr_roads")
    arcpy.SelectLayerByAttribute_management ("attr_roads", "NEW_SELECTION", ' "lengt_road" >= 20 ')
    arcpy.CopyFeatures_management("attr_roads",spatial_roads_above20m)
    
    segmented_roads = intermediate_layers + "/segmented_roads.shp"
    _40m_points = intermediate_layers + "/_40m_points.shp"
    arcpy.GeneratePointsAlongLines_management(spatial_roads_above20m, _40m_points, 'DISTANCE', Distance='40 meters')
    arcpy.SplitLineAtPoint_management(spatial_roads_above20m, _40m_points, 'segmented_roads')
    arcpy.CopyFeatures_management('segmented_roads', segmented_roads)

    step2_endTime = bk_logger.currentSecondsTime()
    bk_logger.showPyMessage(" -- Step 2 done. Took {}".format(bk_logger.timeTaken(step2_startTime, step2_endTime)), logger)


    #Step 3: Selecting all roads that are less than 40m from a property and then export layer
    bk_logger.showPyMessage("Step 3: Selecting all roads that are less than 40m from a property and then export layer ", logger)
    step3_startTime = bk_logger.currentSecondsTime()

    cad_proximal_roads = intermediate_layers + "/cad_proximal_roads.shp"
    arcpy.MakeFeatureLayer_management (segmented_roads, "segmented_roads")
    arcpy.MakeFeatureLayer_management (cad, "cad")
    arcpy.SelectLayerByLocation_management("segmented_roads", "WITHIN_A_DISTANCE", "cad", "40 Meters", "NEW_SELECTION", "NOT_INVERT")
    arcpy.CopyFeatures_management("segmented_roads",cad_proximal_roads)
    
    step3_endTime = bk_logger.currentSecondsTime()
    bk_logger.showPyMessage(" -- Step 3 done. Took {}".format(bk_logger.timeTaken(step3_startTime, step3_endTime)), logger)    


    #Step 4: Convert bin collection road strips into bin collection points
    bk_logger.showPyMessage("Step 4: Convert bin collection road strips into bin collection points ", logger)
    step4_startTime = bk_logger.currentSecondsTime()

    rough_bin_collection_points = intermediate_layers + "/rough_bin_collection_points.shp"
    arcpy.FeatureToPoint_management(cad_proximal_roads, rough_bin_collection_points, "INSIDE")

    step4_endTime = bk_logger.currentSecondsTime()
    bk_logger.showPyMessage(" -- Step 4 done. Took {}".format(bk_logger.timeTaken(step4_startTime, step4_endTime)), logger)
    
    
    #Step 5: Assign service points to their closest bin collection point
    bk_logger.showPyMessage("Step 5: Assign service points to their closest bin collection point ", logger)
    step5_startTime = bk_logger.currentSecondsTime()

    bin_collection_points = working_directory + "/bin_collection_points.shp"
    arcpy.SpatialJoin_analysis(rough_bin_collection_points, service_points, bin_collection_points, "JOIN_ONE_TO_MANY", "KEEP_COMMON", "#", "CLOSEST", "80 meters", "dist_diff")

    step5_endTime = bk_logger.currentSecondsTime()
    bk_logger.showPyMessage(" -- Step 5 done. Took {}".format(bk_logger.timeTaken(step5_startTime, step5_endTime)), logger)   


    shutil.rmtree(intermediate_layers)


    endTime = bk_logger.currentSecondsTime()
    bk_logger.showPyMessage(" -- Process Completed. Took {}".format(bk_logger.timeTaken(startTime, endTime)), logger)   


except:
    bk_logger.handleExcept(logger)
