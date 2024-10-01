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
    <a href="[Interactive PowerPoint Presentation](https://edubuas-my.sharepoint.com/:p:/g/personal/214936_buas_nl/EfDtobFMb3FJgJW2LjLcmWEBUXR3-ITpDCHQWaUocMHQxA?e=4zoQwj)" target="_blank">View the PowerPoint Presentation</a>
  </div>
</div>


<div class="accordion">
  <input type="checkbox" id="projectNPEC" />
  <label for="projectNPEC">Project: AI-Driven Plant Analysis for NPEC</label>
  <div class="content">
    <h3>Project: <strong>AI-Driven Plant Analysis for the Netherlands Plant Eco-phenotyping Center (NPEC)</strong></h3>
    <p>
      From November 2023 to February 2024, I worked on a project in collaboration with the <strong>Netherlands Plant Eco-phenotyping Center (NPEC)</strong>, through my association with Breda University of Applied Sciences. The project's primary objective was to revolutionize plant phenotyping by integrating computer vision and robotics to enhance plant root analysis and improve automation in precision inoculation.
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
      <li><strong>Robotics</strong>: Developed and simulated a liquid handling robot with a PID controller for precise inoculation tasks.</li>
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
  <label for="project3">Project 3: CNN-Based Animal Species Classification</label>
  <div class="content">
    <h3>Project 3: <strong>CNN-Based Animal Species Classification</strong></h3>
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
  <input type="checkbox" id="project4" />
  <label for="project4">Project 4: CRISP-DM Cycle and Streamlit Application for the Municipality of Breda</label>
  <div class="content">
    <h3>Project 4: <strong>CRISP-DM Cycle and Streamlit Application for the Municipality of Breda</strong></h3>
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
