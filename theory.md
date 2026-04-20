# Applied Data Science — Theory

---

## Experiment 1

**Abstract:** In real-world data analysis, understanding the central tendency, variability, and distribution shape of a dataset is fundamental to drawing meaningful conclusions. Given two datasets — a Body Mass Index (BMI) dataset and a Wine Quality dataset — the objective is to statistically analyze the typical values, degree of spread, directional imbalance, and presence of extreme outliers in each. The study aims to evaluate whether planning decisions should rely on mean-based or median-based estimation in the presence of outliers, using computational analysis through Python-based tools.

The analysis should address the following key questions:
- What are the mean and median values of the dataset, and what do they indicate about typical behavior and the influence of extreme values?
- What do the standard deviation and coefficient of variation reveal about the consistency, dispersion, and reliability of the data?
- Does the distribution exhibit skewness and high kurtosis, and what do these measures indicate about directional imbalance and extreme behaviors?
- Which individual observations are identified as statistically abnormal using Z-score analysis, and how do they contribute to overall risk?
- In the presence of extreme values, should decisions be based on the mean or the median, and why?

**Theory:**

**Descriptive Statistics:**

Descriptive statistics can be defined as the measures that summarize a given data, and these measures can be broken down further into:
1. Measure of central tendency
2. Measure of spread/dispersion
3. Measure of symmetry/shape

**Measure of Central Tendency:**

Measure of central tendency is used to describe the middle/centre value of the data. Mean, Median, and Mode are measures of central tendency.

1. **Mean**
   - Mean is the average value of the dataset.
   - Mean is calculated by adding all values in the dataset divided by the number of values in the dataset.
   - We can calculate the mean for only numerical variables.

2. **Median**
   - The Median is the middle number in the dataset.
   - Median is the best measure when we have outliers.

3. **Mode**
   - The mode is used to find the common number in the dataset.

**Measure of Spread:**

- The measure of spread/dispersion is used to describe how data is spread. It also describes the variability of the dataset.
- Standard Deviation, Variance, Range, IQR are used to describe the measure of spread/dispersion.
- The measure of spread can be shown in graphs like boxplot.

1. **Variance**
   - Variance is used to describe how far each number in the dataset is from the mean.
   - Formula to calculate population variance: σ² = Σ(xᵢ − μ)² / N

2. **Standard Deviation**
   - Standard Deviation is the measure of the spread of data from the mean.
   - Standard deviation is the square root of variance.
   - More the standard deviation, more the spread.

3. **Range**
   - The range is the difference between the largest number and the smallest number.
   - Larger the range, the more the dispersion.

4. **Interquartile Range (IQR)**
   - Quartiles describe the spread of data by breaking into quarters. The median exactly divides the data into two parts.
   - Q1 (Lower quartile) is the middle value in the first half of the sorted dataset.
   - Q2 is the median value.
   - Q3 (Upper quartile) is the middle value in the second half of the sorted dataset.
   - The interquartile range is the difference between the 75th percentile (Q3) and the 25th percentile (Q1).
   - 50% of data fall within this range.

**Boxplot** is used to describe how the data is distributed in the dataset. This graph represents five-point summary (minimum, maximum, median, lower quartile, and upper quartile) and is used to identify outliers.
- Whiskers — denote the spread of data
- Box — represents the IQR; 50% of data lies within this range.

**Measure of Shape:**

1. **Skewness**
   - Skewness is the measure of the symmetry, or lack of it, for a real-valued random variable about its mean. The skewness value can be positive, negative, or undefined. In a perfectly symmetrical distribution, the mean, the median, and the mode will all have the same value.

2. **Kurtosis**
   - Kurtosis provides a measurement about the extremities (i.e. tails) of the distribution of data, and therefore provides an indication of the presence of outliers. Kurtosis is a measure of whether the data are heavy-tailed or light-tailed relative to a normal distribution. Data sets with high kurtosis tend to have heavy tails, or outliers. Data sets with low kurtosis tend to have light tails, or lack of outliers.

---

## Experiment 2

**Abstract:** In this experiment, two datasets are used — a Wine Quality dataset consisting of multiple numerical attributes representing chemical properties of wine samples, and a Customer Demographic dataset containing numerical attributes (age, income) and categorical attributes (gender, city, purchase status). The Wine dataset features are measured on different scales, requiring standardization and normalization. The Customer dataset contains missing values and non-numeric categorical features that cannot be directly used in machine learning algorithms. The problem is to preprocess both datasets by handling missing values using appropriate imputation strategies, converting categorical variables into numerical form using label encoding and one-hot encoding, and applying feature scaling techniques such as standardization and normalization. The objective is to transform the raw data into clean, consistent, and machine-learning-ready formats suitable for further analysis and model development.

**Theory:**

Data cleaning is the collective name for a series of actions performed on data in the process of getting it ready for analysis.

Some of the steps in data cleaning are:
- Handling missing values
- Encoding categorical features
- Outlier detection
- Transformations, etc.

Handling missing values is a key part of data preprocessing and hence, it is of utmost importance for data scientists/machine learning engineers to learn different techniques in relation to imputing/replacing numerical or categorical missing values with appropriate values based on appropriate strategies.

That is primarily the reason we need to convert categorical columns to numerical columns so that a machine learning algorithm understands it. This process is called categorical encoding.

**SimpleImputer** is a class found in the package `sklearn.impute`. It is used to impute/replace the numerical or categorical missing data related to one or more features with appropriate values.

Typically, any structured dataset includes multiple columns — a combination of numerical as well as categorical variables. A machine can only understand the numbers. It cannot understand the text. That is essentially the case with Machine Learning algorithms too. There are multiple ways of handling categorical variables.

The two most widely used techniques:
- **Label Encoding** — Each label is assigned a unique integer based on alphabetical ordering.
- **One-Hot Encoding** — Creates additional features based on the number of unique values in the categorical feature. Every unique value in the category will be added as a feature.

---

## Experiment 3

**Abstract:** The aim of this experiment is to enhance practical understanding of statistical hypothesis testing through realistic data-driven scenarios using appropriate t-test techniques.

Two real-world datasets are given — (i) the Website Response Time dataset recording performance before and after backend optimization, and (ii) the Smart Energy Meter dataset recording daily household electricity consumption against a standard population mean. The objective is to design and implement programs to perform appropriate t-test-based inferential statistical analyses.

**Case 1: Paired Sample t-test (Website Response Time Dataset)**
Given the Website Response Time dataset collected before and after backend optimization, write a program to perform a paired sample t-test to analyze whether the optimization has resulted in a statistically significant reduction in response time. The program should formulate appropriate null and alternative hypotheses, compute the t-statistic and p-value, and interpret the results at a chosen level of significance.

**Case 2: One-Sample t-test (Smart Energy Meter Dataset)**
Given the Smart Energy Meter dataset recording daily energy consumption of households, write a program to perform a one-sample t-test to analyze whether the average energy usage differs significantly from the standard population mean of 11 kWh. The program should formulate appropriate hypotheses, compute the test statistic, and interpret the results.

**Theory:**

- Z-Test and T-Tests are Parametric Tests, where the Null Hypothesis is less than, greater than, or equal to some value.
- A z-test is used if the population variance is known, or if the sample size is larger than 30.
- If the sample size is less than 30 and the population variance is unknown, we must use a t-test.

T-test is a type of inferential statistic used to study if there is a statistical difference between two groups. Mathematically, it establishes the problem by assuming that the means of the two distributions are equal (H₀: μ₁ = μ₂). If the t-test rejects the null hypothesis (H₀: μ₁ = μ₂), it indicates that the groups are highly different.

The statistical test can be one-tailed or two-tailed. The one-tailed test is appropriate when there is a difference between groups in a specific direction. It is less common than the two-tailed test.

When choosing a t-test, you will need to consider two things: whether the groups being compared come from a single population or two different populations, and whether you want to test the difference in a specific direction.

**There are three main types of t-test:**
- **One Sample t-test:** Compares mean of a single group against a known/hypothesized population mean.
- **Two Sample: Paired Sample t-test:** Compares means from the same group at different times.
- **Two Sample: Independent Sample t-test:** Compares means for two different groups.

**One Sample t-test:**

t = (x̄ − μ) / (s / √n)

Where:
- x̄ = Sample mean
- μ = Population mean
- s = Sample standard deviation
- n = Sample size

**Two-Sample Paired Sample t-test:**

t = d̄ / (s / √n)

Where:
- d̄ = Mean of the difference
- s = Standard deviation of the difference
- n = Sample size (i.e., size of d)

**Decision Rules:**
- If the calculated t-value is less than the critical t-value or greater than the critical value (obtained from a critical value table called the T-distribution table), then reject the null hypothesis.
- P-value < significance level (α) => Reject your null hypothesis in favor of your alternative hypothesis. Your result is statistically significant.
- P-value >= significance level (α) => Fail to reject your null hypothesis. Your result is not statistically significant.

---

## Experiment 4

**Abstract:** The objective is to perform exploratory data analysis on the Seaborn Titanic and Penguins datasets by applying suitable data visualization techniques in order to understand the underlying structure and behavior of the data.

- The Titanic dataset consists of numerical attributes such as age and fare, along with categorical attributes including sex, passenger class, and embarkation port. The task is to identify and apply appropriate visualization methods to represent frequency distributions of categorical variables and distribution characteristics of numerical variables, and to analyze survival patterns with respect to gender and class.
- The Penguins dataset consists of numerical attributes such as bill length, bill depth, flipper length, and body mass, along with categorical attributes including species and sex. The task is to visualize physical characteristics across species and analyze relationships between numerical attributes using relational and multivariate plots.
- The final objective is to interpret the visual outputs and draw meaningful inferences that support data-driven understanding and exploratory data analysis skills.

**Theory:**

Visualizations make it easier to explore and extract relevant information from the data by identifying patterns, relationships, outliers, and much more. Seaborn is a statistical plotting library in Python and is an extended version of Matplotlib. It supports complex visualizations and makes the plotting of graphs simple and intuitive. It can be used in Python scripts, Jupyter notebooks, and web application servers.

Seaborn uses less syntax as compared to Matplotlib. Hence, it is easier to use. It is easier to customize themes and high-level interfaces in Seaborn to make the plots more attractive and readable. Seaborn is much more functional and organized than Matplotlib and is better integrated to work with Pandas DataFrames.

Seaborn provides different plots for different types of variables as follows:

**a. Frequency Distribution — Categorical Variables**
- countplot
- catplot

**b. Distribution of Numerical Variables**
- histplot (histogram)
- kdeplot
- boxplot
- violinplot

**c. Relationship between 2 Numerical Variables**
- lineplot
- scatterplot
- relplot
- lmplot
- heatmap
- pairplot
- FacetGrid

**d. Relationship between Numerical and Categorical Variables**
- pointplot
- barplot
- boxplot
- violinplot
- swarmplot
- catplot
- FacetGrid

---

## Experiment 5

**Abstract:** In real-world data analysis, selecting appropriate machine learning models and accurately evaluating their performance is a critical challenge, as different learning paradigms require different validation strategies. This experiment addresses the problem of developing and systematically evaluating supervised and unsupervised learning models using the Iris and Wholesale Customers datasets. The task involves classifying Iris flower species into predefined categories using classification algorithms, and identifying inherent group structures in customer spending data using clustering methods. The performance of each model is assessed using relevant evaluation metrics such as Accuracy, Precision, Recall, F1-score, Confusion Matrix, Silhouette Score, Davies–Bouldin Index, Calinski–Harabasz Index, and Adjusted Rand Index. The experiment aims to analyze and compare the effectiveness of different evaluation measures across classification and clustering tasks to ensure reliable and meaningful model validation.

**Theory:**

**Classification:** Classification predicts categorical labels.

Evaluation Metrics:
- **Accuracy** — Ratio of correct predictions to total predictions.
- **Precision** — Correct positive predictions / Total predicted positives.
- **Recall** — Correct positive predictions / Total actual positives.
- **F1 Score** — Harmonic mean of precision and recall.
- **Confusion Matrix** — Matrix showing actual vs predicted values.
- **ROC Curve (Receiver Operating Characteristic Curve)** — Plots TPR vs FPR.
- **ROC–AUC Score** — Area under ROC curve (measures classification separability).

**Clustering:** Clustering groups similar data points without labels.

Evaluation Metrics:
- **Silhouette Score** — Measures how well samples are clustered.
- **Davies–Bouldin Index** — Lower value indicates better clustering.
- **Calinski–Harabasz Index** — Higher value indicates better clustering.
- **Adjusted Rand Index (ARI)** — Measures similarity between true labels and clusters.

---

## Experiment 6

**Abstract:** The objective is to implement the Synthetic Minority Oversampling Technique (SMOTE) to address the problem of class imbalance in classification datasets. Two datasets are used — the Credit Card Fraud Detection dataset, where fraudulent transactions form a very small minority, and the Breast Cancer Wisconsin dataset, which exhibits class imbalance between benign and malignant cases. The task is to analyze the class distribution, build classification models on the original imbalanced datasets, apply SMOTE to generate synthetic samples for the minority class, retrain the models on the balanced datasets, and evaluate the results using performance metrics such as confusion matrix, accuracy, precision, recall, and F1-score. The impact of SMOTE on classification performance is to be compared and analyzed.

**Theory:**

The most widely used approach to synthesizing new examples is called the Synthetic Minority Oversampling Technique, or SMOTE for short. SMOTE works by selecting examples that are close in the feature space, drawing a line between the examples in the feature space and drawing a new sample at a point along that line. Specifically, a random example from the minority class is first chosen. Then k of the nearest neighbors for that example are found (typically k=5). A randomly selected neighbor is chosen and a synthetic example is created at a randomly selected point between the two examples in feature space. The advantage of SMOTE is that you are not generating duplicates, but rather creating synthetic data points that are slightly different from the original data points.

**The SMOTE algorithm works as follows:**
- Draw a random sample from the minority class.
- For the observations in this sample, identify the k nearest neighbors.
- Take one of those neighbors and identify the vector between the current data point and the selected neighbor.
- Multiply the vector by a random number between 0 and 1.
- To obtain the synthetic data point, add this to the current data point.

This operation is very much like slightly moving the data point in the direction of its neighbor. This way, you make sure that your synthetic data point is not an exact copy of an existing data point while making sure that it is also not too different from the known observations in your minority class.

---

## Experiment 7

**Abstract:** Real-world datasets often contain noise and outliers that affect the accuracy of clustering and data analysis. Traditional clustering algorithms are not always effective in detecting clusters of arbitrary shapes or distinguishing noise points. Therefore, there is a need for a density-based clustering approach that can identify dense regions in a dataset and detect outliers effectively. Apply the DBSCAN algorithm using the Python sklearn library on the Iris and Breast Cancer Wisconsin datasets based on parameters such as epsilon (ε) and minimum points (MinPts). Classify the data points as core, border, or noise based on neighborhood density, and visualize the identified clusters and outliers using the matplotlib library to better interpret the data distribution.

**Theory:**

Density-Based Spatial Clustering of Applications with Noise (DBSCAN) is a base algorithm for density-based clustering. It can discover clusters of different shapes and sizes from a large amount of data, which contains noise and outliers.

**The DBSCAN algorithm uses two parameters:**

- **minPts:** The minimum number of points (a threshold) clustered together for a region to be considered dense. For example, if we set the minPts parameter as 5, then we need at least 5 points to form a dense region.
- **eps (ε):** A distance measure that will be used to locate the points in the neighborhood of any point. It specifies how close points should be to each other to be considered a part of a cluster. If the distance between two points is lower or equal to this value (eps), these points are considered neighbors.

**There are three types of points after the DBSCAN clustering is complete:**

- **Core** — A point that has at least minPts points within distance eps from itself.
- **Border** — A point that has at least one Core point at a distance eps.
- **Noise** — A point that is neither a Core nor a Border. It has less than minPts points within distance eps from itself.

The algorithm proceeds by arbitrarily picking up a point in the dataset (until all points have been visited). If there are at least minPts points within a radius of ε to the point, then we consider all these points to be part of the same cluster. The clusters are then expanded by recursively repeating the neighborhood calculation for each neighboring point.

**DBSCAN algorithm can be abstracted in the following steps:**
- Find all the neighbor points within eps and identify the core points — those visited with more than minPts neighbors.
- For each core point, if it is not already assigned to a cluster, create a new cluster.
- Find recursively all its density-connected points and assign them to the same cluster as the core point.
- Points a and b are said to be density-connected if there exists a point c which has a sufficient number of points in its neighbors and both the points a and b are within the eps distance. This is a chaining process — if b is a neighbor of c, c is a neighbor of d, d is a neighbor of e, which in turn is a neighbor of a, implies that b is a neighbor of a.
- Iterate through the remaining unvisited points in the dataset. Those points that do not belong to any cluster are noise.

---

## Experiment 8

**Abstract:** Real-world datasets often contain abnormal observations that deviate significantly from the majority of the data and may affect the accuracy of data analysis and machine learning models. Traditional data analysis techniques may fail to identify such anomalous points effectively. Therefore, there is a need for a distance-based approach that can measure the similarity between data points and identify those that behave differently from their neighbors. Apply the k-Nearest Neighbours (k-NN) algorithm using Python libraries on the Wine and Breast Cancer Wisconsin datasets by computing the distances between data points and their nearest neighbors. Identify observations that have significantly larger distances from their neighbors and classify them as anomalies. Visualize the detected anomalies to better understand the distribution of normal and abnormal data points in the dataset.

**Theory:**

The k-NN algorithm is a simple and intuitive method for classification and regression tasks, but it can also be adapted for outlier detection.

**Outlier detection using k-NN works as follows:**

1. **Data Preparation:** Begin with a dataset consisting of features and corresponding target labels (if any). Ensure that the features are appropriately scaled, as k-NN is sensitive to differences in feature scales.

2. **Choosing a Value for k:** Decide on the value of k, which represents the number of nearest neighbors to consider when identifying outliers. A smaller value of k may be more sensitive to outliers, while a larger value of k may be more robust but might miss local outliers.

3. **Calculating Distances:** For each data point in the dataset, calculate its distance to the k nearest neighbors. The distance metric used (e.g., Euclidean distance, Manhattan distance) depends on the nature of the data and the problem domain.

4. **Identifying Outliers:** Once distances to the k nearest neighbors are calculated for each data point, calculate a measure of 'outlierness' for each point. This measure could be based on various factors such as the distance to the kth nearest neighbor, the average distance to the k nearest neighbors, or the density of points in the neighborhood.

5. **Setting a Threshold:** Determine a threshold value that defines what constitutes an outlier. This threshold can be set manually based on domain knowledge or statistical properties of the dataset, or it can be determined empirically through techniques such as cross-validation.

6. **Labeling Outliers:** Finally, classify data points as outliers or non-outliers based on whether their 'outlierness' measure exceeds the chosen threshold.

---

## Experiment 9

**Abstract:** Real-world data collected over time often exhibits patterns such as long-term trends, seasonal variations, and random fluctuations. Identifying these components is important for understanding the behavior of the data and for making accurate predictions. However, separating these components from the original time series can be challenging. Therefore, there is a need for methods that can analyze time-dependent data and identify its underlying patterns. Apply time series decomposition techniques to separate the car retail dataset into trend, seasonal, and noise components. Estimate the trend component using the moving averages method and apply Simple Exponential Smoothing on demand data to generate forecasts. Visualize the different components to better understand the underlying patterns present in the time series data.

**Theory:**

A given time series is thought to consist of three systematic components — trend, seasonality, and cycle — and one non-systematic component called noise.

In an **additive decomposition**, the components are decomposed in such a way that when they are added together, the original time series can be obtained:

Time Series = Trend + Seasonality + Noise

In the case of **multiplicative decomposition**, the components are decomposed in such a way that when they are multiplied together, the original time series can be derived back:

Time Series = Trend × Seasonality × Noise

Both additive and multiplicative time series decomposition can be represented by these equations, where Tₜ, Sₜ, and Eₜ are the trend, seasonal, and error components respectively.

The first step in a classical decomposition is to use a **moving average method** to estimate the trend-cycle.

**Moving Averages Method** gives a trend with a fair degree of accuracy. In this method, we take the arithmetic mean of the values for a certain time span. The time span can be three years, four years, five years, and so on depending on the dataset and our interest.
