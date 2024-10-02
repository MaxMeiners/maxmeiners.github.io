---
layout: page
title: Machine Learning Projects
subtitle: A collection of my machine learning projects
cover-img: /assets/img/ai_cover_photo.jpg
thumbnail-img: /assets/img/Cropped_Image.png
share-img: /assets/img/ai_cover_photo.jpg
gh-repo: maxmeiners
gh-badge: [star, fork, follow]
tags: [computer vision, data science, deep learning, artificial intelligence, projects]
comments: true
author: Max Meiners
---

<div class="accordion">
  <input type="checkbox" id="image_recognition" />
  <label for="image_recognition">CNN-Based Animal Species Classification</label>
  <div class="content">
    <h3><strong>CNN-Based Animal Species Classification</strong></h3>
    <p>This project involved developing a Convolutional Neural Network (CNN) model to classify images of different animal species using TensorFlow and Keras. I specifically chose to build an image classifier capable of distinguishing between cheetahs, foxes, hyenas, lions, tigers, and wolves. The project aimed to create a robust model that could accurately classify images into these categories. The dataset was preprocessed using Python libraries such as OpenCV, and additional image manipulation was done using the Keras ImageDataGenerator to improve model performance.
    </p>
    <p>
      As part of this project, I also developed a small (non-working) application for users to what kind of animal they have spotted. The app is called "In the W(A.)I.ld". The application would then classify the animal and display the area of the image that the model paid the most attention to in order to classify it into its specific class. In addition, the app included a small game, where users were given an animal image and had to assign it to one of the six classes (Cheetah, Fox, Hyena, Lion, Tiger, Wolf). This interactive feature was designed to make the project more engaging while demonstrating the practical use of the CNN model.
    </p>

    <h4>Interactive Application</h4>
    <p>
      Below is the interactive application I created. You can try the app here:
    </p>
    
    <iframe src="/assets/app/preview.html" width="800" height="600" frameborder="0" allowfullscreen="true"></iframe>


    <h4>Key Findings:</h4>
    <ul>
      <li>The CNN model achieved high accuracy in classifying the different animal species, with the best model achieving over 90% accuracy on the validation set.</li>
      <li>Grad-CAM provided useful visual explanations of which parts of the image the model was focusing on to make predictions, helping to interpret the results.</li>
      <li>Data augmentation significantly improved model performance by preventing overfitting, especially in the case of smaller datasets.</li>
    </ul>

    <h4>Skills Gained:</h4>
    <ul>
      <li><strong>Deep learning and CNN architecture</strong> using TensorFlow and Keras to build and train animal species classification models.</li>
      <li><strong>Image processing</strong> using OpenCV and Skimage for data preprocessing and augmentation.</li>
      <li><strong>Model interpretability</strong> through Grad-CAM and LIME to visualize and explain model decisions.</li>
      <li><strong>Application development</strong> to create an interactive image classification tool and a game for user engagement.</li>
      <li><strong>GPU configuration and optimization</strong> for training deep learning models using TensorFlow.</li>
    </ul>

    <p>
      You can view the full code for this project in my Jupyter Notebook here: <a href="https://nbviewer.org/github/MaxMeiners/maxmeiners.github.io/blob/master/Year%201%20ADS%26AI%20repositories/Project%203/Deliverables/Creative-Brief-CNN.ipynb" target="_blank">NBViewer link</a>.
    </p>
  </div>
</div>