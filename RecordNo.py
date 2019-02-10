# Program populates the record numbers of the geometric objects of a target shapefile

import arcpy, os
arcpy.env.overwriteOutput = True

# Request input of workspace
ws = raw_input('Enter workspace path (NB use forward slash delineators)\n')
os.chdir(ws.replace("\r", ""))
arcpy.env.workspace = r'%s' % ws
    
# Declare target and source shapefile names
target_shp = "TargetFileInput.shp"

# Declare the field names that need to be copied from the source layer to the target layer
target_field = str(target_field)

codeBlock = """ recordNo (target_field):
# Perfom if conditions and and generate corresponding return values
country = "COUNTRY"
province = "PROVINCE"
feature = "FEATURE"
cent_x = "CENT_X[1:7]".replace(".","")
cent_y = "CENT_Y[1:7]".replace(".","") 

ecCount = 1
fsCount = 1
gpCount = 1
kznCount = 1
lmCount = 1
mpCount = 1
nwCount = 1
ncCount = 1
wcCount = 1

if province == "ECP":
        if len(count) == 1:
                return country + province + feature + cent_x + cent_y + 13 * "0" + str(count)

        if len(count) == 2:
                return country + province + feature + cent_x + cent_y + 12 * "0" + str(count)

        if len(count) == 3:
                return country + province + feature + cent_x + cent_y + 11 * "0" + str(count)

        if len(count) == 4:
                return country + province + feature + cent_x + cent_y + 10 * "0" + str(count)

        if len(count) == 5:
                return country + province + feature + cent_x + cent_y + 9 * "0" + str(count)

        if len(count) == 6:
                return country + province + feature + cent_x + cent_y + 8 * "0" + str(count)

        if len(count) == 7:
                return country + province + feature + cent_x + cent_y + 7 * "0" + str(count)

        if len(count) == 8:
                return country + province + feature + cent_x + cent_y + 6 * "0" + str(count)

        if len(count) == 9:
                return country + province + feature + cent_x + cent_y + 5 * "0" + str(count)

        if len(count) == 10:
                return country + province + feature + cent_x + cent_y + 4 * "0" + str(count)

        if len(count) == 11:
                return country + province + feature + cent_x + cent_y + 3 * "0" + str(count)

        if len(count) == 12:
                return country + province + feature + cent_x + cent_y + 2 * "0" + str(count)

        if len(count) == 13:
                return country + province + feature + cent_x + cent_y + 1 * "0" + str(count)

        if len(count) == 14:
                return country + province + feature + cent_x + cent_y + str(count)

        ecCount += 1 

if province == "fSP":
        if len(count) == 1:
                return country + province + feature + cent_x + cent_y + 13 * "0" + str(count)

        if len(count) == 2:
                return country + province + feature + cent_x + cent_y + 12 * "0" + str(count)

        if len(count) == 3:
                return country + province + feature + cent_x + cent_y + 11 * "0" + str(count)

        if len(count) == 4:
                return country + province + feature + cent_x + cent_y + 10 * "0" + str(count)

        if len(count) == 5:
                return country + province + feature + cent_x + cent_y + 9 * "0" + str(count)

        if len(count) == 6:
                return country + province + feature + cent_x + cent_y + 8 * "0" + str(count)

        if len(count) == 7:
                return country + province + feature + cent_x + cent_y + 7 * "0" + str(count)

        if len(count) == 8:
                return country + province + feature + cent_x + cent_y + 6 * "0" + str(count)

        if len(count) == 9:
                return country + province + feature + cent_x + cent_y + 5 * "0" + str(count)

        if len(count) == 10:
                return country + province + feature + cent_x + cent_y + 4 * "0" + str(count)

        if len(count) == 11:
                return country + province + feature + cent_x + cent_y + 3 * "0" + str(count)

        if len(count) == 12:
                return country + province + feature + cent_x + cent_y + 2 * "0" + str(count)

        if len(count) == 13:
                return country + province + feature + cent_x + cent_y + 1 * "0" + str(count)

        if len(count) == 14:
                return country + province + feature + cent_x + cent_y + str(count)

        fsCount += 1 """

#Declare value
arcpy.CalculateField_management(target_shp, target_field, expression, "PYTHON", codeBlock )


print("Process Complete: record numbers populated in the target shapefile")