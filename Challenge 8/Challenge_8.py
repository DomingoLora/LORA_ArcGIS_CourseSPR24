#DOMINGO LORA MEDINA | 04/03/2024

#CHALLENEGE 8: FUNCTIONS

#This challenges draws inspiration on the Midterm project by adding buffering to
# lakes in Rhode Island

#RULES:
# 1) More than one input for function
# 2) Two or more arguments
# 3) Include a zip file

#PART 1: SET WORK ENVIROMENT

import arcpy
arcpy.env.overwriteOutput = True # This command is designed to overwrite any repeated files

def buffer_shapefile(in_features, out_feature_class, buffer_distance_or_field): #Here is the function in use
    arcpy.env.workspace = r"C:\Users\domingo_lora\PycharmProjects\domingo_loraNRS\Challenges\Challenge 8"
    line_side = "#"
    line_end_type = "#"
    dissolve_option = "#"
    dissolve_field = "#"
    method = "GEODESIC"
    arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, line_side,
                          line_end_type, dissolve_option, dissolve_field, method)
    if arcpy.Exists(out_feature_class):
        print("File was buffered successfully!")

def polygon_to_raster(in_features, val_field, out_raster, assignment_type, priority_field, cell_size):
    arcpy.env.workspace = r"C:\Users\domingo_lora\PycharmProjects\domingo_loraNRS\Challenges\Challenge 8"
    arcpy.conversion.PolygonToRaster(in_features, val_field, out_raster, assignment_type, priority_field, cell_size)
    if arcpy.Exists(out_raster):
        print("Raster created successfully!")

#PART 2: SETTING OUTPUT FEATURES

in_features_lakes = r"C:\Users\domingo_lora\PycharmProjects\domingo_loraNRS\Challenges\Challenge 8\Lakes_Data\Lakes.shp"
out_feature_class_lakes = r"C:\Users\domingo_lora\PycharmProjects\domingo_loraNRS\Challenges\Challenge 8\Lakes_Output.shp"

buffer_distance_or_field_lakes = "200 meters" #This command dictates the buffering distance

in_features_towns = r"C:\Users\domingo_lora\PycharmProjects\domingo_loraNRS\Challenges\Challenge 8\RI_towns\towns.shp"
val_field_towns = "NAME"
out_raster_towns = r"C:\Users\domingo_lora\PycharmProjects\domingo_loraNRS\Challenges\Challenge 8\Towns_raster"
assignment_type_towns = "#"
priority_field_towns = "#"
cell_size_towns = 800 #Cell Count for the Rhode Island TOWNS dataset

buffer_shapefile(in_features_lakes, out_feature_class_lakes, buffer_distance_or_field_lakes)
polygon_to_raster(in_features_towns, val_field_towns, out_raster_towns, assignment_type_towns, priority_field_towns, cell_size_towns)


