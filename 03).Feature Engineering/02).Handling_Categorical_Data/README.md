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
* One-Hot Encoding is the most common, correct way to deal with non-ordinal categorical data. 
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

