---
layout: page
title: Machine Learning Projects
subtitle: A collection of my machine learning projects
cover-img: /assets/img/ai_cover_photo.jpg
# thumbnail-img: /assets/img/Cropped_Image.png
share-img: /assets/img/ai_cover_photo.jpg
gh-repo: maxmeiners
gh-badge: [star, fork, follow]
tags: [computer vision, data science, deep learning, artificial intelligence, projects]
comments: true
author: Max Meiners
---

<style>
  .accordion {
    margin-bottom: 1em;
  }

  .accordion input[type="checkbox"] {
    display: none;
  }

  /* Accordion label styling */
  .accordion label {
    background-color: #2D3748; /* Match navbar color */
    color: #F7FAFC; /* Match navbar text color */
    cursor: pointer;
    padding: 18px;
    width: 100%;
    border: none;
    text-align: left;
    outline: none;
    font-size: 18px;
    transition: background-color 0.4s ease;
    display: block;
  }

  /* Hover effect for label */
  .accordion label:hover {
    background-color: #A0AEC0; /* Match navbar border color for hover */
  }

  /* Symbol for dropdown state */
  .accordion label:after {
    content: '+';
    float: right;
  }

  .accordion input:checked + label:after {
    content: '-';
  }

  /* Content section styling */
  .accordion .content {
    height: 0;
    overflow: hidden;
    transition: height 0.4s ease;
    background-color: #F0F4F8; /* Match page background color */
  }

  /* When accordion is open */
  .accordion input:checked + label + .content {
    height: auto;
    padding: 18px;
    border-top: 1px solid #A0AEC0; /* Match navbar border color */
  }

  /* Links within content */
  .accordion .content a {
    color: #FF6B6B; /* Match link color */
  }

  /* Hover effect for links */
  .accordion .content a:hover {
    color: #FF8E72; /* Match hover color */
  }
</style>

<h2>Computer Vision Projects</h2>

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


<div class="accordion">
  <input type="checkbox" id="npec" />
  <label for="npec">AI-Driven Plant Analysis for NPEC</label>
  <div class="content">
    <h3><strong>AI-Driven Plant Analysis for the Netherlands Plant Eco-phenotyping Center (NPEC)</strong></h3>
    <p>
      For this project, I worked in collaboration with the <strong>Netherlands Plant Eco-phenotyping Center (NPEC)</strong>, through my association with Breda University of Applied Sciences. The project's primary objective was to revolutionize plant phenotyping by integrating computer vision and robotics to enhance plant root analysis and improve automation in precision inoculation.
    </p>
    
    <p>
      To address plant phenotyping challenges, computer vision techniques were employed to isolate Petri dishes from background noise and perform semantic segmentation of plant components like seeds, shoots, and roots. With a refined and preprocessed dataset, I developed a machine learning model capable of accurately predicting masks for different plant structures. This allowed for instance segmentation, which identified individual plants in the images and facilitated detailed measurements, such as root length and the precise localization of root tips—a critical step in assessing plant growth and traits.
    </p>

    <p>
      In parallel with the computer vision work, the robotics aspect of the project focused on automating the delivery of inoculants to the identified plant root tips. I simulated and developed a precision liquid handling robot that was programmed using a PID controller for accurate liquid dispensing. The robot was integrated with the computer vision system, enabling it to locate and deliver the liquid to targeted areas on the Petri dish. This demonstrated how vision-based analysis could be seamlessly combined with robotic automation, allowing for precise interventions in plant phenotyping experiments.
    </p>

    <p>
      Additionally, I incorporated reinforcement learning to enhance the robot’s navigation and precision. By designing appropriate reward functions and conducting hyperparameter tuning, I ensured that the robot could autonomously navigate to the correct root tips for liquid delivery. The integration of reinforcement learning further improved the system's efficiency, as the robot learned to optimize its path and actions based on real-time feedback.
    </p>

    <h4>Key Findings:</h4>
    <ul>
      <li>The computer vision model was able to achieve high accuracy in isolating plant structures, particularly roots, enabling more efficient plant trait analysis.</li>
      <li>The liquid handling robot demonstrated precise inoculation capabilities when integrated with vision-based localization, enhancing automation in plant phenotyping.</li>
      <li>Reinforcement learning significantly improved the robot’s precision in liquid delivery, ensuring accurate targeting of plant root tips.</li>
      <li>The combination of machine learning, computer vision, and robotics proved to be an effective approach for automated plant phenotyping.</li>
    </ul>

    <p>
      The project culminated in a comprehensive technical report, which documented the methodologies used for dataset acquisition and preprocessing, and detailed the computer vision and robotics pipelines. The report included a flowchart that depicted the overall workflow and performance metrics that evaluated the accuracy of root segmentation, robot precision, and the effectiveness of reinforcement learning in task execution.
    </p>

    <h4>Skills Gained:</h4>
    <ul>
      <li><strong>Robotics</strong>: Developed and simulated a robot with a PID controller for precise inoculation tasks.</li>
      <li><strong>Computer Vision</strong>: Applied segmentation techniques to isolate plant structures, enabling accurate plant root phenotyping.</li>
      <li><strong>Reinforcement Learning</strong>: Crafted reward functions and optimized RL models for autonomous robot navigation and liquid delivery.</li>
      <li><strong>Machine Learning</strong>: Built predictive models for plant segmentation and collaborated on enhancing robotics through ML integration.</li>
    </ul>

    <p>
      The outcomes of this project demonstrated the successful synergy between computer vision and robotics, advancing automated plant phenotyping. The technical report and findings offered a valuable contribution to NPEC's goal of improving plant analysis through AI technologies.
    </p>
  </div>
</div>