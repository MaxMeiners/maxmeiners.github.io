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
    background-color: #eee;
    color: #444;
    cursor: pointer;
    padding: 18px;
    width: 100%;
    border: none;
    text-align: left;
    outline: none;
    font-size: 18px;
    transition: 0.4s;
    margin-bottom: 5px;
  }

  .accordion.active, .accordion:hover {
    background-color: #ccc;
  }

  .accordion:after {
    content: '\002B'; /* Plus sign */
    color: #777;
    font-weight: bold;
    float: right;
  }

  .accordion.active:after {
    content: "\2212"; /* Minus sign */
  }

  .panel {
    padding: 0 18px;
    display: none;
    background-color: white;
    overflow: hidden;
    transition: max-height 0.2s ease-out;
  }

  .panel.show {
    display: block;
  }
</style>

<h2>Year 1 Projects</h2>

<button class="accordion">Project 1: SDG Indicators Data Analysis and Visualization</button>
<div class="panel">
  <h3>Project 1: <strong>SDG Indicators Data Analysis and Visualization</strong></h3>
  <p>For this project, I was given the freedom to choose any of the United Nations' Sustainable Development Goals (SDGs) to explore. I decided to focus on <strong>SDG 2: Zero Hunger</strong>, specifically looking at the relationship between GDP per capita and undernourishment or malnutrition rates in African countries. The goal of my analysis was to see if a country’s wealth had a strong impact on reducing malnutrition across the continent.</p>

  <p><strong>Key Findings:</strong></p>
  <ul>
    <li>Nearly 10% of people worldwide are malnourished, with most of them living in Sub-Saharan Africa.</li>
    <li>Economic struggles, conflict, and natural disasters like drought worsen the malnutrition problem in this region.</li>
    <li>The analysis explores whether wealthier countries are more successful in reducing hunger.</li>
  </ul>

  <h4>Dashboard</h4>
  <p>Below is the interactive Power BI dashboard that was the final deliverable for this project.</p>
  <iframe title="SDGIndicatorsDashboard_MaxMeiners" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNWQyNDgwNTItMThiMC00MWVlLTgwMzYtNDAzMmU2ODJlODc2IiwidCI6IjBhMzM1ODliLTAwMzYtNGZlOC1hODI5LTNlZDA5MjZhZjg4NiIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>
</div>

<button class="accordion">Project 2: Coming Soon</button>
<div class="panel">
  <p>More projects will be added soon...</p>
</div>

<button class="accordion">Project 3: Coming Soon</button>
<div class="panel">
  <p>More projects will be added soon...</p>
</div>

<button class="accordion">Project 4: Coming Soon</button>
<div class="panel">
  <p>More projects will be added soon...</p>
</div>

<script>
  var acc = document.getElementsByClassName("accordion");
  var i;

  for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var panel = this.nextElementSibling;
      if (panel.style.display === "block") {
        panel.style.display = "none";
      } else {
        panel.style.display = "block";
      }
    });
  }
</script>