# Experiment Concepts Before Coding

This file explains the core concepts behind each experiment topic. It intentionally avoids experiment aims and abstracts. The purpose is to understand what each technique means, why it is used, and how to think about it before writing Python code.

---

## 1. Descriptive Statistical Analysis

### What is descriptive statistical analysis?

Descriptive statistical analysis is the process of summarizing and describing the main characteristics of a dataset. It does not predict future values and does not generalize from a sample to a population. It only explains what is present in the given data.

Before writing code for descriptive statistics, the main question is: "What does this data look like?"

For example, if we have a column of student marks, descriptive analysis helps us understand the average marks, middle marks, most common marks, spread of marks, and whether there are unusually high or low marks.

---

### Why do we use descriptive statistics?

We use descriptive statistics to quickly understand a dataset. Raw data may contain hundreds or thousands of values, and it is difficult to understand by just looking at rows. Descriptive statistics reduce the data into meaningful numerical summaries.

It helps answer questions such as:

1. What is the typical value?
2. How much variation exists?
3. Are the values symmetric or skewed?
4. Are there any extreme values?
5. Is mean or median a better summary?

---

### What are measures of central tendency?

Measures of central tendency describe the center or typical value of the data.

**Mean** is the arithmetic average.

`Mean = sum of all values / number of values`

Mean is easy to calculate but is affected by outliers. For example, if salaries are `20000, 22000, 25000, 300000`, the mean becomes high because of one very large salary.

**Median** is the middle value after sorting the data. It is more reliable when outliers are present.

**Mode** is the most frequently occurring value. It is useful for categorical data also.

For viva, remember: mean is sensitive to outliers, median is robust, and mode gives the most common value.

---

### What are measures of spread?

Measures of spread describe how far the data values are scattered.

**Range** is the difference between maximum and minimum value.

`Range = maximum - minimum`

**Variance** measures the average squared deviation from the mean.

**Standard deviation** is the square root of variance. It shows how much values usually deviate from the mean.

**Interquartile range** measures the spread of the middle 50 percent of the data.

`IQR = Q3 - Q1`

Spread is important because two datasets can have the same mean but very different variability.

---

### What are skewness and kurtosis?

**Skewness** measures asymmetry in the distribution.

1. Positive skew means the right tail is longer.
2. Negative skew means the left tail is longer.
3. Zero skew means the distribution is approximately symmetric.

**Kurtosis** measures tail heaviness or the presence of extreme values.

1. High kurtosis means heavy tails and more chance of outliers.
2. Low kurtosis means flatter distribution and fewer extreme values.

In code, skewness and kurtosis help us understand the shape of numerical data.

---

### What is a Z-score?

A Z-score tells how far a value is from the mean in terms of standard deviations.

`Z = (x - mean) / standard deviation`

If a value has a Z-score of 2, it is 2 standard deviations above the mean. If a value has a Z-score of -3, it is 3 standard deviations below the mean.

Generally, values with absolute Z-score greater than 3 are treated as possible outliers.

---

### What should be understood before coding descriptive analysis?

Before coding, identify:

1. Which numerical column is being analyzed.
2. Whether the goal is to find center, spread, shape, or outliers.
3. Whether the data has extreme values.
4. Whether mean or median is more appropriate.
5. Which plots can support the analysis, such as boxplot or histogram.

The code usually follows this logic: load data, select column, compute statistics, visualize, and interpret.

---

## 2. Data Preprocessing

### What is data preprocessing?

Data preprocessing is the process of converting raw data into a clean, consistent, and machine-learning-ready form. Real-world data is usually incomplete, inconsistent, duplicated, noisy, or not in numerical format. Preprocessing handles these issues before model building.

In simple terms, preprocessing prepares the data so that algorithms can understand and use it correctly.

---

### Why is preprocessing necessary?

Machine learning models depend strongly on data quality. If data contains missing values, text categories, or variables on different scales, models may produce poor or biased results.

For example, if one feature is salary ranging from 10000 to 100000 and another feature is age ranging from 18 to 60, distance-based algorithms may give more importance to salary only because its numerical scale is larger.

Preprocessing prevents such problems.

---

### What are missing values?

Missing values are absent or unknown values in a dataset. They may occur because of data entry errors, system failures, incomplete surveys, or unavailable information.

Common ways to handle missing values:

1. Remove rows with missing values.
2. Replace numerical missing values with mean, median, or a constant.
3. Replace categorical missing values with mode or a constant.
4. Use advanced imputation methods.

Mean is useful when data is symmetric. Median is better when outliers are present.

---

### What is imputation?

Imputation means replacing missing values with suitable estimated values.

For numerical columns:

1. Mean imputation replaces missing values with the average.
2. Median imputation replaces missing values with the middle value.
3. Constant imputation replaces missing values with a fixed value.

For categorical columns:

1. Most frequent imputation replaces missing values with the mode.
2. Constant imputation replaces missing values with a fixed category such as "Unknown".

In Python, `SimpleImputer` is commonly used for imputation.

---

### What is categorical encoding?

Categorical encoding converts text categories into numerical values because machine learning algorithms usually work with numbers.

**Label encoding** assigns each category an integer value.

Example:

`Low = 0, Medium = 1, High = 2`

It is suitable when categories have order.

**One-hot encoding** creates separate binary columns for each category.

Example:

If city has values Mumbai, Pune, Delhi, then one-hot encoding creates columns such as `City_Mumbai`, `City_Pune`, and `City_Delhi`.

It is suitable when categories do not have natural order.

---

### What is feature scaling?

Feature scaling changes numerical values to a common scale. It is important for algorithms that depend on distances or gradients.

**Standardization** transforms data to have mean 0 and standard deviation 1.

`z = (x - mean) / standard deviation`

It is useful when data is approximately normally distributed.

**Normalization** transforms data into a fixed range, commonly 0 to 1.

`x_scaled = (x - minimum) / (maximum - minimum)`

It is useful when values need to be bounded within a range.

---

### What should be understood before coding preprocessing?

Before coding, identify:

1. Which columns are numerical.
2. Which columns are categorical.
3. Which values are missing.
4. Which categorical variables need label encoding or one-hot encoding.
5. Which numerical variables need scaling.
6. Which column is the target variable.

The usual coding flow is: load data, inspect missing values, impute, encode, scale, split features and target, and prepare for modeling.

---

## 3. T-Test and Inferential Statistics

### What is inferential statistics?

Inferential statistics is used to make conclusions about a population using sample data. Since collecting data from an entire population is often difficult, we collect a sample and use statistical tests to make decisions.

For example, instead of testing every student in a university, we may test a sample of students and infer whether a teaching method improves marks.

---

### What is hypothesis testing?

Hypothesis testing is a formal statistical method for making decisions. It begins with two statements:

**Null hypothesis H0:** There is no significant difference or no effect.

**Alternative hypothesis H1:** There is a significant difference or effect.

The test calculates a test statistic and p-value. The p-value helps decide whether to reject the null hypothesis.

Decision rule:

1. If p-value is less than significance level, reject H0.
2. If p-value is greater than or equal to significance level, fail to reject H0.

The common significance level is 0.05.

---

### What is a t-test?

A t-test is a statistical test used to compare means. It is commonly used when the sample size is small and the population standard deviation is unknown.

The t-test checks whether the observed difference in means is large enough to be considered statistically significant.

For example, a t-test can check whether average response time before optimization is significantly different from average response time after optimization.

---

### What are the types of t-test?

**One-sample t-test:**  
Compares the mean of one sample with a known or assumed population mean.

Example: Testing whether average daily electricity consumption is different from 11 kWh.

**Independent two-sample t-test:**  
Compares the means of two independent groups.

Example: Comparing average marks of students from two different classes.

**Paired t-test:**  
Compares two related measurements from the same subjects.

Example: Comparing patient temperature before and after taking medicine.

---

### What is a p-value?

A p-value is the probability of getting the observed result, or a more extreme result, assuming the null hypothesis is true.

If the p-value is small, it means the observed result is unlikely under the null hypothesis. Therefore, we reject the null hypothesis.

For viva, remember:

1. p-value less than 0.05 means statistically significant.
2. p-value greater than or equal to 0.05 means not statistically significant.
3. A p-value does not measure the size of the effect; it only helps test significance.

---

### What assumptions are important for t-test?

Important assumptions include:

1. Data should be numerical.
2. Observations should be randomly selected.
3. Data should be approximately normally distributed, especially for small samples.
4. For independent t-test, groups should be independent.
5. For paired t-test, observations should be matched pairs.

If assumptions are badly violated, the t-test result may be unreliable.

---

### What should be understood before coding a t-test?

Before coding, identify:

1. What is being compared.
2. Whether there is one sample, two independent samples, or paired samples.
3. What are H0 and H1.
4. What significance level is used.
5. Which function is appropriate: `ttest_1samp`, `ttest_ind`, or `ttest_rel`.
6. How to interpret the p-value.

The code should not just calculate the t-test. It should also include a clear interpretation.

---

## 4. Data Visualization and Exploratory Data Analysis

### What is data visualization?

Data visualization is the graphical representation of data. It helps us see patterns, trends, distributions, relationships, and outliers that may not be clear from tables.

Visualization is a major part of exploratory data analysis because it helps understand data before modeling.

---

### What is exploratory data analysis?

Exploratory Data Analysis, or EDA, is the process of investigating a dataset using statistics and visualizations. It is performed before model building to understand the structure and behavior of the data.

EDA helps answer:

1. What variables are present?
2. What are their data types?
3. Are values missing?
4. What are the distributions?
5. Are variables related?
6. Are there outliers?

---

### What is univariate visualization?

Univariate visualization analyzes one variable at a time.

Examples:

1. Histogram for numerical distribution.
2. Count plot for categorical frequency.
3. Boxplot for spread and outliers.
4. Density plot for smooth distribution.

For example, a histogram of age shows whether the dataset contains mostly young, middle-aged, or older people.

---

### What is bivariate and multivariate visualization?

Bivariate visualization studies the relationship between two variables.

Example: Scatter plot of total bill and tip.

Multivariate visualization studies more than two variables at the same time.

Example: Scatter plot of total bill and tip, with color representing gender and size representing group size.

These visualizations help identify patterns, correlations, clusters, and group differences.

---

### What are common visualization plots and their use?

**Count plot:**  
Shows frequency of categories. Example: number of male and female passengers.

**Histogram:**  
Shows distribution of numerical data. Example: distribution of age.

**Boxplot:**  
Shows median, quartiles, spread, and outliers.

**Scatter plot:**  
Shows relationship between two numerical variables.

**Pairplot:**  
Shows pairwise relationships among multiple variables.

**Heatmap:**  
Shows correlation or matrix values using colors.

**Violin plot:**  
Combines boxplot and density distribution.

**Bar plot:**  
Compares aggregated values across categories.

---

### What is correlation heatmap?

A correlation heatmap visually shows correlation values between numerical variables. Dark or intense colors usually indicate strong relationships.

Correlation values range from -1 to +1:

1. +1 means perfect positive correlation.
2. -1 means perfect negative correlation.
3. 0 means no linear correlation.

For example, in the tips dataset, total bill and tip may show positive correlation because higher bills often result in higher tips.

---

### What should be understood before coding visualization?

Before coding, identify:

1. Which variables are categorical.
2. Which variables are numerical.
3. Whether the goal is distribution, comparison, relationship, or outlier detection.
4. Which plot is suitable for the data type.
5. What interpretation should be written after the plot.

The purpose of visualization is not only to draw graphs, but to explain what the graphs reveal.

---

## 5. Evaluation Metrics

### What are evaluation metrics?

Evaluation metrics are numerical measures used to judge how well a model performs. Different tasks require different metrics. Classification, regression, and clustering cannot be evaluated using the same measures.

Before writing code, the main question is: "What type of model am I evaluating?"

---

### What are regression metrics?

Regression predicts continuous numerical values. Regression metrics measure prediction error.

**Mean Absolute Error, MAE:**  
Average absolute difference between actual and predicted values.

`MAE = average of absolute errors`

It is easy to interpret because it is in the same unit as the target.

**Mean Squared Error, MSE:**  
Average of squared errors. It penalizes large errors strongly.

**Root Mean Squared Error, RMSE:**  
Square root of MSE. It is also in the same unit as the target.

**R2 score:**  
Measures how much variation in the target is explained by the model. A value closer to 1 is better.

---

### How do outliers affect regression metrics?

Outliers can greatly increase MSE and RMSE because errors are squared. MAE is less affected than MSE and RMSE.

For example, if most prediction errors are small but one prediction error is extremely large, RMSE increases sharply.

This is why regression metric comparison helps us understand model sensitivity to large errors.

---

### What are classification metrics?

Classification predicts class labels. Common classification metrics are:

**Accuracy:**  
Proportion of total correct predictions.

**Precision:**  
Out of predicted positive cases, how many are actually positive.

**Recall:**  
Out of actual positive cases, how many are correctly predicted.

**F1-score:**  
Harmonic mean of precision and recall.

**Confusion matrix:**  
Table showing true positives, true negatives, false positives, and false negatives.

**ROC-AUC:**  
Measures how well the model separates classes.

---

### Why is accuracy not always enough?

Accuracy can be misleading when the dataset is imbalanced.

Example:

If 99 percent of transactions are genuine and only 1 percent are fraud, a model that predicts all transactions as genuine gets 99 percent accuracy. But it detects no fraud.

In such cases, recall, precision, F1-score, confusion matrix, and ROC-AUC are more meaningful.

---

### What are clustering metrics?

Clustering is unsupervised learning, so true labels may not be available. Clustering metrics check how compact and separated clusters are.

**Silhouette score:**  
Measures how similar a point is to its own cluster compared with other clusters. Higher is better.

**Davies-Bouldin score:**  
Measures cluster similarity. Lower is better.

**Calinski-Harabasz score:**  
Measures cluster separation and compactness. Higher is better.

**Adjusted Rand Index:**  
Compares cluster labels with actual labels if true labels are available.

---

### What is cross-validation?

Cross-validation evaluates a model on multiple train-test splits. It gives a more reliable estimate of model performance than a single split.

In K-fold cross-validation, data is divided into K parts. The model is trained on K-1 parts and tested on the remaining part. This is repeated K times, and the average score is used.

For example, in 5-fold cross-validation, the model is trained and tested 5 times.

---

### What should be understood before coding evaluation metrics?

Before coding, identify:

1. Whether the task is regression, classification, or clustering.
2. Which metric is suitable for the task.
3. Whether the dataset is balanced or imbalanced.
4. Whether predictions are class labels or probabilities.
5. Whether cross-validation is needed.
6. How to interpret each metric.

The goal is not only to print metric values, but to explain model performance.

---

## 6. SMOTE and Class Imbalance

### What is class imbalance?

Class imbalance occurs when one class has many more observations than another class. This is common in fraud detection, disease detection, spam detection, and rare event prediction.

Example:

In a credit card dataset, 99.8 percent transactions may be genuine and only 0.2 percent may be fraudulent.

The problem is that a model may learn the majority class very well and ignore the minority class.

---

### Why is class imbalance harmful?

Class imbalance is harmful because models tend to favor the majority class. The model may show high accuracy but fail to identify the minority class, which is often the most important class.

For example, in cancer detection, missing a malignant case is more serious than misclassifying a benign case. Therefore, recall and F1-score become important.

---

### What are common methods to handle class imbalance?

Common methods are:

1. Random oversampling.
2. Random undersampling.
3. SMOTE.
4. Class weights.
5. Better evaluation metrics such as recall and F1-score.

**Oversampling** increases minority class records.

**Undersampling** reduces majority class records.

**SMOTE** creates synthetic minority class records.

---

### What is SMOTE?

SMOTE stands for Synthetic Minority Over-sampling Technique. It creates new synthetic samples for the minority class instead of simply duplicating existing minority records.

SMOTE works by:

1. Selecting a minority class sample.
2. Finding its nearest minority class neighbors.
3. Choosing one of those neighbors.
4. Creating a new point between the sample and the neighbor.

This helps the model learn a broader decision boundary for the minority class.

---

### Why is SMOTE better than simple duplication?

Simple oversampling duplicates existing minority records. This can cause overfitting because the model sees the same records repeatedly.

SMOTE creates new synthetic records, so it adds variety to the minority class. This usually helps the classifier generalize better.

However, SMOTE should be applied only to the training data, not the test data. Applying SMOTE before train-test split causes data leakage.

---

### How do we compare models before and after SMOTE?

We train one model on the original imbalanced training data and another model on the SMOTE-balanced training data. Then both models are tested on the same original test data.

Metrics to compare:

1. Confusion matrix.
2. Accuracy.
3. Precision.
4. Recall.
5. F1-score.
6. ROC-AUC.

Often, recall improves after SMOTE because the model detects more minority class samples.

---

### What should be understood before coding SMOTE?

Before coding, identify:

1. Which column is the target class.
2. Whether the classes are imbalanced.
3. Which class is the minority class.
4. Which metrics are more important.
5. Whether the train-test split is done before applying SMOTE.
6. Whether scaling is needed before modeling.

The correct flow is: split data, scale if needed, apply SMOTE only on training data, train model, test on original test data, and compare metrics.

---

## 7. DBSCAN

### What is DBSCAN?

DBSCAN stands for Density-Based Spatial Clustering of Applications with Noise. It is an unsupervised learning algorithm used for clustering and outlier detection.

DBSCAN groups points that are close to each other in dense regions. Points that do not belong to any dense region are treated as noise or outliers.

Unlike K-Means, DBSCAN does not require the number of clusters in advance.

---

### What is the basic idea behind DBSCAN?

The basic idea is density. A cluster is a region where many points are close together. If a point has enough neighboring points within a specified radius, it belongs to a dense region.

DBSCAN uses two main parameters:

1. `eps`: Radius around a point.
2. `min_samples`: Minimum number of points required inside that radius.

If enough points exist within the eps neighborhood, DBSCAN forms or expands a cluster.

---

### What are core points, border points, and noise points?

**Core point:**  
A point is a core point if it has at least `min_samples` points within distance `eps`.

**Border point:**  
A point is a border point if it does not have enough neighbors to be a core point but lies within the neighborhood of a core point.

**Noise point:**  
A point is a noise point if it is neither a core point nor a border point. Noise points are marked as outliers.

In DBSCAN output, noise points usually receive label `-1`.

---

### Why is DBSCAN useful?

DBSCAN is useful because:

1. It can find clusters of arbitrary shape.
2. It does not require the number of clusters beforehand.
3. It identifies outliers naturally.
4. It works well when clusters are dense and separated by sparse regions.

For example, DBSCAN can cluster circular data where K-Means may fail because K-Means assumes roughly spherical clusters.

---

### What are the limitations of DBSCAN?

DBSCAN has some limitations:

1. It is sensitive to `eps` and `min_samples`.
2. It struggles when clusters have very different densities.
3. It can perform poorly in high-dimensional data because distance becomes less meaningful.
4. Feature scaling is important because distance calculation depends on scale.

Therefore, standardization is usually done before applying DBSCAN.

---

### How do we interpret DBSCAN results?

DBSCAN returns cluster labels for each data point.

1. Label `0`, `1`, `2`, etc. represent clusters.
2. Label `-1` represents noise or outliers.
3. The number of clusters is the number of unique labels excluding `-1`.
4. The number of outliers is the count of points labeled `-1`.

Visualization using scatter plots or PCA helps understand the cluster structure.

---

### What should be understood before coding DBSCAN?

Before coding, identify:

1. Which features should be used for clustering.
2. Whether features need scaling.
3. Suitable values for `eps` and `min_samples`.
4. How many points are marked as noise.
5. Whether the clusters make practical sense.

The coding flow is: load data, select features, scale data, apply DBSCAN, count clusters and noise points, visualize results, and interpret.

---

## 8. k-Nearest Neighbors Anomaly Detection

### What is k-Nearest Neighbors?

k-Nearest Neighbors, or k-NN, is a distance-based method. It finds the `k` closest points to a given data point. Although k-NN is commonly used for classification and regression, it can also be used for anomaly detection.

In anomaly detection, the idea is simple: normal points usually have nearby neighbors, while anomalies are far from other points.

---

### How does k-NN detect anomalies?

k-NN anomaly detection uses neighbor distances.

Steps:

1. Choose the value of `k`.
2. For each point, find its k nearest neighbors.
3. Calculate the distance to the kth nearest neighbor.
4. Points with unusually large kth-neighbor distances are considered anomalies.

If a point is far from its neighbors, it is likely to be unusual.

---

### Why is scaling important in k-NN?

k-NN depends on distance calculations. If features have different scales, the feature with larger numerical range dominates the distance.

Example:

If income ranges from 10000 to 100000 and age ranges from 18 to 60, income will dominate distance unless scaling is applied.

Therefore, standardization or normalization is usually required before applying k-NN.

---

### How is the anomaly threshold selected?

The anomaly threshold decides which points are considered outliers.

Common methods:

1. Use a percentile, such as the 90th or 95th percentile of kth-neighbor distances.
2. Use mean plus two standard deviations.
3. Choose a threshold based on domain knowledge.

Points with distance above the threshold are marked as anomalies.

---

### How is k-NN different from DBSCAN?

k-NN anomaly detection and DBSCAN both use distance, but their logic is different.

1. k-NN focuses on how far each point is from its nearest neighbors.
2. DBSCAN focuses on whether a point belongs to a dense region.
3. k-NN needs an anomaly threshold.
4. DBSCAN identifies noise automatically using `eps` and `min_samples`.
5. k-NN is mainly anomaly scoring, while DBSCAN is clustering with noise detection.

---

### What should be understood before coding k-NN anomaly detection?

Before coding, identify:

1. Which numerical features represent behavior.
2. Whether features must be scaled.
3. What value of `k` should be used.
4. How to define the anomaly threshold.
5. How to visualize anomalies.
6. Whether detected anomalies make practical sense.

The coding flow is: load data, select features, scale if needed, fit nearest-neighbor model, compute kth distances, set threshold, mark anomalies, and visualize.

---

## 9. Time Series Analysis and Forecasting

### What is a time series?

A time series is a sequence of observations collected over time. The order of observations matters because current values may depend on past values.

Examples:

1. Monthly sales.
2. Daily temperature.
3. Yearly population.
4. Hourly website traffic.
5. Stock prices.

Time series analysis is different from normal tabular analysis because time dependency is important.

---

### What is time series forecasting?

Time series forecasting predicts future values using past time-based observations.

For example, a business can forecast next month's product demand using previous monthly demand.

Forecasting is useful in inventory planning, weather prediction, finance, electricity demand, and sales planning.

---

### What are the components of a time series?

A time series may contain the following components:

**Trend:**  
Long-term increase or decrease in the data.

**Seasonality:**  
Pattern that repeats at fixed intervals.

**Cyclical variation:**  
Long-term rise and fall that does not have a fixed period.

**Irregular component:**  
Random noise or unpredictable variation.

Understanding these components helps select the correct forecasting method.

---

### What is time series decomposition?

Time series decomposition separates a series into trend, seasonal, and residual components.

There are two common models:

**Additive model:**  
`Observed = Trend + Seasonal + Residual`

Used when seasonal variation is roughly constant.

**Multiplicative model:**  
`Observed = Trend * Seasonal * Residual`

Used when seasonal variation changes with the level of the series.

Decomposition helps us understand whether changes are due to long-term trend, repeating seasonal behavior, or random noise.

---

### What is moving average smoothing?

Moving average smoothing reduces random fluctuations by averaging nearby values.

For a 3-period moving average:

`MA = (current value + previous value + value before previous) / 3`

It helps reveal the underlying trend.

Example:

If monthly demand is 250, 235, and 200, the 3-month moving average is:

`(250 + 235 + 200) / 3 = 228.33`

---

### What is Simple Exponential Smoothing?

Simple Exponential Smoothing, or SES, is a forecasting method that gives more weight to recent observations and less weight to older observations.

Formula:

`Forecast_new = alpha * actual_current + (1 - alpha) * previous_forecast`

Where `alpha` is the smoothing constant between 0 and 1.

If alpha is high, the forecast reacts quickly to recent changes. If alpha is low, the forecast is smoother and reacts slowly.

SES is best suited for data without strong trend or seasonality.

---

### What is ARIMA?

ARIMA stands for AutoRegressive Integrated Moving Average. It is used for forecasting stationary time series.

ARIMA has three parts:

1. `p`: Autoregressive order, which uses past values.
2. `d`: Differencing order, which removes trend and makes the series stationary.
3. `q`: Moving average order, which uses past forecast errors.

ARIMA is written as `ARIMA(p, d, q)`.

Before using ARIMA, we usually check whether the series is stationary.

---

### What is stationarity?

A time series is stationary if its mean, variance, and pattern remain stable over time.

Many time series models require stationarity. If a series has a strong trend or changing variance, it is usually non-stationary.

Methods to make a series stationary include:

1. Differencing.
2. Log transformation.
3. Removing trend.
4. Removing seasonality.

---

### What are time series evaluation metrics?

Forecasting models are evaluated by comparing actual and predicted values.

**MAE:**  
Average absolute error.

**RMSE:**  
Square root of average squared error. It penalizes large errors more.

**MAPE:**  
Average percentage error.

**MASE:**  
Compares model error with naive forecast error.

These metrics help judge whether the forecast is accurate enough for practical use.

---

### What should be understood before coding time series analysis?

Before coding, identify:

1. Which column represents time.
2. Which column contains the observed value.
3. Whether the data has trend or seasonality.
4. Whether the index is properly converted to dates.
5. Whether decomposition, smoothing, regression, or ARIMA is appropriate.
6. Which evaluation metric should be used.

The coding flow is: load time series, set time index, plot data, inspect trend and seasonality, apply decomposition or smoothing, forecast, plot results, and evaluate.

---

## Quick Revision Table

| Experiment Topic | Main Concept | Main Question Before Coding |
|---|---|---|
| Descriptive Statistical Analysis | Summarize data using center, spread, shape, and outliers | What does the data look like? |
| Data Preprocessing | Clean and transform raw data for modeling | Is the data usable by algorithms? |
| T-Test | Test whether mean differences are statistically significant | Is the observed difference real or due to chance? |
| Data Visualization | Understand data through graphs | What patterns can be seen visually? |
| Evaluation Metrics | Measure model performance | How good is the model? |
| SMOTE | Handle class imbalance using synthetic minority samples | Is the minority class being learned properly? |
| DBSCAN | Density-based clustering and noise detection | Which points form dense clusters and which are noise? |
| k-NN Anomaly Detection | Distance-based outlier detection | Which points are far from their neighbors? |
| Time Series | Analyze and forecast time-ordered data | What pattern exists over time and what may happen next? |

