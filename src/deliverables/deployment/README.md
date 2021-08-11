## Launch the website 
[![](https://brand.heroku.com/static/media/heroku-logo-stroke-black.bc730a06.svg)](https://road-safety-bd-omdena.herokuapp.com/)

## How to Reproduce this Web Application

To recreate this web app on your own computer, do the following.

### Create conda environment
Firstly, we will create a conda environment called *bd-road-safety*
```
conda create -n bd-road-safety python=3.7.9
```
Secondly, we will login to the *bd-road-safety* environement
```
conda activate bd-road-safety
```
### Install prerequisite libraries

Download requirements.txt file

```
wget https://github.com/TechForGoodInc/MLaaS/blob/main/Natural%20Language%20Processing/Streamlit/requirements.txt
```

Pip install libraries
```
pip install -r requirements.txt
```

### Download and unzip this directory

Download [this directory](https://github.com/TechForGoodInc/MLaaS/tree/main/Natural%20Language%20Processing/Streamlit) and unzip as your working directory.

###  Launch the app

```
streamlit run app.py
```
