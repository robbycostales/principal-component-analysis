#! /usr/bin/env python3

#
# Graded by Amanda on 4/17
# 0/30
#

# Authors: Robert Costales, Roop Pal
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


def pca(data, dim_reduced, show_plot=True):
    """
    :param data: the data we want to transform (grayscale valued matrix)
    :param dim_reduced: the size of the transformed data
    :return: error, (n, m, c)
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
    p = qt[0:dim_reduced]                 # takes first dim_reduced rows of qt

    v = np.matmul(p, y)
    n = len(qt)
    if dim_reduced ==0:
        m = 0
    else:
        m = len(v[0])
    c = len(y)

    vt = np.transpose(v)
    redyt = np.matmul(vt, p)
    redy = np.transpose(redyt)

    error = np.linalg.norm(y - redy, ord=2) / np.linalg.norm(y, ord=2)

    # Print statements
    if show_plot:
        print("P Dimensions:  ", len(p), " ")
        if len(p) != 0:
            print(len(p[0]))
        else:
            print(" ")
        print("Error: {}".format(error))
        print("Image Dimensions:  ", len(redy), len(redy[0]))
        print(" ")

    if show_plot:
        plt.clf()
        plt.gray()  # comment this out for fun colors
        plt.imshow(redy)
        fig = plt.gcf()
        fig.canvas.set_window_title("k = {}".format(dim_reduced))
        plt.gcf()
        plt.show()

    return error, (n, m, c), v

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_ IMAGE PROCESSING _-_-_-_-_-_-_-_-_-_-_-_-_-_ #
if __name__ == '__main__':
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
    # When we decrease our k value from the original dimension of the nxn covariance matrix,
    # and we multiply vT with P (for that k), we get a compressed image
    #

    show_int_images = True
    print("k = {}".format(441))
    pca(gray, 441, show_int_images)
    print("k = {}".format(310))
    pca(gray, 310, show_int_images)
    print("k = {}".format(231))
    pca(gray, 231, show_int_images)
    print("k = {}".format(100))
    pca(gray, 100, show_int_images)
    print("k = {}".format(50))
    pca(gray, 50, show_int_images)
    print("k = {}".format(25))
    pca(gray, 25, show_int_images)
    print("k = {}".format(7))
    pca(gray, 7, show_int_images)
    print("k = {}".format(3))
    pca(gray, 3, show_int_images)
    print("k = {}".format(1))
    pca(gray, 1, show_int_images)
    print("k = {}".format(0))
    pca(gray, 0, show_int_images)

    # _-_-_-_-_-_-_-_-_-_-_-_-_-_-_ ERROR _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ #

    min_aic = -1
    min_k = -1
    aics = []
    ks = range(1, 200, 3)

    print("Please wait for results... (may take up to a minute--trying to fix)\n")
    for i in ks:
        error, (n, m, c) = pca(gray, i, False)
        aic = ((n+m)*i)/c + error*255*8
        aics.append(aic)
        if aic < min_aic or min_aic == -1:
            min_k = i
            min_aic = aic


    print("Minimized error around k={0}".format(min_k))

    plt.clf()
    plt.scatter(ks, aics)
    plt.title("AIC vs K")
    fig = plt.gcf()
    fig.canvas.set_window_title("Optimizing K")
    plt.show()

    print("k = {}\n".format(min_k))
    pca(gray, min_k)
