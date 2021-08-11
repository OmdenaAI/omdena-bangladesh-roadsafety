## Launch the Web Application
[![](https://brand.heroku.com/static/media/heroku-logo-stroke-black.bc730a06.svg)](https://road-safety-bd-omdena.herokuapp.com/)

## How to Reproduce this Web Application

To recreate this web app on your own computer, do the following.

### Create Conda Environment
Firstly, we will create a conda environment called *bd-road-safety*
```
conda create -n bd-road-safety python=3.7.9
```
Secondly, we will login to the *bd-road-safety* environement
```
conda activate bd-road-safety
```
### Install Prerequisite Libraries

Download requirements.txt file

```
wget https://github.com/OmdenaAI/omdena-bangladesh-roadsafety/blob/main/src/deliverables/deployment/Streamlit/requirements.txt
```

Pip install libraries
```
pip install -r requirements.txt
```

### Download & Unzip this Directory

Download [this directory](https://github.com/OmdenaAI/omdena-bangladesh-roadsafety/tree/main/src/deliverables/deployment/Streamlit) and unzip as your working directory.

###  Launch the App

```
streamlit run app-bd.py
```
