---
layout: page
title: Emotion Detection AI for "Expeditie Robinson"
subtitle: Analyzing and detecting emotions in a TV series
cover-img: /assets/img/deep_learning_cover.jpg
thumbnail-img: /assets/img/wildlife_recognition.png
share-img: /assets/img/deep_learning_cover.jpg
gh-repo: maxmeiners
gh-badge: [star, fork, follow]
tags: [computer vision, deep learning, classification, projects]
comments: true
author: Max Meiners
---

<div>
  <p>For this group project, my team and I continued the work from our previous project, building upon models and methodologies we had already developed. One example is the use of the RoBERTa model that I created in the previous block, which served as a foundation for developing a new AI-driven emotion detection model based on the popular reality TV series "Expeditie Robinson." Our goal was to create a machine learning solution capable of analyzing and detecting emotions in video footage from the show. Leveraging tools like Microsoft Azure Machine Learning and Docker, we designed and built an end-to-end MLOps pipeline that processed, trained, and deployed our models for real-time emotion inference.</p>
  
  <p>
    The project emphasized <strong>cloud-based deployment and visualization</strong> of the model's predictions. We developed an interactive web-based platform using Streamlit, called the "Emotion Detection Platform." This platform enables users to train models by providing text input data and selecting hyperparameters. Once trained, the model can analyze both audio and video files, delivering predictions at the sentence level. The platform aims to provide valuable insights into viewer engagement and preferences for TV series, allowing stakeholders to make informed data-driven decisions.
  </p>

  <h4>Key Findings:</h4>
  <ul>
    <li>Video data from "Expeditie Robinson" provided a rich source of emotional expressions, which the model successfully identified and classified.</li>
    <li>Our analysis highlighted patterns in contestant emotions, offering insights into mood shifts and emotional dynamics throughout the series.</li>
    <li>The Streamlit application enabled seamless interaction with the model, enhancing stakeholders' ability to visualize emotional trends and validate model accuracy.</li>
  </ul>

  <h4>Skills Gained:</h4>
  <ul>
    <li><strong>Machine Learning</strong> for emotion recognition, utilizing Azure ML for model training and cloud deployment.</li>
    <li><strong>Data Processing</strong> through video analysis and feature extraction to support accurate emotion detection.</li>
    <li><strong>Application Development</strong> using Streamlit to create a user-friendly interface for model training and visualization.</li>
    <li><strong>MLOps & Containerization</strong>: Employed Docker to ensure consistent and reproducible environments for development and deployment.</li>
  </ul>

  <h4>Screenshots:</h4>
  <div>
    <img src="/assets/img/emotion_detection_homepage.png" alt="Emotion Detection Platform Home" style="width:100%; max-width:600px;">
    <p><em>Figure 1: The homepage of the Emotion Detection Platform, explaining what the goal of the platform is.</em></p>
  </div>
  <div>
    <img src="/assets/img/model_training_page.png" alt="Model Training Interface" style="width:100%; max-width:600px;">
    <p><em>Figure 2: The model training interface, allowing users to input data and select hyperparameters for model training.</em></p>
  </div>
</div>
