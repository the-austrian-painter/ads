# Data Science Concepts for Viva

This document is organized module-wise and topic-wise. Each topic is written as a viva-style question followed by an answer that can be understood, remembered, and spoken in an academic manner.

---

## Module 1: Introduction to Data Science

### Q1. What is Data Science?

**Answer:**  
Data Science is an interdisciplinary field that uses scientific methods, statistics, mathematics, programming, and domain knowledge to extract meaningful insights from data. It involves collecting data, preparing it, analyzing patterns, building models, and using the results for decision-making.

In simple terms, Data Science converts raw data into useful knowledge.

**Example:**  
An e-commerce company can use Data Science to analyze customer purchase history and recommend products that a customer is likely to buy.

---

### Q2. Why is Data Science important?

**Answer:**  
Data Science is important because modern organizations generate a large amount of data from websites, mobile applications, sensors, transactions, and social media. This data is valuable only when it is analyzed properly. Data Science helps organizations discover patterns, predict future behavior, automate decisions, and improve efficiency.

**Example:**  
A bank can use Data Science to detect fraudulent transactions by identifying unusual spending patterns.

---

### Q3. What is the Data Science process?

**Answer:**  
The Data Science process is a systematic sequence of steps used to solve a data-driven problem. The common steps are:

1. **Problem definition:** Understand the business or research problem.
2. **Data collection:** Gather relevant data from databases, files, APIs, sensors, or surveys.
3. **Data preparation:** Clean missing, duplicate, noisy, and inconsistent data.
4. **Data exploration:** Use statistics and visualization to understand patterns and relationships.
5. **Feature engineering:** Create or transform variables to improve model performance.
6. **Model building:** Apply machine learning or statistical models.
7. **Model evaluation:** Check model performance using suitable metrics.
8. **Deployment:** Use the model in a real-world system.
9. **Monitoring:** Continuously check whether the model remains accurate over time.

**Example:**  
For house price prediction, the process begins with collecting house data, cleaning it, exploring relationships such as area versus price, training a regression model, evaluating error, and finally using the model to predict prices for new houses.

---

### Q4. What motivates the use of Data Science techniques?

**Answer:**  
Data Science techniques are needed because modern data is large in volume, high in dimensions, and complex in nature.

**Volume:**  
Data is generated in very large quantities. Manual analysis becomes impossible.

**Dimensions:**  
Datasets may contain many features or variables. For example, a medical dataset may contain age, blood pressure, glucose level, cholesterol, BMI, and many more attributes.

**Complexity:**  
Data may be structured, semi-structured, or unstructured. It may contain missing values, noise, outliers, images, text, or time-dependent observations.

Data Science provides mathematical and computational methods to handle these challenges efficiently.

**Example:**  
Social media platforms generate huge volumes of text, images, likes, comments, and shares. Data Science helps analyze user behavior and recommend relevant content.

---

### Q5. What are common Data Science tasks?

**Answer:**  
Common Data Science tasks include:

1. **Classification:** Assigning data into predefined classes.  
   Example: Classifying an email as spam or not spam.

2. **Regression:** Predicting a continuous numerical value.  
   Example: Predicting house price.

3. **Clustering:** Grouping similar data points without predefined labels.  
   Example: Segmenting customers based on spending behavior.

4. **Anomaly detection:** Identifying unusual observations.  
   Example: Detecting fraudulent credit card transactions.

5. **Recommendation:** Suggesting items based on user preferences.  
   Example: Product recommendation on Amazon.

6. **Time series forecasting:** Predicting future values using past time-based data.  
   Example: Forecasting weather or sales demand.

7. **Descriptive analysis:** Summarizing what has happened.  
   Example: Monthly sales report.

8. **Predictive analysis:** Predicting what may happen in the future.  
   Example: Predicting customer churn.

---

### Q6. What is data preparation?

**Answer:**  
Data preparation is the process of transforming raw data into a clean and usable form for analysis or modeling. It is one of the most important steps in Data Science because poor-quality data leads to poor results.

Important data preparation steps include:

1. Handling missing values.
2. Removing duplicate records.
3. Correcting inconsistent values.
4. Detecting and treating outliers.
5. Encoding categorical variables.
6. Scaling numerical features.
7. Splitting data into training and testing sets.
8. Creating new useful features.

**Example:**  
If a dataset contains missing age values, they may be replaced by the mean or median age before building a model.

---

### Q7. What is modeling in Data Science?

**Answer:**  
Modeling is the process of applying statistical or machine learning algorithms to data in order to learn patterns and make predictions or decisions. A model is trained using existing data and then used to make predictions on new data.

Common modeling techniques include:

1. Linear Regression.
2. Logistic Regression.
3. Decision Trees.
4. K-Nearest Neighbors.
5. K-Means Clustering.
6. DBSCAN.
7. ARIMA for time series.

**Example:**  
A Logistic Regression model can be used to predict whether a student will pass or fail based on attendance, marks, and study hours.

---

### Q8. What is the difference between Data Science and Data Analytics?

**Answer:**  
Data Analytics mainly focuses on examining existing data to understand past and present trends. Data Science is broader and includes data analytics, machine learning, prediction, automation, and model deployment.

| Basis | Data Analytics | Data Science |
|---|---|---|
| Main focus | Interpreting existing data | Extracting insights and building predictive models |
| Time orientation | Mostly past and present | Past, present, and future |
| Techniques | Reports, dashboards, descriptive statistics | Statistics, machine learning, AI, big data tools |
| Output | Insights and summaries | Predictions, models, automated decisions |
| Example | Monthly sales analysis | Sales forecasting model |

In short, Data Analytics explains what happened, while Data Science can explain what happened, why it happened, what may happen, and what action should be taken.

---

## Module 2: Data Exploration

### Q1. What is data exploration?

**Answer:**  
Data exploration is the process of understanding a dataset before formal modeling. It includes studying data types, missing values, summary statistics, distributions, relationships, and outliers. It helps the analyst understand the structure and quality of the data.

**Example:**  
Before building a model to predict student marks, we may explore average marks, missing attendance values, score distribution, and relationship between study hours and marks.

---

### Q2. What are the main types of data?

**Answer:**  
Data can be classified in different ways:

1. **Structured data:** Organized in rows and columns.  
   Example: Excel sheet, SQL table.

2. **Semi-structured data:** Has some structure but not a fixed table format.  
   Example: JSON, XML.

3. **Unstructured data:** Does not have a predefined structure.  
   Example: Images, videos, emails, audio.

Data can also be classified as:

1. **Qualitative data:** Describes categories.  
   Example: Gender, city, product type.

2. **Quantitative data:** Describes numerical values.  
   Example: Age, salary, temperature.

Quantitative data may be:

1. **Discrete:** Countable values.  
   Example: Number of students.

2. **Continuous:** Measurable values.  
   Example: Height, weight, income.

---

### Q3. What are the levels of measurement in data?

**Answer:**  
The levels of measurement describe how data values can be interpreted mathematically.

1. **Nominal data:** Categories with no order.  
   Example: Blood group, gender, city.

2. **Ordinal data:** Categories with meaningful order.  
   Example: Low, medium, high.

3. **Interval data:** Numerical data with equal intervals but no true zero.  
   Example: Temperature in Celsius.

4. **Ratio data:** Numerical data with equal intervals and a true zero.  
   Example: Age, income, weight.

These levels are important because they decide which statistical methods can be applied.

---

### Q4. What are the important properties of data?

**Answer:**  
Important properties of data include:

1. **Accuracy:** Data should represent the true value.
2. **Completeness:** Required values should not be missing.
3. **Consistency:** Data should not contradict itself.
4. **Validity:** Data should follow defined rules and formats.
5. **Uniqueness:** Duplicate records should be avoided.
6. **Timeliness:** Data should be up to date.
7. **Dimensionality:** Number of variables or features in the dataset.
8. **Noise:** Random errors or irrelevant variation in data.
9. **Sparsity:** Presence of many zero or empty values.

**Example:**  
If a customer's age is recorded as 250, it violates validity because human age cannot normally be 250 years.

---

### Q5. What is descriptive statistics?

**Answer:**  
Descriptive statistics refers to methods used to summarize and describe the main features of a dataset. It does not make predictions; it only explains what is present in the data.

Descriptive statistics includes:

1. Measures of central tendency.
2. Measures of spread.
3. Measures of shape such as skewness and kurtosis.
4. Tables, charts, and graphs.

**Example:**  
Mean marks, highest marks, lowest marks, and standard deviation of marks are descriptive statistics.

---

### Q6. What is univariate exploration?

**Answer:**  
Univariate exploration means analyzing one variable at a time. It is used to understand the distribution, center, spread, and shape of a single variable.

Common tools for univariate exploration are:

1. Mean, median, and mode.
2. Range, variance, standard deviation, and IQR.
3. Histogram.
4. Boxplot.
5. Frequency table.

**Example:**  
Studying only the age column of a dataset to find average age and age distribution is univariate exploration.

---

### Q7. What are measures of central tendency?

**Answer:**  
Measures of central tendency describe the central or typical value of a dataset. The main measures are mean, median, and mode.

**Mean:**  
Mean is the arithmetic average. It is calculated as:

`Mean = sum of all observations / number of observations`

It is affected by extreme values.

**Median:**  
Median is the middle value after arranging data in ascending or descending order. It is less affected by outliers.

**Mode:**  
Mode is the most frequently occurring value.

**Example:**  
For marks `10, 20, 20, 30, 100`, mean is affected by 100, but median gives a better central value.

---

### Q8. What are measures of spread?

**Answer:**  
Measures of spread describe how much the data values vary from each other or from the center.

Important measures are:

1. **Range:**  
   `Range = maximum value - minimum value`

2. **Variance:**  
   Average squared deviation from the mean.

3. **Standard deviation:**  
   Square root of variance. It shows average dispersion around the mean.

4. **Interquartile range:**  
   `IQR = Q3 - Q1`  
   It represents the spread of the middle 50 percent of data.

5. **Coefficient of variation:**  
   `CV = standard deviation / mean`  
   It compares relative variability.

**Example:**  
If two classes have the same average marks but one has a higher standard deviation, that class has more variation in student performance.

---

### Q9. What is symmetry in data distribution?

**Answer:**  
A distribution is symmetric when the left and right sides of the distribution are approximately mirror images around the center. In a perfectly symmetric distribution, mean, median, and mode are approximately equal.

**Example:**  
The normal distribution is symmetric. In exam marks, if most students score around the average and equal numbers score above and below average, the distribution may be symmetric.

---

### Q10. What is skewness?

**Answer:**  
Skewness measures the asymmetry of a distribution.

1. **Positive skewness:** Tail is longer on the right side. Mean is usually greater than median.  
   Example: Income distribution.

2. **Negative skewness:** Tail is longer on the left side. Mean is usually less than median.  
   Example: Easy exam where most students score high.

3. **Zero skewness:** Distribution is approximately symmetric.

Skewness is important because many statistical models assume approximate symmetry.

---

### Q11. What is Karl Pearson's coefficient of skewness?

**Answer:**  
Karl Pearson's coefficient of skewness is a numerical measure of asymmetry in a distribution. It is commonly calculated as:

`Skewness = (Mean - Mode) / Standard Deviation`

If mode is not well defined, the alternative formula is:

`Skewness = 3(Mean - Median) / Standard Deviation`

Interpretation:

1. Positive value indicates right-skewed distribution.
2. Negative value indicates left-skewed distribution.
3. Value near zero indicates symmetry.

**Example:**  
If mean salary is greater than median salary due to a few very high salaries, Karl Pearson's skewness will be positive.

---

### Q12. What is Bowley's coefficient of skewness?

**Answer:**  
Bowley's coefficient of skewness is based on quartiles and is less affected by extreme values. It is calculated as:

`Bowley's skewness = (Q3 + Q1 - 2Q2) / (Q3 - Q1)`

Where:

1. `Q1` is the first quartile.
2. `Q2` is the median.
3. `Q3` is the third quartile.

Interpretation:

1. Positive value means right skewness.
2. Negative value means left skewness.
3. Zero means symmetric distribution.

Bowley's coefficient is useful when data contains outliers because quartiles are robust.

---

### Q13. What is kurtosis?

**Answer:**  
Kurtosis measures the heaviness of the tails and the peakedness of a distribution compared with a normal distribution. It indicates whether the data contains extreme values.

Types of kurtosis:

1. **Mesokurtic:** Similar to normal distribution.
2. **Leptokurtic:** More peaked with heavy tails; more outliers are likely.
3. **Platykurtic:** Flatter with lighter tails; fewer extreme values.

**Example:**  
Financial return data often has high kurtosis because extreme gains or losses may occur.

---

### Q14. What is multivariate exploration?

**Answer:**  
Multivariate exploration means analyzing two or more variables together to understand relationships, patterns, and dependencies among them.

Common techniques include:

1. Correlation analysis.
2. Scatter plots.
3. Scatter matrix.
4. Heatmaps.
5. Pairplots.
6. Bubble charts.

**Example:**  
Studying the relationship between advertising budget, product price, and sales is multivariate exploration.

---

### Q15. What is a central data point?

**Answer:**  
A central data point is an observation that best represents the center of a multidimensional dataset. Unlike a simple mean, it is an actual data point that is closest to the center of all observations.

It can be identified by calculating the distance of each point from the mean vector and selecting the point with the smallest distance.

**Example:**  
In customer segmentation, the central data point of a cluster can represent the typical customer of that cluster.

---

### Q16. What is correlation?

**Answer:**  
Correlation measures the degree and direction of relationship between two variables. It tells whether two variables move together.

Correlation does not prove causation. It only indicates association.

**Example:**  
Study hours and exam marks may have a positive correlation because marks generally increase when study hours increase.

---

### Q17. What are the different forms of correlation?

**Answer:**  
The main forms of correlation are:

1. **Positive correlation:** Both variables move in the same direction.  
   Example: Height and weight.

2. **Negative correlation:** One variable increases while the other decreases.  
   Example: Product price and demand.

3. **Zero correlation:** No meaningful relationship exists.  
   Example: Shoe size and exam marks.

4. **Linear correlation:** Relationship can be represented by a straight line.

5. **Nonlinear correlation:** Relationship exists but not in a straight-line form.

6. **Perfect correlation:** Correlation coefficient is exactly `+1` or `-1`.

7. **Spurious correlation:** Variables appear correlated but the relationship is accidental or due to another factor.

---

### Q18. What is Karl Pearson's correlation coefficient?

**Answer:**  
Karl Pearson's correlation coefficient measures the strength and direction of a linear relationship between two numerical variables. It is denoted by `r`.

The value of `r` lies between `-1` and `+1`.

1. `r = +1`: Perfect positive correlation.
2. `r = -1`: Perfect negative correlation.
3. `r = 0`: No linear correlation.

Formula:

`r = covariance(X, Y) / (standard deviation of X * standard deviation of Y)`

For bivariate data:

`r = sum((x - mean_x)(y - mean_y)) / sqrt(sum((x - mean_x)^2) * sum((y - mean_y)^2))`

**Example:**  
If advertising expenditure and sales have `r = 0.85`, it indicates a strong positive linear relationship.

---

### Q19. What is inferential statistics?

**Answer:**  
Inferential statistics is used to draw conclusions about a population based on a sample. Since studying an entire population is often impossible, a sample is analyzed and results are generalized to the larger population.

Important methods include:

1. Hypothesis testing.
2. Confidence intervals.
3. Z-test.
4. t-test.
5. ANOVA.
6. Estimation.

**Example:**  
Surveying 500 voters to estimate the opinion of all voters in a city is an application of inferential statistics.

---

### Q20. What is a normal distribution?

**Answer:**  
Normal distribution is a continuous probability distribution that is symmetric and bell-shaped. In a normal distribution, mean, median, and mode are equal.

Properties:

1. It is symmetric about the mean.
2. Total area under the curve is 1.
3. Most values lie near the mean.
4. The spread is controlled by standard deviation.

Empirical rule:

1. About 68 percent of values lie within 1 standard deviation.
2. About 95 percent lie within 2 standard deviations.
3. About 99.7 percent lie within 3 standard deviations.

**Example:**  
Human heights in a large population often approximately follow a normal distribution.

---

### Q21. What is a Poisson distribution?

**Answer:**  
Poisson distribution is a discrete probability distribution used to model the number of times an event occurs in a fixed interval of time or space, when events occur independently and at a constant average rate.

It is commonly used for count data.

**Examples:**

1. Number of calls received by a call center per hour.
2. Number of accidents at a signal per month.
3. Number of website visits per minute.

If the average number of events is `lambda`, then the Poisson distribution gives the probability of observing a specific number of events.

---

### Q22. What is hypothesis testing?

**Answer:**  
Hypothesis testing is a statistical method used to make decisions about a population based on sample data. It begins with two competing statements:

1. **Null hypothesis (H0):** Assumes no significant difference or no effect.
2. **Alternative hypothesis (H1):** Assumes a significant difference or effect exists.

The result is decided using a test statistic and p-value.

Decision rule:

1. If `p-value < significance level`, reject H0.
2. If `p-value >= significance level`, fail to reject H0.

**Example:**  
Testing whether a new teaching method improves average marks compared with the old method.

---

### Q23. What is the Central Limit Theorem?

**Answer:**  
The Central Limit Theorem states that if we take sufficiently large random samples from any population, the distribution of the sample means will be approximately normal, regardless of the original population distribution.

This theorem is important because it allows us to use normal-based statistical methods even when the original data is not normally distributed.

**Example:**  
Even if individual customer spending is skewed, the average spending of many random samples will approximately follow a normal distribution.

---

### Q24. What is a confidence interval?

**Answer:**  
A confidence interval is a range of values within which the true population parameter is expected to lie with a certain level of confidence.

For example, a 95 percent confidence interval means that if we repeat the sampling process many times, about 95 percent of the calculated intervals would contain the true population mean.

General form:

`Estimate +/- margin of error`

**Example:**  
If the average height of a sample is 165 cm with a 95 percent confidence interval of 162 cm to 168 cm, we are 95 percent confident that the true population mean lies within this range.

---

### Q25. What is a Z-test?

**Answer:**  
A Z-test is a hypothesis test used when the sample size is large or the population standard deviation is known. It compares a sample mean with a population mean or compares two means.

Common conditions:

1. Sample size is usually greater than 30.
2. Population standard deviation is known, or sample size is sufficiently large.
3. Data is approximately normally distributed or sample size is large.

Formula for one-sample Z-test:

`Z = (sample mean - population mean) / (population standard deviation / sqrt(n))`

**Example:**  
Testing whether the average weight of a product differs from the claimed weight when population standard deviation is known.

---

### Q26. What is a t-test?

**Answer:**  
A t-test is a hypothesis test used to compare means when the sample size is small and the population standard deviation is unknown.

Types of t-test:

1. **One-sample t-test:** Compares sample mean with a known value.
2. **Independent two-sample t-test:** Compares means of two independent groups.
3. **Paired t-test:** Compares means of the same group before and after treatment.

Formula for one-sample t-test:

`t = (sample mean - population mean) / (sample standard deviation / sqrt(n))`

**Example:**  
A paired t-test can be used to test whether student marks improved after training.

---

### Q27. What are Type-I and Type-II errors?

**Answer:**  
Errors in hypothesis testing occur because decisions are made using sample data.

**Type-I error:**  
Rejecting the null hypothesis when it is actually true. It is also called a false positive. The probability of Type-I error is denoted by `alpha`.

**Type-II error:**  
Failing to reject the null hypothesis when it is actually false. It is also called a false negative. The probability of Type-II error is denoted by `beta`.

**Example:**  
In medical testing, Type-I error means declaring a healthy person diseased. Type-II error means declaring a diseased person healthy.

---

### Q28. What is ANOVA?

**Answer:**  
ANOVA stands for Analysis of Variance. It is used to compare the means of three or more groups. Instead of performing many t-tests, ANOVA checks whether at least one group mean is significantly different from the others.

Hypotheses:

1. `H0`: All group means are equal.
2. `H1`: At least one group mean is different.

ANOVA uses the F-statistic, which compares between-group variation with within-group variation.

**Example:**  
Testing whether the average marks of students differ among three teaching methods can be done using ANOVA.

---

## Module 3: Methodology and Data Visualization

### Q1. What is model building?

**Answer:**  
Model building is the process of creating a mathematical or computational model that learns patterns from data and uses those patterns for prediction, classification, clustering, or decision-making.

Steps in model building:

1. Define the problem.
2. Select input and output variables.
3. Split data into training and testing sets.
4. Choose a suitable algorithm.
5. Train the model.
6. Evaluate performance.
7. Tune parameters.
8. Deploy and monitor the model.

**Example:**  
In fraud detection, a classification model is trained using past transaction data to classify new transactions as fraudulent or genuine.

---

### Q2. What is cross validation?

**Answer:**  
Cross validation is a model evaluation technique used to estimate how well a model will perform on unseen data. Instead of using only one train-test split, cross validation uses multiple splits and evaluates the model repeatedly.

It reduces the risk of evaluating the model on a lucky or unlucky split of data.

**Example:**  
In 5-fold cross validation, the dataset is divided into 5 parts. The model is trained on 4 parts and tested on 1 part. This is repeated 5 times, and the average performance is reported.

---

### Q3. What is K-fold cross validation?

**Answer:**  
K-fold cross validation divides the dataset into `k` approximately equal parts called folds. The model is trained `k` times. Each time, one fold is used for testing and the remaining `k-1` folds are used for training.

Steps:

1. Divide data into `k` folds.
2. Train the model on `k-1` folds.
3. Test the model on the remaining fold.
4. Repeat until each fold has been used as test data.
5. Average the performance scores.

**Example:**  
In 10-fold cross validation, the model is trained and tested 10 times. The final accuracy is the average of all 10 accuracies.

---

### Q4. What is leave-one-out cross validation?

**Answer:**  
Leave-one-out cross validation, or LOOCV, is a special case of K-fold cross validation where `k` is equal to the number of observations in the dataset. In each iteration, one observation is used for testing and all remaining observations are used for training.

Advantages:

1. Uses maximum data for training.
2. Useful for small datasets.

Disadvantages:

1. Computationally expensive.
2. Can be time-consuming for large datasets.

**Example:**  
If a dataset has 100 records, LOOCV trains the model 100 times, each time testing on one record.

---

### Q5. What is bootstrapping?

**Answer:**  
Bootstrapping is a resampling technique in which multiple samples are created from the original dataset by sampling with replacement. It is used to estimate uncertainty, confidence intervals, and model stability.

Sampling with replacement means the same observation can appear more than once in a bootstrap sample.

**Example:**  
If we want to estimate the confidence interval of average salary, we can create many bootstrap samples, calculate the mean for each sample, and study the distribution of those means.

---

### Q6. What is data visualization?

**Answer:**  
Data visualization is the graphical representation of data. It helps in understanding patterns, trends, distributions, comparisons, relationships, and outliers.

Visualization is important because humans can understand visual patterns faster than raw numbers.

**Example:**  
A line chart of monthly sales helps identify whether sales are increasing or decreasing over time.

---

### Q7. What is univariate visualization?

**Answer:**  
Univariate visualization represents one variable at a time. It is used to understand the distribution, frequency, center, and spread of a single variable.

Common univariate visualizations:

1. Histogram.
2. Boxplot.
3. Distribution chart.
4. Bar chart.

**Example:**  
A histogram of student marks shows whether most students scored low, average, or high marks.

---

### Q8. What is a histogram?

**Answer:**  
A histogram is a graph used to show the distribution of a numerical variable. It divides data into intervals called bins and shows the frequency of observations in each bin.

Uses:

1. To identify the shape of distribution.
2. To detect skewness.
3. To observe spread.
4. To identify possible outliers.

**Example:**  
A histogram of customer age can show whether most customers are young, middle-aged, or elderly.

---

### Q9. What is a quartile chart or boxplot?

**Answer:**  
A boxplot is a visualization that represents the five-number summary of a dataset:

1. Minimum.
2. First quartile Q1.
3. Median Q2.
4. Third quartile Q3.
5. Maximum.

It also helps detect outliers using the interquartile range.

Outlier rule:

1. Lower boundary: `Q1 - 1.5 * IQR`
2. Upper boundary: `Q3 + 1.5 * IQR`

**Example:**  
A boxplot of salaries can show median salary, spread, and unusually high salaries.

---

### Q10. What is a distribution chart?

**Answer:**  
A distribution chart shows how values of a variable are spread over a range. It may include a histogram, density curve, or both. It helps understand whether data is normal, skewed, uniform, or multimodal.

**Example:**  
A distribution chart of delivery time can show whether most deliveries happen within expected time or whether delays are common.

---

### Q11. What is multivariate visualization?

**Answer:**  
Multivariate visualization represents relationships among two or more variables. It is used to understand dependencies, group differences, clusters, and interactions.

Common multivariate visualizations:

1. Scatter plot.
2. Scatter matrix.
3. Bubble chart.
4. Density chart.
5. Heatmap.

**Example:**  
A scatter plot of total bill and tip amount can show whether larger bills are associated with larger tips.

---

### Q12. What is a scatter plot?

**Answer:**  
A scatter plot displays the relationship between two numerical variables by representing each observation as a point on a two-dimensional plane.

Uses:

1. To detect positive or negative relationships.
2. To detect clusters.
3. To detect outliers.
4. To understand linear or nonlinear trends.

**Example:**  
Plotting house area on the x-axis and house price on the y-axis can show whether larger houses generally have higher prices.

---

### Q13. What is a scatter matrix?

**Answer:**  
A scatter matrix is a grid of scatter plots showing pairwise relationships among multiple numerical variables. It is useful when we want to explore relationships among many variables at once.

**Example:**  
In the Iris dataset, a scatter matrix can show relationships among sepal length, sepal width, petal length, and petal width.

---

### Q14. What is a bubble chart?

**Answer:**  
A bubble chart is an extension of a scatter plot where each point has a size that represents a third variable. Color may represent a fourth variable.

**Example:**  
A chart with advertising cost on the x-axis, sales on the y-axis, and bubble size representing profit can show the relationship among three variables.

---

### Q15. What is a density chart?

**Answer:**  
A density chart shows the smoothed distribution of a numerical variable. It is similar to a histogram but gives a continuous curve instead of bars.

It is useful for comparing distributions across groups.

**Example:**  
A density chart can compare the age distribution of male and female customers.

---

### Q16. What is the roadmap for data exploration?

**Answer:**  
A roadmap for data exploration is a systematic plan for understanding data before modeling.

Steps:

1. Understand the problem and objective.
2. Identify data sources and variables.
3. Check data types.
4. Check missing values and duplicates.
5. Study descriptive statistics.
6. Perform univariate analysis.
7. Perform bivariate and multivariate analysis.
8. Detect outliers and anomalies.
9. Study correlations.
10. Visualize important relationships.
11. Prepare insights and decide preprocessing steps.

**Example:**  
Before predicting house prices, we explore price distribution, missing values, relation between area and price, outliers in price, and correlation among features.

---

### Q17. What is a parallel coordinates chart?

**Answer:**  
A parallel coordinates chart is used to visualize high-dimensional data. Each variable is shown as a vertical axis, and each observation is represented as a line crossing all axes.

It helps observe patterns, clusters, and outliers across many dimensions.

**Example:**  
In the Iris dataset, sepal length, sepal width, petal length, and petal width can be shown as parallel axes to compare flower species.

---

### Q18. What is a deviation chart?

**Answer:**  
A deviation chart shows how much each value differs from a reference value such as mean, target, or previous period. It highlights positive and negative deviations clearly.

**Example:**  
A company can use a deviation chart to show monthly sales above or below the target sales.

---

### Q19. What are Andrews Curves?

**Answer:**  
Andrews Curves are used to visualize high-dimensional data by converting each observation into a curve using a mathematical function. Similar observations produce similar curves.

They are useful for identifying clusters, class separation, and unusual observations.

**Example:**  
In a medical dataset, Andrews Curves can help visualize whether patients with different disease categories form different curve patterns.

---

## Module 4: Anomaly Detection

### Q1. What are outliers?

**Answer:**  
Outliers are observations that are significantly different from the majority of data. They may be unusually high, unusually low, or inconsistent with the general pattern.

Outliers are important because they can affect statistical measures, visualizations, and machine learning models.

**Example:**  
If most students score between 40 and 90 marks and one student has a recorded score of 500, that value is an outlier.

---

### Q2. What are the causes of outliers?

**Answer:**  
Outliers may occur due to several reasons:

1. **Data entry errors:** Wrong value entered manually.
2. **Measurement errors:** Faulty sensor or instrument.
3. **Sampling errors:** Observation from a different population.
4. **Natural variation:** Rare but valid extreme value.
5. **Fraud or abnormal behavior:** Unusual transaction or activity.
6. **Data processing errors:** Incorrect merging or transformation.

**Example:**  
A credit card transaction of Rs. 5,00,000 may be an outlier if the customer usually spends Rs. 500 to Rs. 2,000.

---

### Q3. What is anomaly detection?

**Answer:**  
Anomaly detection is the process of identifying data points, events, or patterns that do not conform to expected behavior. These unusual points are called anomalies or outliers.

Anomaly detection is widely used in fraud detection, network security, medical diagnosis, industrial monitoring, and quality control.

**Example:**  
Detecting unusual login activity from a different country can be considered anomaly detection in cybersecurity.

---

### Q4. What are common anomaly detection techniques?

**Answer:**  
Common anomaly detection techniques are:

1. **Statistical methods:** Z-score, IQR method.
2. **Distance-based methods:** k-Nearest Neighbors anomaly detection.
3. **Density-based methods:** DBSCAN, Local Outlier Factor.
4. **Machine learning methods:** Isolation Forest, One-Class SVM.
5. **Time series methods:** Detecting unusual spikes, drops, or seasonal deviations.

The choice of method depends on the type, size, distribution, and dimensionality of data.

---

### Q5. How is outlier detection done using statistics?

**Answer:**  
Statistical outlier detection identifies values that are far away from expected statistical limits.

Common methods:

**Z-score method:**  
`Z = (x - mean) / standard deviation`

If absolute Z-score is greater than 3, the point is often considered an outlier.

**IQR method:**  
`IQR = Q3 - Q1`

Lower boundary:

`Q1 - 1.5 * IQR`

Upper boundary:

`Q3 + 1.5 * IQR`

Values outside these boundaries are considered outliers.

**Example:**  
In salary data, a very high salary outside the upper IQR boundary may be detected as an outlier.

---

### Q6. What is distance-based outlier detection?

**Answer:**  
Distance-based outlier detection identifies observations that are far away from their neighboring data points. If a point has large distances from its nearest neighbors, it may be considered an outlier.

A common method is k-Nearest Neighbors:

1. Select value of `k`.
2. Calculate distance from each point to its neighbors.
3. Find the distance to the kth nearest neighbor.
4. Points with unusually large kth-neighbor distances are marked as anomalies.

**Example:**  
In customer data, a customer with very high income but very low spending score may be far from other customers and detected as an anomaly.

---

### Q7. What is density-based outlier detection?

**Answer:**  
Density-based outlier detection identifies points that lie in low-density regions compared with the surrounding data. The main idea is that normal points belong to dense groups, while outliers are isolated.

DBSCAN is a popular density-based clustering method. It classifies points as:

1. **Core points:** Have enough neighbors within a radius.
2. **Border points:** Near a core point but do not have enough neighbors themselves.
3. **Noise points:** Do not belong to any dense region and are treated as outliers.

**Example:**  
In geographical accident data, dense accident regions may form clusters, while isolated accident locations may be treated as noise.

---

### Q8. What is DBSCAN?

**Answer:**  
DBSCAN stands for Density-Based Spatial Clustering of Applications with Noise. It is an unsupervised clustering algorithm that groups points based on density and identifies noise points as outliers.

Important parameters:

1. **eps:** Radius around a point.
2. **min_samples:** Minimum number of points required to form a dense region.

Advantages:

1. Does not require number of clusters in advance.
2. Can detect arbitrary-shaped clusters.
3. Can identify outliers.

Limitation:

It is sensitive to the choice of `eps` and `min_samples`.

---

### Q9. What is SMOTE?

**Answer:**  
SMOTE stands for Synthetic Minority Over-sampling Technique. It is used to handle class imbalance in classification problems. Instead of simply duplicating minority class records, SMOTE creates synthetic minority samples by interpolating between existing minority class observations.

Steps:

1. Select a minority class sample.
2. Find its nearest minority class neighbors.
3. Choose one neighbor.
4. Create a new synthetic point between the sample and the neighbor.

**Example:**  
In fraud detection, fraudulent transactions are much fewer than normal transactions. SMOTE can generate synthetic fraud samples so that the classifier learns the minority class better.

---

### Q10. Why is class imbalance a problem?

**Answer:**  
Class imbalance occurs when one class has many more observations than another class. In such cases, a model may become biased toward the majority class and ignore the minority class.

Accuracy can become misleading in imbalanced data.

**Example:**  
If 99 percent transactions are genuine and 1 percent are fraud, a model that predicts every transaction as genuine will have 99 percent accuracy but will fail to detect fraud. Therefore, precision, recall, F1-score, and ROC-AUC should also be used.

---

## Module 5: Time Series Forecasting

### Q1. What is a time series?

**Answer:**  
A time series is a sequence of observations recorded at regular or irregular time intervals. The order of observations is important because each value may depend on previous values.

**Examples:**

1. Daily temperature.
2. Monthly sales.
3. Stock prices.
4. Yearly population.
5. Hourly website traffic.

Time series analysis is used to understand patterns and forecast future values.

---

### Q2. What is time series forecasting?

**Answer:**  
Time series forecasting is the process of predicting future values based on past observations arranged over time. It is widely used in business, economics, weather, finance, and operations.

**Example:**  
A retail store can forecast next month's demand using previous monthly sales data.

---

### Q3. What is the taxonomy of time series forecasting methods?

**Answer:**  
Time series forecasting methods can be classified into:

1. **Naive methods:** Future value is assumed to be equal to the last observed value.
2. **Average methods:** Forecast is based on average of past values.
3. **Smoothing methods:** Use weighted averages, giving more importance to recent observations.
4. **Decomposition methods:** Separate series into trend, seasonality, and residual components.
5. **Regression-based methods:** Use time or external variables as predictors.
6. **ARIMA models:** Use autoregression, differencing, and moving average components.
7. **Machine learning methods:** Use algorithms such as Random Forest, XGBoost, or neural networks.

The method is selected based on trend, seasonality, stationarity, data size, and forecasting objective.

---

### Q4. What is time series decomposition?

**Answer:**  
Time series decomposition separates a time series into components:

1. **Trend:** Long-term upward or downward movement.
2. **Seasonality:** Repeating pattern at fixed intervals.
3. **Cyclical component:** Long-term fluctuations not of fixed period.
4. **Residual or irregular component:** Random noise left after removing other components.

Models:

**Additive model:**  
`Observed = Trend + Seasonal + Residual`

Used when seasonal variation is roughly constant.

**Multiplicative model:**  
`Observed = Trend * Seasonal * Residual`

Used when seasonal variation increases or decreases with the level of the series.

**Example:**  
Ice cream sales may have an increasing trend and seasonal peaks during summer.

---

### Q5. What is smoothing in time series?

**Answer:**  
Smoothing is a technique used to reduce random fluctuations in a time series so that the underlying pattern becomes clearer. It helps identify trend and make stable forecasts.

Common smoothing methods include:

1. Average method.
2. Moving average smoothing.
3. Exponential smoothing.

**Example:**  
Daily sales may fluctuate due to random factors. A moving average can smooth the series and show the general sales trend.

---

### Q6. What is the average method of forecasting?

**Answer:**  
The average method forecasts all future values as the average of historical observations.

Formula:

`Forecast = sum of past observations / number of observations`

It is simple and useful when the series has no clear trend or seasonality.

**Example:**  
If sales for four months are 100, 120, 110, and 130, the forecast by average method is 115.

---

### Q7. What is moving average smoothing?

**Answer:**  
Moving average smoothing calculates the average of a fixed number of recent observations and uses it to smooth the time series.

For a 3-period moving average:

`MA = (value at t + value at t-1 + value at t-2) / 3`

It reduces short-term fluctuations and highlights trend.

**Example:**  
If monthly demand is 250, 235, and 200, the 3-month moving average is `(250 + 235 + 200) / 3 = 228.33`.

---

### Q8. What is time series analysis using linear regression?

**Answer:**  
In linear regression for time series, time is used as an independent variable and the observed value is used as the dependent variable. The model estimates a trend line.

General equation:

`Y = a + bT`

Where:

1. `Y` is the forecasted value.
2. `T` is time.
3. `a` is intercept.
4. `b` is slope or trend.

**Example:**  
If sales increase by approximately 100 units each month, linear regression can estimate this trend and forecast future sales.

---

### Q9. What is ARIMA?

**Answer:**  
ARIMA stands for AutoRegressive Integrated Moving Average. It is a time series forecasting model used for stationary or transformed stationary data.

ARIMA has three parameters:

1. **p:** AutoRegressive order. It uses past values.
2. **d:** Integrated order. It represents differencing needed to make the series stationary.
3. **q:** Moving Average order. It uses past forecast errors.

ARIMA is written as `ARIMA(p, d, q)`.

**Example:**  
ARIMA can be used to forecast monthly sales after removing trend through differencing.

---

### Q10. What is stationarity in time series?

**Answer:**  
A time series is stationary if its statistical properties such as mean, variance, and autocorrelation remain constant over time. Many time series models, especially ARIMA, work better when the series is stationary.

Non-stationary data can be made stationary using:

1. Differencing.
2. Log transformation.
3. Removing trend and seasonality.

**Example:**  
A sales series with a strong upward trend is usually non-stationary because its mean changes over time.

---

### Q11. What is Mean Absolute Error?

**Answer:**  
Mean Absolute Error, or MAE, measures the average absolute difference between actual and predicted values.

Formula:

`MAE = average of absolute(actual - predicted)`

It is easy to understand because it is in the same unit as the original data.

**Example:**  
If MAE for sales forecasting is 20 units, predictions are wrong by 20 units on average.

---

### Q12. What is Root Mean Square Error?

**Answer:**  
Root Mean Square Error, or RMSE, measures the square root of the average squared difference between actual and predicted values.

Formula:

`RMSE = sqrt(average of (actual - predicted)^2)`

RMSE penalizes large errors more strongly than MAE.

**Example:**  
If RMSE is high, it indicates that the model sometimes makes large forecasting errors.

---

### Q13. What is Mean Absolute Percentage Error?

**Answer:**  
Mean Absolute Percentage Error, or MAPE, measures forecasting error as a percentage of actual values.

Formula:

`MAPE = average of absolute((actual - predicted) / actual) * 100`

It is useful for comparing forecasting accuracy across datasets with different scales.

Limitation:

MAPE is not suitable when actual values are zero or very close to zero.

**Example:**  
If MAPE is 8 percent, the forecast is wrong by about 8 percent on average.

---

### Q14. What is Mean Absolute Scaled Error?

**Answer:**  
Mean Absolute Scaled Error, or MASE, compares the forecasting error of a model with the error of a naive forecasting method. It is scale-independent and useful for comparing forecasts across different time series.

Interpretation:

1. `MASE < 1`: Model performs better than naive forecast.
2. `MASE = 1`: Model performs similar to naive forecast.
3. `MASE > 1`: Model performs worse than naive forecast.

**Example:**  
If MASE is 0.7, the forecasting model performs better than the naive benchmark.

---

### Q15. What are evaluation parameters for classification?

**Answer:**  
Classification models are evaluated using metrics such as:

1. **Accuracy:** Proportion of correct predictions.
2. **Precision:** Out of predicted positive cases, how many are actually positive.
3. **Recall:** Out of actual positive cases, how many are correctly predicted.
4. **F1-score:** Harmonic mean of precision and recall.
5. **Confusion matrix:** Table of true positives, true negatives, false positives, and false negatives.
6. **ROC-AUC:** Measures ability to separate classes.

**Example:**  
In fraud detection, recall is important because missing a fraud case is costly.

---

### Q16. What are evaluation parameters for regression?

**Answer:**  
Regression models are evaluated using error-based metrics:

1. **MAE:** Average absolute error.
2. **MSE:** Average squared error.
3. **RMSE:** Square root of MSE.
4. **R2 score:** Proportion of variance explained by the model.
5. **MAPE:** Percentage-based error.

**Example:**  
For house price prediction, RMSE tells the typical prediction error in price units.

---

### Q17. What are evaluation parameters for clustering?

**Answer:**  
Clustering is evaluated using internal and external metrics.

Internal metrics:

1. **Silhouette score:** Measures how similar a point is to its own cluster compared with other clusters.
2. **Davies-Bouldin index:** Lower value indicates better clustering.
3. **Calinski-Harabasz score:** Higher value indicates better separation.

External metrics:

1. **Adjusted Rand Index:** Compares clustering result with true labels if available.

**Example:**  
For customer segmentation, a high silhouette score means customers within the same segment are similar and different from other segments.

---

## Module 6: Applications of Data Science

### Q1. What are applications of Data Science?

**Answer:**  
Data Science is applied in many domains to support prediction, decision-making, automation, and optimization.

Important applications include:

1. Predictive modeling.
2. Fraud detection.
3. Customer segmentation.
4. Time series forecasting.
5. Recommendation systems.
6. Healthcare diagnosis.
7. Sentiment analysis.
8. Risk analysis.

**Example:**  
Hospitals use Data Science to predict disease risk using patient history and medical test results.

---

### Q2. What is predictive modeling?

**Answer:**  
Predictive modeling is the process of using historical data to predict future outcomes. It uses statistical or machine learning models to learn patterns from past data.

Types:

1. **Regression:** Predicts continuous values.
2. **Classification:** Predicts categories or classes.

**Example:**  
Predicting whether a customer will buy a product is classification. Predicting the price of a house is regression.

---

### Q3. How is Data Science used in house price prediction?

**Answer:**  
House price prediction is a regression problem where the goal is to predict the selling price of a house based on features such as area, number of bedrooms, location, age of property, and amenities.

Steps:

1. Collect historical house sale data.
2. Clean missing and inconsistent values.
3. Encode categorical variables such as location.
4. Explore relationships such as area versus price.
5. Train a regression model.
6. Evaluate using MAE, RMSE, or R2 score.
7. Predict prices for new houses.

**Example:**  
A model may learn that houses in prime locations with larger area and more bedrooms generally have higher prices.

---

### Q4. How is Data Science used in fraud detection?

**Answer:**  
Fraud detection is usually a classification or anomaly detection problem. The aim is to identify fraudulent behavior from transaction patterns.

Features may include:

1. Transaction amount.
2. Location.
3. Time of transaction.
4. Merchant type.
5. Frequency of transactions.
6. User history.

Challenges:

1. Fraud data is highly imbalanced.
2. Fraud patterns change over time.
3. False negatives can be costly.

**Example:**  
If a user normally spends small amounts in one city but suddenly makes a very large transaction in another country, the system may flag it as fraud.

---

### Q5. What is customer segmentation?

**Answer:**  
Customer segmentation is the process of dividing customers into groups based on similar characteristics or behavior. It is commonly done using clustering algorithms.

Common features:

1. Age.
2. Income.
3. Spending score.
4. Purchase frequency.
5. Product preferences.

Benefits:

1. Targeted marketing.
2. Personalized offers.
3. Better customer retention.
4. Improved business strategy.

**Example:**  
A mall can segment customers into high-income high-spending, low-income low-spending, and high-income low-spending groups.

---

### Q6. How is Data Science used in weather forecasting?

**Answer:**  
Weather forecasting is a time series and predictive modeling application. It uses historical and real-time weather data to predict future weather conditions.

Data used:

1. Temperature.
2. Humidity.
3. Wind speed.
4. Pressure.
5. Rainfall.
6. Satellite data.

Methods:

1. Time series models.
2. Regression models.
3. Machine learning models.
4. Deep learning models.

**Example:**  
Past rainfall, humidity, and pressure data can be used to predict the probability of rain tomorrow.

---

### Q7. What is a recommendation engine?

**Answer:**  
A recommendation engine is a system that suggests products, movies, songs, or content to users based on their preferences, behavior, or similarity with other users.

Types:

1. **Content-based filtering:** Recommends items similar to what the user liked before.
2. **Collaborative filtering:** Recommends items based on preferences of similar users.
3. **Hybrid recommendation:** Combines content-based and collaborative methods.

**Example:**  
If a user buys a mobile phone, an e-commerce website may recommend a phone case, charger, or earphones.

---

### Q8. How does product recommendation work?

**Answer:**  
Product recommendation works by analyzing user behavior, product features, and purchase patterns. The system identifies items that a user is likely to prefer.

Steps:

1. Collect user activity such as views, clicks, ratings, and purchases.
2. Create user and product profiles.
3. Find similar users or similar products.
4. Rank products based on predicted interest.
5. Recommend top-ranked products.

**Example:**  
If many customers who bought a laptop also bought a wireless mouse, the system may recommend a wireless mouse to a new laptop buyer.

---

### Q9. Why is domain knowledge important in Data Science applications?

**Answer:**  
Domain knowledge means understanding the field in which Data Science is applied. It is important because it helps in selecting relevant features, interpreting results correctly, detecting unrealistic values, and making useful decisions.

**Example:**  
In healthcare, a data scientist must understand that extremely high blood pressure values may indicate either a medical emergency or a measurement error. Without domain knowledge, the interpretation may be wrong.

---

### Q10. What ethical issues should be considered in Data Science applications?

**Answer:**  
Ethical issues in Data Science include:

1. **Privacy:** Personal data should be protected.
2. **Bias:** Models should not unfairly discriminate against groups.
3. **Transparency:** Decisions should be explainable where possible.
4. **Security:** Data must be protected from misuse.
5. **Consent:** Data should be collected and used with proper permission.
6. **Accountability:** Organizations must take responsibility for automated decisions.

**Example:**  
A loan approval model should not unfairly reject applicants based on gender, caste, race, or other sensitive attributes.

