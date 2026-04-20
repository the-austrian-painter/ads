# Applied Data Science - Algorithms

This file contains algorithms for all experiment and exercise programs in this directory. The algorithms are based on the Python scripts and their corresponding notebooks.

---

## Experiment 1: Descriptive Statistical Analysis

### Program: `descriptive_statistical_analysis/descriptive_statistical_analysis.py`

**Algorithm: Descriptive statistics on Party Time dataset**

1. Start.
2. Import `numpy`, `pandas`, `matplotlib.pyplot`, and `scipy.stats`.
3. Read `Party_Data.xlsx` into a DataFrame.
4. Select the `Time` column for statistical analysis.
5. Display the descriptive summary of the `Time` column.
6. Compute and print the mean of `Time`.
7. Compute and print the median of `Time`.
8. Compute and print the mode of `Time`.
9. Compute and print the harmonic mean of `Time`.
10. Find the maximum and minimum values of `Time`.
11. Compute and print the range as `maximum - minimum`.
12. Compute the first quartile and third quartile.
13. Compute and print the interquartile range as `Q3 - Q1`.
14. Draw a boxplot for the `Time` column to visualize spread and possible outliers.
15. Compute and print standard deviation and variance.
16. Compute and print coefficient of variation as `standard deviation / mean`.
17. Compute and print the data quality ratio as `harmonic mean / mean`.
18. Compute and print skewness and kurtosis.
19. Compute and print Z-scores for all `Time` values.
20. Interpret the measures of central tendency, dispersion, shape, and outlier tendency.
21. Stop.

### Program: `descriptive_statistical_analysis/descriptive_statistical_analysis_exercise.py`

**Algorithm: Exercise 1 - BMI descriptive analysis**

1. Start.
2. Import `numpy`, `pandas`, `matplotlib.pyplot`, and `scipy.stats`.
3. Read `bmi.csv` into a DataFrame.
4. Generate descriptive statistics using `describe()`.
5. Select the `bmi` column.
6. Compute mean, median, standard deviation, skewness, and kurtosis for BMI.
7. Store the computed BMI statistics in a dictionary.
8. Compute BMI Z-scores using `(value - mean) / standard deviation`.
9. Add the Z-score values as a new column named `BMI_Zscore`.
10. Review descriptive statistics, computed BMI measures, and Z-scores.
11. Interpret typical BMI, variability, skewness, heavy-tail behavior, and outlier status.
12. Stop.

**Algorithm: Exercise 2 - Wine descriptive analysis**

1. Start.
2. Read `wine.csv` into a DataFrame.
3. Generate descriptive statistics using `describe()`.
4. Select `alcohol` and `quality` columns for focused analysis.
5. Compute mean, median, standard deviation, skewness, and kurtosis for alcohol.
6. Compute mean, median, and standard deviation for quality.
7. Store these summary measures in a dictionary.
8. Create quality groups using bins: low, medium, and high.
9. Group the data by `quality_group`.
10. For each quality group, compute mean, standard deviation, and median of `alcohol` and `volatile acidity`.
11. For `alcohol`, `sulphates`, and `volatile acidity`, compute Z-scores.
12. Mark rows as outliers if the absolute Z-score of any selected column is greater than 2.
13. Review descriptive statistics, group statistics, and detected outliers.
14. Interpret alcohol distribution, quality relationship, skewness, and outlier influence.
15. Stop.

---

## Experiment 2: Data Preprocessing

### Program: `preprocessing/preprocessing.py`

**Algorithm: Missing value imputation on student data**

1. Start.
2. Import `pandas` and `numpy`.
3. Create a student dataset containing marks, gender, and result.
4. Convert the list into a DataFrame.
5. Assign column names: `marks`, `gender`, and `result`.
6. Count missing values in the DataFrame.
7. Split the data into features `X` containing marks and gender, and target `y` containing result.
8. Import `SimpleImputer`.
9. Create a mean imputer for numeric missing values.
10. Fit the imputer on the marks column and replace missing marks with the mean.
11. Create a constant imputer for categorical missing values.
12. Replace missing gender values with `M`.
13. Print the transformed feature matrix.
14. Stop.

**Algorithm: Country, age, and salary preprocessing**

1. Start.
2. Read `CountryAgeSalary.csv` into a DataFrame.
3. Split independent variables into `X` and dependent variable into `Y`.
4. Use mean imputation to replace missing age values.
5. Use median imputation to replace missing salary values.
6. Print the imputed feature matrix.
7. Apply `LabelEncoder` to convert the country column into integer labels.
8. Print the label-encoded data.
9. Apply `OneHotEncoder` through `ColumnTransformer` to one-hot encode the country column.
10. Convert the transformed output into a NumPy array.
11. Select age and salary columns for scaling.
12. Apply `MinMaxScaler` to normalize age and salary to a fixed range.
13. Store normalized values in a DataFrame.
14. Apply `StandardScaler` to standardize age and salary.
15. Store standardized values in a DataFrame.
16. Compare normalization and standardization results.
17. Stop.

### Program: `preprocessing/preprocessing_exercise.py`

**Algorithm: Exercise 1 - Standardization and normalization of wine quality data**

1. Start.
2. Import `pandas`, `numpy`, `StandardScaler`, and `MinMaxScaler`.
3. Read `winequality-red.csv` into a DataFrame.
4. Separate features `X` by dropping the `quality` column.
5. Store the target column `quality` in `y`.
6. Create a `StandardScaler`.
7. Fit and transform all feature columns using standardization.
8. Convert standardized values into a DataFrame with original feature names.
9. Create a `MinMaxScaler`.
10. Fit and transform all feature columns using normalization.
11. Convert normalized values into a DataFrame with original feature names.
12. Display the standardized and normalized feature sets.
13. Stop.

**Algorithm: Exercise 2 - Customer dataset preprocessing**

1. Start.
2. Import preprocessing libraries and `SimpleImputer`.
3. Read `customer_preprocessing_dataset.xlsx` into a DataFrame.
4. Display the original dataset.
5. Identify numerical columns: `Age` and `Annual_Income`.
6. Identify categorical columns: `Gender`, `City`, and `Purchased`.
7. Apply mean imputation to missing numerical values.
8. Apply most-frequent imputation to missing categorical values.
9. Display the imputed dataset.
10. Apply label encoding to the target column `Purchased`.
11. Apply one-hot encoding to `Gender` and `City` using `get_dummies()` with `drop_first=True`.
12. Display the encoded dataset.
13. Drop `Customer_ID` and `Purchased` to form feature matrix `X`.
14. Store `Purchased` as target `y`.
15. Standardize `X` using `StandardScaler`.
16. Normalize `X` using `MinMaxScaler`.
17. Convert both scaled outputs into DataFrames.
18. Display standardized and normalized datasets.
19. Stop.

---

## Experiment 3: T-Test Analysis

### Program: `t_test/t_test.py`

**Algorithm: One-sample t-test on Reliance data**

1. Start.
2. Import `pandas` and `scipy.stats`.
3. Read `RelianceDataMart.xlsx` into a DataFrame.
4. Generate descriptive statistics for the data.
5. Set the hypothesized population mean as `25.0`.
6. Apply one-sample t-test using `stats.ttest_1samp()`.
7. Obtain the t-statistic and p-value.
8. Compare the p-value with the significance level.
9. Reject or accept the null hypothesis based on the decision rule.
10. Stop.

**Algorithm: Independent t-test on pre-course and post-course scores**

1. Start.
2. Read `Pre_Post_Score.xlsx` into a DataFrame.
3. Select `Pre_Score` and `Post_Score` columns.
4. Apply independent two-sample t-test using `stats.ttest_ind()`.
5. Obtain the t-statistic and p-value.
6. State the null hypothesis: no significant difference between pre-score and post-score marks.
7. State the alternative hypothesis: a significant difference exists.
8. Compare the p-value with the significance level.
9. Interpret the result.
10. Stop.

**Algorithm: Independent t-test on Crocin temperature data**

1. Start.
2. Read `Crocin_Data_ST.xlsx` into a DataFrame.
3. Select `Before_Crocin` and `After_Crocin` columns.
4. Apply independent two-sample t-test using `stats.ttest_ind()`.
5. Obtain the t-statistic and p-value.
6. State the null hypothesis: no significant difference in temperature before and after Crocin.
7. State the alternative hypothesis: a significant difference exists.
8. Compare the p-value with the significance level.
9. Interpret the result.
10. Stop.

### Program: `t_test/t_test_exercise.py`

**Algorithm: Exercise 1 - Paired t-test on website response time**

1. Start.
2. Import `pandas` and `scipy.stats`.
3. Create a dataset containing test cases, response time before optimization, and response time after optimization.
4. Convert the data into a DataFrame.
5. Select the before and after response-time columns.
6. Apply paired t-test using `stats.ttest_rel()`.
7. Obtain the t-statistic and p-value.
8. Compare the calculated t-value with the table value and compare p-value with alpha `0.05`.
9. If p-value is less than alpha, conclude that optimization significantly changed response time.
10. Stop.

**Algorithm: Exercise 2 - One-sample t-test on daily energy consumption**

1. Start.
2. Create a dataset containing household IDs and daily energy consumption values.
3. Convert the data into a DataFrame.
4. Set the hypothesized population mean as `11`.
5. Apply one-sample t-test using `stats.ttest_1samp()`.
6. Obtain the t-statistic and p-value.
7. Compare the t-statistic with the critical value and p-value with alpha `0.05`.
8. If p-value is greater than alpha, accept the null hypothesis.
9. Conclude whether the sample mean significantly differs from 11 kWh.
10. Stop.

---

## Experiment 4: Data Visualization

### Program: `visualization/visualization.py`

**Algorithm: Visualization and EDA on the Tips dataset**

1. Start.
2. Import `numpy`, `pandas`, `seaborn`, `matplotlib.pyplot`, `scipy.stats`, and `warnings`.
3. Load the Seaborn `tips` dataset.
4. Convert it into a DataFrame.
5. Check for missing values.
6. Display descriptive statistics for the dataset.
7. Display descriptive statistics for the `tip` column.
8. Select `total_bill` and compute maximum, minimum, standard deviation, median, and mean.
9. Select `tip` and compute maximum, minimum, standard deviation, median, and mean.
10. Draw a count plot for `sex`.
11. Draw a count plot for `sex` grouped by `smoker`.
12. Draw a count plot for `day`.
13. Draw a categorical count plot for `day` grouped by `sex`.
14. Draw distribution plots for `tip`.
15. Draw boxplots for `total_bill` and `tip` to visualize outliers.
16. Create a DataFrame containing `total_bill`, `tip`, and `size`.
17. Compute and print IQR for `total_bill` and `tip`.
18. Draw relational plots between `total_bill` and `tip`, separated by `time`, with smoker and size as additional variables.
19. Draw a scatter plot of `total_bill` versus `tip` grouped by `sex`.
20. Draw a regression plot of `total_bill` versus `tip` separated by `time` and grouped by smoker status.
21. Draw swarm, bar, and violin categorical plots for tip behavior across day and time.
22. Draw a pairplot grouped by `sex`.
23. Compute and draw a correlation heatmap for numeric columns.
24. Apply label encoding to `sex`, `smoker`, `day`, and `time`.
25. Compute and draw another correlation heatmap after encoding categorical variables.
26. Interpret the relationship between total bill, tip, sex, smoker status, day, and time.
27. Stop.

### Program: `visualization/visualization_exercise.py`

**Algorithm: Exercise 1 - Titanic visualization analysis**

1. Start.
2. Import `seaborn` and `matplotlib.pyplot`.
3. Load the Seaborn `titanic` dataset.
4. Create subplots for categorical frequency analysis.
5. Draw count plots for `sex`, `class`, and `embark_town`.
6. Draw histograms with KDE for numerical variables `age` and `fare`.
7. Draw a boxplot to compare passenger `class` with `fare`.
8. Limit the fare axis to improve readability.
9. Draw a bar catplot showing survival rate by passenger class and gender.
10. Interpret frequency distribution, fare distribution, class relationship, and survival pattern.
11. Stop.

**Algorithm: Exercise 2 - Penguins visualization analysis**

1. Start.
2. Load the Seaborn `penguins` dataset.
3. Create subplots for numerical attribute distributions.
4. Draw histograms with KDE for `bill_length_mm`, `bill_depth_mm`, and `body_mass_g`.
5. Draw a violin plot comparing body mass by species and sex.
6. Draw a relational scatter plot between `flipper_length_mm` and `body_mass_g`, grouped by species and styled by sex.
7. Draw a pairplot grouped by species.
8. Interpret differences in physical characteristics across species and sex.
9. Stop.

---

## Experiment 5: Evaluation Metrics

### Program: `eval_metrics/eval_metrics.py`

**Algorithm: Regression metric evaluation on Wine data**

1. Start.
2. Import numerical, plotting, dataset, preprocessing, regression, and metric libraries.
3. Load the Scikit-learn Wine dataset.
4. Store feature data in `X` and class labels in `y`.
5. Create a DataFrame using Wine feature names.
6. Add the class labels as a `class` column.
7. For regression, set `alcohol` as the target variable.
8. Use all columns except `alcohol` and `class` as regression features.
9. Split the regression data into training and testing sets.
10. Train a `LinearRegression` model.
11. Predict alcohol values on the test set.
12. Compute MAE, MSE, RMSE, and R2 score.
13. Print the regression metrics.
14. Copy the original predictions.
15. Add artificial large errors to the first five predictions to simulate outliers.
16. Recompute MAE, MSE, RMSE, and R2 score for original and outlier predictions.
17. Print both sets of metric values.
18. Draw a bar chart comparing original and outlier metric values.
19. Stop.

**Algorithm: Classification metric evaluation on Wine data**

1. Start.
2. Use all Wine features as `X_clf` and the `class` column as `y_clf`.
3. Split the classification data into training and testing sets.
4. Standardize the training data using `StandardScaler`.
5. Apply the same scaler to the test data.
6. Train a Logistic Regression classifier.
7. Predict class labels for the test data.
8. Predict class probabilities for the test data.
9. Compute and print accuracy, macro precision, macro recall, macro F1 score, and confusion matrix.
10. Binarize the test labels for one-vs-rest ROC analysis.
11. Compute multiclass ROC-AUC score.
12. For each class, compute FPR and TPR.
13. Plot ROC curves for all Wine classes.
14. Stop.

**Algorithm: Clustering metric evaluation on Wine data**

1. Start.
2. Select all Wine features except `class` for clustering.
3. Standardize the selected features.
4. Apply K-Means clustering with `n_clusters=3`.
5. Generate cluster labels.
6. Compute Silhouette score.
7. Compute Davies-Bouldin score.
8. Compute Calinski-Harabasz score.
9. Compute Adjusted Rand score by comparing cluster labels with actual Wine class labels.
10. Print all clustering evaluation metrics.
11. Stop.

### Program: `eval_metrics/eval_metrics_exercise.py`

**Algorithm: Exercise 1 - Iris classification and cross-validation**

1. Start.
2. Import `pandas`, train-test splitting, Logistic Regression, and classification metrics.
3. Define column names for the Iris dataset.
4. Read `iris.data` into a DataFrame.
5. Convert the class labels into categorical integer codes.
6. Draw a pairplot grouped by class.
7. Split the data into features `X` and target `y`.
8. Split `X` and `y` into training and testing sets.
9. Train a Logistic Regression classifier.
10. Predict labels on the test set.
11. Compute and print accuracy, macro precision, macro recall, macro F1 score, and confusion matrix.
12. Create a `StratifiedKFold` object with 5 folds.
13. Initialize lists to store accuracy, precision, recall, and F1 scores.
14. For each fold, split the data into training and test fold sets.
15. Train a new Logistic Regression model on the training fold.
16. Predict labels on the test fold.
17. Append accuracy, macro precision, macro recall, and macro F1 score to their lists.
18. Compute mean and standard deviation for each metric.
19. Print the mean and standard deviation values.
20. Stop.

**Algorithm: Exercise 2 - Wholesale customer clustering**

1. Start.
2. Read `Wholesale customers data.csv` into a DataFrame.
3. Display the first five rows, dataset information, missing-value counts, and descriptive statistics.
4. Select spending columns: `Fresh`, `Milk`, `Grocery`, `Frozen`, `Detergents_Paper`, and `Delicassen`.
5. Draw histograms with KDE for all spending columns.
6. Compute the correlation matrix for spending columns.
7. Draw a heatmap of the correlation matrix.
8. Standardize the spending columns using `StandardScaler`.
9. For cluster counts from 1 to 10, fit K-Means and store WCSS values.
10. Plot WCSS against number of clusters to apply the elbow method.
11. For cluster counts from 2 to 10, fit K-Means and compute Silhouette scores.
12. Plot Silhouette score against number of clusters.
13. Fit final K-Means model with `n_clusters=3`.
14. Predict cluster labels for all customers.
15. Add the cluster labels to the original DataFrame.
16. Apply PCA with 2 components to the scaled spending data.
17. Print PCA shape and explained variance ratio.
18. Create a PCA DataFrame containing `PC1`, `PC2`, and cluster labels.
19. Draw a scatter plot of customer segments using the two PCA components.
20. Group customers by cluster and compute mean spending for each product category.
21. Print the spending pattern of each cluster.
22. Stop.

---

## Experiment 6: SMOTE and Class Imbalance

### Program: `smote/smote.py`

**Algorithm: Admission classification before and after SMOTE**

1. Start.
2. Import `pandas` and `seaborn`.
3. Read `Admission_St.xlsx` into a DataFrame.
4. Select columns 1 to 3 as features `X`.
5. Select column 0 as target `Y`.
6. Count target class frequencies.
7. Generate descriptive statistics.
8. Draw a count plot for the `Admit` class distribution.
9. Split the data into training and testing sets.
10. Standardize the training features and transform the test features.
11. Train a Logistic Regression model on the original training data.
12. Predict labels and probabilities on the test data.
13. Compute accuracy, precision, recall, F1 score, and classification report before SMOTE.
14. Apply Random Over Sampling to the training data and inspect class counts.
15. Apply Random Under Sampling to the training data and inspect class counts.
16. Apply SMOTE with `k_neighbors=3` to the training data.
17. Train a second Logistic Regression model on the SMOTE-balanced data.
18. Predict labels and probabilities on the unchanged test data.
19. Compute accuracy, precision, recall, F1 score, and classification report after SMOTE.
20. For class 0 and class 1, compute ROC curves before SMOTE.
21. For class 0 and class 1, compute ROC curves after SMOTE.
22. Compute AUC scores for all four ROC curves.
23. Plot ROC curves for class 0 and class 1 before and after SMOTE.
24. Print AUC scores.
25. Stop.

### Program: `smote/smote_exercise.py`

**Algorithm: Exercise 1 - Credit card fraud detection with SMOTE**

1. Start.
2. Import data handling, preprocessing, Logistic Regression, evaluation metrics, and SMOTE libraries.
3. Read `creditcard.csv` into a DataFrame.
4. Check missing values and generate descriptive statistics.
5. Count values in the target column `Class`.
6. Split the data into features `X` and target `y`.
7. Standardize `Amount` and `Time` columns.
8. Split the data into stratified training and testing sets.
9. Train a Logistic Regression model on the original training data.
10. Predict test labels.
11. Print confusion matrix, accuracy, precision, recall, and F1 score before SMOTE.
12. Apply SMOTE to the training data.
13. Train a second Logistic Regression model on the SMOTE-balanced training data.
14. Predict test labels.
15. Print confusion matrix, accuracy, precision, recall, and F1 score after SMOTE.
16. Predict test probabilities from both models.
17. Compute ROC curve values and AUC scores before and after SMOTE.
18. Plot both ROC curves with a random-classifier reference line.
19. Stop.

**Algorithm: Exercise 2 - Breast cancer diagnosis with SMOTE**

1. Start.
2. Define column names for the Breast Cancer Wisconsin dataset.
3. Read `wdbc.data` into a DataFrame using the defined column names.
4. Check shape, missing values, descriptive statistics, and target distribution.
5. Map diagnosis labels: malignant `M` to `1`, benign `B` to `0`.
6. Drop the `ID` column.
7. Split the data into features `X` and target `y`.
8. Standardize all feature columns.
9. Split the data into stratified training and testing sets.
10. Train a Logistic Regression model on the original training data.
11. Predict test labels.
12. Print confusion matrix, accuracy, precision, recall, and F1 score before SMOTE.
13. Apply SMOTE to the training data.
14. Train a second Logistic Regression model on the SMOTE-balanced data.
15. Predict test labels.
16. Print confusion matrix, accuracy, precision, recall, and F1 score after SMOTE.
17. Predict test probabilities from both models.
18. Compute ROC curve values and AUC scores before and after SMOTE.
19. Plot both ROC curves with a random-classifier reference line.
20. Stop.

---

## Experiment 7: DBSCAN Outlier Detection

### Program: `dbscan/dbscan.py`

**Algorithm: DBSCAN on a small manual dataset**

1. Start.
2. Import `DBSCAN`, `numpy`, and `matplotlib.pyplot`.
3. Create a small two-dimensional array of points.
4. Plot the points.
5. Apply DBSCAN with `eps=3` and `min_samples=2`.
6. Inspect cluster labels.
7. Apply DBSCAN again with `eps=10` and `min_samples=2`.
8. Inspect the new cluster labels and compare the effect of epsilon.
9. Stop.

**Algorithm: DBSCAN on circular synthetic data**

1. Start.
2. Generate circular data using `make_circles`.
3. Create a DBSCAN model with `eps=0.1` and `min_samples=5`.
4. Fit the model and predict cluster labels.
5. Plot the points colored by cluster label.
6. Stop.

**Algorithm: DBSCAN on blob synthetic data**

1. Start.
2. Generate blob data using `make_blobs`.
3. Convert the generated points into a DataFrame with `x` and `y` columns.
4. Plot the original blob data.
5. Apply DBSCAN with `eps=1` and `min_samples=5`.
6. Store the cluster labels.
7. Count the number of unique cluster labels.
8. Count noise points where label is `-1`.
9. Define a helper function to plot each cluster with a separate color and noise in red.
10. Call the helper function to visualize clusters and noise.
11. Stop.

**Algorithm: DBSCAN on Mall Customer data before and after added outliers**

1. Start.
2. Read `Mall_Customers_sample.csv` into a DataFrame.
3. Select `Annual Income (k$)` and `Spending Score (1-100)` as features.
4. Standardize the selected features.
5. Apply DBSCAN with `eps=1.2` and `min_samples=4`.
6. Predict cluster labels before adding new points.
7. Count outliers where label equals `-1`.
8. Plot scaled points colored by cluster and mark outliers in red.
9. Create new extreme points representing possible outliers.
10. Append the new points to the original feature values.
11. Standardize the combined data.
12. Apply DBSCAN again with the same parameters.
13. Predict cluster labels after adding new points.
14. Plot the combined scaled points and mark outliers in red.
15. Count noise points and non-noise points after adding outliers.
16. Interpret DBSCAN behavior with changing data distribution.
17. Stop.

### Program: `dbscan/dbscan_exercise.py`

**Algorithm: Exercise 1 - DBSCAN on Iris dataset**

1. Start.
2. Import numerical, plotting, dataset, DBSCAN, scaling, and PCA libraries.
3. Load the Iris dataset.
4. Select feature data.
5. Standardize features using `StandardScaler`.
6. Apply DBSCAN with `eps=0.8` and `min_samples=5`.
7. Store predicted labels.
8. Find unique cluster labels.
9. Compute number of clusters, excluding label `-1`.
10. Count noise points where label is `-1`.
11. Print cluster labels, number of clusters, and number of noise points.
12. Reduce standardized data to 2 dimensions using PCA.
13. For each cluster label, select a color and label name.
14. Plot PCA points grouped by cluster label, using black for noise.
15. Add axis labels, title, and legend.
16. Stop.

**Algorithm: Exercise 2 - DBSCAN on Breast Cancer dataset**

1. Start.
2. Load the Breast Cancer Wisconsin dataset.
3. Select feature data and target labels.
4. Standardize the feature data.
5. Apply DBSCAN with `eps=2.5` and `min_samples=5`.
6. Store predicted cluster labels.
7. Find unique cluster labels.
8. Compute number of clusters, excluding label `-1`.
9. Count noise points where label is `-1`.
10. Print cluster labels, number of clusters, and number of noise points.
11. Reduce standardized data to 2 dimensions using PCA.
12. Plot PCA points grouped by DBSCAN cluster label, using black for noise.
13. Add axis labels, title, and legend.
14. Stop.

---

## Experiment 8: k-NN Anomaly Detection

### Program: `knn/knn.py`

**Algorithm: k-NN anomaly detection on synthetic data**

1. Start.
2. Import `NearestNeighbors`, `numpy`, and `matplotlib.pyplot`.
3. Set the random seed for reproducibility.
4. Generate normally distributed two-dimensional data.
5. Generate uniformly distributed outlier points.
6. Combine shifted normal clusters and outlier points into one dataset.
7. Fit a `NearestNeighbors` model with `k=10`.
8. Compute distances from each point to its nearest neighbors.
9. Extract the distance to the kth nearest neighbor for each point.
10. Set the anomaly threshold as the 95th percentile of kth-neighbor distances.
11. Mark points with kth-neighbor distance greater than the threshold as outliers.
12. Plot all data points.
13. Highlight detected outliers using red outlined markers.
14. Stop.

**Algorithm: k-NN anomaly detection on customer data**

1. Start.
2. Read `customer.csv` into a DataFrame.
3. Display the first rows and dataset information.
4. Select `Annual_Income` and `Spending_Score` as anomaly-detection features.
5. Standardize the selected features.
6. Fit a `NearestNeighbors` model with `k=5`.
7. Compute distances to nearest neighbors for each customer.
8. Extract the kth-neighbor distance.
9. Set the anomaly threshold as the 90th percentile of kth-neighbor distances.
10. Mark customers above the threshold as outliers.
11. Plot all customers using annual income and spending score.
12. Highlight detected outliers with red outlined markers.
13. Stop.

### Program: `knn/knn_exercise.py`

**Algorithm: Exercise 1 - k-NN anomaly detection on Wine dataset**

1. Start.
2. Load the Scikit-learn Wine dataset.
3. Convert features into a DataFrame with feature names.
4. Print the first five rows.
5. Set `k=5`.
6. Fit a `NearestNeighbors` model on the Wine feature data.
7. Compute nearest-neighbor distances for each observation.
8. Extract the kth-neighbor distance for each observation.
9. Set the anomaly threshold as `mean(kth distances) + 2 * standard deviation(kth distances)`.
10. Select observations whose kth-neighbor distance exceeds the threshold as anomalies.
11. Print detected anomalies.
12. Reduce Wine features to two principal components using PCA.
13. Plot all observations in PCA space.
14. Highlight anomaly points in red.
15. Stop.

**Algorithm: Exercise 2 - k-NN anomaly detection on Breast Cancer dataset**

1. Start.
2. Load the Scikit-learn Breast Cancer dataset.
3. Convert features into a DataFrame with feature names.
4. Print the first five rows.
5. Set `k=5`.
6. Fit a `NearestNeighbors` model on the feature data.
7. Compute nearest-neighbor distances for each observation.
8. Extract the kth-neighbor distance for each observation.
9. Set the anomaly threshold as `mean(kth distances) + 2 * standard deviation(kth distances)`.
10. Select observations above the threshold as anomalies.
11. Print the number of anomalies and the anomaly rows.
12. Reduce features to two principal components using PCA.
13. Plot all observations in PCA space.
14. Highlight anomaly points in red.
15. Stop.

---

## Experiment 9: Time Series Analysis

### Program: `time_series/time_series.py`

**Algorithm: Multiplicative decomposition of airline passenger data**

1. Start.
2. Import `pandas` and `matplotlib.pyplot`.
3. Read `airlinepassenger.csv` with the first column as the index.
4. Plot the time series.
5. Apply seasonal decomposition using a multiplicative model with `period=1`.
6. Plot the decomposed components.
7. Observe trend, seasonal, and residual components.
8. Stop.

**Algorithm: Moving average trend estimation on demand data**

1. Start.
2. Import `pandas`, `numpy`, and `matplotlib.pyplot`.
3. Create a monthly product demand dictionary.
4. Convert the dictionary into a DataFrame.
5. Compute a 3-month simple moving average using rolling mean.
6. Store the result in `pandas_SMA_3`.
7. Compute a 4-month simple moving average using rolling mean.
8. Store the result in `pandas_SMA_4`.
9. Plot original demand, 3-month moving average, and 4-month moving average.
10. Add grid and legend.
11. Stop.

### Program: `time_series/time_series_exercise.py`

**Algorithm: Exercise 1 - Retail time series decomposition**

1. Start.
2. Import `pandas`, `numpy`, plotting libraries, and `seasonal_decompose`.
3. Read `retail.csv` with the first column as the index.
4. Plot the retail time series.
5. Apply multiplicative seasonal decomposition with `period=1`.
6. Plot the decomposed trend, seasonal, and residual components.
7. Interpret the decomposed patterns.
8. Stop.

**Algorithm: Exercise 2 - Simple Exponential Smoothing on demand data**

1. Start.
2. Create monthly product demand data for 12 months.
3. Convert the data into a DataFrame.
4. Import `SimpleExpSmoothing`.
5. Replace the numeric month column with a monthly date range starting from January 2023.
6. Set the month column as the DataFrame index.
7. Create a Simple Exponential Smoothing model on the `demand` series.
8. Fit the model using smoothing level `0.3` and `optimized=False`.
9. Store fitted smoothed values in a new column named `SES_fit`.
10. Forecast demand for the next 3 months.
11. Print the forecasted values.
12. Plot original demand, smoothed demand, and forecasted demand.
13. Add a legend.
14. Stop.

