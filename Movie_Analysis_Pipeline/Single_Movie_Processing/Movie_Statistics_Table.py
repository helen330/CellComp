import os
import sys
sys.path.append("../")

import statistics as stats
from texttable import Texttable              # creates simple ASCII tables
from Whole_Movie_Check_Plots.Server_Movies_Paths import GetMovieFilesPaths
from Whole_Movie_Check_Plots.Tracking_Plots_Class import AnalyseAllCellIDs


def GetMovieSummary(exp_type):
    """ Print a table & write a file summarising the properties of all movies available per experiment.
    Args:
        exp_type (string)  ->   Type of experiment.
                                 Options: "MDCK_WT_Pure", "MDCK_Sc_Tet-_Pure", "MDCK_Sc_Tet+_Pure"
    Return:
        None.
        Prints a table into a console.
        Writes a txt_file into the directory given by cell_type.
    """

    name = "C E L L  T Y P E : '{}'\n".format(exp_type)
    _, txt_file_list = GetMovieFilesPaths(exp_type=exp_type)

    movie_number = []
    movie_date = []
    movie_pos = []
    total_frames = []
    total_divisions = []
    mean_div_time = []
    std_div_time = []
    num_lines_raw = []
    num_lines_trimmed = []
    num_lines_sorted = []
    num_lines_filtered = []

    # How many movies do you have available?
    total_movies = 0
    if exp_type == "MDCK_WT_Pure":
        total_movies = 18
    if exp_type == "MDCK_Sc_Tet-_Pure":
        total_movies = 13
    if exp_type == "MDCK_Sc_Tet+_Pure":
        total_movies = 13
    if exp_type == "MDCK_90WT_10Sc_NoComp":
        total_movies = 3    # out of 16


    for order, raw_file in enumerate(sorted(txt_file_list)):

        print("\nProcessing txt_file: {}".format(raw_file))

        # Initialise 3 types of files:
        trimmed_file = raw_file.replace("raw", "trimmed")
        sorted_file = raw_file.replace("raw", "sorted")
        filtered_file = raw_file.replace("raw", "filtered")

        # Order the movies, get their date & pos:
        movie_number.append(order + 1)
        movie_date.append(sorted_file.split("/")[-4])
        movie_pos.append(sorted_file.split("/")[-3])

        # Get total number of frames per movie:
        path = "/Volumes/lowegrp/Data/Kristina/{}/{}/{}/segmented/".format(exp_type, movie_date[order], movie_pos[order])
        frame_count = os.listdir(path)
        frame_count = [item for item in frame_count if str(item).startswith("s_") and str(item).endswith(".tif")]
        total_frames.append(len(frame_count))

        # Get number of divisions (every non-leaf cell):
        div_counter = 0
        for line in open(sorted_file, 'r'):
            line = line.rstrip().split('\t')
            if line[0] != 'Cell_ID' and line[7] == "False":
                div_counter += 1
        total_divisions.append(div_counter)

        # Extract cell cycle duration according to given limit:
        cct_hrs = []
        for line in open(filtered_file, "r"):
            line = line.rstrip().split("\t")
            if line[0] == 'Cell_ID':
                continue
            # Include only non-root & non-leaf cell_IDs:
            if line[6] == "False" and line[7] == "False":
                cct_hrs.append(float(line[4]))

        # Get mean division time per movie (condition for movies which are too short to output usable data):
        if len(cct_hrs) >= 2:
            mean_div_time.append(round(stats.mean(cct_hrs), 2))
            std_div_time.append(round(stats.stdev(cct_hrs), 2))
        else:
            mean_div_time.append(0.0)
            std_div_time.append(0.0)

        # Count number of lines per file:   (-1 to exclude header OR -2 to take the weird line out from 'raw_file')
        num_lines_raw.append(sum(1 for line in open(raw_file)) - 2)
        num_lines_trimmed.append(sum(1 for line in open(trimmed_file)) - 1)
        num_lines_sorted.append(sum(1 for line in open(sorted_file)) - 1)
        num_lines_filtered.append(sum(1 for line in open(filtered_file)) - 1)

    # Write the table & file name & header:
    table = Texttable(max_width=0)
    print (name)
    header = ["Movie", "DataDate", "Pos", "Frms", "Div#", "MeanDT", "StdDT", "Raw-l", "Trim-l", "Sort-l", "Filt-l"]
    table.header(header)

    # Write into a new file:
    summary_file = "/Volumes/lowegrp/Data/Kristina/{}/summary_movies.txt".format(exp_type)
    summary_file = open(summary_file, "w")
    summary_file.write(name)
    header_string = ''
    for item in header:
        header_string += str(item) + "\t"
    header_string = header_string[:-1]
    header_string += "\n"
    summary_file.write(header_string)

    for i in list(range(0, total_movies)):
        my_list = [movie_number[i], movie_date[i], movie_pos[i], total_frames[i], total_divisions[i], mean_div_time[i],
                   std_div_time[i], num_lines_raw[i], num_lines_trimmed[i], num_lines_sorted[i], num_lines_filtered[i]]
        table.add_row(my_list)
        string = ''
        for item in my_list:
            string += str(item) + "\t"
        string = string[:-1]
        string += "\n"
        summary_file.write(string)

    # Print the table & close the newly-written file:
    print(table.draw())
    summary_file.close()


GetMovieSummary(exp_type="MDCK_WT_Pure")
#GetMovieSummary(exp_type="MDCK_Sc_Tet-_Pure")      # tracking not completed
#GetMovieSummary(exp_type="MDCK_Sc_Tet+_Pure")      # tracking not completed
#GetMovieSummary(exp_type="MDCK_90WT_10Sc_NoComp")  # 2 channels!