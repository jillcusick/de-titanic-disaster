# MLDS-400 Homework 3
# Titanic Disaster Analysis
## Jill Cusick

Please follow the steps below in order to run my Python and R models that address the [Titanic - Machine Learning from Disaster Kaggle competition]https://www.kaggle.com/competitions/titanic/overview. Docker will be used to allow you, the user, to reproduce my code and output on your own machine. You will use Docker to run Python and R scripts that will train regression models using the available training dataset and produce two CSV outputs (one in Python and one in R) with my predictions for Titanic survival per passenger in the test dataset. 

## STEP 1: CLONE REPO
- [ ] Clone this repo onto your machine. (I would suggest using an SSH key.)
- [ ] Open the repo within your preferred IDE. (I used VS Code.) 

## STEP 2: INSTALL DOCKER 

- [ ]If you do not already have Docker, you will need to install it on your machine. 
    If you have a Mac, you can install Docker with this link: [Docker install on Mac]https://docs.docker.com/desktop/setup/install/mac-install/ 
    If you have Windows, you can install Docker with this link: [Docker install on PC]https://docs.docker.com/desktop/setup/install/windows-install/

- [ ]Once you have Docker installed, open it on your machine. 

## STEP 3: DOWNLOAD DATA

The data used in my scripts can be downloaded on Kaggle.

- [ ]Go to this link: [Kaggle data]https://www.kaggle.com/competitions/titanic/data
- [ ]Click test.csv under Data Explorer on the right side and download that file. 
- [ ]Click train.csv under Data Explorer and download that file. 
- [ ]Save files in a subfolder titled "data" under the "src" folder in the repo (src/data/). If you do not save the data here, you will need to update the file path in the Python and R scripts when accessing the data. 

## STEP 4: RUN PYTHON SCRIPT USING DOCKER

Enter the code below in your terminal to build and run the Docker image, and to troubleshoot if the .csv file does not appear. 

Steps:
- [ ]Build docker image: `docker build -f dockerfile-python -t titanic-model-python .`
- [ ]Run docker image: `docker run titanic-model-python`
- [ ]If csv file is not saved in src folder, use this code: `docker run -v $(pwd)/src:/app/src titanic-model-python`

Results: You will see output in the terminal with my print statements after running the docker image. The file test_predictions.csv should save within the src folder. 

## STEP 5: RUN R SCRIPT USING DOCKER

Enter the code below in your terminal to build and run the Docker image, and to troubleshoot if the .csv file does not appear. 

Steps: 
- [ ]Build docker image: `docker build -f dockerfile-r -t titanic-model-r .`
- [ ]Run docker image: `docker run titanic-model-r`
- [ ]If csv file is not saved in src folder, use this code: `docker run -v $(pwd)/src:/app/src titanic-model-r`

Results: You will see output in the terminal with my print statements after running the docker image. The file test_predictions_R.csv should save within the src folder. 