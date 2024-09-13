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
  .dropdown-container {
    display: none;
    padding-left: 20px;
  }
  .dropdown-btn {
    background-color: #f1f1f1;
    color: #333;
    padding: 10px;
    font-size: 18px;
    border: none;
    text-align: left;
    cursor: pointer;
    width: 100%;
    border-bottom: 1px solid #ddd;
  }
  .dropdown-btn:hover {
    background-color: #ddd;
  }
  .dropdown-btn:after {
    content: '\25BC';
    float: right;
  }
  .dropdown-btn.active:after {
    content: '\25B2';
  }
</style>

<h2>Year 1 Projects</h2>

<button class="dropdown-btn">Project 1: SDG Indicators Data Analysis and Visualization</button>
<div class="dropdown-container">
  ### Project 1: **SDG Indicators Data Analysis and Visualization**

  For this project, I was given the freedom to choose any of the United Nations' Sustainable Development Goals (SDGs) to explore. I decided to focus on **SDG 2: Zero Hunger**, specifically looking at the relationship between GDP per capita (a measure of a country’s wealth) and undernourishment or malnutrition rates in African countries. The goal of my analysis was to see if a country’s wealth, as measured by GDP per capita, had a strong impact on reducing malnutrition across the continent.

  **Research Question:**
  - **What is the correlation between GDP per capita and undernourishment/malnutrition in the continent of Africa?**

  **Key Findings:**
  - Nearly 10% of people worldwide are malnourished, with most of them living in Sub-Saharan Africa.
  - The region’s malnutrition problem is worsened by economic struggles, conflict, and natural disasters like drought.
  - By analyzing the data, I aimed to understand if wealthier countries are more successful in reducing hunger and how economic differences affect hunger rates.

  **Skills Gained:**
  - **Data cleaning and preparation** in Power BI to make sure the dataset was ready for analysis.
  - **Exploratory Data Analysis (EDA)** to spot key trends and connections between GDP per capita and undernourishment rates.
  - **Data visualization** using Power BI to create an interactive dashboard that clearly presents the insights and results of the analysis, allowing users to explore the link between GDP and hunger in different African countries.

  ### Dashboard
  Below is the interactive Power BI dashboard that was the final deliverable for this project.

  <iframe title="SDGIndicatorsDashboard_MaxMeiners" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNWQyNDgwNTItMThiMC00MWVlLTgwMzYtNDAzMmU2ODJlODc2IiwidCI6IjBhMzM1ODliLTAwMzYtNGZlOC1hODI5LTNlZDA5MjZhZjg4NiIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>
</div>

<button class="dropdown-btn">Project 2: Coming Soon</button>
<div class="dropdown-container">
  More projects will be added soon...
</div>

<button class="dropdown-btn">Project 3: Coming Soon</button>
<div class="dropdown-container">
  More projects will be added soon...
</div>

<button class="dropdown-btn">Project 4: Coming Soon</button>
<div class="dropdown-container">
  More projects will be added soon...
</div>

<script>
  var dropdown = document.getElementsByClassName("dropdown-btn");
  var i;

  for (i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var dropdownContent = this.nextElementSibling;
      if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
      } else {
        dropdownContent.style.display = "block";
      }
    });
  }
</script>