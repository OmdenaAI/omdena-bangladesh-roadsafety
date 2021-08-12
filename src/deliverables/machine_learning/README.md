# Machine Learning Final Models

This repository contains the machine learning models of this project which are finilized for deployment.
There are three types of models present in here.
- Time Series Forecasting Models
- Time Series Classification Models
- Natural Language processing Models

## Time Series Analysis:

A time series is a sequence of sequential data points that occur over a particular interval of time. A "metric", in this case, refers to the piece of data that is tracked at each increment of time. Normally, each point is a pair of two items; the moment the metric was measured and the value of that metric at that point of time.

In a time series, time is often the independent variable and the goal is usually to make a forecast for the future. Depending on the frequency of observations, a time series may typically be hourly, daily, weekly, monthly, quarterly and annual.



### Time Series Forecasting Models:

**In this project, several time series forcasting models have been created to forecast death count of people.**

#### [LSTM: Prediction of Death Count (Weekly)](https://github.com/OmdenaAI/omdena-bangladesh-roadsafety/blob/main/src/deliverables/machine_learning/LSTM%20TS%20Forecast.ipynb)
>
* Mean Absolute Error: 2.7500
* Mean Squared Error: 14.5000
* Root Mean Square Error: 3.8079
* Mean Absolute Percentage Error: 28.8332
* R2 Score: 0.7197


#### [ARIMA: Prediction of Death Count (Weekly)](https://github.com/OmdenaAI/omdena-bangladesh-roadsafety/blob/main/src/deliverables/machine_learning/ARIMA_Time-series_prediction.ipynb)


* Mean Absolute Error: 7.0
* Mean Squared Error: 59.8571
* Root Mean Square Error: 7.7367
* Mean Absolute Percentage Error: 99.2122
* R2 Score: 0.1197


### Time Series Classification Models:

**In this project, Time Series Classification model has been trained to find if there will be any death in a particular date.**

#### [PyCaret QDA: death or not?](https://github.com/OmdenaAI/omdena-bangladesh-roadsafety/blob/main/src/deliverables/machine_learning/QDA%20TS%20Classification.ipynb)


* Accuracy Score of Test Set: 0.6222<br>
--
* Micro Average Recall Score: 0.6222
* Macro Average of Recall Score: 0.6037
* Weighted Average of Recall Score: 0.6222<br>
--
* Micro Average Precision Score: 1
* Macro Average of Precision Score: 0.5936
* Weighted Average of Precision Score: 0.6509<br>
--
* Micro Average of F1 Score: 0.6222
* Macro Average of F1 Score: 0.5933
* Weighted Average of F1 Score: 0.6319




## Natural Language Processing (NLP):

Natural language processing (NLP) refers to the branch of computer science—and more specifically, the branch of artificial intelligence or AI—concerned with giving computers the ability to understand text and spoken words in much the same way human beings can.

NLP combines computational linguistics—rule-based modeling of human language—with statistical, machine learning, and deep learning models. Together, these technologies enable computers to process human language in the form of text or voice data and to ‘understand’ its full meaning, complete with the speaker or writer’s intent and sentiment.


### Natural Language Processing (NLP) model:

**In this project, a Natural Language Processing model has been created which uses Named Entity Recognition (NER) to extract the accident prone location names.**

#### [Named_Entity_Recognition](https://github.com/OmdenaAI/omdena-bangladesh-roadsafety/blob/main/src/deliverables/machine_learning/named_entity_recognition_with_heatmap.ipynb)

**The Heatmap:**

![Heat_Map](heatmap_from_NER.png)
