# **Exercises ADS&AI Block A**

---

> Philosophy AI & GitHub (1)
## 2) Foundations of AI
### 2.1 What is Artificial Intelligence?
#### b. How would you define Artificial Intelligence?
- A system that makes our everyday lives a lot easier

#### c. Give three examples of AI applications. You can choose real-life examples, but also examples from popular culture (e.g., movies, books, video games etc.).
- A self-driving car
- Smart assistants
- Robots in manufacturing businesses

### 2.2 Philosophy of Artificial Intelligence
#### b. Define the following terms: ‘weak AI', and ‘strong AI'.
- Strong AI has a complex algorithm that helps it act in different situations, while weak AI are pre-programmed by a human.

#### d. What is the ‘Chinese room experiment'? Describe its procedure.
- It holds that a digital computer executing a program can’t have a mind or consciousness, regardless of how intelligently or human-like the program may make the computer behave.

#### e. What is the ‘Chinese room experiment' supposed to show? Select the correct statement, and elaborate on your choice:

- a) Computers are not yet able to simulate the human ability to understand 
- b) Understanding involves more than the ability to formally reproduce appropriate outputs 
- c) It is only possible for systems to demonstrate understanding 
- d) No machine can demonstrate genuine understanding
- **D, because, according to the Chinese room experiment, it is impossible for a computer to have a mind of it’s own. Or to understand, like us people do.**

#### f. Connect the Post It notes (Fig 2.) to the relevant quadrant in the philosophy matrix (Fig 3.). For example, A = 1, 2, and B = 3, 4, 5 etc. Elaborate on your choices.
- A=2
- B=3, 4, 8
- C=1, 5, 9
- D=6, 7

---
---

> History of AI & GitHub (2)
## (1) History of Artificial Intelligence
### 1.1 Timeline
#### c. Find, and describe one ‘milestone' in the history of AI. Be creative, so no ‘milestones' by Alan Turing! No worries, we are going to extensively discuss his accomplishments in DataLab 1, Week 2.
- The first autonomous robots. In 1948 William Grey Walter created Elmer and Elsie. These two robots were the first to work autonomously - independent of a human. They could navigate their way around obstacles using light and touch.

### 1.2 Alan Turing
#### a. Besides the Turing Test, Alan Turing is renowned for his work on:
1. Cracking the Enigma, a mechanical device used by the German army to encode secure messages.
2. He was prosecuted for being gay.
3. He rode his bike 62 miles to get to the first day of school.

#### d. Describe the procedure, and main objective of Turing's ‘Imitation Game'. Write your answer down.
- e. There’s a human interrogator and 2 entities.  One of the entities is a machine, and the other one a human. The human interrogator communicates with the other 2 entities on the other side of the wall by passing notes. After some time, the interrogator is tasked to find out which one of the 2 entities is a human, and which one is the machine.

---
---

> Intelligent Agents & Conversational AI
## 1) Intelligent Agents
### 1.1 What is an intelligent agent?
#### c. Two intelligent agents are playing chess with a clock. One of them is Deep Blue, while the other is Gary Kasparov. Roughly specify the task environment for Deep Blue (this means you will have to specifying each letter in PEAS), and determine each of the following properties of this task environment:

Specifying the task environment:

- Performance measure: Winning the game, minimize time loss
- Environment: A chess board, chess pieces
- Actuators: Jointed arm and hand, a screen which shows what to do.
- Sensors: Camera, sensors in the chess pieces, sensors in the chess board.
---
- Properties of the task environment:
- a) Fully observable or b) partially observable
- a) Deterministic or b) stochastic
- a) Episodic or b) sequential
- a) Static, b) dynamic or c) semi-dynamic
- a) Discrete or b) continuous
- a) Single agent or b) multi-agent

Explain your answer.
- Fully observable, because the agent's sensors give it access to the complete state of the environment at each point in time.
- Deterministic, because the environment is completely observable by the agent.
- Sequential, because a move an agent makes can affect all other decisions the other agents makes.
- Semi-dynamic, because the environment does not change with the passage of time, but the agent's performance score does.
- Continuous, because it has a finite number of distinct states.
- Multi-agent, because it's playing chess with another intelligent agent.

#### d. Provide an example of an intelligent agent, and give a PEAS description of the task environment, and characterize it in terms of the task properties listed in Section 2.3.2 (p. 61) in AIMA.
- Vacuum cleaner - Cleanness, Efficiency, Battery life, security - Room, Table, Wood floor, Carpet - Wheels, Brushes, Vacuum extractor - Camera, Dirt detection sensor, Bump sensor, Wall sensor

#### e. Compare and contrast the following agent types:

1. Simple reflex
2. Model-based reflex
3. Goal-based
4. Utility-based

Explain your answer.
1. The Simple reflex agents are the simplest agents. These agents take decisions on the basis of the current percepts and ignore the rest of the percept history.
2. The Model-based agent can work in a partially observable environment, and track the situation.
A model-based agent has two important factors:
- Model: It is knowledge about "how things happen in the world," so it is called a Model-based agent.
- Internal State: It is a representation of the current state based on percept history.
3. The agent needs to know its goal which describes desirable situations.
- Goal-based agents expand the capabilities of the model-based agent by having the "goal" information.
4. These agents are similar to the goal-based agent but provide an extra component of utility measurement which makes them different by providing a measure of success at a given state.
- Utility-based agent act based not only goals but also the best way to achieve the goal.

---

### 1.2 Conversational AI
#### b. Provide three examples of a chatbot, which you might encounter in your everyday life. Write your answer down.
1. Siri
2. Alexa
3. Bixby

#### d. List, and describe the advantages and disadvantages of using the following response generation chatbot types: rule-based, retrieval-based, and generative.
- Rule-based: this is where chatbot responses are entirely predefined and returned to the user according to a series of rules. 
- Retrieval-based: this is where chatbot responses are pulled from an existing corpus of dialogs. Like rule-based models, retrieval-based models rely on predefined responses, but they have the additional ability to self-learn and improve their selection of response over time.
- Generative: they are capable of formulating their own original responses based on user input, rather than relying on existing text. While generative models are very flexible and powerful in that they are not confined to a predefined set of rules or responses, they are also significantly more challenging to implement.

#### f. ELIZA is an example of a …

1. rule-based chatbot 
2. retrieval-based chatbot 
3. generative chatbot

Select the correct statement, and elaborate on your choice.

- A rule-based chatbot, because the programme is triggered by certain phrases to come out with stock responses. So the responses are predefined.

---
---

> Taxonomy of AI (1)
## 1) What is data, information & knowledge?
#### c. Provide two additional examples, where you specify the four DIKW stages:
1. 
- Example: Rain
- Data: It is raining.
- Information: The sky turned dark and grey and clouds began to form.
- Knowledge: Some droplets fall through the cloud and form into raindrops on their way down. As more and more droplets join together they become too heavy and fall from the cloud as rain.
- Wisdom: Based on previous observations and statistical models, we are able to predict the weather in the future. We have weather apps on our phone that tell us when it's about to rain.

2. 
- Example: Hail
- Data: It is hailing.
- Information: Clouds are beginning to form and it's freezing outside.
- Knowledge: A thunderstorm updraft lifts a water droplet above the freezing level in the atmosphere. The frozen water droplet then accretes super-cooled water, which freezes once it comes in contact with the frozen droplet. This process causes a hailstone to grow.
- Wisdom: Based on previous observations and statistical models, we are able to predict the weather in the future. Weather apps can give us information about when it is about to hail.

## 2) Data analysis methods
#### e. Come up with at least one situation, where you could deploy a descriptive, diagnostic, predictive, and prescriptive analysis. Elaborate on your answer.
- A store that is going to renovate:
  The owner doesn't completely want to renovate but wants to keep selling the best products. By using these types of analysis the owner can look at what the best and worst selling products are.

#### f. Power BI is one of the most popular dashboarding tools. List another dashboarding tool, and provide at least one ‘strength' and ‘weakness'. Write your answer down.
- Databox is another dashboarding tool.
- Strenght = It has customizable tools and has various data visualization options.
- Weakness = It takes a long time to set up and it lacks customizable dates.

---
---

> Taxonomy of AI (2)
## 1) Predictive analytics: To learn or not to learn…
#### b. Define the terms ‘supervised' and ‘unsupervised' learning. How do these types of machine learning differ from each other? Write your answer down.
- Supervised machine learning relies on labelled input and output training data, whereas unsupervised learning processes unlabelled or raw data.

#### d. Define the terms ‘inference', and ‘expert system' (Be concise!).
- The inference engine is part of the expert system.

#### e. Are artificial neural networks (ANNs) similar to the human brain? Support your answer with arguments.
- It looks the same as the human brain, but it is not. The number of neurons in a human brain is about 86 billion, where the neurons in an ANN is less then 1000. This is nowhere close to the number of neurons in the human brain.

#### f. An ANN uses a a) symbolic or b) connectionist approach to AI? Select one of the options, and explain your choice.
- It uses an connectionist approach, because each connection can transmit a signal to other neurons. An artificial neuron receives signals and then processes them, when he can then signal other neurons connected to it.

#### g. Can you think of a real-life scenario where an AI method that uses a symbolic approach would be more suited than a method that uses a connectionist approach? Explain your answer.
- In video games, for example, the AI will be better of with a symbolic approach. This is because it can learn quicker by seeing everything as symbols and then using that knowledge to play like a normal player would.

---
---

> Taxonomy of AI (3)
## 1) Taxonomy of AI: Domains, subdomains, and keywords
#### b. Find information that can help you to connect the following AI applications, algorithms etc. to the relevant domains and subdomains presented in the Taxonomy of AI:

- ELIZA = Communication, Natural Language Processing (NLP).
- Deep Blue = Learning, Machine Learning (ML)
- AlphaGo = Learning, Machine Learning (ML)
- AlexNet = Perception, Computer Vision
- GPT-3 = Communication, Natural Language Processing (NLP).
- Google's robot dog, Laikago = Integration & Interaction, Robotics & Automation
- Tesla car = Integration and Interaction, Connected and Automated Vehicles (CAV). 

---
---

> Risk & Benefits of AI
## 1) Introduction to data ethics
#### c. In the video, she makes the following statement: ‘Algorithms are opinions embedded in code'. What do you think she means with this statement, and what are the possible implications that could arise from it? Explain your answer.
- .

## 2) Applied data ethics
#### a.  In the article How to make a chatbot that isn't racist or sexist Will Douglas Heaven presents three approaches to making chatbots safe for public use. List, and briefly describe these approaches, and explain why it is so difficult to stop a language model from generating offensive texts. Write your answer down.
- 1. Bolt it onto a language model and have the filter remove inappropriate language from the output.
- 2. Use a filter to remove offensive examples from the training data.
- 3. Make chatbots safer by baking in appropriate responses.
- It is difficult to stop a language model from generating offensive texts because a model trained on a data set stripped of offensive language can still repeat back offensive words uttered by a human.

#### b. Find three newspaper articles on a risk and/or benefit associated with a domain and subdomain of AI (e.g., perception, computer vision, planning, natural language processing, searching, etc.), and fill in the table below:
1. Robot dog
  - Boston Dynamics.
  - Robot dog identifying safety and structural issues.
  - Machine learning, robotics and automation
  - Can inspect even de smallest of spaces, while gathering and recording data useful for the study and planning of interventions.

2. Racist Chatbot
  - Twitter
  - AI Chatbot you can have a conversation with
  - Communication, NLP
  - This AI technology can get really out of hand.

3. Retina scanners
  - Amsterdam Airport
  - Surveillance cameras equipped with facial recognition software
  - Perception, computer vision, learning, and machine learning
  - This AI technology is able to pick out people whom may not travel due to things they have done.

---
---

> State-of-the-art AI & Minority Report (3)
## 1) Research & Applications
#### b. Read a blog, and note down the research topic, author, and affiliated university/company, etc.
- Berkeley Artificial Intelligence Research (BAIR)
  - Research topic = Keeping Learning-Based Control Safe by Regulating Distributional Shift
  - Author = Katie Kang
  - University/company = UC Berkeley
- Google AI Blog
  - Research topic = TensorStore for High-Performance, Scalable Array Storage
  - Author = Jeremy Maitin-Shepard and Laramie Leavitt
  - University/company = Google
- OpenAI Blog
  - Research topic = Training and open-sourcing a neural net called Whisper
  - Author = Alec Radford, Jong Wook Kim, Christine McLeavey Payne, Pamela Mishkin, Tao Xu, Greg Brockman, Ilya Sutskever
  - University/company = /