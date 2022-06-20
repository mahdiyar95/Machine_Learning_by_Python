# ML Intuition


I've tried to share codes that give us better intuition of algorithms, For instance, running an algorithm with different parameter values.


#### Epsilon_Greedy_EPS_effect : (Reinforcement Learning --> Epsilon_Greedy)
  - As mentioned in the ML_algoriths branch, the "epsilon_greedy" method has two parameters: epsilon and the number of iterations. Choosing the appropriate epsilon value is critical to making our algorithm converge into selecting the best casino machine and maximizing the overall reward. Assume we have four simple machines that generate 1 (win) with their p probability, and we aim to maximize the overall reward (or equivalently, always choose the best machine). The actual issue is we don't know machines' p parameters, so we should play with them to obtain a sense of which machine has the highest p and this matter costs. To say that, We can play only 10,000 times and not more, so our exploration to find the best machine reduces our opportunities to exploit that.

  - To illustrate the effects of epsilon values on our results, the "Epsilon_Greedy" code has used six different values of epsilon: 0.01, 0.05, 0.1, 0.2, 0.3, and 0.4. As you can see, for the epsilon values more than 0.1, our overall rewards decrease as a result of unnecessary explorations and losing more exploitation opportunities. With more machines (20 machines, for instance), it seems reasonable to explore more. On the other hand, by decreasing the epsilon to less than 0.1, we can obtain more rewards, although the figures show that the convergence has taken place slower than when the epsilon is equal to 0.1. 
