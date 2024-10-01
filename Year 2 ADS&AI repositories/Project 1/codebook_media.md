# Codebook on survey for AI implementation in media academy

## Project description
The main goal of this project is to deliver a policy paper for the media academy of Breda University of Applied Sciences (BUas). We are looking into ways to incorporate AI tools and solutions into the curriculum as they are now more accessible to everyone. However, we need to understand what we are working with first. If everyone knows a lot already, we can start from a different point compared with no knowledge whatsoever. Similarly, we want to measure the attitudes or even the need for the implementation of AI tools. Therefore the survey described below was created.

## Data collection
The data collection process is divided into two parts. Quantitative data is collected through the survey distributed to BUas lecturers and students. In total, 586 people participated in the survey including 413 students and 173 educators or staff members. On top of that, qualitative data was collected via interviews with lecturers and focus groups with students.

## Data cleaning
An R script was written to extract only data relevant for the analysis. The process consisted of discarding rows with participants who did not give consent, choosing only rows with media domain selected, and selecting only columns with demographics, general questions, and questions designed for media participants.

## Variables

### media_experience

- **Full question:** How much work / study experience with AI or AI tools do you have?
 The amount of knowledge/experience with AI/AI tools in years.
- **How the Variable Was Measured:** Year ranges
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- less than 1 year
- 1 - 2 years
- 3 - 4 years
- more than 5 years
- **Unit of Measurement:** years

### media_subdomain

- **Full question:** What sub-domain are you most interested / knowledgeable in?
- **How the Variable Was Measured:** Different categories to select (single answer)
- **Data type:** Categorical
- **Unique Values of the Variable:**
- Content
- Production
- Marketing
- Interactive
- **Unit of Measurement:** None

### media_knowledge_1

- **Full question:** There are many beneficial applications of artificial intelligence.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_knowledge_2

- **Full question:** I am impressed by what artificial intelligence can do.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_knowledge_3

- **Full question:** In comparison to my colleagues in my domain, I have more knowledge on the topic.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_knowledge_4

- **Full question:** I am aware of a wide variety of AI applications.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_knowledge_5

- **Full question:** I have a good knowledge of AI.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_knowledge_6

- **Full question:** I have experience working with ChatGPT/ BingAI.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_knowledge_7

- **Full question:** I have experience working with AI tools other than ChatGPT/ BingAI.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_trust

- **Name of Variable:** media_trust_1
- **Full question:** Artificial intelligence can a have positive impact on people's wellbeing
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_trust_2

- **Full question:** Artificial intelligence can provide new economic opportunities for this country
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_trust_3

- **Full question:** Artificially intelligent systems can perform better than humans
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_trust_4

- **Full question:** For routine transactions, I would rather interact with an artificial intelligence
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_trust_5

- **Full question:** Artificial intelligence makes me feel great about human ingenuity
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_trust_6

- **Full question:** Artificially intelligent systems can help people feel happier
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_trust_7

- **Full question:** Some complex decisions are best left to artificial intelligence
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_trust_8

- **Full question:** I would entrust my life savings to an artificially intelligent investment system
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### will_to_learn_1

- **Full question:** I am interested in using artificial intelligence in my daily life
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### will_to_learn_2

- **Full question:** Artificial intelligence is exciting
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### will_to_learn_3

- **Full question:** I love everything about artificial intelligence
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### will_to_learn_4

- **Full question:** I am satisfied with how my domain is equipped for the application of AI
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### will_to_learn_5

- **Full question:** I am willing to learn about AI
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### will_to_learn_6

- **Full question:** I would like schools to offer AI related training
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_domain_1

- **Full question:** An artificially intelligent agent would be better than an employee in many routine jobs.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_domain_2

- **Full question:** I would like to use artificial intelligence in my own job.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_domain_3

- **Full question:** I often use AI in my daily work.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_domain_4

- **Full question:** There are many AI application possibilities in your domain.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_domain_5

- **Full question:** AI has a noticeable impact on my profession.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_domain_6

- **Full question:** AI will create new jobs in my field.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_domain_7

- **Full question:** The introduction of AI will lead to improvement in my profession.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_domain_8

- **Full question:** AI will boost the domain
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_domain_9

- **Full question:** AI will be used more widely in the domain
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_development_1

- **Full question:** Much of society will benefit from a future full of artificial intelligence
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_development_2

- **Full question:** I am willing to use AI if needed
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_development_3

- **Full question:** Employees who use AI will replace those who don't
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_development_4

- **Full question:** The development in AI makes me more willing to engage in the domain
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_development_5

- **Full question:** The development of AI makes the domain less attractive to me
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_sp_1

- **Full question:** I understand the ethical implications of using AI in media, especially in terms of deepfakes and misinformation.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_sp_2

- **Full question:** AI can enhance creative processes in media by offering suggestions or automating mundane tasks.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_sp_3

- **Full question:** AI can lead to innovative storytelling techniques in the media industry.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_sp_4

- **Full question:** AI can offer deeper insights into audience preferences, leading to more tailored and engaging media content.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_sp_5

- **Full question:** Traditional grading methods may not be suitable when AI tools are used in assignments.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_sp_6

- **Full question:** I treat AI as a tool more than a decision maker
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_sp_7

- **Full question:** AI is more of a buzzword than a tangible tool in the media curriculum right now.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_sp_8

- **Full question:** Assignments should focus more on human creativity and critical thinking rather than just AI-generated content.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_sp_9

- **Full question:** Guest lectures from AI industry experts would be beneficial for students.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None

### media_sp_10

- **Full question:** The distinction between a story and a well-crafted story is essential when using AI in content creation.
- **How the Variable Was Measured:** 5-point Likert scale
- **Data type:** Ordinal
- **Unique Values of the Variable:**
- Strongly disagree
- Somewhat disagree
- Neither agree or disagree
- Somewhat agree
- Strongly agree
- **Unit of Measurement:** None