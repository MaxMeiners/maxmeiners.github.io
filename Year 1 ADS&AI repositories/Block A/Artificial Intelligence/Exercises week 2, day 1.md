# **Exercises week 2, day 1**

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