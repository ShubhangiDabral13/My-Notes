# Feature Transformation

* Oftentimes, we have datasets in which different columns have different units – like one column can be in kilograms, while another column can be in centimeters. Furthermore, we can have columns like income which can range from 20,000 to 100,000, and even more; while an age column which can range from 0 to 100(at the most). Thus, Income is about 1,000 times larger than age.

* But how can we be sure that the model treats both these variables equally? When we feed these features to the model as is, there is every chance that the income will influence the result more due to its larger value. But this doesn’t necessarily mean it is more important as a predictor. So, to give importance to both Age, and Income, we need feature scaling.

Hence it is important to perform feature transformation.

*Feature transformation is simply a function that transforms features from one representation to another.*

>Note: Some algorithms(where we have to find global values) like linear regression, logistc regression feature transformation place a major role. Also for those 
algorithm where Euclidian distance is calculated like KNN, K-means there also feature transformation for algorithm performance.

## Types of Feature Transformation
* Standardization
* Min-Max/Normalization
* Scaling To Median And Quantiles
* Guassian Transformation 

### 1).Normalization and Standardization

* Standardization is another scaling technique where the values are centered around the mean with a unit standard deviation. This means that the mean of the attribute becomes zero and the resultant distribution has a unit standard deviation.

* Formula is:

                    z=(x-x_mean)/std  
                    
* Standardization can be helpful in cases where the data follows a Gaussian distribution. However, this does not have to be necessarily true. Standardization does not have a bounding range. So, even if you have outliers in your data, they will not be affected by standardization.


### 2).Min-Max/Normalization

* Normalization is a scaling technique in which values are shifted and rescaled so that they end up ranging between 0 and 1. It is also known as Min-Max scaling.
* Formula is:

        X_scaled = (X - X.min / (X.max - X.min)
        
* Normalization is good to use when you know that the distribution of your data does not follow a Gaussian distribution. This can be useful in algorithms that do not assume any distribution of the data like K-Nearest Neighbors and Neural Networks.


### 3).Robust Scaler
* It is used to scale the feature to median and quantiles Scaling using median and quantiles consists of substracting the median to all the observations, and then dividing by the interquantile difference. The interquantile difference is the difference between the 75th and 25th quantile:

* Formula is:

       IQR = 75th quantile - 25th quantile
       X_scaled = (X - X.median) / IQR



## How to transform non Gussian distrbution into Gussian distribution?
* Before converting the feature into Gaussian distribution it is quite important that we know wether the distrbution is Gussian or not for that we will use Q-Q Plot.

* If our features not in Gussian we will use Guassian Transformation to convert it into Gussian Distribution.

* Some machine learning algorithms like linear and logistic assume that the features are normally distributed. If a distribution is normally distrbuted then it will increase the  *Accuracy  and Performance* of the algorithm.


Gaussian Distribution are of different types:
* logarithmic transformation
* reciprocal transformation
* square root transformation
* exponential transformation (more general, you can use any exponent)
* boxcox transformation

### 1).Logarithmic Transformation
* The Logarithmic Transformation is a simple but controversial step in the analysis for positive continuous data measured on an interval scale. 
* Logarithmic transformation work well when data is right or left skewed.
* If any feature has zero value so doing logarithmic transformation may cause log(0) error so for that we use log1p tranformation.


            import numpy as np
            log_val = np.log1p(data)
            
            
### 2).Reciprocal transformation 
 * The reciprocal transformation is defined as the transformation of x to 1/x. 
 
 * The transformation has a little effect on the shape of the distribution, reversing the order of values with the same sign. 
 
 * The transformation can only be used for non-zero values.

        reciproc_val = 1/data
        
### 3).Square Root Transformation
* when one applies a square root transformation, the square root of every value is taken. 

* However, as one cannot take the square root of a negative number, if there are negative values for a variable a constant must be added to move the minimum value of the distribution above 0, preferably to 1.

      square_val = data**(1/2)
      
### 4).Exponential Transformation

* Exponential transformation has a reasonable effect on distribution shape; generally, we apply exponential transformation (power of two usually) to reduce left skewness.


       expon_val = data*(1/1.2)

### 5).Boxcox Transformation 
* Box-Cox Transformation is used to modify the distributional shape of a set of data to be more normally distributed so that tests and confidence limits that require normality can be appropriately used.

          from scipy.stats import boxcox
          Trans_val, Fitted_Val= boxcox(data)
