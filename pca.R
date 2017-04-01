
library(imager)

image = load.image("./virginica.jpg")
gray = grayscale(image)
data = as.matrix(gray[,,1,1])

dim_reduced = 20

results = pca(data, dim_reduced)

plot(as.cimg(results$representation))
print(results$`relative residual`)

pca <- function(data, dim_reduced){
  
  N = dim(data); num_samples = N[1]; num_features = N[2];
  
  C = cov(data)
  
  eigs_decomp = eigen(C, symmetric = TRUE)
  
  principal_components = eigs_decomp$vectors[,1:dim_reduced]
  
  D = dim(principal_components)
  
  if(D[1] != num_samples){
    
    X = t(principal_components) %*% t(data)
    repr = t(X) %*% t(principal_components)
    error = norm( data - repr, '2')/norm(data, '2')
      
  }else{
  
    X = t(principal_components) %*% data
    repr = principal_components %*% X
    error = norm(data - repr, '2')/norm(data, '2')
  
  }
  
  principal_values = eigs_decomp$values[1:dim_reduced]
  
  return( list("transform" = principal_components, "values" = principal_values, "representation" = repr, "relative residual" = error))
  
}