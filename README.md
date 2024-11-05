# From Transistors to Tensors

*Original course curriculum cc: Chip Huyen's [MLOps Guide](https://huyenchip.com/mlops/).*

A collection of materials from introductory to advanced. This is roughly the path I’d follow if I were to start my MLOps journey again.

## Table of Contents
- [ML + Engineering Fundamentals](#ml--engineering-fundamentals)
- [MLOps](#mlops)
  - [Overview](#overview)
  - [Intermediate](#intermediate)
  - [Advanced](#advanced)
- [Career](#career)
- [Case Studies](#case-studies)
- [Bonus](#bonus)

---

## ML + Engineering Fundamentals
While it’s tempting to want to get straight to ChatGPT, it’s important to have a good grasp of machine learning, deep learning, NLP, and reinforcement learning fundamentals.

- [10 free ML courses](#): make sure to take these classes in order.
- [Book] *Machine Learning: A Probabilistic Perspective* by Kevin P. Murphy. [PDF link available here](#).
- [Book] *Information Theory, Inference, and Learning Algorithms* by David MacKay. [Free online version here](#).
- [Book] *Deep Learning* by Ian Goodfellow, Yoshua Bengio, and Aaron Courville. [Free online version](#).
- [Book] *Introduction to Information Retrieval* by Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze. Essential for anyone interested in NLP. [Free online version](#).
- [Book] *Reinforcement Learning: An Introduction* by Richard S. Sutton and Andrew G. Barto. Essential for reinforcement learning. [Free online version](#).
- [Tutorials] OpenAI’s *Spinning up in Deep Reinforcement Learning*: A collection of articles that provide intuition for many RL algorithms.
- [Video] *Zero to Hero series* by Andrej Karpathy.
- *Tools and concepts I’d prioritize learning*
- *A survivor’s guide to AI courses at Stanford (Updated Feb 2020)*

---

## MLOps
**What’s MLOps?**  
*Ops* in MLOps comes from *DevOps*, short for *Developments and Operations*. To operationalize something means to bring it into production, including deploying, monitoring, and maintaining it.

Currently, this section contains a lot of my writing, largely because when I started learning about MLOps, resources were scarce. I’ll add more materials soon!

- [Book] *Designing Machine Learning Systems* (O’Reilly, 2022).
- [Community] Join discussions on our *MLOps Discord server* [15k+ members]. Ask questions and join our monthly talks/discussions!

### Overview
Overview of ML in production.

- [Video] *Machine learning production myths* (Stanford’s MLSys Seminars)
- [Lecture note] *Introduction to machine learning in production*
- *Rules of Machine Learning: Best Practices for ML Engineering* by Martin Zinkevich (2019)
- *What I learned from looking at 200 machine learning tools* [Jun 2020]
- *Machine Learning Tools Landscape v2 (+84 new tools)* [Dec 2020]
- *The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction* by Breck et al., 2017
- *Building LLM applications for production*

### Intermediate
Deep dives into different aspects of ML production.

- [Lecture note] *Creating training data: sampling, labeling, handling class imbalance, data augmentation*
- [Lecture note] *Feature engineering*
- [Book excerpt] *Data Distribution Shifts and Monitoring*
- *Instrumentation, Observability & Monitoring of Machine Learning Models* by Josh Wills (2019)
- *RLHF: Reinforcement Learning from Human Feedback*

### Advanced
Build the best MLOps platform for your organization!

- *Real-time machine learning: challenges and solutions*
- [Lecture note] *Data system fundamentals for data scientists*
- *A friendly introduction to machine learning compilers and optimizers*
- *Why data scientists shouldn’t need to know Kubernetes*
- *Self-serve feature platforms: architectures and APIs*

---

## Career
- [Free book] *Machine Learning Interviews Book*
- [Twitter thread] *The ML interviews process*
- *Career advice for recent Computer Science graduates*
- *Four lessons I learned after my first full-time job after college*
- *7 reasons not to join a startup and 1 reason to*
- *Analysis of compensation, level, and experience details of 19k tech workers*
- *What Glassdoor interview reviews reveal about tech hiring cultures*
- *What we look for in a resume*

---

## Case Studies
To get a sense of the challenges of machine learning production, it’s helpful to learn from companies who are doing it.

- *Using Machine Learning to Predict Value of Homes On Airbnb* by Robert Chang, Airbnb Engineering & Data Science (2017).
- *Using Machine Learning to Improve Streaming Quality at Netflix* by Chaitanya Ekanadham, Netflix Technology Blog (2018).
- *150 Successful Machine Learning Models: 6 Lessons Learned at Booking.com* by Bernardi et al., KDD (2019).
- *Machine Learning-Powered Search Ranking of Airbnb Experiences* by Mihajlo Grbovic, Airbnb Engineering & Data Science (2019).
- *From shallow to deep learning in fraud* by Hao Yi Ong, Lyft Engineering (2018).
- *Space, Time and Groceries* by Jeremy Stanley, Tech at Instacart (2017).
- *Creating a Modern OCR Pipeline Using Computer Vision and Deep Learning* by Brad Neuberg, Dropbox Engineering (2017).
- *Scaling Machine Learning at Uber with Michelangelo* by Jeremy Hermann and Mike Del Balso, Uber Engineering (2019).
- *How we grew from 0 to 4 million women on our fashion app, with a vertical machine learning approach* by Gabriel Aldamiz, HackerNoon (2018).

---

## Bonus
Some stuff I did that doesn’t quite fit into any section above, but I want to share anyway :P

- [Code] *Python-is-cool*: Cool Python features that I used to be too afraid to use.
- [Code] *just-pandas-things*: Pandas quirks that used to traumatize me.
- [Code] *Coding exercises and solutions for coding interviews*.
- [Video] *Switching From a Batch to Streaming Mindset w/ Chip Huyen*.
- [VentureBeat] *4 AI and ML job hunting tips from Chip Huyen*.
- [Booklet] *Machine learning systems design (2019)*: My initial notes on ML systems, inspiring the book *Designing Machine Learning Systems* (2022).



<!--- ## From Transistors to Tensors

## How to Learn
- [ ] [5 Tips to Boost Your Learning](https://gordicaleksa.medium.com/5-tips-to-boost-your-learning-d6eb5edfe6d)
- [ ] [Learning How to Learn](https://www.coursera.org/learn/learning-how-to-learn)

## Data Structures and Algorithms
- [ ] [Algorithms and Data  Structures for Begineers](https://neetcode.io/courses/dsa-for-beginners/2)
- [ ] [Advanced Algorithms](https://neetcode.io/courses/advanced-algorithms/1)
  
<!-- ## Prerequisite Math for ML
- [ ] Linear Algebra
- [ ] Analytic Geometry
- [ ] Matrix Decompositions
- [ ] Vector Calculus
- [ ] Probability and Distributions
- [ ] Continuous Optimisation 

## ML + Engineering Fundamentals

- [ ] **Introduction to Statistics by Stanford (Coursera)**
  - [See course materials](https://www.coursera.org/learn/stanford-statistics) (free online course)
  - This self-paced course covers basic concepts in probability and statistics spanning over four fundamental aspects of machine learning: exploratory data analysis, producing data, probability, and inference.

- [ ] **18.06: Linear Algebra by MIT**
  - Textbook: _Introduction to Linear Algebra_ (5th ed.) by Gilbert Strang
  - [See course materials](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/) (videos available)

- [ ] **CS231N: Convolutional Neural Networks for Visual Recognition by Stanford**
  - [See video lectures (2017)](https://www.youtube.com/playlist?list=PLzUTmXVwsnXod6WNdg57Yc3zFx_f-RYsq)
  - [See course materials](http://cs231n.github.io/)

- [ ] **Practical Deep Learning for Coders by fast.ai**
  - [See course materials](https://course.fast.ai/) (free online course)

- [ ] **CS224N: Natural Language Processing with Deep Learning by Stanford**
  - [See video lectures (2017)](https://www.youtube.com/playlist?list=PLU40WL8Ol94IJzQtileLTqGZuXtGlLMP_)
  - [See course materials](http://web.stanford.edu/class/cs224n/syllabus.html)

- [ ] **Machine Learning by Coursera**
  - [See course materials](https://www.coursera.org/learn/machine-learning) (free online course)

- [ ] **Probabilistic Graphical Models Specialization by Coursera**
  - Textbook: _Probabilistic Graphical Models: Principles and Techniques_ by Daphne Koller and Nir Friedman
  - [See course materials](https://www.coursera.org/specializations/probabilistic-graphical-models) (free online courses)

- [ ] **Introduction to Reinforcement Learning by DeepMind**
  - [See lecture videos](https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ)

- [ ] **Full Stack Deep Learning Bootcamp**
  - [See lecture videos](https://course.fullstackdeeplearning.com/)

- [ ] **How to Win a Data Science Competition: Learn from Top Kagglers by Coursera**
    - [See course materials](https://www.coursera.org/projects/ml-basics-kaggle-competition) (free online course)
     
## **Projects**
- [ ] Win Kaggle Competitions
- [ ] Implement ML Papers
- [ ] Contribute to Open-Source Projects
- [ ] Build Side-Projects 

<!-- ## Python

- [X] [Python Fundamentals](https://www.kaggle.com/learn/python)
- [ ] [Replit's 100 Days of Code (Python)](https://replit.com/learn/100-days-of-python)
- [X] [Data Visualisation](https://www.kaggle.com/learn/data-visualization)
- [X] [ML Fundamentals](https://www.kaggle.com/learn/intro-to-machine-learning)
- [ ] [Practical Deep Learning for Coders](https://course.fast.ai/)
- [ ] [PyTorch](https://pytorch.org/tutorials/beginner/basics/intro.html)
- [ ] [matplotlib](https://matplotlib.org/stable/tutorials/index)
- [ ] [pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [ ] [FastApi](https://fastapi.tiangolo.com/learn/) -->

<!-- ## Mathematics for Computer Science

- [ ] [Calculus 1A: Differentiation](https://mitxonline.mit.edu/courses/course-v1:MITxT+18.01.1x/)
- [ ] [Calculus 1B: Integration](https://openlearninglibrary.mit.edu/courses/course-v1:MITx+18.01.2x+3T2019/about)
- [ ] [Calculus 1C: Coordinate Systems & Infinite Series](https://openlearninglibrary.mit.edu/courses/course-v1:MITx+18.01.3x+1T2020/about)
- [ ] [Essence of calculus by 3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
- [ ] [Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/download/)
- [ ] [Mathematics for Computer Science](https://openlearninglibrary.mit.edu/courses/course-v1:OCW+6.042J+2T2019/about)

## Mathematics for Machine Learning

- ### Linear Algebra
    - [ ] [Essence of linear algebra by 3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
    - [ ] [Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/)

- ### Probability
   - [ ] [Introduction to Probability - The Science of Uncertainty](https://www.edx.org/learn/probability/massachusetts-institute-of-technology-probability-the-science-of-uncertainty-and-data)
   - [ ] [Statistics 110: Probability](https://projects.iq.harvard.edu/stat110/youtube)

## Containerisation

- [ ] [Docker](https://docs.docker.com/get-started/overview/)

## Core Systems

- [ ] [Nand2Tetris Part I](https://www.coursera.org/learn/build-a-computer)
- [ ] [Nand2Tetris Part II](https://www.coursera.org/learn/nand2tetris2)
- [ ] [Computer Networking: a Top-Down Approach](https://gaia.cs.umass.edu/kurose_ross/online_lectures.htm)

## Advanced Systems

- [ ] [Computation Structures 1: Digital Circuits](https://learning.edx.org/course/course-v1:MITx+6.004.1x_3+3T2016/block-v1:MITx+6.004.1x_3+3T2016+type@sequential+block@c1s1/block-v1:MITx+6.004.1x_3+3T2016+type@vertical+block@c1s1v1)
- [ ] [Computation Structures 2: Computer Architecture](https://learning.edx.org/course/course-v1:MITx+6.004.2x+3T2015/home)
- [ ] [Computation Structures 3: Computer Organization](https://learning.edx.org/course/course-v1:MITx+6.004.3x_2+1T2017/home) --->



<!--- ## Optional

## Kaggle Competitions

- [X] [Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic)
- [X] [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)
- [ ] [Store Sales - Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting)
- [ ] [Digit Recognizer](https://www.kaggle.com/competitions/digit-recognizer)

## Generative AI
- [ ] [Generative AI by Andrej Karpathy](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)
- [ ] [Neural networks by 3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- [ ] [Statistics Fundamentals by StatQuest with Josh Starmer](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9)

- ### Prompt Engineering

  - [ ] [Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)

  
- ### Machine Learning Specialization

  - [ ] [Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction)

- ### Deep Learning Specialization

  - [ ] [Deep Learning Specialization](https://www.deeplearning.ai/courses/deep-learning-specialization/)

- ### Natural Language Processing Specialization

  - [ ] [Natural Language Processing Specialization](https://www.deeplearning.ai/courses/natural-language-processing-specialization/)

- ### Machine Learning Engineering for Production (MLOps) Specialization

  - [ ] [Machine Learning Engineering for Production (MLOps) Specialization](https://www.deeplearning.ai/courses/machine-learning-engineering-for-production-mlops/)
