#Although Challenge 4 encourages students to use open source data,
#for this exercise, I will be modifying one of RIDEM's proprietary dataset for
#mosquitoes capture within the state of Rhode Island. This data was provided
#to Jannelle Couret and was shared with me as part of my dissertation work.

#PART 1:

import arcpy
import os

try:
    directory = r'C:\Users\domingo_lora\PycharmProjects\domingo_loraNRS\Week 5' #location

    arcpy.env.workspace = directory

    in_table = "EEEV_PosCsMelanura_RI.csv" #Data name

    in_table_path = os.path.join(directory, in_table)

    out_feature_class = "EEE_positive.shp" #This is the name of the output feature, as requiered
    #by the tool in use

    x_coords = "Longitude"
    y_coords = "Latitude"
    z_coords = ""


    spRef = arcpy.SpatialReference(4326)
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(26919) #The spatial reference
    #code was added in an attempt to overcome an error message where YX Table to Point feature
    #was not found.

#PART 2

    arcpy.management.XYTableToPoint(in_table_path, out_feature_class, x_coords, y_coords, z_coords, spRef)

    if arcpy.Exists(out_feature_class):
        print(f"Conversion to point features successful: {out_feature_class}")

        in_data = out_feature_class
        in_feature = "EEE_positive.shp"

#PART 3

        arcpy.Copy_management(in_data, in_feature)
        arcpy.AddXY_management(in_feature)
        print(f"Copying and adding XY coordinates successful: {in_feature}")

    else:
        print(f"Failed to create point features. Check input CSV file and field names.")

except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
except Exception as e:
    print(e)