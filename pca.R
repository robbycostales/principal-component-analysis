# compile the function, pca, first
# otherwise R does not recognize

#
# param: data - a matrix
# param: dim_reduced - the dimension you want to reduce data to
#
# returns a list containing the principal components, 
#                the principal values, the low-rank representation of data, 
#                and the relative accuracy of the low-rank representation
#
pca <- function(data, dim_reduced){
  
  # get the dimensions of the data
  N = dim(data)
  num_samples =  
  num_features = 
  
  # determine the covariance matrix of data
  C = 
  
  # find the eigen decomposition
  eigs_decomp = 
  
  # determine which columns of the eigenvector matrix are the principal components
  principal_components = 
  
  # X is the transformed data
  X = 
  # This is how we get the low-dimensional representation of data
  repr = t(X) %*% t(principal_components)
  # how we calculate the relative accuracy
  error = norm( data - repr, '2')/norm(data, '2')
      
  principal_values = 
  
  return( list("transform" = principal_components, "values" = principal_values, "representation" = repr, "relative residual" = error))
  
}

# you'll need to install a library called imager in order to read in the image
library(imager)

image = load.image("./virginica.jpg")
gray = grayscale(image)
data = as.matrix(gray[,,1,1])

#determine your own values for the rank
dim_reduced = 

results = pca(data, dim_reduced)

# what does your image look like?  Include it in your final write up.
plot(as.cimg(results$representation))


