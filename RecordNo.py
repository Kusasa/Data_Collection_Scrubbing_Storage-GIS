# Program populates the record numbers of the geometric objects of a target shapefile

import arcpy, os
arcpy.env.overwriteOutput = True

# Request input of workspace
ws = arcpy.GetParameterAsText(0)
arcpy.env.workspace = r'%s' % ws
    
# Request target shapefile and declare target field
target_shp = arcpy.GetParameterAsText(1)
target_field = "RECNO"

# Declare global variables
province = "PROVINCE"
ecCount = 0
fsCount = 0
gpCount = 0
kznCount = 0
lmCount = 0
mpCount = 0
ncCount = 0
nwCount = 0
wcCount = 0
country = 'RSA'

#Declare function
def recordNo (province, feature, cent_y, cent_x):
        global ecCount
        global fsCount
        global gpCount
        global kznCount
        global lmCount
        global mpCount
        global ncCount
        global nwCount
        global wcCount
        global country

        if province == 'Eastern Cape':
                ecCount += 1
                if len(str(ecCount)) == 1:
                        return country + province + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000000' + str(ecCount)
                        
                elif len(str(ecCount)) == 2:
                        return country + 'ECP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000000' + str(ecCount)                       

                elif len(str(ecCount)) == 3:
                        return country + 'ECP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000000' + str(ecCount)
                        
                elif len(str(ecCount)) == 4:
                        return country + 'ECP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000' + str(ecCount)
                        
                elif len(str(ecCount)) == 5:
                        return country + 'ECP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000' + str(ecCount)

                elif len(str(ecCount)) == 6:
                        return country + 'ECP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000' + str(ecCount)
                        
                elif len(str(ecCount)) == 7:
                        return country + 'ECP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000' + str(ecCount)
                        
                elif len(str(ecCount)) == 8:
                        return country + 'ECP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000' + str(ecCount)
                        
                elif len(str(ecCount)) == 9:
                        return country + 'ECP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000' + str(ecCount)
                        
                elif len(str(ecCount)) == 10:
                        return country + 'ECP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000' + str(ecCount)
                        
                elif len(str(ecCount)) == 11:
                        return country + 'ECP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000' + str(ecCount)
                        
                elif len(str(ecCount)) == 12:
                        return country + 'ECP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00' + str(ecCount)
                        
                elif len(str(ecCount)) == 13:
                        return country + 'ECP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0' + str(ecCount)
                        
                elif len(str(ecCount)) == 14:
                        return country + 'ECP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + str(ecCount)

                else:
                        return None

        elif province == 'Free State':
                fsCount += 1
                if len(str(fsCount)) == 1:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000000' + str(fsCount)
                        
                elif len(str(fsCount)) == 2:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000000' + str(fsCount)
                        
                elif len(str(fsCount)) == 3:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000000' + str(fsCount)
                        
                elif len(str(fsCount)) == 4:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000' + str(fsCount)
                        
                elif len(str(fsCount)) == 5:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000' + str(fsCount)
                        
                elif len(str(fsCount)) == 6:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000' + str(fsCount)
                        
                elif len(str(fsCount)) == 7:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000' + str(fsCount)
                        
                elif len(str(fsCount)) == 8:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000' + str(fsCount)
                        
                elif len(str(fsCount)) == 9:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000' + str(fsCount)
                        
                elif len(str(fsCount)) == 10:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000' + str(fsCount)
                        
                elif len(str(fsCount)) == 11:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000' + str(fsCount)
                        
                elif len(str(fsCount)) == 12:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00' + str(fsCount)
                        
                elif len(str(fsCount)) == 13:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0' + str(fsCount)
                        
                elif len(str(fsCount)) == 14:
                        return country + 'FSP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + str(fsCount)

                else:
                        return None

        elif province == 'Gauteng':
                gpCount += 1
                if len(str(gpCount)) == 1:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000000' + str(gpCount)
                        
                elif len(str(gpCount)) == 2:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000000' + str(gpCount)
                        
                elif len(str(gpCount)) == 3:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000000' + str(gpCount)
                        
                elif len(str(gpCount)) == 4:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000' + str(gpCount)
                        
                elif len(str(gpCount)) == 5:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000' + str(gpCount)
                        
                elif len(str(gpCount)) == 6:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000' + str(gpCount)
                        
                elif len(str(gpCount)) == 7:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000' + str(gpCount)
                        
                elif len(str(gpCount)) == 8:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000' + str(gpCount)
                        
                elif len(str(gpCount)) == 9:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000' + str(gpCount)
                        
                elif len(str(gpCount)) == 10:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000' + str(gpCount)
                        
                elif len(str(gpCount)) == 11:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000' + str(gpCount)
                        
                elif len(str(gpCount)) == 12:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00' + str(gpCount)
                        
                elif len(str(gpCount)) == 13:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0' + str(gpCount)
                        
                elif len(str(gpCount)) == 14:
                        return country + 'GAU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + str(gpCount)
                
                else:
                        return None
                
        elif province == 'KwaZulu-Natal':
                kznCount += 1
                if len(str(kznCount)) == 1:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000000' + str(kznCount)
                        
                elif len(str(kznCount)) == 2:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000000' + str(kznCount)
                        
                elif len(str(kznCount)) == 3:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000000' + str(kznCount)
                        
                elif len(str(kznCount)) == 4:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000' + str(kznCount)
                        
                elif len(str(kznCount)) == 5:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000' + str(kznCount)
                        
                elif len(str(kznCount)) == 6:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000' + str(kznCount)
                        
                elif len(str(kznCount)) == 7:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000' + str(kznCount)
                        
                elif len(str(kznCount)) == 8:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000' + str(kznCount)
                        
                elif len(str(kznCount)) == 9:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000' + str(kznCount)
                        
                elif len(str(kznCount)) == 10:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000' + str(kznCount)
                        
                elif len(str(kznCount)) == 11:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000' + str(kznCount)
                        
                elif len(str(kznCount)) == 12:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00' + str(kznCount)
                        
                elif len(str(kznCount)) == 13:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0' + str(kznCount)
                        
                elif len(str(kznCount)) == 14:
                        return country + 'KZN' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + str(kznCount)

                else:
                        return None        

        elif province == 'Limpopo':
                lmCount += 1
                if len(str(lmCount)) == 1:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000000' + str(lmCount)
                        
                elif len(str(lmCount)) == 2:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000000' + str(lmCount)
                        
                elif len(str(lmCount)) == 3:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000000' + str(lmCount)
                        
                elif len(str(lmCount)) == 4:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000' + str(lmCount)
                        
                elif len(str(lmCount)) == 5:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000' + str(lmCount)
                        
                elif len(str(lmCount)) == 6:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000' + str(lmCount)
                        
                elif len(str(lmCount)) == 7:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000' + str(lmCount)
                        
                elif len(str(lmCount)) == 8:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000' + str(lmCount)
                        
                elif len(str(lmCount)) == 9:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000' + str(lmCount)
                        
                elif len(str(lmCount)) == 10:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000' + str(lmCount)
                        
                elif len(str(lmCount)) == 11:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000' + str(lmCount)
                        
                elif len(str(lmCount)) == 12:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00' + str(lmCount)
                     
                elif len(str(lmCount)) == 13:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0' + str(lmCount)
                        
                elif len(str(lmCount)) == 14:
                        return country + 'LMP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + str(lmCount)

                else:
                        return None        

        elif province == 'Mpumalanga':
                mpCount += 1
                if len(str(mpCount)) == 1:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000000' + str(mpCount)
                        
                elif len(str(mpCount)) == 2:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000000' + str(mpCount)
                        
                elif len(str(mpCount)) == 3:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000000' + str(mpCount)
                        
                elif len(str(mpCount)) == 4:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000' + str(mpCount)
                        
                elif len(str(mpCount)) == 5:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000' + str(mpCount)
                        
                elif len(str(mpCount)) == 6:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000' + str(mpCount)
                        
                elif len(str(mpCount)) == 7:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000' + str(mpCount)
                        
                elif len(str(mpCount)) == 8:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000' + str(mpCount)
                        
                elif len(str(mpCount)) == 9:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000' + str(mpCount)
                        
                elif len(str(mpCount)) == 10:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000' + str(mpCount)
                        
                elif len(str(mpCount)) == 11:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000' + str(mpCount)
                        
                elif len(str(mpCount)) == 12:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00' + str(mpCount)
                        
                elif len(str(mpCount)) == 13:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0' + str(mpCount)
                        
                elif len(str(mpCount)) == 14:
                        return country + 'MPU' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","")  + str(mpCount)

                else:
                        return None        

        elif province == 'Northern Cape':
                ncCount += 1
                if len(str(ncCount)) == 1:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000000' + str(ncCount)
                        
                elif len(str(ncCount)) == 2:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000000' + str(ncCount)
                        
                elif len(str(ncCount)) == 3:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000000' + str(ncCount)
                        
                elif len(str(ncCount)) == 4:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000' + str(ncCount)
                        
                elif len(str(ncCount)) == 5:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000' + str(ncCount)
                        
                elif len(str(ncCount)) == 6:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000' + str(ncCount)
                        
                elif len(str(ncCount)) == 7:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000' + str(ncCount)
                        
                elif len(str(ncCount)) == 8:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000' + str(ncCount)
                        
                elif len(str(ncCount)) == 9:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000' + str(ncCount)
                        
                elif len(str(ncCount)) == 10:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000' + str(ncCount)
                        
                elif len(str(ncCount)) == 11:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000' + str(ncCount)
                        
                elif len(str(ncCount)) == 12:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00' + str(ncCount)
                        
                elif len(str(ncCount)) == 13:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0' + str(ncCount)
                        
                elif len(str(ncCount)) == 14:
                        return country + 'NCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","")  + str(ncCount)

                else:
                        return None        

        elif province == 'North West':
                nwCount += 1
                if len(str(nwCount)) == 1:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000000' + str(nwCount)
                        
                elif len(str(nwCount)) == 2:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000000' + str(nwCount)
                        
                elif len(str(nwCount)) == 3:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000000' + str(nwCount)
                        
                elif len(str(nwCount)) == 4:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000' + str(nwCount)
                        
                elif len(str(nwCount)) == 5:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000' + str(nwCount)
                        
                elif len(str(nwCount)) == 6:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000' + str(nwCount)
                        
                elif len(str(nwCount)) == 7:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000' + str(nwCount)
                        
                elif len(str(nwCount)) == 8:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000' + str(nwCount)
                        
                elif len(str(nwCount)) == 9:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000' + str(nwCount)
                        
                elif len(str(nwCount)) == 10:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000' + str(nwCount)
                        
                elif len(str(nwCount)) == 11:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000' + str(nwCount)
                        
                elif len(str(nwCount)) == 12:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00' + str(nwCount)
                        
                elif len(str(nwCount)) == 13:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0' + str(nwCount)
                        
                elif len(str(nwCount)) == 14:
                        return country + 'NWP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + str(nwCount)

                else:
                        return None        

        elif province == 'Western Cape':
                wcCount += 1
                if len(str(wcCount)) == 1:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000000' + str(wcCount)
                        
                elif len(str(wcCount)) == 2:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000000' + str(wcCount)
                        
                elif len(str(wcCount)) == 3:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000000' + str(wcCount)
                        
                elif len(str(wcCount)) == 4:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000000' + str(wcCount)
                        
                elif len(str(wcCount)) == 5:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000000' + str(wcCount)
                        
                elif len(str(wcCount)) == 6:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000000' + str(wcCount)
                        
                elif len(str(wcCount)) == 7:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000000' + str(wcCount)
                        
                elif len(str(wcCount)) == 8:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000000' + str(wcCount)
                        
                elif len(str(wcCount)) == 9:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00000' + str(wcCount)
                        
                elif len(str(wcCount)) == 10:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0000' + str(wcCount)
                        
                elif len(str(wcCount)) == 11:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '000' + str(wcCount)
                        
                elif len(str(wcCount)) == 12:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '00' + str(wcCount)
                        
                elif len(str(wcCount)) == 13:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","") + '0' + str(wcCount)
                        
                elif len(str(wcCount)) == 14:
                        return country + 'WCP' + feature + str(cent_y)[1:8].replace(".","") + str(cent_x)[0:7].replace(".","")  + str(wcCount)

                else:
                        return None        

        else:
                return None

#Evaluate field values using update cursor
with arcpy.da.UpdateCursor(target_shp, ["RECNO", "PROVINCE", "FEATURE", "CENT_Y", "CENT_X"]) as cursor:
        for row in cursor:
                row[0] = recordNo (row[1], row[2], row[3], row[4])
                cursor.updateRow(row)

print("Process Complete: record numbers populated in the target shapefile")
