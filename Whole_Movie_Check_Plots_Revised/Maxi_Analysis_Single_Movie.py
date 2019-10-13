# Do the analysis of single selected server movie all at once:

import time
start_time = time.process_time()

from Whole_Movie_Check_Plots_Revised.A_Extractor_CellIDdetails_Class import GetCellDetails
from Whole_Movie_Check_Plots_Revised.B_Processor_TxtFile_RawToFiltered import FilterRawTxtFile
from Whole_Movie_Check_Plots_Revised.C_Checker_General_Movie_Graphs import AnalyseAllCellIDs
from Whole_Movie_Check_Plots_Revised.D_Plotter_Branched_Lineage_Trees import PlotLineageTree


# Which movies to analyse? Create a list [one-item list if single movie]:
for i in range(15, 25):
    xml_file = "/Volumes/lowegrp/Data/Kristina/MDCK_90WT_10Sc_NoComp/17_07_24/pos13/tracks_try_{}/tracks_type2.xml".format(i)
    raw_file = "/Volumes/lowegrp/Data/Kristina/MDCK_90WT_10Sc_NoComp/17_07_24/pos13/analysis_try_{}/channel_RFP/cellIDdetails_raw.txt".format(i)

    call_A = GetCellDetails(xml_file=xml_file).IterateTrees()
    call_B = FilterRawTxtFile(raw_file=raw_file)
    call_C = AnalyseAllCellIDs(txt_file=raw_file)
    call_C.PlotCellIDLifeTime()
    call_C.PlotCellIDsPerFrame()
    call_C.PlotCellCycleAbsTime()
    call_C.PlotHistCellCycleTime()

    call_D = PlotLineageTree(xml_file=xml_file)
    print ("Trees_total = {}; Trees_plotted = {}".format(call_D[0], call_D[1]))


#call_C.PlotCellIDRelabelling(print_stats=True)
#TODO: print_stats=True     Fix ZeroDivisionError
#TODO: print_stats=False    ValueError: shape mismatch: objects cannot be broadcast to a single shape