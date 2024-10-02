---
layout: page
title: Robotics Projects
subtitle: A collection of my robotics projects
cover-img: /assets/img/ai_cover_photo.jpg
# thumbnail-img: /assets/img/Cropped_Image.png
share-img: /assets/img/ai_cover_photo.jpg
gh-repo: maxmeiners
gh-badge: [star, fork, follow]
tags: [robotics, computer vision, machine learning, artificial intelligence, projects]
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

<h2>Robotics Projects</h2>

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