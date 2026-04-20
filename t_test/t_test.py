# -*- coding: utf-8 -*-
"""t-test.ipynb

"""

import pandas as pd
from scipy import stats

reliance_data = pd.read_excel('/content/RelianceDataMart.xlsx')

reliance_data.describe()

one_sample_result = stats.ttest_1samp(reliance_data, 25.0)

one_sample_result

#Since the p-value is less than the significance level we reject the null hypothesis.
#This suggests that there is a statistically significant difference between the sample mean and the hypothesized population mean of 25.0.



pre_post_score = pd.read_excel("/content/Pre_Post_Score.xlsx")

two_sample_result = stats.ttest_ind(pre_post_score['Pre_Score'], pre_post_score['Post_Score'])

two_sample_result

#Null hypothesis: there is no significant diff between marks of students before and after the course
#Alternative hypothesis: there is a significant diff between marks of students before and after the course

#Since the p-value is greater than significant value, we reject the null hypothesis.



crocin = pd.read_excel("/content/Crocin_Data_ST.xlsx")

two_sample_result2 = stats.ttest_ind(crocin['Before_Crocin'], crocin['After_Crocin'])

two_sample_result2

#Null hypothesis: there is no significant diff between patient's temperature before and after taking tablet
#Alternative hypothesis: there is a significant diff between patient's temperature before and after taking tablet

#Since the p-value is greater than significant value, we reject the null hypothesis.
