---
layout: page
title: Projects Year 2
subtitle: A collection of projects from my second year
cover-img: /assets/img/path.jpg
# thumbnail-img: /assets/img/Cropped_Image.png
share-img: /assets/img/path.jpg
gh-repo: maxmeiners
gh-badge: [star, fork, follow]
tags: [introduction, cv]
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

<h2>Year 2 Projects</h2>

<div class="accordion">
  <input type="checkbox" id="project1" />
  <label for="project1">Project 1: AI in Media Studies at BUAS</label>
  <div class="content">
    <h3>Project 1: <strong>AI in Media Studies at BUAS</strong></h3>
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
  <input type="checkbox" id="project2" />
  <label for="project2">Project 2: AI-Driven Plant Analysis for NPEC</label>
  <div class="content">
    <h3>Project 2: <strong>AI-Driven Plant Analysis for the Netherlands Plant Eco-phenotyping Center (NPEC)</strong></h3>
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


<div class="accordion">
  <input type="checkbox" id="project3" />
  <label for="project3">Project 3: Advanced Emotion Classification System for Banijay</label>
  <div class="content">
    <h3>Project 3: <strong>Advanced Emotion Classification System for Banijay</strong></h3>
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
  <input type="checkbox" id="project4" />
  <label for="project4">Project 4: Emotion Detection AI for "Expeditie Robinson"</label>
  <div class="content">
    <h3>Project 4: <strong>Emotion Detection AI for "Expeditie Robinson"</strong></h3>
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
