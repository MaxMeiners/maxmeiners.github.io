---
layout: page
title: Deep Learning Projects
subtitle: A collection of my deep learning projects
cover-img: /assets/img/ai_cover_photo.jpg
# thumbnail-img: /assets/img/Cropped_Image.png
share-img: /assets/img/ai_cover_photo.jpg
gh-repo: maxmeiners
gh-badge: [star, fork, follow]
tags: [deep learning, artificial intelligence, projects]
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

<h2>Deep Learning Projects</h2>

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
  <input type="checkbox" id="classification_banijay" />
  <label for="classification_banijay">Advanced Emotion Classification System for Banijay</label>
  <div class="content">
    <h3><strong>Advanced Emotion Classification System for Banijay</strong></h3>
    <p>For this group project, my team and I collaborated with <strong>Banijay</strong>, in association with Breda University of Applied Sciences, to develop an emotion classification system utilizing natural language processing (NLP) and machine learning models. The objective was to analyze video content, detecting and classifying emotions to enhance the content's emotional impact and insights.</p>
    
    <p>The data preprocessing involved cleaning text data using regular expressions, and normalizing it through tokenization and stemming techniques. Word embeddings were then used to represent words as vectors, enabling the integration of these vectors into machine learning models. Additional feature extraction methods like TF-IDF and Part-of-Speech (POS) tagging were applied. A custom word embedding model, trained on our project-specific corpus, was incorporated to enhance emotion classification accuracy.</p>

    <p>We experimented with multiple models for emotion classification. Initial models were developed using Naïve Bayes and Logistic Regression algorithms. Further sophistication was added with sequence models such as Recurrent Neural Networks (RNN), XGBoost, and Long Short-Term Memory (LSTM) networks, each contributing to an improved understanding of emotional cues in text.</p>

    <p>A robust pipeline was developed to break down video content into fragments, extract text from these fragments, and predict emotions for each segment. To ensure optimal performance, we tested transformer models using Hugging Face, selecting RoBERTA as the core model. RoBERTa was fine-tuned on the dataset and achieved high accuracy in emotion classification.</p>

    <p>Comprehensive model evaluation was performed using metrics such as accuracy, precision, recall, and F1-score. Through error analysis, we identified areas for improvement, balancing performance metrics to select the most effective model. The process and results were documented in a detailed technical report, showcasing the methodologies and findings.</p>

    <h4>Key Findings:</h4>
    <ul>
      <li>RoBERTa outperformed other models in emotion classification, achieving significant accuracy improvements after fine-tuning on the project-specific dataset.</li>
      <li>Data preprocessing and feature extraction were critical in improving model performance, with POS tagging and word embeddings contributing to enhanced emotion detection.</li>
      <li>The pipeline's automated process for splitting video and extracting text enabled efficient emotion classification across various video content.</li>
      <li>Combining traditional algorithms with advanced transformer models provided a deeper understanding and classification of emotions in media content.</li>
    </ul>

    <h4>Skills Gained:</h4>
    <ul>
      <li><strong>Transformer Models</strong> – Implemented and fine-tuned transformer models, specifically RoBERTa, for NLP tasks.</li>
      <li><strong>Performance Metrics Analysis</strong> – Evaluated models using accuracy, precision, recall, and F1-score.</li>
      <li><strong>Feature Engineering</strong> – Applied techniques such as tokenization, TF-IDF, and POS tagging for improved model performance.</li>
      <li><strong>Natural Language Processing (NLP)</strong> – Developed emotion classification models using advanced NLP techniques.</li>
      <li><strong>Model Evaluation</strong> – Conducted comprehensive model performance assessments and error analyses.</li>
    </ul>

    <p>The project provided Banijay with a robust tool for analyzing emotional content in their video assets, offering actionable insights to enhance viewer engagement through AI-driven emotion classification.</p>

    <p>
      You can view the full code for the RoBERTa model in my Jupyter Notebook here: <a href="https://nbviewer.org/github/MaxMeiners/maxmeiners.github.io/blob/master/Year%202%20ADS%26AI%20repositories/Project%203/RoBERTa%20model/roberta_model_best_performing.ipynb" target="_blank">NBViewer link</a>.
    </p>
  </div>
</div>


<div class="accordion">
  <input type="checkbox" id="expeditie_robinson" />
  <label for="expeditie_robinson">Emotion Detection AI for "Expeditie Robinson"</label>
  <div class="content">
    <h3><strong>Emotion Detection AI for "Expeditie Robinson"</strong></h3>
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
</div>
