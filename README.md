# Telco Churn Classification Project
Stephanie Jones<br>
Codeup | Hopper Cohort<br>
Presented on Monday, November 29, 2021

## I. Project Overview
### A. Project Description
>Telco Communications is a fictional telecommunications company looking to reduce customer churn (aka customer attrition, aka >customers leaving Telco for competitors). I will be using Telco customer data and machine learning methodologies to determine >what is driving customer churn and, with that information, providing management (<i>non-data scientists</i>) with recommendations >for reducing customer churn.


### B. Business Goals
>Management already knows that customers on month to month payment plans are churning at higher rates but removing the month to >month payment option is not feasible at this time. The goal is to look at the results from the best performing machine learning >model and determine which of our existing customers are at a high risk for churning. I will then provide recommendations on how >we can incentivize these customers to remain with Telco, as the cost of retaining an existing customer is much less than the cost >of acquiring a new one.


### C. Deliverables
- final_project_report.ipynb (<i>Jupyter Notebook for project presentation walkthrough</i>)
- working_project_report.ipynb (<i>working Jupyter Notebook</i>)
- predictions.csv (<i>a csv file containing the churn predictions from my best performing model and the actual churn values from the test data set</i>)
- acquire.py and prepapre.py (<i>modules containing data acquisition and preparation functions, respectively</i>)

## II. Project Information
### A. Data Dictionary

### B. Steps to Reproduce
>:white_check_mark: Read this README.md file<br>
>:white_medium_square: Clone my Github repo to your local directory<br>
>:white_medium_square: Create your own local env.py file with your host, username, and password (<i>hide using .gitignore</i>)<br>
>:white_medium_square: Python 3 installed, along with the following libraries:
>- matplotlib
>- seaborn
>- graphviz
>- sklearn

## III. Key Findings and Takeaways
>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Elit >duis tristique sollicitudin nibh sit amet commodo. Viverra vitae congue eu consequat ac felis donec et. Non odio euismod lacinia >at quis risus sed. Vitae purus faucibus ornare suspendisse sed nisi lacus sed. Pulvinar sapien et ligula ullamcorper malesuada >proin libero nunc consequat. Lobortis elementum nibh tellus molestie nunc. Lacus viverra 

## IV. Process | Project Pipeline
###### Steps Moving through the Data Science Pipeline
---
:large_blue_circle: <b>Plan</b> >> Acquire >> Prepare >> Explore >> Model >> Evaluate >> Conclusions
#### 0. Plan Project
- Read project specs
- Created Trello Board
- Created local project folder and remote Github repository
- Created this README.file

---
Plan >> :large_blue_circle: <b>Acquire</b> >> Prepare >> Explore >> Model >> Evaluate >> Conclusions
#### 1. Acquire Data
- Established connection to Codeup DB
- Read telco DB into a DataBase and store in raw_data variable
- Cached data into local file, telco_data.csv, if one does not already exist
- Created acquire.py that stores data acquistion functions that perform the above steps

---
Plan >> Acquire >> :large_blue_circle: <b>Prepare</b> >> Explore >> Model >> Evaluate >> Conclusions
#### 2. Prepare Data

---
Plan >> Acquire >> Prepare >> :large_blue_circle: <b>Explore</b> >> Model >> Evaluate >> Conclusions
#### 3. Explore Data
Positive: Customer churns (<i>leaves Telco for competitor</i>)<br>
Negative: Customer does not church (<i>remains a Telco customer</i>)<br>
> Initial Hypothesis:<br>
> (My initial hypothesis)

---
Plan >> Acquire >> Prepare >> Explore >> :large_blue_circle: <b>Model</b> >> Evaluate >> Conclusions
#### 4. Data Modeling

----
Plan >> Acquire >> Prepare >> Explore >> Model >> :large_blue_circle: <b>Evaluate</b> >> Conclusions
#### 5. Model Evaluation

----
Plan >> Acquire >> Prepare >> Explore >> Model >> Evaluate >> :large_blue_circle: <b>Conclusions</b>

#### 6. Conclusions
>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Elit >duis tristique sollicitudin nibh sit amet commodo. Viverra vitae congue eu consequat ac felis donec et. Non odio euismod lacinia >at quis risus sed. Vitae purus faucibus ornare suspendisse sed nisi lacus sed. Pulvinar sapien et ligula ullamcorper malesuada >proin libero nunc consequat. Lobortis elementum nibh tellus molestie nunc. Lacus viverra vitae congue eu consequat ac felis. Eget >mi proin sed libero enim sed. Turpis egestas integer eget aliquet nibh praesent tristique. 

## V. Recommendations and Next Steps
>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Elit >duis tristique sollicitudin nibh sit amet commodo. Viverra vitae congue eu consequat ac felis donec et. Non odio euismod lacinia >at quis risus sed. Vitae purus faucibus ornare suspendisse sed nisi lacus sed. Pulvinar sapien et ligula ullamcorper malesuada >proin libero nunc consequat. Lobortis elementum nibh tellus molestie nunc. Lacus 
#### If I had more time...
>I would like to explore the x11 rows that had blank values for total_charges (dropped from DataFrame during 02_prepare)

# Addtional Project Information
Technical Skills
> - Structured Query Language
> - Python
> - Markdown
> - Jupyter Notebok
> - Data Cleaning
> - Statistical Modeling

Soft Skills
> - Visual Communication
> - Technical Communication
> - Information Structure and Organization