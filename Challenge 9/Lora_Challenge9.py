#DOMINGO LORA MEDINA | 04/13/2024

#CHALLENGE 8: USING arcpy.da

#RULES:
#1 - Print the count of individual record with and without numbers
#2 - Print count of unique species
#3 - Create 2 shapefiles, one with photos and the other without.

#PART 1: SET WORK ENVIRONMENT

import arcpy
arcpy.env.overwriteOutput = True # This command is designed to overwrite any repeated files

arcpy.env.workspace = r'C:\Users\domingo_lora\PycharmProjects\domingo_loraNRS\Challenges\Challenge 9'
input_shp = r'RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp'

photo_count = 0     #In this text, I count how many records have photos and how many do not
no_photo_count = 0
fields = ['PHOTO']

with arcpy.da.SearchCursor(input_shp, fields) as cursor:
    for row in cursor:
        if row[0]:
            photo_count += 1
        else:
            no_photo_count += 1

print(f"Records with photos: {photo_count}")
print(f"Records without photos: {no_photo_count}")

#PART 2: COUNT OF SPECIES
species_set = set()
fields = ['Species']

with arcpy.da.SearchCursor(input_shp, fields) as cursor:
    for row in cursor:
        species_set.add(row[0])  # Add species to set

print(f"Unique species count: {len(species_set)}")

output_with_photos = r'RI_FHWP_invasives_pts_with_photos.shp' #Here I am trying to generate shapefile with photos
where_clause_with_photos = "PHOTO IS NOT NULL"
arcpy.management.SelectLayerByAttribute(input_shp, "NEW SELECTION", where_clause_with_photos)
arcpy.management.CopyFeatures(input_shp, output_with_photos)

print(f"Shapefile generated with photos: {output_with_photos}")

output_without_photos = r'RI_FHWP_invasives_pts_without_photos.shp'
where_clause_without_photos = "PHOTO IS NULL"
arcpy.management.SelectLayerByAttribute(input_shp, "NEW SELECTION", where_clause_without_photos)
arcpy.management.CopyFeatures(input_shp, output_without_photos)

print(f"Shapefile generated without photos: {output_without_photos}")
