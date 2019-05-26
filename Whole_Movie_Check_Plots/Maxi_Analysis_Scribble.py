# TODO: Do the analysis of all server movies at the same time:

import sys
sys.path.append("../")

from Server_Movies_Paths import GetMovieFilesPaths
from JobScript_Creator.JobScriptCreator_Class import ProcessMovies
from Cell_IDs_Analysis.Extractor_CellIDdetails_Class import GetCellDetails
from Whole_Movie_Check_Plots.Sort_CellIDs_Numerically import SortCellIDFile
from Whole_Movie_Check_Plots.Filter_Root_Leaf_CellIDs import FilterRootLeafCellIDs
from Whole_Movie_Check_Plots.Tracking_Plots_Class import AnalyseAllCellIDs
from Cell_Cycle_Duration.Plot_CC_Duration_Hist import *

import time
start_time = time.process_time()


# Iterate through all movies:
xml_file_list, txt_file_list = GetMovieFilesPaths(exp_type="MDCK_Sc_Tet-_Pure")

for file in sorted(xml_file_list):
    print ("XML File: {}".format(file))
    call = ProcessMovies(file)
    #call.SegClass(BF=True, GFP=False, RFP=True)
    call.Tracking(to_track_GFP=False, to_track_RFP=True)
    #TODO: Check if the output is still called 'tracks_type1.xml' or 'type2'!!!


# Extract cell_ID details by iterating trees:
"""
for xml_file in xml_file_list:
    print ("Processing XML file: {}".format(xml_file))
    GetCellDetails(xml_file=xml_file).IterateTrees()
    print("XML file processed in {} seconds".format(round(time.process_time() - start_time, 2)))
"""

# Sort the cell_IDs in numerical order:
"""
for txt_file in txt_file_list:
    print ("Processing TXT file: {}".format(txt_file))
    SortCellIDFile(txt_file=txt_file)
    print("XML file processed in {} seconds".format(round(time.process_time() - start_time, 2)))
"""

# Filter for files to be used for cell cycle duration analysis:
"""
for sorted_file in txt_file_list:
    sorted_file = sorted_file.replace("raw", "sorted")
    print ("Filtering file (input): {}".format(sorted_file))
    FilterRootLeafCellIDs(txt_file=sorted_file)
    print("Filtered file processed in {} seconds".format(round(time.process_time() - start_time, 2)))
"""

# Do the sanity check for all the movies:
"""
for sorted_file in txt_file_list:
    sorted_file = sorted_file.replace("raw", "sorted")
    print ("Plotting movie graphs for (input): {}".format(sorted_file))
    call = AnalyseAllCellIDs(txt_file=sorted_file)
    call.PlotCellIDLifeTime()
    call.PlotCellIDsPerFrame()
    call.PlotCellCycleAbsoluteTime()
    for i in [80, 40, 20, 5]:
        call.PlotHist_CellCycleDuration(limit=i)
    print("Plotting movie graphs done in {} seconds".format(round(time.process_time() - start_time, 2)))
"""

# Plot stacked histograms for all generations captured per movie:
"""
for filtered_file in txt_file_list:
    filtered_file = filtered_file.replace("raw", "filtered")
    print("Filtered file (input): {}".format(filtered_file))
    try:
        # Some files are empty so nothing can be plotted - prevent printing an error message:
        PlotHistGenerationCCT(txt_file=filtered_file, show=True)
    except:
        print ("File {} could not be processed!".format(filtered_file))
    print("Plotting generational histogram took {} seconds".format(round(time.process_time() - start_time, 2)))
"""

# Plot stacked histograms for all generations in ALL movies at once:
"""
PlotHistGenerationCCT("/Volumes/lowegrp/Data/Kristina/MDCK_WT_Pure/cellIDdetails_merged.txt", show=True)
"""