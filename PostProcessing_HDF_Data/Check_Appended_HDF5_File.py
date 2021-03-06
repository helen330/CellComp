import os
import h5py
import matplotlib.pyplot as plt
#from Movie_Analysis_Pipeline.Single_Movie_Processing.Server_Movies_Paths import Get_MDCK_Movies_Paths


filename = "/Volumes/lowegrp/Data/Kristina/Cells_MDCK/GV0795/pos12/HDF/segmented.hdf5"
print ("Does server path exist? {}".format(os.path.exists("/Volumes/lowegrp/")))


f = h5py.File(filename, 'r')

print ("Hdf5 file keys:\t{}".format(list(f.keys())))
print ("Hdf5 file vals:\t{}".format(list(f.values())))
print ("Hdf5 file vals:\t{}".format(len(list(f.values())[0])))

print ()

print ("List of members 'segmentation':\t{}".format(list(f['segmentation']["images"][0])))
print ("List of members 'segmentation':\t{}".format(len(f['segmentation']["images"])))
print ("List of members 'segmentation':\t{}".format(len(f['segmentation']["images"][0])))
print ("List of members 'segmentation':\t{}".format(len(f['segmentation']["images"][0][0])))

#plt.imshow(X=list(f['segmentation']["images"][0]))  # plots a 2D array straight ahead!
#plt.imsave(fname="/Volumes/lowegrp/Data/Kristina/Cells_MDCK/GV0795/pos12/HDF/frm0.png",
#           arr=list(f['segmentation']["images"][0]))
#plt.title("Raw Segmented Binary Mask at frame #0")
#plt.show()
#plt.close()


#print ("List of members 'tracks':\t{}".format(list(f['tracks'])))


# Access 'objects' details:
print ("List of members 'objects':\t{}".format(list(f['objects'])))

print ("Keys per 'objects':\t{}".format(list(f["objects"]["obj_type_1"].keys())))
print ("Vals per 'objects':\t{}".format(list(f["objects"]["obj_type_1"].values())))
print ("Elements per 'coords' GFP:\t{}".format(f["objects"]["obj_type_1"]["coords"]))
print ("Elements per 'coords':\t{}".format(list(f["objects"]["obj_type_1"]["coords"][0:10])))
print ("Elements per 'local_density':\t{}".format(f["objects"]["obj_type_1"]["local_density"]))
print ("Elements per 'local_density':\t{}".format(list(f["objects"]["obj_type_1"]["local_density"][0:10])))
print ("Elements per 'nucleus_size':\t{}".format(f["objects"]["obj_type_1"]["nucleus_size"]))
print ("Elements per 'nucleus_size':\t{}".format(list(f["objects"]["obj_type_1"]["nucleus_size"][0:10])))
# [172, 157, 23, 37, 223, 177, 155, 62, 205, 110]
print ("Elements per 'fluo_signal_sum':\t{}".format(f["objects"]["obj_type_1"]["fluo_signal_sum"]))
print ("Elements per 'fluo_signal_sum':\t{}".format(list(f["objects"]["obj_type_1"]["fluo_signal_sum"][0:10])))

print ("Elements per 'labels':\t{}".format(f["objects"]["obj_type_1"]["labels"]))
print ("Elements per 'labels':\t{}".format(list(f["objects"]["obj_type_1"]["labels"][0:10])))
print ("Elements per 'map':\t{}".format(len(f["objects"]["obj_type_1"]["map"])))
print ("Elements per 'map':\t{}".format(list(f["objects"]["obj_type_1"]["map"][0:10])))

# Access 'tracks' details:
print ("List of members 'tracks':\t{}".format(list(f['tracks'])))

print("Keys per 'objects':\t{}".format(list(f["tracks"]["obj_type_1"].keys())))
print("Vals per 'objects':\t{}".format(list(f["tracks"]["obj_type_1"].values())))
print("Elements per 'fates':\t{}".format(f["tracks"]["obj_type_1"]["fates"]))
print("Elements per 'fates':\t{}".format(list(f["tracks"]["obj_type_1"]["fates"][0:10])))
print("Elements per 'tracks':\t{}".format(f["tracks"]["obj_type_1"]["tracks"]))
print("Elements per 'tracks':\t{}".format(list(f["tracks"]["obj_type_1"]["tracks"][0:10])))
print("Elements per 'map':\t{}".format(f["tracks"]["obj_type_1"]["map"]))
print("Elements per 'map':\t{}".format(list(f["tracks"]["obj_type_1"]["map"][0:10])))
print("Elements per 'LBEPR':\t{}".format(f["tracks"]["obj_type_1"]["LBEPR"]))
print("Elements per 'LBEPR':\t{}".format(list(f["tracks"]["obj_type_1"]["LBEPR"][0:10])))
print("Elements per 'Ch_Ch_Gen_CCT':\t{}".format(f["tracks"]["obj_type_1"]["Ch_Ch_Gen_CCT"]))
print("Elements per 'Ch_Ch_Gen_CCT':\t{}".format(list(f["tracks"]["obj_type_1"]["Ch_Ch_Gen_CCT"][0:10])))



if f.__bool__():
    f.close()

