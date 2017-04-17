#! /usr/bin/env python3

#
# Graded by Amanda on 4/17
# 0/30
#

# Author: Robert Costales
# Date: 2017 04 12
# Language: Python 3
# Overview: This program converts the matrix of pixel values of an image
#           into a lower dimensional space using the PCA method

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_ IMPORT STATEMENTS _-_-_-_-_-_-_-_-_-_-_-_-_-_ #

import copy
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import time

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_ RUN PREFERENCES _-_-_-_-_-_-_-_-_-_-_-_-_-_-_ #

show_init_image = False     # shows initial image from gray-scale matrix

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_ FUNCTIONS _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ #


def pca(data, dim_reduced):
    """
    :param data: the data we want to transform (grayscale valued matrix)
    :param dim_reduced: the size of the transformed data
    :return: reduced dimension image matrix
    """
    # find the covariance matrix
    y = data
    yt = np.transpose(y)
    c = np.cov(y)             # create covariance matrix
    eig_val, eig_vec = np.linalg.eig(c)                  # eig_val, eig_vec
    idx = eig_val.argsort()[::-1]
    eig_val = eig_val[idx]
    eig_vec = eig_vec[:, idx]

    q = eig_vec                             # is full eigen-vector matrix
    qt = np.transpose(q)                    # transpose of q
    p = qt[0:dim_reduced]                  # takes first dim_reduced rows of qt

    print("P Dimensions:  ", len(p), " ")
    if len(p) != 0:
        print(len(p[0]))
    else:
        print(" ")

    v = np.matmul(p, y)
    vt = np.transpose(v)
    redyt = np.matmul(vt, p)
    redy = np.transpose(redyt)

    error = np.linalg.norm(y - redy, ord=2) / np.linalg.norm(y, ord=2)
    print("Error: {}".format(error))


    print("Image Dimensions:  ", len(redy), len(redy[0]))
    print(" ")

    plt.gray()  # comment this out for fun colors
    plt.imshow(redy)
    plt.show()


# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_ IMAGE PROCESSING _-_-_-_-_-_-_-_-_-_-_-_-_-_ #

rgb = misc.imread('virginica.jpg')  # 441x600x3 array (RGB)

gray = []
for i in rgb:           # matrix converted to gray-scale values
    a = []
    for j in i:
        a.append(sum(j)/len(j)/255)
    gray.append(copy.deepcopy(a))

# gray is a 441x600 matrix of gray-scale intensity values between 0 and 1

plt.gray()              # comment this out for fun colors
plt.imshow(gray)
if show_init_image:
    plt.show()

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_ PCA CALL _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ #

#
# Robby, for some reason this doesn't work? Nothing appears for me, just black images, even when k = 441
#
print("k = {}".format(441))
pca(gray, 441)
print("k = {}".format(310))
pca(gray, 310)
print("k = {}".format(231))
pca(gray, 231)
print("k = {}".format(100))
pca(gray, 100)
print("k = {}".format(50))
pca(gray, 50)
print("k = {}".format(25))
pca(gray, 25)
print("k = {}".format(7))
pca(gray, 7)
print("k = {}".format(3))
pca(gray, 3)
print("k = {}".format(1))
pca(gray, 1)
print("k = {}".format(0))
pca(gray, 0)
