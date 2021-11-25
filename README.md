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

Train: 3937 ~56% (~70% of ~80%)<br>
Validate: 1688 ~ 24% (~30% of 80%)<br> 
Test: 1407 ~ 20%<br>
##### Cleaning
a. removed x11 rows where total_charges was an empty value<br>
b. changed total_charges values from object to float dtype<br>
c. created dummy variables for object columns:<br>
>'churn', 'contract_type', 'dependents',
'device_protection', 'gender', 'internet_service_type',
'multiple_lines', 'online_backup', 'online_security', 
'paperless_billing', 'partner', 'payment_type', 'phone_service', 
'streaming_movies', 'streaming_tv', 'tech_support'
                                  
d. concatenated dummy columns with the original df<br>
e. dropped unnecessary columns and customer_id column, which is not needed for exploration and modeling:<br>
- e-1. dummy columns w/boolean values:<br>
>'churn_No', 'dependents_No', 'gender_Female', 'paperless_billing_No',
'partner_No', 'phone_service_No'

- e-2. dropped unneeded customer_id column<br>
- e-3.dropped redundant columns:<br>
>                                'contract_type_id', 'internet_service_type_id', 'payment_type_id'

f. renamed columns to be shorter and more understable:<br>
>'churn_Yes': 'churn', 'contract_type_Month-to-month': 'contract_mtm',
'contract_type_One year': 'contract_one_yr', 'contract_type_Two year':
'contract_two_yr', 'dependents_Yes': 'dependents', 'gender_Male': 
'gender_m', 'internet_service_type_DSL': 'internet_dsl', 
'internet_service_type_Fiber optic': 'internet_fiber', 
'internet_service_type_None': 'internet_none', 'paperless_billing_Yes':
'paperless_bill', 'partner_Yes': 'partner', 
'payment_type_Bank transfer (automatic)': 'pay_xfer_auto', 
'payment_type_Credit card (automatic)': 'pay_credit_auto', 
'payment_type_Electronic check': 'pay_echeck', 
'payment_type_Mailed check':'pay_mail', 'phone_service_Yes': 
'phone_service'

g. lowercased column names

##### Splitting
a. split the cleaned telco data, first into train_and_validate (80%) and test (20%)
b. splt the train_and_validate into train (70% of the 80%, 56% of the total) and validate (30% of the 80%, 24% of the total)

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
>Explore the x11 rows that had blank values for total_charges (dropped from DataFrame during 02_prepare)

>Shorten some of the longer column names

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