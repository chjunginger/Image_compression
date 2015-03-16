__author__ = 'christianjunginger'
from PIL import Image
from sklearn.cluster import MiniBatchKMeans
import numpy as np
import re
import math


#This is a program that reduces an Image to a specific number of colors by using a KNN-Algorithm
#Note that since KNN depends on initialconditions, the output might vary very time


#Input an image (jpg) and parameters (number of colors and "k")
in_path='%s'%raw_input("Path to the image: ")
out_path=re.sub(r'.[^.]+$','_reduced.gif',in_path)

#set number of colors
n=256


#Step1: Convert image to R,G and B Matrix
picture=Image.open(in_path)
aspect=picture.size
pixmap=list(picture.getdata())
print(pixmap)

#Step2: run kmeans Clustering on it
Clust=MiniBatchKMeans(n_clusters=n,compute_labels=True,)
Clust.fit(pixmap)
centers=Clust.cluster_centers_.astype(int)
centers=tuple([tuple(row) for row in centers])
labels=np.array(Clust.labels_)

#built reduced pixelmatrix
pixmap_red=[centers[i] for i in labels]

#Output reduced image
out=Image.new("RGB",aspect)
out.putdata(pixmap_red)
out.save(out_path)
