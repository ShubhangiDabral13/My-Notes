# Handling missing values

Data plays a major role in Machine Learning/Deep Learning algorithms. Before building any model our main focus is to do various feature engineering techinque so 
that we get the clean and well formatted data. 
Handling missing values is the first and foremost technique in Feature Engineering.

## How we get this missing values in the first place ?
There are various reason of getting missing values in the dataset. 
 * Human error.
 * Data collection error.
 * People hesitate to share personal information.
 * Device error.
 
 
## Why is it important to handle missing values?
 Is it impotant to handle missing values because
 * The absence of data reduces statistical power.
 * Data cannot be analysed properly.
 * It can reduce the representativeness of the samples.
 
 
 Before diving into different techniques to handle missing values. it is quite important to know different types of Missing values.
 
## Different types of missing values.
1) Missing Completely at Random — (MCAR).
2) Missing Not at Random — (MNAR).
3) Missing at Random — (MAR).

### 1).Missing Completely at Random(MCAR)
There’s no relationship between whether a data point is missing and any values in the data set (missing or observed) .The missing data are just a random 
subset of the data . The missingness is nothing to do with any other variable .



### 2).Missing Data Not At Random(MNAR)
Systematic missing Values. There is absolutely some relationship between the data missing and any other values, observed or missing, within the dataset.



### 3).Missing at Random — (MAR)
The missing data here is affected only by the complete (observed ) variables and not by the characteristics of the missing data itself. in other words ,
for a data point , to be missing is not related to the missing data, but it is related to some of ( or all ) the observed data


 
 
## How to handle missing values?
 Techniques to handle missing values are
 * Mean/median/Mode Replacement.
 * Random Sample Imputation.
 * Capturing NAN values with new Features.
 * End of Distribution Implementation.
 * Arbitrary Imputation.
 * Frequent Categories Imputation.
 
 
 
### 1).Mean/ Median/ Mode Imputation
*  In this imputation technique goal is to replace missing data with statistical estimates of the missing values. Mean, Median or Mode can be used as imputation
 value.
 * It is applied to numerical data
 
 
 * *Mean Implementation:* One of the technique is mean imputation in which the missing values are replaced with the mean value of the entire feature column. 
 In case of skewed data and also the data that contain outliers it may not be good idea to use mean imputation for replacing the missing values. Note that 
 imputing missing data with mean value can only be done with numerical data.
 
      
                                    df.fillna(df.mean())
                                    
                                    
                                    
                                    
 * *Median Implementation:* Another technique is median imputation in which the missing values are replaced with the median value of the entire feature column.
 When the data is skewed, or when it has outliers then it is good to consider using median value for replacing the missing values. Note that imputing missing
 data with median value can only be done with numerical data.

                                  df.fillna(df.median())




* *Mode Implementation:* Yet another technique is mode imputation in which the missing values are replaced with the mode value or most frequent value of the entire feature column.
When the data is skewed, it is good to consider using mode value for replacing the missing values. Note that imputing missing data with mode value can be done 
with numerical and categorical data.

### 2).Random Sample Imputation
* In random sample imputation, we take random observation from the dataset and we use it to fill the NaN values.
* It also assumes that the data are missing completely at random(MCAR).
* Works for all categorical and numeric data.

#### Advantages:
* Easy to implement.
* Less distortion in variance/standard-deviation.

#### Disadvantage:
* In every situation randomness won't work.

### 3).Capturing NaN Values With A New Features
* Here we make a new columns which will capture the NaN values.
* The new column will have 1 where the NaN value is present and 0 where it's not present.
* Works for both categorical and numeric data.

#### Advantage:
* Easy to implement.
* Captures the importance of missing value.

#### Disadvantage:
* Creating additional features(curse of dimensionality)

### 3).End of Distribution Imputation
* Here, we pick the values from end of the distribution and fill NaN values with these values.
* For a normal distribution values which are greater than and equal to mean + 3std* are the extreme values.
* This will remove the outliers from the data.
* Works for numeric data.

### 4).Arbitrary Value Imputation
* Arbitrary value imputation consists of replacing all occurrences of missing values (NA) within a variable with an arbitrary value. 
* The arbitrary value should be different from the mean or median and not within the normal values of the variable.
* Works for numeric data.

#### Advantages
* Easy to implement.
* Captures the importance of missingess if there is one.

#### Disadvantages
* Distorts the original distribution of the variable.
* If missingess is not important, it may mask the predictive power of the original variable by distorting its distribution.
* Hard to decide which value to use.

### 5).Frequent Categories Imputation.
* Frequent category imputation—or mode imputation—consists of replacing all occurrences of missing values (NA) within a variable with the mode, or the most frequent value.
* This method is suitable for numerical and categorical variables, but in practice, we use this technique with categorical variables.

#### Advantages
* Easy To implement
* Fater way to implement

#### Disadvantages
* Since we are using the more frequent labels, it may use them in an over respresented way, if there are many nan's.
* It distorts the relation of the most frequent label.



For more info click on this link: https://heartbeat.fritz.ai/hands-on-with-feature-engineering-techniques-imputing-missing-values-6c22b49d4060

