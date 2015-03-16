# Image_compression
I programmed this little app myself when I saw something similar in one of the coursera MOOCs I took. I liked the kind of unconventional application of the K-Means Algorithm, that's why I wanted to share it.
The idea of the project was as follows: Let the user chose (the path to a) picture, which the program will read in represent its pixels as points in the 3-dimensional RGB-Space. It will be compressed by representing it with a fewer number of colors.
The amount of distinct colors (say n) to represent the entire image is prespecified in the code.
K-Means finds clusters in which each pixels fall. The cluster-centroids will represent good approximations to each of the pixel values in the clusters.
Each pixel is replaced by its cluster-centroid and the pixels are recomposed to an image and saved to file.

I ran it on the tree.tiff image in the data folder. It's compressions for n=16 and n=256 colors are shown in there as well.

tree_reduced_16 tree_reduced_265 tree

The 16 color version is 375KB, the 265 color version 495KB and the original 1.9MB. Obviously not the most efficient way to compress pictures, but you can clearly see the difference in all three pictures - especially in the gradients of the clouds.

