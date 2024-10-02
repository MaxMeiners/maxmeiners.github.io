---
layout: page
title: Machine Learning Projects
subtitle: A collection of my machine learning projects
cover-img: /assets/img/ai_cover_photo.jpg
# thumbnail-img: /assets/img/Cropped_Image.png
share-img: /assets/img/ai_cover_photo.jpg
gh-repo: maxmeiners
gh-badge: [star, fork, follow]
tags: [machine learning, data science, deep learning, artificial intelligence, projects]
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

  .accordion label {
    background-color: #eee;
    color: #444;
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

  .accordion label:hover {
    background-color: #ccc;
  }

  .accordion label:after {
    content: '+';
    float: right;
  }

  .accordion input:checked + label:after {
    content: '-';
  }

  .accordion .content {
    height: 0;
    overflow: hidden;
    transition: height 0.4s ease;
    background-color: #f9f9f9;
  }

  .accordion input:checked + label + .content {
    height: auto;
    padding: 18px;
    border-top: 1px solid #ddd;
  }
</style>

<h2>Machine Learning Projects</h2>

<div class="accordion">
  <input type="checkbox" id="ml_banijay" />
  <label for="ml_banijay">Machine Learning for TV Show Ratings Prediction for Banijay</label>
  <div class="content">
    <h3><strong>Machine Learning for TV Show Ratings Prediction for Banijay</strong></h3>
    <p>For this project, we were approached by <strong>Banijay</strong>, a leading content creation company, to analyze their television viewership data. Banijay provided us with detailed datasets related to their TV shows, including air dates, hosts, viewership ratings, and social media engagement data. My task was to develop a machine learning model that could predict TV show ratings based on this data, with the goal of helping Banijay enhance their data usage and ultimately increase their ratings.
    </p>
    <p>
      After receiving the data from Banijay, I conducted an extensive Exploratory Data Analysis (EDA) using Python, which allowed me to identify key trends and relationships in the data. I then proceeded to develop machine learning models, including Linear Regression and Decision Tree models, to predict viewership ratings based on the features extracted from the data. The final outcome of my analysis was delivered back to Banijay, along with actionable insights to help them optimize their content and ratings.
    </p>

    <h4>Key Findings:</h4>
    <ul>
      <li>Social media engagement, particularly metrics like retweets and likes on Twitter, had a significant correlation with the ratings of the show.</li>
      <li>The analysis revealed that certain hosts were consistently more popular, which positively influenced the show's ratings.</li>
      <li>Linear Regression performed better than the Decision Tree model in predicting the ratings, with an R-squared value of 0.93 compared to 0.89 for the Decision Tree model.</li>
    </ul>

    <h4>Skills Gained:</h4>
    <ul>
      <li><strong>Data cleaning and preparation</strong> by merging multiple datasets and handling missing values to ensure the data was ready for analysis.</li>
      <li><strong>Exploratory Data Analysis (EDA)</strong> using Python to identify key trends in viewership and social media metrics.</li>
      <li><strong>Machine Learning model development</strong> by implementing Linear Regression and Decision Tree models to predict TV ratings.</li>
      <li><strong>Ethical considerations</strong> in data handling, ensuring all data used complied with GDPR standards, and reflecting on the broader implications of using social media data for predictive analysis.</li>
    </ul>

    <p>
      The final model and insights were delivered back to <strong>Banijay</strong>, providing them with actionable recommendations on how to leverage social media data and optimize their host selection to improve TV show ratings.
    </p>
  </div>
</div>


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
  <input type="checkbox" id="municipality" />
  <label for="municipality">CRISP-DM Cycle and Streamlit Application for the Municipality of Breda</label>
  <div class="content">
    <h3><strong>CRISP-DM Cycle and Streamlit Application for the Municipality of Breda</strong></h3>
    <p>For this project, my team and I worked on a project for the municipality of Breda. The goal was to apply the full CRISP-DM (Cross-Industry Standard Process for Data Mining) cycle in a real-world setting. After completing individual tasks such as legal reviews and Exploratory Data Analysis (EDA) using Python and SQL, we presented project proposals based on our findings. Our team selected the best idea and started collaborating to build a data science product for deployment.
    </p>
    <p>
      The primary focus of this block was on the <strong>Deployment</strong> phase of the CRISP-DM lifecycle, where we had the opportunity to turn our project idea into a tangible solution for the municipality. We explored different ways to tackle their data-related problems and developed a web-based application using Streamlit, which allowed us to visualize and interact with the data in real time. This project combined technical and project management skills, requiring us to handle everything from client communication to final deployment.
    </p>

    <h4>Key Findings:</h4>
    <ul>
      <li>The municipality of Breda had multiple data sources but lacked a unified way to extract meaningful insights.</li>
      <li>Our analysis revealed key patterns in the data, such as correlations between certain municipal issues and geographic areas.</li>
      <li>We proposed and implemented a real-time data visualization tool using Streamlit, which helped the municipality identify and address these issues more efficiently.</li>
    </ul>

    <h4>Skills Gained:</h4>
    <ul>
      <li><strong>Data cleaning and preparation</strong> using Python and SQL to ensure the dataset was ready for analysis.</li>
      <li><strong>Exploratory Data Analysis (EDA)</strong> to uncover key trends and correlations in the municipal data.</li>
      <li><strong>Application development and deployment</strong> using Streamlit to build a real-time data visualization tool for the client.</li>
      <li><strong>Project management</strong> and communication skills in a team setting, ensuring collaboration and meeting client expectations.</li>
    </ul>

    <p>
      You can view the Streamlit page we created for this project here: <a href="https://bredauniversityadsai-2022-23d-1fc-deliverables1-homepage-0ylp0q.streamlit.app" target="_blank">Streamlit Application Link</a>.
    </p>
  </div>
</div>


<div class="accordion">
  <input type="checkbox" id="ai_in_media" />
  <label for="ai_in_media">AI in Media Studies at BUAS</label>
  <div class="content">
    <h3><strong>AI in Media Studies at BUAS</strong></h3>
    <p>As part of a five-person team at Breda University of Applied Sciences (BUAS), we explored the impact of Artificial Intelligence (AI) on students, staff, and the organization. Our mixed-method study combined surveys and interviews to investigate attitudes towards AI within media studies. The project concluded with a research paper, policy recommendations, and an interactive PowerPoint presentation presented at a conference, providing actionable insights and strategic direction.</p>

    <h4>Data Collection & Analysis:</h4>
    <p>I played a significant role in the data collection phase by creating a comprehensive survey using Qualtrics. Additionally, my team and I conducted in-depth interviews with lecturers and students, gathering both quantitative and qualitative data. The survey data was preprocessed using R scripting, which allowed me to perform a detailed analysis and uncover valuable trends and patterns.</p>

    <h4>Visualization & Presentation:</h4>
    <p>Utilizing R scripting, my team and I developed visualizations, such as dynamic charts and interactive graphs, to effectively communicate our findings. We culminated our efforts by developing a PowerPoint presentation, which was showcased at the Conference, highlighting our research results and actionable recommendations.</p>

    <h4>Stakeholder Collaboration:</h4>
    <p>Our team maintained active engagement with Media stakeholders to ensure our study aligned with industry needs. Regular meetings facilitated our progress, fostering meaningful outcomes and targeted recommendations for the BUAS community.</p>

    <h4>Impact & Personal Growth:</h4>
    <p>The project provided valuable insights to BUAS for enhancing Media studies and helped me grow as an analytics translator. I developed my expertise in data analysis, stakeholder engagement, and strategic problem-solving. Additionally, it deepened my understanding of research methodologies, data collection, and analysis using R.</p>

    <h4>Skills Gained:</h4>
    <ul>
      <li><strong>Qualitative Research</strong> – Conducting interviews to gather detailed perspectives.</li>
      <li><strong>Data Visualization</strong> – Using R to create impactful visualizations for presentations.</li>
      <li><strong>Data Analysis</strong> – Preprocessing and analyzing survey data in R.</li>
      <li><strong>Quantitative Research</strong> – Designing surveys to collect data on AI perceptions.</li>
      <li><strong>Teamwork</strong> – Collaborating within a multi-disciplinary team to achieve project goals.</li>
      <li><strong>Stakeholder Engagement</strong> – Regularly communicating with Media stakeholders to align project outcomes.</li>
    </ul>

    <h4>PowerPoint Presentation</h4>
    <p>Below is the link to the interactive PowerPoint presentation that was the final deliverable for this project:</p>
    <a href="https://edubuas-my.sharepoint.com/:p:/g/personal/214936_buas_nl/EfDtobFMb3FJgJW2LjLcmWEBUXR3-ITpDCHQWaUocMHQxA?e=4zoQwj" target="_blank">View the Interactive PowerPoint Presentation</a>
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
