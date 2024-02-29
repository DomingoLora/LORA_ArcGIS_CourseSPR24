#PART 1: Importing systems

import arcpy
import csv
import os

#PART2: Overwrting Code
arcpy.env.overwriteOutput = True

#This line of code allows for other files to be overwritten when running the script

#PART 3: Path directory

arcpy.env.workspace = r"C:\Users\domingo_lora\PycharmProjects\domingo_loraNRS\Challenges\Challenge 5"
workspace = r"C:\Users\domingo_lora\PycharmProjects\domingo_loraNRS\Challenges\Challenge 5"

#PART 4: Creating a function capable of creating a shapefile from CSV
def create_shapefile(csv_file, out_shapefile):
    spRef = arcpy.SpatialReference(4326)
    lyr = arcpy.MakeXYEventLayer_management(csv_file, "X", "Y", "EventLayer", spRef)
    arcpy.CopyFeatures_management(lyr, out_shapefile)
    return out_shapefile

# PART 5: Creating a function that allows to create what is described as a "fishnet extent"
#In other words, this creates the area of study
def create_fishnet(input_shapefile, cell_size, out_fishnet):
    desc = arcpy.Describe(input_shapefile)
    extent = desc.extent
    originCoordinate = f"{extent.XMin} {extent.YMin}"
    yAxisCoordinate = f"{extent.XMin} {extent.YMin + 10}"
    numRows = ""
    numColumns = ""
    oppositeCorner = f"{extent.XMax} {extent.YMax}"
    labels = "NO_LABELS"
    templateExtent = "#"
    geometryType = "POLYGON"
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
    arcpy.CreateFishnet_management(out_fishnet, originCoordinate, yAxisCoordinate,
                                   cell_size, cell_size, numRows, numColumns,
                                   oppositeCorner, labels, templateExtent, geometryType)
    return out_fishnet

#PART6: Spatial join
def spatial_join(target_features, join_features, out_feature_class):
    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                               "JOIN_ONE_TO_ONE", "KEEP_ALL", "", "INTERSECT")

#PART 7: Creating an empty species list to populate with a loop clause from imported csv
species_list = []

with open("../Challenge 5_NEW/DataPYTHON.csv") as species_csv:
    csv_reader = csv.reader(species_csv, delimiter=',')
    next(csv_reader)  # Skip header
    for row in csv_reader:
        if row[0] not in species_list:
            species_list.append(row[0])


for species in species_list:
    # Create separate CSV file for each species
    species_csv_file = f"{species}.csv"
    with open("../Challenge 5_NEW/DataPYTHON.csv") as all_species_csv:
        csv_reader_all_species = csv.reader(all_species_csv, delimiter=',')
        with open(species_csv_file, "w") as species_file:
            species_file.write("Species,X,Y\n")
            for row in csv_reader_all_species:
                if row[0] == species:
                    species_file.write(','.join(row) + '\n')

    #PART 8: Create shapefile from CSV file povided above "DataPYTHON"
    species_shapefile = f"{species}.shp"
    create_shapefile(species_csv_file, species_shapefile)
    print(f"Created shapefile '{species_shapefile}' successfully!")

    # PART 9: Create fishnet
    fishnet_file = f"{species}_Fishnet.shp"
    create_fishnet(species_shapefile, cell_size="2", out_fishnet=fishnet_file)
    print(f"Created Fishnet file '{fishnet_file}' successfully!")

    #PART 10: Perform spatial join to create heatmap
    heatmap_file = f"{species}_heatmap.shp"
    spatial_join(fishnet_file, species_shapefile, heatmap_file)
    print(f"Created Heatmap file '{heatmap_file}' successfully!")

    #PART11: Deleting the intermediate files
    arcpy.Delete_management(fishnet_file)
    arcpy.Delete_management(species_shapefile)
    os.remove(species_csv_file)

print("Processing completed.")

#NOTES: This was a very dificult assignement to complete and I relayed on reddit and other sources
#of open coding to sucessfully complete the homework.

#This project was completed using internal data provided to Jannelle Couret by RIDEM

#Species of study: Aedes albopictus and Aedes aegypti
