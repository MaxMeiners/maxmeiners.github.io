---
layout: page
title: Data Visualization Projects
subtitle: A collection of my data visualization projects
cover-img: /assets/img/ai_cover_photo.jpg
# thumbnail-img: /assets/img/Cropped_Image.png
share-img: /assets/img/ai_cover_photo.jpg
gh-repo: maxmeiners
gh-badge: [star, fork, follow]
tags: [data visualization, data science, projects]
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

<h2>Data Visualization Projects</h2>

<div class="accordion">
  <input type="checkbox" id="sdg" />
  <label for="sdg">SDG Indicators Data Analysis and Visualization</label>
  <div class="content">
    <h3><strong>SDG Indicators Data Analysis and Visualization</strong></h3>
    <p>For this project, I was given the freedom to choose any of the United Nations' Sustainable Development Goals (SDGs) to explore. I decided to focus on <strong>SDG 2: Zero Hunger</strong>, specifically looking at the relationship between GDP per capita (a measure of a country’s wealth) and undernourishment or malnutrition rates in African countries. The goal of my analysis was to see if a country’s wealth, as measured by GDP per capita, had a strong impact on reducing malnutrition across the continent.</p>

    <p>The <strong>Sustainable Development Goals (SDGs)</strong>, especially SDG 2, aim to end hunger and malnutrition around the world. While progress has been made, undernourishment is still a big problem in many parts of Africa. Factors like poverty, conflict, and environmental challenges, such as drought, contribute to ongoing food insecurity. By studying the connection between a country’s economy and its ability to fight hunger, this project aimed to find trends that could lead to better solutions for reducing malnutrition.</p>

    <h4>Research Question:</h4>
    <p><strong>What is the relationship between GDP per capita and undernourishment/malnutrition in Africa?</strong></p>

    <h4>Key Findings:</h4>
    <ul>
      <li>Nearly 10% of people worldwide are malnourished, with most of them living in Sub-Saharan Africa.</li>
      <li>The region’s malnutrition problem is worsened by economic struggles, conflict, and natural disasters like drought.</li>
      <li>By analyzing the data, I aimed to understand if wealthier countries are more successful in reducing hunger and how economic differences affect hunger rates.</li>
    </ul>

    <h4>Skills Gained:</h4>
    <ul>
      <li><strong>Data cleaning and preparation</strong> in Power BI to make sure the dataset was ready for analysis.</li>
      <li><strong>Exploratory Data Analysis (EDA)</strong> to spot key trends and connections between GDP per capita and undernourishment rates.</li>
      <li><strong>Data visualization</strong> using Power BI to create an interactive dashboard that clearly presents the insights and results of the analysis, allowing users to explore the link between GDP and hunger in different African countries.</li>
    </ul>

    <h4>Dashboard</h4>
    <p>Below is the interactive Power BI dashboard that was the final deliverable for this project.</p>
    <iframe title="SDGIndicatorsDashboard_MaxMeiners" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNWQyNDgwNTItMThiMC00MWVlLTgwMzYtNDAzMmU2ODJlODc2IiwidCI6IjBhMzM1ODliLTAwMzYtNGZlOC1hODI5LTNlZDA5MjZhZjg4NiIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>
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
