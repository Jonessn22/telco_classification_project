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
##### Cleaning
>a. Dropped unecessary columns
b. Map binary, yes/no to 1/0
c. Map gender column male/female to 1/0


##### Splitting
>a. split the cleaned telco data, first into train_and_validate (80%) and test (20%)<br>
b. splt the train_and_validate into train (70% of the 80%, 56% of the total) and validate (30% of the 80%, 24% of the total)

---
Plan >> Acquire >> Prepare >> :large_blue_circle: <b>Explore</b> >> Model >> Evaluate >> Conclusions
#### 3. Explore Data
<b>Initial Questions<br>
1. Do customers who pay a certain way churn more?
- Customers who pay by eCheck have highest churn

2. Do customers with a certain type of internet service churn more?
- Customers with Fiber have highest churn
- Customers with no internet service have lowest churn

3. Do customers with lower monthly charges churn less than those with higher monthly charges?
- There is not much correlation between monthly charges and tenure
- Most of our customers who are churning have high monthly_charges and churning earlier in tenure
    - The higher a customer’s tenure the less likely they are to churn


---
Plan >> Acquire >> Prepare >> Explore >> :large_blue_circle: <b>Model</b> >> Evaluate >> Conclusions
#### 4. Data Modeling
>Baseline Accuracy: 0.73

>Model 1: Decision Tree with max_depth of 2<br>
Accuracy of Model 1 Decision Tree classifier on training set: 0.77<br>
Accuracy of Model 1 Decision Tree classifier on validate set: 0.76<br>

>Model 2: Decision Tree with max_depth of 4<br>
Accuracy of Model 2 Decision Tree classifier on training set: 0.77<br>
Accuracy of Model 2 Decision Tree classifier on validate set: 0.76<br>

>Model 3: Decision Tree with max_depth of 6<br>
Accuracy of Model 3 Decision Tree classifier on training set: 0.78<br>
Accuracy of Model 3 Decision Tree classifier on validate set: 0.77
----
Plan >> Acquire >> Prepare >> Explore >> Model >> :large_blue_circle: <b>Evaluate</b> >> Conclusions

----
Plan >> Acquire >> Prepare >> Explore >> Model >> Evaluate >> :large_blue_circle: <b>Conclusions</b>

#### 6. Conclusions, Recommendations, and Next Steps
>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Elit >duis tristique sollicitudin nibh sit amet commodo. Viverra vitae congue eu consequat ac felis donec et. Non odio euismod lacinia >at quis risus sed. Vitae purus faucibus ornare suspendisse sed nisi lacus sed. Pulvinar sapien et ligula ullamcorper malesuada >proin libero nunc consequat. Lobortis elementum nibh tellus molestie nunc. Lacus viverra vitae congue eu consequat ac felis. Eget >mi proin sed libero enim sed. Turpis egestas integer eget aliquet nibh praesent tristique. 

#### If I had more time...
>Explore the x11 rows that had blank values for total_charges<br>
>Compare other variables against eCheck payment type to see what types of customers are paying that way<br>
>Bin 'monthly_charges' and 'total_charges' by quartiles, decitiles and look for any patterns, additional insights