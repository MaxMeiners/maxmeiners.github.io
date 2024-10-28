---
layout: page
title: Advanced Emotion Classification System for Banijay
subtitle: Developing an AI-driven emotion classification system using NLP and machine learning
cover-img: /assets/img/ai_cover.jpg
thumbnail-img: /assets/img/banijay_thumbnail.png
share-img: /assets/img/ai_cover.jpg
gh-repo: maxmeiners
gh-badge: [star, fork, follow]
tags: [NLP, machine learning, emotion classification, projects]
comments: true
author: Max Meiners
---

<div>
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
