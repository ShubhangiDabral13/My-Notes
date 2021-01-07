# Handling Categorical Data 

## Categorical Data
Categorical data is simply information aggregated into groups rather than being in numeric formats, such as Gender, Sex or Education Level. 


### Types Of Categorical Data
* Nominal

  Nominal data simply names something without assigning it to an order in relation to other numbered objects or pieces of data. An example of nominal data might be   a "pass" or "fail" classification for each student's test result.

* Ordinal

  Ordinal data, unlike nominal data, involves some order; ordinal numbers stand in relation to each other in a ranked fashion. For example, suppose you receive a   survey from your favorite restaurant that asks you to provide feedback on the service you received. You can rank the quality of service as "1" for poor, "2" for   below average, "3" for average, "4" for very good and "5" for excellent. The data collected by this survey are examples of ordinal data. Here the numbers           assigned have an order or rank; that is, a ranking of "4” is better than a ranking of “2.”
  
  
## Different ways for handling Categorical Data

### 1).One Hot Encoding
* One-Hot Encoding is the most common, correct way to deal with *non-ordinal categorical data*. 
* It simply creates additional features based on the number of unique values in the categorical feature.
* Every unique value in the category will be added as a feature.

#### We apply One-Hot Encoding when:
* The categorical feature is not ordinal.
* The number of categorical features is less so one-hot encoding can be effectively applied.

#### Advantage
* Easy to implement.
* Works well with few features.

#### Disadvantage
* As features increases hence it suffer from curse of dimensionality.

### 2). Ordinal Number Encoding 
* You use ordinal encoding to preserve order of categorical data i.e. cold, warm, hot; low, medium, high.
* In ordinal encoding, each unique category value is assigned an integer value.
* For example, “red” is 1, “green” is 2, and “blue” is 3.

#### Advantage
* Easy to implement.
* Maintain the order of categories.

#### Disadvantage
*  it requires coding to tell ordinal values.

### 3).Count Or Frequency Encoding
* Replace the categories by the count of the observations that show that category in the dataset. 
* Similarly, we can replace the category by the frequency -or percentage- of observations in the dataset. 
* That is, if 10 of our 100 observations show the color blue, we would replace blue by 10 if doing count encoding, or by 0.1 if replacing by the frequency.


#### Advantages
* Easy To Use.
* Not increasing feature space.

##### Disadvantages
* It will provide same weight if the frequencies are same.


### 4).Target Guided Ordinal Encoding
* Ordering the labels according to the target.
* Replace the labels by the joint probability of being 1 or 0.


### 5).Mean Encoding
