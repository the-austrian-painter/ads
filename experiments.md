# Applied Data Science — Experiments

---

## Experiment 1

**Aim:** To perform descriptive statistical analysis on a real-world time-based dataset using statistical computing and data analysis tools in order to evaluate central tendency, variability, distribution characteristics, and risk-causing outliers for effective decision-making under uncertainty.

### Exercise 1: Descriptive Statistics on BMI Dataset

**Dataset:** A fictitious dataset of Body Mass Index (BMI) containing 10 observations and 5 variables — Height, Weight, Age, BMI, and Gender.

**Abstract:**
- What is the typical BMI level of the study group, and how much variability exists in body mass across individuals falling within the clinical risk ranges of 25–27 (pre-diabetic), 28–30 (hypertensive–cholesterol), and ≥30 (obesity–cardiac)?
- Does the distribution of BMI exhibit asymmetry and heavy-tailed behavior due to the presence of individuals in the extreme obesity category (BMI ≥ 30), indicating concentrated cardiac risk within the group?
- Are any individuals statistically abnormal based on BMI Z-scores, particularly in the obesity range (BMI ≥ 30), and do these individuals emerge as true medical risk outliers capable of distorting overall group health assessment?
- Which individual BMI values act as dominant health-risk contributors by disproportionately inflating the group's average BMI and overall disease-risk perception?
- If preventive health planning must be based on a single robust statistical measure, should the group intervention strategy rely on mean BMI or median BMI to minimize misclassification caused by extreme obesity values (BMI ≥ 30)?

---

### Exercise 2: Descriptive Statistics on Wine Dataset

**Dataset:** A wine quality dataset containing physicochemical properties such as fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, alcohol, sulphates, density, pH, and a sensory quality score (0–10).

**Abstract:**
- What is the typical alcohol content and quality score of the wine samples, and how much variability exists in these attributes across wines categorized as low quality (≤4), medium quality (5–6), and high quality (≥7)?
- Does the distribution of alcohol content or volatile acidity exhibit skewness or heavy-tailed behaviour, particularly due to the presence of wines with exceptionally high alcohol levels or acidity, indicating concentrated quality-enhancing or quality-degrading effects?
- Are there any wines that can be classified as statistical outliers based on Z-scores of alcohol content, sulphates, or volatile acidity, and do these extreme values correspond to unusually high- or low-quality ratings?
- Does the presence of wines with very high alcohol content cause a noticeable difference between the mean and median alcohol values, indicating the influence of extreme observations?
- How large is the spread (standard deviation and interquartile range) of alcohol content, and does it suggest that most wines cluster around a typical alcohol level or are widely dispersed?

---

## Experiment 2

**Aim:** To preprocess a given dataset by handling missing values, encoding categorical variables, and applying feature scaling techniques to make the data suitable for machine learning analysis.

### Exercise 1: Standardization and Normalization of Wine Dataset

**Dataset:** Wine Quality Dataset — https://drive.google.com/file/d/1h517mn-VNYMQqMun6XJv9ip5dUHpZgst/view?usp=drive_link

**Abstract:** The dataset is a Wine dataset consisting of multiple numerical attributes representing the chemical properties of wine samples. These features are measured on different scales and ranges, which can negatively influence the performance of machine learning algorithms that are sensitive to feature magnitude. The problem is to preprocess the wine dataset by applying standardization and normalization techniques to rescale the numerical features, ensuring uniform feature contribution and making the dataset suitable for effective machine learning analysis.

---

### Exercise 2: Missing Value Imputation and Encoding of Customer Dataset

**Dataset:** Customer Demographic and Purchasing Dataset — https://docs.google.com/spreadsheets/d/1q807a7AR9_kuP7RkW5SsEY4LoxTkm21Z/edit?usp=drive_link&ouid=103898840011638763198&rtpof=true&sd=true

**Abstract:** A retail company has collected customer demographic and purchasing information to analyze buying behavior and build predictive models. The collected dataset includes numerical attributes such as age and annual income, as well as categorical attributes like gender, city, and purchase status. However, the dataset contains missing values and non-numeric data, making it unsuitable for direct use in machine learning algorithms. The objective of this task is to preprocess the dataset by handling missing values using appropriate imputation techniques, converting categorical variables into numerical form using label encoding and one-hot encoding, and applying feature scaling through standardization and normalization. The preprocessed dataset will be used for further data analysis and model building.

---

## Experiment 3

**Aim:** To analyze the inferential statistical results of the given dataset.

### Exercise 1: Paired Sample t-test on Website Response Time

**Dataset:** Website Response Time Optimization Dataset

| Test_Case | Response_Time_Before (ms) | Response_Time_After (ms) |
|-----------|--------------------------|--------------------------|
| T1        | 420                      | 360                      |
| T2        | 450                      | 390                      |
| T3        | 410                      | 355                      |
| T4        | 470                      | 400                      |
| T5        | 440                      | 380                      |
| T6        | 460                      | 395                      |
| T7        | 430                      | 370                      |
| T8        | 445                      | 385                      |

**Abstract:** A paired sample t-test is conducted to evaluate the impact of backend optimization techniques on website response time. Performance measurements collected before and after optimization for the same test cases are analyzed to determine whether the observed reduction in response time is statistically significant. This exercise helps students develop analytical skills in performance evaluation and evidence-based system optimization using inferential statistics.

---

### Exercise 2: One-Sample t-test on Smart Energy Meter Consumption

**Dataset:** Smart Energy Meter Consumption Dataset (Assumed population mean daily consumption = 11 kWh)

| Household_ID | Daily_Energy_Consumption (kWh) |
|--------------|-------------------------------|
| H1           | 11.2                          |
| H2           | 10.8                          |
| H3           | 11.5                          |
| H4           | 10.6                          |
| H5           | 11.0                          |
| H6           | 11.3                          |
| H7           | 10.9                          |
| H8           | 11.1                          |
| H9           | 10.7                          |
| H10          | 11.4                          |

**Abstract:** This exercise involves applying a one-sample t-test to analyze daily electricity consumption recorded from smart energy meters. The objective is to examine whether the average energy usage of households significantly differs from a predefined standard consumption level. Students will analyze the data by framing appropriate hypotheses, calculating the test statistic, and interpreting the results to support data-driven decisions related to energy efficiency and consumption monitoring.

---

## Experiment 4

**Aim:** To explore data visualization techniques on the given dataset.

### Exercise 1: Visualization-Based Analysis of the Titanic Dataset

**Dataset:** Seaborn Titanic Dataset

**Abstract:** Using the Seaborn Titanic dataset, perform exploratory data visualization to understand passenger survival patterns.

1. Visualize the frequency distribution of categorical variables such as sex, class, and embarkation port using appropriate plots.
2. Analyse the distribution of numerical variables such as age and fare using suitable distribution plots.
3. Examine the relationship between passenger class and fare using comparative plots.
4. Visualize survival rates with respect to gender and passenger class.
5. Interpret the visualizations and summarize the key insights regarding factors that influenced passenger survival.

---

### Exercise 2: Visualization-Based Analysis of the Penguins Dataset

**Dataset:** Seaborn Penguins Dataset

**Abstract:** Using the Seaborn Penguins dataset, perform exploratory data visualization to study physical characteristics across different penguin species.

1. Visualize the distribution of numerical attributes such as bill length, bill depth, and body mass.
2. Compare physical characteristics across different species and sex using appropriate categorical–numerical plots.
3. Analyse the relationship between flipper length and body mass using relational plots.
4. Use multivariate visualizations to observe interactions among multiple attributes.
5. Draw meaningful inferences from the visual analysis and discuss observable patterns or differences among species.

---

## Experiment 5

**Aim:** To evaluate the performance of different machine learning models using standard evaluation metrics.

### Exercise 1: Classification on the Iris Dataset (Supervised Learning)

**Dataset:** Iris Flower Dataset — UCI Repository: https://archive.ics.uci.edu/ml/datasets/iris

**Abstract:** The objective is to predict the species of an Iris flower based on its sepal and petal measurements. The Iris dataset consists of 150 samples, each described by four numerical features: sepal length, sepal width, petal length, and petal width. A suitable classification model such as Logistic Regression, K-Nearest Neighbors, or Decision Tree is to be developed. The task involves performing exploratory data analysis and necessary preprocessing, followed by training and validating the model on the given data. The performance of the trained model is to be assessed using standard evaluation metrics including accuracy, precision, recall, F1-score, and confusion matrix, along with cross-validation to ensure reliability. The results obtained from these evaluation strategies are to be interpreted to understand the effectiveness of the model and the significance of each performance metric.

---

### Exercise 2: Clustering on the Wholesale Customers Dataset (Unsupervised Learning)

**Dataset:** Wholesale Customers Data Set
- UCI Repository: https://archive.ics.uci.edu/ml/datasets/wholesale+customers
- Kaggle: https://www.kaggle.com/datasets/binovi/wholesale-customers-data-set

**Abstract:** The objective is to segment wholesale customers based on their annual spending patterns across different product categories. The Wholesale Customers dataset contains numerical attributes representing yearly expenditure on items such as fresh products, milk, grocery, frozen foods, detergents and paper, and delicatessen. Since no predefined class labels are available, unsupervised learning techniques are to be applied to identify natural groupings within the data. The task involves performing exploratory data analysis and preprocessing steps such as feature scaling, followed by the application of a clustering algorithm like K-Means or Hierarchical Clustering. The optimal number of clusters is to be determined using evaluation techniques such as the Elbow method and Silhouette score. The resulting clusters are to be visualized using dimensionality reduction techniques like PCA, and the cluster characteristics are to be analyzed and interpreted to understand customer segmentation and spending behavior.

---

## Experiment 6

**Aim:** To implement the SMOTE technique to generate synthetic data to solve the problem of class imbalance.

### Exercise 1: SMOTE on Credit Card Fraud Detection

**Dataset:** Credit Card Fraud Detection — https://github.com/MedicharlaKarthik/Credit-Card-Fraud-Detection

**Abstract:** The Credit Card Fraud Detection dataset contains transactions made by credit card holders, where fraudulent transactions form a very small minority compared to legitimate transactions, resulting in a highly imbalanced dataset. Perform exploratory data analysis and preprocessing to understand the class distribution. Build a classification model to detect fraudulent transactions and evaluate its performance using metrics such as confusion matrix, precision, recall, F1-score, and accuracy. Apply SMOTE (Synthetic Minority Over-sampling Technique) to balance the dataset and retrain the model. Compare model performance before and after applying SMOTE and interpret the impact of class imbalance handling on model evaluation metrics.

---

### Exercise 2: SMOTE on Breast Cancer Wisconsin Dataset

**Dataset:** Breast Cancer Wisconsin (Diagnostic) — https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)

**Abstract:** The Breast Cancer Wisconsin dataset contains diagnostic measurements of breast cell nuclei used to classify tumors as benign or malignant. The dataset exhibits class imbalance that may affect classification performance. Perform data preprocessing and exploratory analysis, followed by training a classification model for tumor prediction. Evaluate model performance using confusion matrix, accuracy, precision, recall, and F1-score. Apply SMOTE to balance the minority class and compare the performance of the model before and after resampling. Analyze the improvement in classification performance and discuss the effectiveness of SMOTE in handling imbalanced datasets.

---

## Experiment 7

**Aim:** To implement outlier detection using a density-based method.

### Exercise 1: DBSCAN Outlier Detection on Iris Dataset

**Dataset:** Iris Dataset — UCI Repository: https://archive.ics.uci.edu/ml/datasets/iris

**Abstract:** Apply the DBSCAN density-based clustering algorithm on the Iris dataset to analyze the distribution of data points. Identify dense regions that form clusters and detect possible outliers in the dataset based on the parameters epsilon (ε) and minimum points (MinPts). Visualize the resulting clusters and noise points using appropriate Python libraries.

---

### Exercise 2: DBSCAN Outlier Detection on Breast Cancer Wisconsin Dataset

**Dataset:** Breast Cancer Wisconsin (Diagnostic) — https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)

**Abstract:** Use the DBSCAN algorithm to perform density-based clustering on the Breast Cancer Wisconsin dataset. Analyze the dataset to identify clusters of similar data points and detect observations that behave as outliers or noise. Visualize the clusters and detected outliers to understand the density distribution of the data.

---

## Experiment 8

**Aim:** To implement distance-based anomaly detection using k-Nearest Neighbours.

### Exercise 1: k-NN Anomaly Detection on Wine Dataset

**Dataset:** Wine Dataset — UCI Repository: https://archive.ics.uci.edu/ml/datasets/wine

**Abstract:** The Wine dataset contains chemical analysis results of wines derived from three different cultivars, with multiple features representing chemical properties such as alcohol content, ash, and flavonoids. In such datasets, some observations may significantly differ from the general pattern of the data. Apply the k-Nearest Neighbours (k-NN) algorithm to analyze the dataset by computing the distances between data points and their nearest neighbors. Identify observations that show unusually large distances compared to neighboring points and classify them as anomalies. Visualize the detected anomalies to understand the distribution of normal and abnormal observations in the dataset.

---

### Exercise 2: k-NN Anomaly Detection on Breast Cancer Wisconsin Dataset

**Dataset:** Breast Cancer Wisconsin (Diagnostic) — UCI Repository: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)

**Abstract:** The Breast Cancer Wisconsin dataset contains features computed from digitized images of breast mass samples, describing characteristics such as radius, texture, smoothness, and compactness. Variations in these features may indicate abnormal patterns in the dataset. Apply the k-Nearest Neighbours (k-NN) algorithm to analyze the dataset by measuring the distance between data points and their nearest neighbors. Identify observations that deviate significantly from the majority of the data and classify them as anomalies. Visualize the detected anomalies to interpret the distribution of normal and abnormal data points.

---

## Experiment 9

**Aim:** To implement time series decomposition and moving averages method of trend estimation.

### Exercise 1: Time Series Decomposition on Car Retail Dataset

**Dataset:** Car Retail Dataset (given in program)

**Abstract:** Retail sales data collected over time often exhibits patterns such as long-term trends, seasonal variations, and random fluctuations, making it difficult to directly interpret the underlying behavior. Identifying and separating these components is essential for accurate analysis and forecasting. However, extracting these patterns from raw data can be challenging due to their overlapping nature. Therefore, there is a need for techniques that can decompose time series data into its fundamental components. Apply time series decomposition methods on the car retail dataset to separate it into trend, seasonal, and residual components, and analyze the patterns present in the data.

---

### Exercise 2: Simple Exponential Smoothing on Demand Dataset

**Dataset:** Monthly Product Demand Dataset (given in program)

**Abstract:** In many real-world scenarios, demand data collected over time may exhibit fluctuations due to random variations, making it difficult to identify the underlying pattern. Traditional methods like moving averages assign equal weights to past observations, which may not adequately reflect recent changes. Therefore, there is a need for a method that gives more importance to recent data points. Exponential smoothing is a forecasting technique that assigns exponentially decreasing weights to older observations while giving higher importance to recent values. This exercise focuses on applying Simple Exponential Smoothing (SES) to smooth demand data and generate forecasts. The results help in understanding how smoothing reduces noise and how future values are predicted based on past observations.

**Tasks:**
1. Implement Simple Exponential Smoothing on the given demand dataset using a smoothing constant α = 0.3.
2. Compute the smoothed values manually for the first few observations.
3. Use Python to calculate smoothed values and forecast the next 3 periods.
4. Plot the original data, smoothed values, and forecasted values.
5. Analyze the effect of different values of α on the smoothing behavior.
