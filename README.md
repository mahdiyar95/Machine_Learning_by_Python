# Fundamental codes used in implementation of ML algorithms

1- **KNN** : (Supervised Learning --> KNN)
  - The most important point is "how to search in a multi dimensional array in python" , but I tried to explain A-to-Z. <br />
&emsp; &emsp; &emsp; I studied 3 or 4 websites in order to obtain insights into knn, such as:<br />
&emsp; &emsp; &emsp; https://www.c-sharpcorner.com/article/knn-k-nearest-neighbors/

2- **Linear Regression** : (Supervised Learning --> Linear Regression) <br/>
  - It is roughly the most simplest algorithm in ML. The Linear Regression is used to fit a line to our two-dimensional dataset ( x as input and y as out put) so that the sum of errors throughout the entire dataset is as low as possible ( the Optimization problem is to minimize the summation of errors). Each error is the actual distance between the line and a point in our dataset. When we obtain the line, we can predict new data point by our model (we give x0 to the model and it returens y0). The term regression means that our output is a real number (something like 183.76 and not anything like True, False or ...). I try to code separately in small steps to explain how each line of code works.
<br /><br />

3- **Epsilon_Greedy** : (Reinforcement Learning --> Epsilon_Greedy)<br />
  - Algorithm
    - Our goal is to maximize the total rewards and our limitation is that (in reality) we do not know each machine's win probability, so we choose the best machine. Therefore, to obtain these probabilities, we need to play with all machines. But how much we should explore? The actual aim is to strike a balance between exploration and exploitation. The algorithm's approach to doing this is whenever we want to play, decide between explore and exploit. The decision will be made by chance so that in each step, we generate a random number between 0 and 1, if the number is less than epsilon, we explore and vice versa.

  - Program<br/>
      - Let's say we are in a casino that has 4 machines and we are allowed to play 10000 times. Each time we select one of those machines and play with that. The rule is If the machine returns 1, we obtain 1 dollar and if it returns 0, we don't gain. So, we want to collect dollars as much as possible by applying the epsilon-greedy method. Therefore, the program should simulate us and machines.To do that we need to :
      - Create a machine object. This object simulates a machine that does two functions. First, "pull" : returns 1 (win) with machine probability ("p") and second, "update" : updates the machine's success rate.
<br/>
      - Create 4 machines with 4 different win probabilities
<br/>
      - Run the algorithm over a 70000-iteration period.
<br/>
      - Demonstrate the results including: . the number of explorations . the number of exploitations . the number of selecting the best machine . Total rewards . overall win rate
