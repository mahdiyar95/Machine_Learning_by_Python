# Fundamental codes used in implementation of ML algorithms

1- KNN : the most important point is "how to search in a multi dimensional array in python" , but I tried to explain A-to-Z. <br />
&emsp; &emsp; &emsp; I studied 3 or 4 websites in order to obtain insights into knn, such as:<br />
&emsp; &emsp; &emsp; https://www.c-sharpcorner.com/article/knn-k-nearest-neighbors/

2- Linear Regression : It is roughly the most simplest algorithm in ML. The Linear Regression is used to fit a line to our two-dimensional dataset ( x as input and y as out put) so that the sum of errors throughout the entire dataset is as low as possible ( the Optimization problem is to minimize the summation of errors). Each error is the actual distance between the line and a point in our dataset. When we obtain the line, we can predict new data point by our model (we give x0 to the model and it returens y0). The term regression means that our output is a real number (something like 183.76 and not anything like True, False or ...). I try to code separately in small steps to explain how each line of code works.
