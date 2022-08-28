# -*- coding: utf-8 -*-
"""Exploratory_Data_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WtrLCaHKmuaSYOBIAJnLkJJD5imS8-oh
"""

# Commented out IPython magic to ensure Python compatibility.
#Importing laibraries

import os
import numpy as np
import pandas as pd
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("/content/aspiring_minds_employability_outcomes_2015.xlsx")
df.head()

# Data Exploration

df.tail()

df.shape

df.dtypes

df.columns

# Statistical Analysis

df.describe()

df.info()

# Checking Missing Values

df.isnull().sum()

# Checking number of unique columns with their unique row values

df.nunique()

# Total number of same value in rows

df['Designation'].value_counts()

df['Salary'].value_counts()

df['JobCity'].value_counts()

df['DOJ'].value_counts()

df['DOL'].value_counts()

df['Gender'].value_counts()

df['10percentage'].value_counts()

df['12percentage'].value_counts()

df['12graduation'].value_counts()

df['collegeGPA'].value_counts()

df['CollegeState'].value_counts()

# Checking Outliers

df['Salary'].hist(bins=177)

"""**Observation**

Above salary histogram plot is right skewed and it needs to be normalized.

This column has extreme low value outliers.
"""

df['JobCity'].hist(bins=200, figsize= (50,15))

"""**Observation**

Above JobCity histogram plot is right skewed and it needs to be normalized.

This column has extreme low value outliers.
"""

df['12percentage'].hist(bins=500)

"""**Observation**

Above 12percentage histogram plot has normal distribution.

This column has extreme low value outlier at right.
"""

df['12graduation'].hist()

"""Above 12graduation histogram plot is left skewed and it needs to be normalized.

This column has no outlier.
"""

df['collegeGPA'].hist()

"""Above collegeGPA histogram plot is left skewed and it needs to be normalized.

This column has no outlier.
"""

# Views of relevant columns

df.pivot_table(values='Salary',index='Degree')

"""Above view show the salary of certain degrees."""

df.pivot_table(values='Salary',index='Designation')

"""Above view show the salary wrt certain designations."""

# Data Cleaning

del df['Unnamed: 0']
df

"""With the above command we removed unnamed column."""

df['JobCity']= df['JobCity'].str.replace('-1','Others')
df['JobCity'].unique()

"""With the above command we replace row value.

Checking all the unique row values.
"""

df['JobCity'].value_counts()

df['JobCity'].apply(lambda x : "Bangalore" if x == "BANGLORE" or x == "BANGALORE" or x=="Asifabadbanglore" or x=="Banaglore" 
                    or x=="bangalore" or x=="Banglore" or x=="BAngalore" or x=="Banagalore" or x=="Mangalore" or x=="bengaluru" 
                    or x=="banagalore" or x=="banaglore" or x=="Bengaluru" or x=="Chennai, bangalore" or x=="chennai,bangalore" 
                    or x=="Asifabadbangalore" or x==" bangalore" else
                    
                    "Noida" if x == "noida" or x=="NOIDA" or x=="Nouda" or x=="A-64,sec-64,noida" or x=="Greater Noida" 
                    or x=="noida " or x=="greater noida" or x=="nouda" or x=="a-64,sec-64,noida" or x=="Greater noida" 
                    or x=="GREATER NOIDA" else
                    
                    "new delhi" if x == "delhi" or x=="new dehli" or x=="new delhi/ncr" or x=="ncr" or x=="new new delhi" 
                    or x=="gaziabaad" or x=="gajiabaad" or x=="ghaziabad" or x=="guragaon" or x=="gurgoan" or x=="gurgaon" 
                    or x=="new delhi - jaisalmer" or x=="new delhi " or x==" new delhi" or x=="indirapuram,new delhi" or x==" Delhi" 
                    or x=="Delhi/NCR" else
                    
                    "Hyderabad" if x == "hderabad" or x=="hyderabad(bhadurpally)" or x=="Hyderabad " or x=="navi mumbai , hyderabad" 
                    or x=="hyderabad " or x=="hyderabad" else
                    
                    "Pune" if x == "punr" or x=="pune " or x==" pune" or x==" Pune" else 
                    
                    "mumbai" if x=="Navi Mumbai" or x=="mumbai , hyderabad" or x=="THANE" or x=="Thane" or x=="Mumbai" or x=="MUMBAI" 
                    or x==" mumbai" or x=="NAVI MUMBAI" or x=="Navi Mumbai , Hyderabad" or x=="thane" 
                    or x=="Khopoli" or x=="Navi mumbai" or x==" Mumbai" or x=="mumbai " or x=="Navimumbai" 
                    or x=="mumbai , Hyderabad" else
                    
                    "chennai" if x==" chennai" or x=="kochi/cochin,chennai and coimbatore" or x=="chennai " or x=="chennai & mumbai" 
                    or x=="chennai& mumbai" or x=="Chennai, Bangalore" or x=="Coimbatore" or x=="Kochi/Cochin" or x=="Kochi/Cochin, Chennai and Coimbatore"
                    or x=="Chennai & Mumbai" or x==" Chennai" else
                    
                    "north region" if x=="maharajganj" or x=="rewari" or x=="panchkula" or x=="lucknow" or x=="una" or x=="kanpur " 
                    or x=="faridabad" or x=="haridwar" or x=="unnao" or x=="dehradun" or x=="rudrapur" or x=="dharamshala" 
                    or x=="hissar" or x=="gurga" or x=="chandigarh" or x=="pantnagar" or x=="lucknow " or x=="ludhiana" 
                    or x=="muzaffarnagar" or x=="gagret" or x=="bareli" or x=="kanpur" or x=="dharuhera" or x=="meerut" or x=="agra" 
                    or x=="rohtak" or x=="jaspur" or x=="shimla" or x=="jammu" or x=="jhajjar" or x=="Jhajjar" or x=="nalagarh" or x=="chandigarh " 
                    or x=="joshimath" or x=="bathinda" or x=="kala amb " or x=="karnal" or x=="baddi hp" or x=="bahadurgarh" 
                    or x=="varanasi" or x=="shahibabad" or x=="ambala" or x=="Ambala City" or x=="roorkee" or x=="allahabad" or x=="Allahabad" or x=="panchkula " 
                    or x=="jalandhar" or x=="phagwara" or x=="yamuna nagar" or x=="sampla" or x=="mainpuri" or x=="rae bareli" 
                    or x=="patiala" or x=="gorakhpur" or x=="rajpura"or x=="haryana" or x=="bulandshahar" or x=="sonipat" or x=="gonda"
                    or x=="yamnorth zone nagar" or x=="manesar" or x=="jhansi" or x=="rae north zone" or x=="north zone " else
                    
                    "south region" if x=="mysore" or x=="trivandrum" or x=="Trivandrum" or x=="Technopark, Trivandrum" or x=="coimbatore" or x=="visakhapatnam" 
                    or x=="vsakhapttnam" or x=="kochi/cochin" or x=="mysore " or x=="kochi" or x=="tirupathi" or x=="tirunelvelli" 
                    or x=="tornagallu" or x=="madurai" or x=="cheyyar" or x==" ariyalur" or x=="calicut" or x=="miryalaguda" or x=="trichy" 
                    or x=="kundankulam" or x=="ongole" or x=="ernakulam" or x=="muvattupuzha" or x=="orissa" or x=="mettur" or x=="kurnool" or x=="rayagada, odisha" or x=="nellore" 
                    or x=="vellore" or x=="Vellore" or x=="Nellore" or x=="pondycherry" or x=="secunderabad" or x=="Miryalaguda" or x=="gorakhpur" or x=="hubli" or x=="kakinada" or x=="gulbarga" 
                    or x=="pondy" or x=="keral" or x=="bellary" or x=="Bellary" or x=="hospete" or x=="Hospete" or x=="vandavasi" or x=="salem" or x=="dharmapuri" or x=="belgaum" 
                    or x=="nagari" or x=="trichur" or x=="vijayawada" or x=="south zone " or x=="pondi" or x=="TRIVANDRUM" else
                    
                    "east region" if x=="bhubaneshwar" or x=="Bhubaneswar" or x=="Bhubaneshwar" or x=="dhanbad" or x=="bhagalpur" or x=="bankura" or x=="siliguri " or x=="Siliguri" or x=="jamshedpur" 
                    or x=="ranchi" or x=="siliguri" or x=="angul" or x=="jowai" or x=="ganjam" or x=="chandrapur" 
                    or x=="patna" or x=="burdwan" or x=="east zone " or x=="nagari" or x=="durgapur" or x=="rayagada" 
                    or x=="howrah" or x=="bihar" or x=="baripada" or x=="guwahati" or x=="rourkela" or x=="haldia" or x=="muzaffarpur" or x=="muzzafarpur"
                    or x=="visakhaeast zonem" or x=="sambalpur" or x=="kharagpur" else
                    
                    "west region" if x=="Jaipur" or x=="jaipur" or x=="ahmedabad" or x=="nagpur" or x=="nashik" or x=="kolhapur" 
                    or x=="rajasthan" or x=="SADULPUR,RAJGARH,DISTT-CHURU,RAJASTHAN" or x=="bhiwadi" or x=="rajkot" or x=="daman and diu"
                    or x=="Daman and Diu" or x=="gandhi nagar" or x=="beawar" 
                    or x=="alwar" or x=="jodhpur" or x=="udaipur" or x=="aurangabad" or x=="neemrana" or x=="ahmednagar" or x=="gandhinagar" 
                    or x=="sadulpur" or x=="nanded" or x=="Nanded" or x=="bharuch" or x=="ratnagiri" or x=="Ratnagiri" or x=="jamnagar" or x=="kota" or x=="surat" or x=="vapi" 
                    or x=="pilani" or x=="PILANI" or x=="dausa" or x=="Dausa" or x=="latur (maharashtra )" or x=="latur (Maharashtra )" or x=="karad" or x=="bundi" or x=="vadodara" or x=="mohali" 
                    or x=="West Zone " or x=="jAipur" or x=="Jaipur" else
                    
                    "central region" if x=="indore" or x=="bhopal" or x=="raigarh" or x=="jabalpur" or x=="jagdalpur" or x=="Jagdalpur" or x=="gwalior" 
                    or x=="bareli" or x=="bilaspur" or x=="shahdol" or x=="bhopal " or x=="bhilai" or x=="singaruli" 
                    or x=="Central Zone " or x=="india" or x=="raipur" or x=="Central Zone " else
                    
                    "Abroad" if x=="australia" or x=="dubai" or x=="am" or x=="al jubail,saudi arabia" or x=="kalmar, sweden" 
                    or x=="jeddah saudi arabia" or x=="johannesburg" or x=="london" or x=="ras al khaimah" or x=="dammam" 
                    or x=="dAbroadmAbroad" or x=="LONDON" or x=="Australia" else x).value_counts()

"""With the above command we concatenate some rows with relevant row value.

Through this the unique row value get reduced.
"""

df['Specialization'].unique()

df['Specialization'].value_counts()

df['Specialization'].apply(lambda x : "chemical engineering" if x == "chemical engineering" or x == "polymer technology" else
                           
                           "computer science" if x=="information science" or x=="computer networking" or x=="computer and communication engineering" 
                           or x=="computer science" or x=="information & communication technology" or x=="electronics and computer engineering" 
                           or x=="computer science and technology" or x=="information science engineering" or x=="computer application"
                           or x=="computer engineering" else
                           
                           "mechanical engineering" if x=="mechanical engineering" or x=="mechanical & production engineering"
                           or x=="internal combustion engine" or x=="ceramic engineering" or x=="metallurgical engineering"
                           or x=="mechatronics" or x=="automobile/automotive engineering" or x=="mechanical and automation"
                           or x=="industrial & production engineering" or x=="industrial & management engineering" else
                           
                           "electronics and electrical engineering" if x=="electronics and electrical engineering" 
                           or x=="electronics & telecommunications" or x=="electrical engineering" or x=="electronics engineering"
                           or x=="electrical and power engineering" or x=="electronics" or x=="power systems and automation"
                           or x=="embedded systems technology" else
                           
                           "instrumentation and control engineering" if x=="instrumentation and control engineering"
                           or x=="electronics & instrumentation eng" or x=="electronics and instrumentation engineering"
                           or x=="applied electronics and instrumentation" or x=="instrumentation engineering" 
                           or x=="control and instrumentation engineering" else x).value_counts()

"""With the above command we concatenate some rows with relevant row value.

Through this the unique row value get reduced.
"""

df['Salary'].unique()

df['Salary'].value_counts()

"""With the above command, the unique row values shown."""

df['Designation'].unique()

df['Designation'].value_counts()

"""With the above command, the unique row values shown."""

# Univariate Analysis

# Salary

df['Salary'].hist(bins=150, figsize=(20,8))

"""Column salary histogram show that the graph is right skewed.

This column has many extreme low value outliers.
"""

df['Salary'].plot(kind="box", figsize=(10,10))

"""Both the whiskers are not of same length.

Upper whisker stretched more.

This column has so many ouliers.

The value get centered at 0.4.
"""

df['Salary'].plot(kind="kde", figsize=(10,10))

"""Column having bimodal data.

y-axis shows the relative frequency.
"""

sns.set(rc={'figure.figsize':(20,10)})
sns.countplot(x=df['Salary'])

"""Column having number of records by each category."""

# Specialization

df['Specialization'].hist(bins=150, figsize=(20,8))

"""The graph is right skewed and need to be normalized.

It has extreme low value outliers.
"""

a4_dims = (20,10)
fig, ax = plt.subplots(figsize=a4_dims)
l=sns.countplot(data=df, x='Specialization')
l.set_xticklabels(ax.get_xticklabels(),rotation=90);

"""The graph shows the records of each row by its unique value."""

# Job Location

df['JobCity'].hist(bins=150, figsize=(20,8))

"""The graph is right skewed and need to be normalized.

Column has many outliers.
"""

a4_dims = (50,20)
fig, ax = plt.subplots(figsize=a4_dims)
l=sns.countplot(data=df, x='JobCity')
l.set_xticklabels(ax.get_xticklabels(),rotation=90);

"""The graph is right skewed and need to be normalized.

Column has so many outliers with a large range of unique values.

The outlier value is extremely low till end.
"""

# Bivariate Analysis

from matplotlib.pyplot import figure

figure(num=None, figsize=(25, 10), dpi=80, facecolor='w', edgecolor='k')
plt.plot(df['CollegeState'],df['Salary'], 'r.')
plt.show()

"""This plot show the relation between the collegeState and salary.

Through this graph we can easily observe the impact of collegeState on the salary of a candidate.
"""

a4_dims = (13,6)
fig, ax = plt.subplots(figsize=a4_dims)
f=sns.barplot(data=df, x = 'Specialization', y='Salary', ci=None)
f.set_xticklabels(ax.get_xticklabels(),rotation=90);

"""This bar plot show the relation between the Specialization and salary.

Through this graph we can easily observe the impact of Specialization on the salary of a candidate.
"""

df.plot.scatter(x='Specialization', y='Salary', s=100, c='red', rot=90)

"""This scatterplot also shows the relation between the Specialization and salary.

Through this graph we can easily observe the impact of Specialization on the salary of a candidate.

The above barplot show the effect of a candidate's specialization on his/her salary.
"""

p_p_df=df[['collegeGPA','CollegeTier','CollegeCityTier','JobCity','Specialization','10percentage','12percentage','Salary']]
sns.pairplot(data= p_p_df,  hue = 'Salary')

"""Pairplot shows the different variety of graph plotting used for showing different columns relationships.

It shows the pair wise relationships of respective given columns.

This is used to take best suited variables to build Machine Learning Model.
"""

df.boxplot(rot=90, fontsize=15, figsize=(30,15), by ='Specialization', column =['Salary'], color='red')

"""Boxplot shows the different observations of different rows.

It shows the records to all the other respective row values.

**Research Questions**

Times of India article dated Jan 18, 2019 states that “After doing your Computer Science Engineering if you take up jobs as a Programming Analyst, Software Engineer, Hardware Engineer and Associate Engineer you can earn up to 2.5-3 lakhs as a fresh graduate.”


Test this claim with the data given to you.
Claiming here that the candidates who had done Computer Science Engineering and took jobs as a Programming Analyst, Software Engineer, Hardware Engineer and Associate Engineer you can earn up to 2.5LPA to 3LPA as a fresh graduate.
"""

df['DOJ']=pd.to_datetime(df['DOJ'])
# sample data
data=df[ (df.Specialization =='computer science & engineering') & (df.Salary >=250000) & (df.Salary<=300000) & 
        (df['DOJ'].dt.year == df['GraduationYear']) & ((df.Designation=='software engineer')  | 
                                                       (df.Designation=='programmer analyst')| 
                                                       (df.Designation=='associate software engineer')|
                                                       (df.Designation=='hardware engineer'))] 
data

data[['DOJ','GraduationYear']]

from scipy.stats import t, norm

# sample mean of salary 

np.mean(data['Salary'])

data['Salary'].size

import statistics

statistics.pstdev(df['Salary'])

# z_score for sampling distributions

def z_score(sample_size, sample_mean, pop_mean, pop_std):
    numerator = sample_mean - pop_mean
    denomenator = pop_std / sample_size**0.5
    return numerator / denomenator

    
# Defining the sample and population parameters

sample_mean= 290263.15789473685
sample_size= 19
pop_mean= 307699.8499249625 
pop_std= 212710.89280273343

# Calculating the z-score

z = z_score(sample_size, sample_mean, pop_mean, pop_std)
z

# function for calculation of t_score 

def tscore(sample_mean, pop_mean, sample_std, sample_size):
    numerator = sample_mean - pop_mean
    denominator = sample_std/sample_size**0.5
    return numerator/denominator

sample_std= np.std(data.Salary)
sample_std

t_sc = tscore(sample_mean,pop_mean, sample_std,sample_size)
t_sc

# one tail test
confidence_level = 0.9
alpha = 1-0.95
t_critical = t.ppf(1-alpha, df=18)
t_critical

# Two Tail - Calculating the z-critical value
alpha = 1 - confidence_level
z_critical = norm.ppf(1 - alpha/2)
z_critical

x_min = 230000
x_max = 350000

mean = pop_mean
std = pop_mean/(sample_size**0.5)

x = np.linspace(x_min, x_max, 100)
y = norm.pdf(x, mean, std)

plt.xlim(x_min, x_max)
# plt.ylim(0, 0.03)
import matplotlib.pyplot as plt
plt.plot(x, y)


t_critical_left = pop_mean + (-t_critical * std)

x1 = np.linspace(x_min, t_critical_left, 100)
y1 = norm.pdf(x1, mean, std)
plt.fill_between(x1, y1, color='purple')

plt.scatter(sample_mean, 0)
plt.axvline(mean, color = 'orange')
#plt.figure(figsize=(20,10))
plt.annotate("x_bar", (sample_mean, 0.02))
plt.figure(figsize=(20,10))
plt.show()

# In this case sample mean falls in the rejection region

# i.e. we Reject Null Hypothesis

# Ploting the sampling distribution with acceptance regions

# Defining the x minimum and x maximum
x_min = 230000
x_max = 350000


# Defining the sampling distribution mean and sampling distribution std
mean = pop_mean
std = pop_std / sample_size**0.5


# Ploting the graph and setting the x limits
x = np.linspace(x_min, x_max, 100)
y = norm.pdf(x, mean, std)
plt.xlim(x_min, x_max)
plt.plot(x, y)


# Computing the left and right critical values (Two tailed Test)
z_critical_left = pop_mean + (-z_critical * std)
z_critical_right = pop_mean + (z_critical * std)


# Shading the left rejection region
x1 = np.linspace(x_min, z_critical_left, 100)
y1 = norm.pdf(x1, mean, std)
plt.fill_between(x1, y1, color='orange')


# Shading the right rejection region
x2 = np.linspace(z_critical_right, x_max, 100)
y2 = norm.pdf(x2, mean, std)
plt.fill_between(x2, y2, color='green')


# Ploting the sample mean and concluding the results 
plt.scatter(sample_mean, 0)
plt.axvline(mean, color = 'black')
plt.annotate("x_bar", (sample_mean, 0.0005))
plt.figure(figsize=(20,10))
plt.show()

# In this case sample mean raises in the acceptance region
# i.e. here we fail to reject the Null Hypothesis

"""The above graphs show the proves to claim the researches as true or false.

We can see that the z-test claim that the research is true but on the otherhand t-test claim that the research is false.

The observation must be faulty due to some fluctuate values.
"""

# Conclusion using t test

if(np.abs(t_sc) > t_critical):
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")

# Conclusion using p test

p_value = 2 * (1.0 - norm.cdf(np.abs(t_sc)))

print("p_value = ", p_value)

if(p_value < alpha):
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")

"""As the result of the hypothesis testing we see that the claim is false.

The t-test and probability value i.e.,p_value claiming it as wrong.

Is there a relationship between gender and specialisation?

(i.e. Does the preference of Specialisation depend on the Gender?)
"""

df.groupby(by=['Gender','Specialization']).count()['ID']

df['Gender'].value_counts()['f']

df['Gender'].value_counts()['m']

"""As the result of the second research question we see that there is a relationship between Gender and specialization.

Some specialization or working field does not allow some candidates to work in that field due to some risks.

**Conclusion**

One have to deal with outliers as all the columns in the given data having a large number of outliers.

Have to find the relationships between the columns on which we have to give conclusion.

Data cleaning is much needed.

Columns need to be corrected whose having mixed values like string and datetime and integers.

Data column names should be changed for better understanding.
"""