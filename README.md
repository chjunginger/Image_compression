# Image_compression
I programmed this little app myself when I saw something similar in one of the coursera MOOCs I took. I liked the kind of unconventional application of the K-Means Algorithm, that's why I wanted to share it.
The idea of the project was as follows: Let the user chose (the path to a) picture, which the program will read in represent its pixels as points in the 3-dimensional RGB-Space. It will be compressed by representing it with a fewer number of colors.
The amount of distinct colors (say n) to represent the entire image is prespecified in the code.
K-Means finds clusters in which each pixels fall. The cluster-centroids will represent good approximations to each of the pixel values in the clusters.
Each pixel is replaced by its cluster-centroid and the pixels are recomposed to an image and saved to file.

An exemplary compression can be found on my blog (TBA.)

