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

### Project 1: **SDG Indicators Data Analysis and Visualization**

This project focused on analyzing a dataset containing global Sustainable Development Goals (SDG) indicators, which are designed to track the progress of various countries towards meeting the United Nations' SDG targets. Our primary goal was to derive insights from this dataset and present them visually using a Power BI dashboard. 

The dataset included various metrics, such as poverty rates, environmental sustainability, health, and education indicators. By processing and visualizing these data points, we aimed to highlight key trends and compare progress between countries over time. 

**Project Scope:**
- **Data Source**: SDG indicators dataset (provided by the instructor) containing multi-year data for different countries across a range of SDG targets.
- **Objective**: Analyze the dataset to extract insights related to the progress of countries towards their SDG goals, and visualize the data to make it accessible and comprehensible for stakeholders.

**Steps Taken**:
1. **Data Cleaning and Preprocessing**:  
   The raw dataset contained missing values and inconsistencies, which required cleaning and preprocessing. I used Python libraries such as Pandas and NumPy to handle missing values, normalize country names, and ensure uniformity across all indicators.

2. **Exploratory Data Analysis (EDA)**:  
   After preprocessing, I performed exploratory data analysis to identify patterns, correlations, and trends. Key questions included:
   - Which countries are on track to meet their SDG goals?
   - How do SDG progress trends vary between developed and developing nations?
   - Are there specific regions lagging behind in certain goals (e.g., education or poverty eradication)?

3. **Visualization**:  
   Using Power BI, I created interactive visualizations that allowed users to explore different SDG indicators across countries and over time. The dashboard provides an overview of global SDG progress and detailed comparisons between countries on specific indicators, such as health, education, and environmental sustainability.

**Skills Achieved**:
- **Data cleaning and preprocessing** with Python (Pandas, NumPy).
- **Exploratory Data Analysis (EDA)** to identify key trends and insights from the SDG dataset.
- **Data visualization** using Power BI to build a dashboard that effectively communicates the results of our analysis.

### Dashboard

Below is the interactive Power BI dashboard that was the final deliverable for this project. The dashboard allows users to explore SDG indicators by country, year, and specific targets, offering insights into the progress made towards the global sustainability goals.

<iframe title="SDGIndicatorsDashboard_MaxMeiners" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNWQyNDgwNTItMThiMC00MWVlLTgwMzYtNDAzMmU2ODJlODc2IiwidCI6IjBhMzM1ODliLTAwMzYtNGZlOC1hODI5LTNlZDA5MjZhZjg4NiIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>