# DOMINGO LORA MEDINA   |  05/02/2024


#PART 1: Setting Environment

import arcpy

arcpy.env.overwriteOutput = True

class Toolbox(object):
    def __init__(self):
        self.label = "Transportation Infrastructure"
        self.alias = ""
        self.tools = [Buffer, Dissolve, Intersect] #Tools that are in use

class Buffer(object):
    def __init__(self):
        self.label = "Buffer of Transportation Systems"
        self.description = "The buffer tool will create a 12 meter buffer, as specefied by the user"
        self.canRunInBackground = False

    def getParameterInfo(self):
        shp1 = arcpy.Parameter(
            name="shp1",
            displayName="Enter your first shapefile:",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Input"
        )
        shp1_output = arcpy.Parameter(
            name="shp1_output",
            displayName="Buffered shapefile:",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output"
        )
        return [shp1, shp1_output]

    def execute(self, parameters, messages):
        shp1, shp1_output = parameters
        arcpy.Buffer_analysis(shp1.valueAsText, shp1_output.valueAsText, "12 meters", "FULL", "ROUND", "NONE", "#", "PLANAR")
        arcpy.AddMessage("Buffering of files completed!") #Line above adds the distance (12 meter in this case)

class Dissolve(object):
    def __init__(self):
        self.label = "Dissolve Transportation"
        self.description = ""
        self.canRunInBackground = False
#PART 2: DISSOLVE TOOL
    def getParameterInfo(self):
        return [
            arcpy.Parameter(
                name="input_features",
                displayName="Input Features",
                datatype="DEFeatureClass",
                parameterType="Required",
                direction="Input"
            ),
            arcpy.Parameter(
                name="dissolve_field",
                displayName="Dissolve Field",
                datatype="Field",
                parameterType="Optional",
                direction="Input"
            ),
            arcpy.Parameter(
                name="out_feature_class",
                displayName="Output Feature Class",
                datatype="DEFeatureClass",
                parameterType="Required",
                direction="Output"
            )
        ]

    def execute(self, parameters, messages):
        input_features, dissolve_field, output_feature_class = parameters
        arcpy.management.Dissolve(input_features.valueAsText, output_feature_class.valueAsText, dissolve_field.valueAsText, "", "MULTI_PART", "DISSOLVE_LINES")
        if arcpy.Exists(output_feature_class.valueAsText):
            desc = arcpy.Describe(output_feature_class.valueAsText)
            self.print_description(desc)

    def print_description(self, desc):
        arcpy.AddMessage("File Path = " + str(desc.path))
        arcpy.AddMessage("Shape Type = " + str(desc.shapeType))
        arcpy.AddMessage("Extent = XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax))
        arcpy.AddMessage("Coordinate System name = " + str(desc.spatialReference.name))
        arcpy.AddMessage("Coordinate System type = " + str(desc.spatialReference.type))

class Intersect(object):
    def __init__(self):
        self.label = "Intersect transportation"
        self.description = ""
        self.canRunInBackground = False
#PART 3: Intersect tool
    def getParameterInfo(self):
        return [
            arcpy.Parameter(
                name="input_features",
                displayName="Input Features",
                datatype="Feature Layer",
                parameterType="Required",
                direction="Input"
            ),
            arcpy.Parameter(
                name="intersect_features",
                displayName="Intersect Features",
                datatype="Feature Layer",
                parameterType="Required",
                direction="Input"
            ),
            arcpy.Parameter(
                name="out_feature_class",
                displayName="Output Feature Class",
                datatype="DEFeatureClass",
                parameterType="Required",
                direction="Output"
            )
        ]

    def execute(self, parameters, messages):
        input_features, intersect_features, output_feature_class = parameters
        arcpy.analysis.Intersect([input_features.valueAsText, intersect_features.valueAsText], output_feature_class.valueAsText, "ALL", "", "INPUT")
        if arcpy.Exists(output_feature_class.valueAsText):
            desc = arcpy.Describe(output_feature_class.valueAsText)
            self.print_description(desc)

    def print_description(self, desc):
        arcpy.AddMessage("File Path = " + str(desc.path))
        arcpy.AddMessage("Shape Type = " + str(desc.shapeType))
        arcpy.AddMessage("Extent = XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax))
        arcpy.AddMessage("Coordinate System name = " + str(desc.spatialReference.name))
        arcpy.AddMessage("Coordinate System type = " + str(desc.spatialReference.type))



