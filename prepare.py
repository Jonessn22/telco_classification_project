# Functions to prepare Telco data for exploration and modeling

import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split

import pandas as pd

# Feeder function no1 of 2

def clean_telco(df):
    '''
    This function takes in the raw DataFrame as an argument and returns a cleaned DataFrame, performs the following cleaning actions:
        a. removes x11 rows where total_charges in an empty valuie
        b. changes total_charges values from object to float dtype
        c. creates dummy variables for object columns
        d. concatenates dummy columns with the original df
        e. drops unnecessary columns and customer_id column, which is not needed for exploration and modeling
        f. renames columns to be shorter and more understable
        g. lowercases column names
    
    This is the first of two functions that will feed into our final clean_split() prepare function.
    '''
    
#                                       a. removing empty total_charges values
    df_empty_rows = df[df.total_charges != ' ']

#                                       b. changing total_charges dtype: object --> float
    df_empty_rows.total_charges = df_empty_rows.total_charges.astype(float)
    
#                                       c. creating dummy variables for object columns
    dummies_df = pd.get_dummies(df_empty_rows[['churn', 'contract_type', 'dependents', 
                                               'device_protection', 'gender', 'internet_service_type', 
                                               'multiple_lines', 'online_backup', 'online_security', 
                                               'paperless_billing', 'partner', 'payment_type', 'phone_service', 
                                               'streaming_movies', 'streaming_tv', 'tech_support']])
    
#                                       d. concatenating dummy columns with original df
    df_dummies = pd.concat([df_empty_rows, dummies_df], axis = 1)
    
#                                       e. dropping unnecessary columns
    df_drop = df_dummies.drop(columns = ['churn', 'contract_type', 'dependents', 
                                               'device_protection', 'gender', 'internet_service_type', 
                                               'multiple_lines', 'online_backup', 'online_security', 
                                               'paperless_billing', 'partner', 'payment_type', 'phone_service', 
                                               'streaming_movies', 'streaming_tv', 'tech_support', 
                                         
#                                          e-1. dummy columns w/boolean values                                            
                                             'churn_No', 'dependents_No', 'gender_Female', 'paperless_billing_No',
                                             'partner_No', 'phone_service_No',
                                         
#                                          e-2. dropped unneeded customer_id column                                  
                                             'customer_id', 
                                         
#                                          e-3.dropped redundant columns
                                             'contract_type_id', 'internet_service_type_id', 'payment_type_id'])

#                                       f. renaming columns
    df_clean = df_drop.rename(columns = {'churn_Yes': 'churn', 'contract_type_Month-to-month': 'contract_mtm',
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
        
                                        })
    
#                                       g. lowercare column names
    df_clean.columns = df_clean.columns.str.lower()
    
    
    return df_clean


from sklearn.model_selection import train_test_split

# ----------------------------
# Feeder function no2 of 2

def train_validate_test_split(cleaned_df, seed = 123):
    '''
    This function takes in as arguments the cleaned DataFrame and a random seed and splits the DataFrame,
    first into two samples, train_and_validate (80%) and test (20%). It then splits the train_and_validate
    into train (70% of the 80%, 56% of total) and validate (30% of the 80%, 24% of the total).
    The function returns x3 DataFrames, train, validate, and test.
    
    This is the second of two functions that will feed into our final clean_split() prepare function.
    '''
    
    train_and_validate, test = train_test_split(
                                        cleaned_df, 
                                        test_size = 0.2, 
                                        random_state = seed, 
                                        stratify = cleaned_df.churn)
    
    train, validate = train_test_split(
                                        train_and_validate,
                                        test_size = 0.3,
                                        random_state = seed,
                                        stratify = train_and_validate.churn)
    
    return train, validate, test

# ----------------------------
# Main clean and split function

def clean_split_telco_data(df):
    '''
    This is the function that the above two functions are fed into. It runs the clean_telo() and 
    train_test_validate_split() functions. It takes in the original, raw DataFrame and a random seed
    as arguments and returns cleaned and split train, test, and validate DataFrames.
    '''
    
    cleaned_df = clean_telco(df)
    train, validate, test = train_validate_test_split(cleaned_df, seed = 123)
    
    return train, validate, test