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

  .accordion input:checked + label + .content {
    max-height: 1000px; /* Adjust depending on the content height */
    padding: 18px;
    border-top: 1px solid #ddd;
  }

  .accordion .content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease;
    background-color: #f9f9f9;
  }
</style>

<h2>Year 1 Projects</h2>

<div class="accordion">
  <input type="checkbox" id="project1" />
  <label for="project1">Project 1: SDG Indicators Data Analysis and Visualization</label>
  <div class="content">
    <h3>Project 1: <strong>SDG Indicators Data Analysis and Visualization</strong></h3>
    <p>For this project, I was given the freedom to choose any of the United Nations' Sustainable Development Goals (SDGs) to explore. I decided to focus on <strong>SDG 2: Zero Hunger</strong>, specifically looking at the relationship between GDP per capita and undernourishment or malnutrition rates in African countries.</p>

    <p><strong>Key Findings:</strong></p>
    <ul>
      <li>Nearly 10% of people worldwide are malnourished, with most of them living in Sub-Saharan Africa.</li>
      <li>The region’s malnutrition problem is worsened by economic struggles, conflict, and natural disasters like drought.</li>
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