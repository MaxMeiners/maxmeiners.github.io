### 1. What is machine learning?
- Machine learning is a thing labeler

### 2. How is Machine Learning different from traditional programming?
- It differs on where the recipe comes from.

### 3. When is Machine Learning useful? Try to summarize the video in your own words, and give an example of a problem that can be solved using Machine Learning, and an example of a problem that can be solved using traditional programming
- In situations where it is very difficult to solve problems yourself. If there are no patters visible in the data, then Machine Learning is useful.

### 4. In the example provided, one of the patterns mentioned is the background of the image. Do you feel that this is a useful pattern for Machine Learning and AI to learn as a key feature that distinguishes dogs from cats? If you had to choose one pattern that is most useful to learn what separates dogs from cats, what would it be, and why?
- I don't think that the background of an image is a good pattern, this is because a cat can have the same background as a dog. I would choose to build a model that looks at the sizes of cats and dogs.

### 5. What is the purpose of a test set, and can you think of any other way to evaluate the performance of a machine learning algorithm?
- The purpose of the test set is to evaluate the performance of a Machine Learning algorithm. 
- Another way to evaluate the performance of a machine learning algorithm is by making a confusion matrix.

### 6. Do you agree with the statement that machine learning is an art? Please justify your answer.
- I do, because it takes a lot of time and effort to write good machine learning code.

### 7. You are asked to develop a machine learning system to predict if a given X-Ray image contains a tumour or not. Would you approach this problem with a supervised learning approach, or unsupervised. Please justify your choice of an answer.
- I would use a supervised learning approach, because here the algorithm is trained on a labeled dataset. This means that each example in the dataset, the algorithm knows what the correct output is. When talking about tumours, the algorithm compares pictures of tumours with each other and can then say if it a tumour yes or no.

### 8. You are asked to develop a machine learning system to group the different neighborhoods of Breda into developed and underdeveloped clusters. Would you approach this problem with a supervised learning approach, or unsupervised. Please justify your choice of an answer.
- I would approach this problem with a unsupervised learning approach. An unsupervised model can cluster images by the objects they contain, without being told what those objects were ahead of time.

### 9. Please provide an example of a problem that uses Reinforcement learning. Attach links and videos to your answer.
- In healthcare, patients can receive treatment from polices learned from RL systems. 
- https://neptune.ai/blog/reinforcement-learning-applications#:~:text=Some%20of%20the%20autonomous%20driving,by%20learning%20automatic%20parking%20policies.

### 10. What is a correlation coefficient? What does it tell you about the relationship between two variables?
- A correlation coefficient is a statistical measure of the degree to which changes to the value of one variable predict change to the value of another. In positively correlated variables, the value increases or decreases in tandem.

### 11. Note down your high score in the Guess the correlation in your mentor channel on teams. Create a leaderboard and let's see who can get the highest score.
- Done :), my high score is 93.

### 12. What is the accuracy of your model? Report the accuracy on the training as well as test set?
- It is around 75%.

### 13. What is the difference between the accuracy on the training and test set? What do you observe?
- Difference between training accuracy and test accuracy. Training accuracy means that identical images are used both for training and testing, while test accuracy represents that the trained model identifies independent images that were not used in training.

### 14. In your own words, what is the difference between model_object.fit() and model_object.predict?
-  Fit() method will fit the model to the input training instances while predict() will perform predictions on the testing instances

### 15. Do you think your Model does a good job when it comes to predicting new data?
- It does, but the probability of making a mistake (which is 25%) is quite high and should be improved.

### 16. Is this a form of supervised or unsupervised learning? Why?
- This is a type of supervised learning, because it is used to predict something, which is not possible for unsupervised Machine Learning

### 17. What is the target variable?
- A target variable is predicting if a passenger should have survived the sinking of the ship.

### 18. Please try to list out some variables that you feel can be used to predict the target variable (be creative and do not restrict yourselves to the data at hand).
- Class of the ticket
- Age
- Gender
- Salary
- Location of the house/apartment
- Country