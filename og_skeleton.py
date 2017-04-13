import numpy as np
from numpy import linalg as la
import pandas as pd


#
# param: data - the data we want to transform, it's a pandas data frame
# param: dim_reduced - the size of the transformed data
#
# returns a dictionary containing the principal components, principal values, the low-dimensional representation, and relative accuracy
#
def pca(data, dim_reduced):
    # calculate the dimensions of the data
    num_samples, num_features = len(data), len(data[0])
    # find the covariance matrix
    C = np.cov(data)
    # find the eigen vectors and eigen values of the covariance matrix
    eig_val, eig_vec = la.eig(C)
    # determine which columns in eig_vec are the principal components
    principal_components =

    # multiply the principal components and the data to transform
    X =
    # the low-dimensional representation
    repr = np.matmul(X.transpose(), principal_components.transpose())
    # relative accuracy
    error = np.linalg.norm(data - repr.transpose(), ord=2) / np.linalg.norm(data, ord=2)

    # what are the principal values?
    principal_values =

    return {"transform": principal_components, "values": principal_values, "representation": repr,
            "relative residual": error}


# For the term-document matrix
data = pd.read_csv(open('./Documents/assoc_pressMat.csv'))
# choose your own low-rank
dim_reduced =

results = pca(data, dim_reduced)