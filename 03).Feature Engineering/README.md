
## Feature Engineering 

* [Types of Enodings](https://github.com/ShubhangiDabral13/My-Notes#Types_of_Encodings)
* [Why we feature scaling?](https://github.com/ShubhangiDabral13/My-Notes#Why-we-do-feature-scaling?)
### Types of Encodings 
    A. Nnominal Encodings : the features consist of different catergories like sex: male of female.
    
        A.1 One hot Encoding
   ![feature_eng1](https://user-images.githubusercontent.com/44902363/95049725-f74b3a00-0707-11eb-9f31-4f75c1da17f5.png)

        * Total number of feaures in ONE HOT ENCODING IS total number of categories -1
        * Disadvantage of One Hot Encoding is that if there is large number of categories then column 
          number will also increase and this result in Curse Of Dimensionality.
        
        A.2 One Hot Encodings With many categorical values
        
        * This technique is because of research done during comptiton called KDD Orange. 
        * And it is useful when we have large number of categories about 50 or more.
        * In this we look for the top most fequent occuring categories in the particular
        column and apply one hot encoding to that top categories. 
        * Like in KDD orange one hot encoding is applied to top 10 frequent categories.
        
        
        
        A.3 Mean Encodings
   ![feature_eng4](https://user-images.githubusercontent.com/44902363/95059273-47c99400-0716-11eb-8dc8-a6e59a8db824.png)
        
        * In this we will calculate the mean of all the categories in a particular features with respect to the 
        output columns and then replace the features with it respective mean.
        * Had it been the ordinal data then we would have done Target guided Ordinal Encodings where we would 
        have assigned rank to the means of the categories and then replaced the ctegories with the rank not with
        the means.
        * Advantage of Mean Encodings is that if we have suppose a features with 100 categories now for that if we 
        use one hot encoding then we will have to create 99 columns so to convert those categories to
        float/integers we will Mean Encoding.
        

  ###
    B. Ordinal Encodings : consist of features which consist of different categories whose rank also matter :
    1st,2nd and 3rd.
     
        B.1  Label Encoding
   ![feature_eng2](https://user-images.githubusercontent.com/44902363/95050931-07641900-070a-11eb-814f-ff35872c2415.png)
   
   
        B.2 Target guided Ordinal Encodings
![feature_eng3](https://user-images.githubusercontent.com/44902363/95056859-f10e8b00-0712-11eb-9db7-8ac5e4ef1cba.png)

        * In this we will consider a column which have different categories and the output column. Then we will 
        calcuate the  mean of each of the categories (whether the ouput is 1 or 0) and assign rank on the 
        basis of the means.
        * As the data above is ordinal so we are giving label on the basis of rank(i.e mean) had it been the 
        nominal data we  were not able to know label cause we don't know which categories are important. 
        So for that we will use Mean Encodings.
        
        
### Why we do feature scaling?
    Feature scaling is a step of Data Pre-Processing which is applied to independent variables or features of data. 
    It basically helps to normalise the data within a particular range. Sometimes it speed up the calculations of 
    algorithms also.

#### Algorithms that require feature scaling 

    * Algorthms which have gradient desent.
           * Linear Regression : We do feature scaling then our cofficent might be close to global minima and also 
           we will very quickly converge to gobal minina.
           * Neural Networks.
    * All supervised and unsupervised learning which uses Euclidian Distances.
          * K-means clustering
          * K Nearest Neighbors
        If we Feature Scaling then the euiclidain distance between the points will decrease and our algorithms 
        will work fast.
        
#### Algorithms that does not require features scaling
    
    * Decision Tree
    * Random Forest
    * XGBoost
      
    Whether regression or classification problem we don't need to perform feature scaling cause the number of 
    branches remain same irrespective of the number of features.
    
        
