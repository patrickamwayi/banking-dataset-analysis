# banking-dataset-analysis

***
[[Project Description/Goals](#project_description_goals)]
[[Initial Questions](#initial_questions)]
[[Planning](#planning)]
[[Data Dictionary](#dictionary)]
[[Reproduction Requirements](#reproduce)]

[[Conclusion](#conclusion)]

___

## <a name="project_description_goals"></a>Project Description/Goals:

Bank Dataset Analysis
- About the Project
- This project is about identifying characteristics for marketing analysis for individuals in banking clientele.

### Business understanding
Project Goal
- The goal for this project is to answer initial questions, and analyze the characteristics for banking clientele for marketing purposes. Business goals include which demographic of individuals to create marking improvements on.

### Data understanding
The banking dataset analysis data was obtained from Kaggle open-source dataset. It is stored in a csv file, named as "test.csv" and "train.cvs". It has 17 columns called features, including 45211 and 4521 row numbers. The fetures are age, job, marital, education, default, balance, housing, loan, contact, day, month, duration, campaign, pdays, previous, poutcome and y. 

### Description
A Portuguese bank is experiencing declining revenue, attributed to inadequate customer investments in long-term deposits. To address this issue, the bank aims to identify potential existing customers with a high likelihood of subscribing to long-term deposits and concentrate marketing efforts on this target group.

The banking dataset for analysis is derived from a direct marketing campaign conducted by a Portuguese bank institution. 

This campaign primarily involves making phone calls to clients to encourage them to accept long-term deposits with the bank.

After each call, clients are categorized as either "no" if they did not make a deposit or "yes" if they accepted to make a deposit.

The project's objective is to predict whether a client will agree to a term deposit during a call based on client information.

[[Back to top](#top)]


## <a name="initial_questions"></a>Initial Questions:

- What job types are customers likely to subscribe term deposit?
- What type of customer marital status are more likely to subscribe term deposit?
- Does customer education level has any effect to subscription of term deposit?
- What is the relationship between customers housing and subscription to term deposit?
- What is the relationship between customer loans and subscription to term deposit?
- What was the most effective method used to contact customers?

[[Back to top](#top)]


## <a name="planning"></a>Planning:

- Create README.md with data dictionary, project and business goals, and come up with initial hypotheses.



- Acquire data from The banking dataset analysis data was obtained from Kaggle open-source dataset. It is stored in a csv file, named as "test.csv" and "train.cvs". 
- Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process. 
- Store the acquisition and preparation functions in a wrangle.py module function, and prepare data in Final Report Notebook by importing and using the function.
- Document conclusions in the Final Report Notebook.

[[Back to top](#top)]



## <a name="dictionary"></a>Data Dictionary  


| Feature | Definition | Data Type |
| ----- | ----- | ----- |
| Age |age of the client | int |
| Job |type of job | object |
| Marital |marital status | object |
| Education |education level | object |
| Default | does the client have credit in default? | object |
| Balance |  average yearly balance | int |
| Housing | does the client have housing loan? | object |
| Loan |does the client have personal loan? | object |
| Contact |contact communication type | object |
| Day |last contact day of the month | int |
| Month |last contact month of year  | object |
| Duration |last contact duration, in seconds | int |
| Campaign |number of contacts performed during this campaign and for this client | int |
| Pdays |number of days that passed by after the client was last contacted from a previous campaign | int |
| Previous |number of contacts performed before this campaign and for this client | int |
| Poutcome |outcome of the previous marketing campaign | object |
| y |            | object |





---

[[Back to top](#top)]


## <a name="conclusion"></a>Conclusion:

A summary of the results of the analysis :

Students, housemaids and unemployed people are likely to subscribe to term deposit, on the other management,blue-coller and technician are less likely to sunscribe to term deposit.
Married people are less likely to sunscribe to term deposit, on the other hand single and divorced people are more likely to subscribe to term depoit.
Education seem to have effect on subscription to term deposit, people with secondary education are more likely to subscribe to term deposit unlike people with tertiary and primary education

## <a name="reproduce"></a>Reproduction Requirements:

The banking dataset analysis data was obtained from Kaggle open-source dataset. It is stored in a csv file, named as "test.csv" and "train.cvs". 
From kaggle(https://www.kaggle.com). 

1)Download the following files

- Wrangle.py

- Run the final_report.ipynb notebook


2) After downloading files make sure all files are in the same folder or location

3) Once step two and step one are done you would be able to run finalnotebook without errors



    
[[Back to top](#top)]
