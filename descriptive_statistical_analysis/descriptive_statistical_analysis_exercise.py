# -*- coding: utf-8 -*-
"""descriptive_statistical_analysis_exercise.ipynb



exercise 1
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df=pd.read_csv('bmi.csv')

desc_stats = df.describe()
# BMI analysis
bmi = df["bmi"]
bmi_stats = {
 "Mean BMI": bmi.mean(),
 "Median BMI": bmi.median(),
 "Std Dev BMI": bmi.std(),
 "Skewness": bmi.skew(),
 "Kurtosis": bmi.kurt()
}
# Z-scores
df["BMI_Zscore"] = (bmi - bmi.mean()) / bmi.std()
desc_stats, bmi_stats, df

# Typical BMI & Variability:
# The group’s typical BMI is approximately 26.2 with moderate variability (SD ≈ 2.6), spanning pre-diabetic, hypertensive, and obesity-cardiac risk ranges.
# Asymmetry & Heavy-Tail:
# The BMI distribution shows slight right skewness due to one obese individual (BMI ≥ 30) but does not exhibit strong heavy-tailed behavior.
# Z-Score Outliers:
# No individuals have BMI Z-scores exceeding ±2, indicating no statistical outliers, even within the obesity range.
# Dominant Risk Contributors:
# BMI values around 29.7 and 30.1 disproportionately elevate the mean BMI, acting as dominant contributors to perceived group health risk.
# Mean vs Median for Planning:
# Median BMI is preferred over mean BMI as it is more robust and less influenced by extreme obesity values.

"""exercise 2"""

df=pd.read_csv('wine.csv')

# Basic descriptive statistics
desc = df.describe()
# Alcohol and quality focused analysis
alcohol = df["alcohol"]
quality = df["quality"]
stats = {
 "Mean Alcohol": alcohol.mean(),
 "Median Alcohol": alcohol.median(),
 "Std Alcohol": alcohol.std(),
 "Alcohol Skewness": alcohol.skew(),
 "Alcohol Kurtosis": alcohol.kurt(),
 "Mean Quality": quality.mean(),
 "Median Quality": quality.median(),
 "Std Quality": quality.std()
}
# Quality groups
bins = [0,4,6,10]
labels = ["Low","Medium","High"]
df["quality_group"] = pd.cut(df["quality"], bins=bins, labels=labels, include_lowest=True)
group_stats = df.groupby("quality_group")[["alcohol","volatile acidity"]].agg(["mean","std","median"])
# Z-scores for outlier detection
for col in ["alcohol","sulphates","volatile acidity"]:
 df[f"{col}_z"] = (df[col] - df[col].mean()) / df[col].std()
outliers = df[(df["alcohol_z"].abs()>2) | (df["sulphates_z"].abs()>2) | (df["volatile acidity_z"].abs()>2)]
desc, stats, group_stats, outliers.head()

# Typical Alcohol & Quality:
# The typical wine has an alcohol content of about 10.4% and a quality score near 5–6, with higher alcohol and variability observed in high-quality wines.
# Skewness & Heavy-Tail:
# Alcohol content and volatile acidity distributions are right-skewed, reflecting extreme values that enhance or degrade wine quality.
# Statistical Outliers:
# Yes, several wines show Z-score outliers in alcohol, sulphates, or volatile acidity, which correspond to exceptionally high or low quality ratings.
# Mean vs Median Alcohol:
# The mean alcohol level exceeds the median, confirming that high-alcohol wines influence the average.
# Spread of Alcohol Content:
# Alcohol content shows moderate dispersion (SD ≈ 1.07, IQR ≈ 1.3), indicating most wines cluster around a typical alcohol level

