"""------------------------------------------------------------------------------------------------------
Script Name:      Service Point Allocation
Version:          1.1
Description:      This tool automates the allocation of bins to service points.
Created By:       Kusasalethu Sithole
Date:             2020-02-17
Revised by:       Kusasalethu Sithole
Last Revision:    2020-02-17
------------------------------------------------------------------------------------------------------"""

#Import modules
import time
import logging
import datetime
import sys
import traceback
import os
import arcpy

#Define bk_logger functions
def currentSecondsTime():
    """ Returns the current time in seconds"""
    return int(time.time())


def timeTaken(startTime, endTime):
    """ Returns the difference between a start time and an end time
        formatted as 00:00:00 """
    timeTaken = endTime - startTime
    return str(datetime.timedelta(seconds=timeTaken))


def defineLogger(log_location=""):
    """ Defines the formatting that will be used in the log file """
    logger = logging.getLogger(__name__)
    x = list(logger.handlers)
    for i in x:
        logger.removeHandler(i)
        i.flush()
        i.close()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s : %(message)s')
    file_handler = logging.FileHandler(log_location + '/python_log.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.debug(
        "\n \n ********************** {} ************************\n \n".format(str(time.ctime())))
    return logger


def showPyMessage(message, logger, messageType="Message"):
    """ Shows a formatted message to the user during processing and also adds the 
        same message to the log file together with a time stamp. """
    if (messageType == "Message"):
        os.system('echo ' + str(time.ctime()) + " - " + message + "'")
        logger.debug(message)
    if (messageType == "Warning"):
        os.system('echo ' + str(time.ctime()) + " - " + message + "'")
        logger.warning(message)
    if (messageType == "Error"):
        os.system('echo ' + str(time.ctime()) + " - " + message + "'")
        logger.error(message)


def handleExcept(logger):
    """ Gets an expection and presents it to the user so that the tool doesn't break. 
        Also logs the same message to the log file together with a timestamp. """
    message = "\n*** PYTHON ERRORS *** "
    showPyMessage(message, logger, "Error")
    message = "Python Traceback Info: " + \
        traceback.format_tb(sys.exc_info()[2])[0]
    showPyMessage(message, logger, "Error")
    message = "Python Error Info: " + \
        str(sys.exc_type) + ": " + str(sys.exc_value) + "\n"
    showPyMessage(message, logger, "Error")

try:
    startTime = currentSecondsTime()
    
    #Declare data sources
    #output_location = arcpy.GetParameterAsText(0)
    #cad = arcpy.GetParameterAsText(1)
    #service_pts = arcpy.GetParameterAsText(2)
    #households = arcpy.GetParameterAsText(3)

    output_location = "S:/KUSASA/GIS/GIS_Tools/Tshwane_SW/output"
    cad = "S:/KUSASA/GIS/GIS_Tools/Tshwane_SW/output/properties.shp"
    service_pts = "S:/KUSASA/GIS/GIS_Tools/Tshwane_SW/output/service_pts.shp"
    households = "S:/KUSASA/GIS/GIS_Tools/Tshwane_SW/output/house_count.shp"

    #Set working environment
    os.chdir(output_location)
    
    # initialize logger
    logger = defineLogger(output_location)
    
    #Step 1: Allocating bins to service points
    showPyMessage("Step 1: Allocating bins to service points ", logger)
    step1_startTime = currentSecondsTime()
    
    # Set feauture layers
    arcpy.MakeFeatureLayer_management(cad,"cad_feat_lyr")
    arcpy.MakeFeatureLayer_management(service_pts,"service_pts_feat_lyr")
    arcpy.MakeFeatureLayer_management(households,"households_feat_lyr")

    tblrows = arcpy.SearchCursor(cad)
    for row in tblrows:
            #select cad by attribute using search cursor
            where_clause = "'" + "EKHAYAIDNE" + "'" + " = " + "'" + str(row.getValue("EKHAYAIDNE")) + "'"
            arcpy.SelectLayerByAttribute_management ("cad_feat_lyr", "NEW_SELECTION", where_clause)
            
            #select service point by location using intersection with cad selection
            arcpy.SelectLayerByLocation_management ("service_pts_feat_lyr", "WITHIN", "cad_feat_lyr", "#", "NEW_SELECTION","NOT_INVERT")

            #Declare value to be copied from the service point layer to the household layer
            for rowx in arcpy.SearchCursor("service_pts_feat_lyr"):
                UpdateValue = rowx.getValue("EKHAYAIDNE")
            UpdateValue = UpdateValue.replace("'", "") 
            UpdateValue = UpdateValue.replace("!", "")
            UpdateValue = "'" + UpdateValue + "'"

            #select households by location using intersection with cad selection
            arcpy.SelectLayerByLocation_management ("households_feat_lyr", "WITHIN", "cad_feat_lyr", "#", "NEW_SELECTION","NOT_INVERT")

            #Copy value into the selected rows of the household layer
            arcpy.CalculateField_management("households_feat_lyr", "serv_point", UpdateValue, "PYTHON", "#")
    
    step1_endTime = currentSecondsTime()
    showPyMessage(" -- Step 1 done. Took {}".format(timeTaken(step1_startTime, step1_endTime)), logger)
    
    endTime = currentSecondsTime()
    showPyMessage(" -- Process Completed. Took {}".format(timeTaken(startTime, endTime)), logger)  
except:
    handleExcept(logger)