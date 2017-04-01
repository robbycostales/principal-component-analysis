import numpy as np
from numpy import linalg as la
import pandas as pd

def pca(data, dim_reduced):
  
    num_samples, num_features = np.shape(data); 
    C = np.cov(data)
    
    eig_val, eig_vec = la.eig(C)
    
    principal_components = eig_vec[:,0:dim_reduced]
    
    n, k = np.shape(principal_components)
    
    # X = t(principal_components) %*% t(data)
    # repr = t(X) %*% t(principal_components)
    # error = norm( data - repr, '2')/norm(data, '2')
        
    principal_values = eig_val[0:dim_reduced]
    
    return {"transform":principal_components, "values":principal_values, "representation":repr, "relative residual":error}
    
# For the term-document matrix
data = pd.read_csv(open('./Documents/assoc_pressMat.csv'))
dim_reduced = 20

results = pca(data, dim_reduced)

# plot(as.cimg(results$representation))
# print(results$`relative residual`)


  
