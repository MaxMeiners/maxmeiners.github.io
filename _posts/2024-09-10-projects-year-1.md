---
layout: page
title: Projects Year 1
subtitle: A collection of projects from my first year
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

<h2>Year 1 Projects</h2>

<div class="accordion">
  <input type="checkbox" id="project1" />
  <label for="project1">Project 1: SDG Indicators Data Analysis and Visualization</label>
  <div class="content">
    <h3>Project 1: <strong>SDG Indicators Data Analysis and Visualization</strong></h3>
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
  <input type="checkbox" id="project2" />
  <label for="project2">Project 2: Coming Soon</label>
  <div class="content">
    <p>More projects will be added soon...</p>
  </div>
</div>

<div class="accordion">
  <input type="checkbox" id="project3" />
  <label for="project3">Project 3: Coming Soon</label>
  <div class="content">
    <p>More projects will be added soon...</p>
  </div>
</div>

<div class="accordion">
  <input type="checkbox" id="project4" />
  <label for="project4">Project 4: Coming Soon</label>
  <div class="content">
    <p>More projects will be added soon...</p>
  </div>
</div>