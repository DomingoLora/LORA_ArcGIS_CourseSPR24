#MIDTERM: DOMINGO LORA MEDINA | 3/12/2024

#PART 1: INTRODUCTION

#Wetlands play in important role in supporting and maintaining biodiversity within
#habitats around the United States. In recent decades, and as landuse and landcover changes
#within rural America, wetland preservation has become paramount to ensure the survival
#of numerous habitat.

# This project aims to develop a buffer around Rhode Island wetlands. The goal of this
# project is to showcase where areas of protections should be located to ensure the preservations
# of these important habitat.

#Importing library

import os
import arcpy

arcpy.env.overwriteOutput = True #Command use to overwrite repeated files in library

#Directories
directory = r"C:\Users\domingo_lora\PycharmProjects\domingo_loraNRS\Midterm_FinalTest"
wetlands_dir = os.path.join(directory, "RI_wetlands")
towns_dir = os.path.join(directory, "RI_towns")
output_dir = os.path.join(directory, "Temp_buffer")

#Creating output
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

#Workspace
arcpy.env.workspace = output_dir

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326) # Set  coordinate system (WGS84)

#PART 2: SELECTING STUDY SITE

#Most biodiverse wetlands are found in Washington county, which is why South Kingstown was selected
#as a study site.

buffer_distance = "10 meters" #Buffer distance

# Buffer wetlands
in_features = os.path.join(wetlands_dir, "wetlands.shp")
out_feature_class = os.path.join(output_dir, "wetlands_10_meters.shp")
arcpy.analysis.Buffer(in_features, out_feature_class, buffer_distance)

if arcpy.Exists(out_feature_class):
    print("Wetland's 10-meter Buffer File Has Been Successfully Created!")

#Selecting South Kingstown as the Study Site
input_feature = os.path.join(towns_dir, "towns.shp")
output_feature = os.path.join(output_dir, "SOUTH_KINGSTOWN.shp")
where_category = "NAME"
where_response = 'SOUTH KINGSTOWN'
where_clause = "{} = '{}'".format(arcpy.AddFieldDelimiters(input_feature, where_category), where_response)
arcpy.Select_analysis(input_feature, output_feature, where_clause)

if arcpy.Exists(output_feature):
    print("South Kingstown Has Been Selected From Towns File Successfully!")

#PART 3: INTESECT THE BUFFER WETLANDS IN SK, RI

#Intersect wetlands buffer and South Kingstown
input_layers = [out_feature_class, output_feature]
output_layer = os.path.join(output_dir, where_response + "_WetlandIntersect.shp")
join_attributes = "ALL"
arcpy.Intersect_analysis(input_layers, output_layer, join_attributes)

if arcpy.Exists(output_layer):
    print("Intersect file created successfully!\n")

print("All files created successfully.\n")