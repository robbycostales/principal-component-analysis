# Principal_Component_Analysis

On April 4th - 11th, we will learn about the dimension reduction technique called Principal Component Analysis (PCA).  You will have two homework assignments.  The first homework assignment will be math problems in order to help you firmly grasp the background necessary to understand PCA (see Moodle for this assignment).  The second assignment is to implement your own PCA for two applications: image compression and text classification, and analyze your results.

For the second assignment, you will

1. Write a PCA implementation.  
    * In pca.R, skeleton code is provided in the R language.  This code is given for the application of image compression.
    * In python_pca.py, skeleton code is provided in python3.  This code is given for the application of text classification.
    * In virginica.jpg, you will find a color image of an iris, species virginica.
    * In assoc_pressMat.csv, you will find a very sparse matrix, 2247-by-10474, where the columns are indexed by 10474 terms that appear in 2247 Associated Press articles.
    * In assoc_pressTerms.txt, you have access to each of the 10474 terms.

2. Analyze your results.  
    * After applying PCA to the original image, you retrieve a basis of lesser dimension.  What can you do in order to obtain a compressed image?  Describe the image.  Do you believe the low-rank you choose to be the best?  What have we seen in previous lessons that might help you determine this?
    * How do you think you can analyze your results for the Associated Press data?  Hint: understanding what the rows and columns represent in the low-dimensional model can help you!

**Due on April 18th**
