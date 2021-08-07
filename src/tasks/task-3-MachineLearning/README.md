# Machine Learning Models

This repository contains the machine learning models created by collaborators in this project. 
There are two types of models present in here.
- Time Series Models
- Natural Language processing Models

## Time Series Analysis:
A time series is a sequence of sequential data points that occur over a particular interval of time. A "metric", in this case, refers to the piece of data that is tracked at each increment of time. Normally, each point is a pair of two items; the moment the metric was measured and the value of that metric at that point of time.

In a time series, time is often the independent variable and the goal is usually to make a forecast for the future. Depending on the frequency of observations, a time series may typically be hourly, daily, weekly, monthly, quarterly and annual.

In this project, several time series forcasting models have been created to forecast death count of people.

### Time Series Models:

#### [LSTM: Prediction of Death Count (Weekly)](https://github.com/OmdenaAI/omdena-bangladesh-roadsafety/blob/main/src/tasks/task-3-MachineLearning/Time-Series%20Analysis/lstm-ts-forecast-dhaka-tribune-weekly.ipynb)
>
* Mean Absolute Error: 2.7500
* Mean Squared Error: 14.5000
* Root Mean Square Error: 3.8079
* Mean Absolute Percentage Error: 28.8332
* R2 Score: 0.7197

#### [CNN-LSTM: Prediction of Death Count (Weekly)](https://github.com/OmdenaAI/omdena-bangladesh-roadsafety/blob/main/src/tasks/task-3-MachineLearning/Time-Series%20Analysis/cnn-lstm-ts-forecast-dhaka-tribune-weekly.ipynb)

* Mean Absolute Error: 3.1250
* Mean Squared Error: 20.1250
* Root Mean Square Error: 4.4861
* Mean Absolute Percentage Error: 32.9444
* R2 Score: 0.6110

#### [ARIMA: Prediction of Death Count (Weekly)](https://github.com/OmdenaAI/omdena-bangladesh-roadsafety/blob/main/src/tasks/task-3-MachineLearning/Time-series-analysis(ARIMA%2C%20Facebook%20prophet)/Time_series_prediction(updated).ipynb)


* Mean Absolute Error: 7.0
* Mean Squared Error: 59.8571
* Root Mean Square Error: 7.7367
* Mean Absolute Percentage Error: 99.2122
* R2 Score: 0.1197

#### [Facebook Prophet: Prediction of Death Count (Weekly)](https://github.com/OmdenaAI/omdena-bangladesh-roadsafety/blob/main/src/tasks/task-3-MachineLearning/Time-series-analysis(ARIMA%2C%20Facebook%20prophet)/Time_series_prediction(updated).ipynb)


* Mean Absolute Error: 12.5054
* Mean Squared Error: 380.8478
* Root Mean Square Error: 19.5153
* Mean Absolute Percentage Error: inf
* R2 Score: -0.2961

