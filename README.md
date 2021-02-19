# Color_Pallets_image_filter

* This project implements an image filter than reduces an image to only use a few core colros. 
* Filtering images produces interesting images that looks blurry a little bit.
* If we type specific numbers of colors, the number of clusters are grouping together. 
* Then, we can see the images that have only few or some number of colors.

# K-means algorithm

* I implement K-means algorithm. It uses two primary pieces of data, the "means" list, and the assignments list-of-lists.
* As it keep updating the means list, it recomputes the assignments list, so each pixel is assigned to the "closest" color match in the means list.
* Finally, the algorithm will find a good set of menas, and assignments, and will not change once updated.
