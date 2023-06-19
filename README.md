# POKCreate
> Practical Exercise in Deploying ML in a Project

## Description

This is a project developed as part of the DevLabs program at the Canada Revenue Agency with the purpose of practicing the deployment of machine learning models in a useable application.

POKCreate is a Pokemon creator where you can enter your stats and have your pokemon classified into one of 5 automatically detected clusters.
The dataset behind the model comes from [Kaggle](https://www.kaggle.com/datasets/abcsds/pokemon)! 

This project was developed in June 2023 during a 2 week sprint so it is lacking complexity, but it served well as an experience in deploying my model. 

## About the Model

The dataset was unlabelled, so KMeans was used on the 6 main stats of the pokemon (HP, ATK, DEF, SP. DEF, SP. ATK, Speed) to develop our own cluster labels. 
To create the classifier, KNN was trained on 80% of the data and tuned with cross-validation. There's more information on this kind of thing in the 'model' page!

There are radar charts for each cluster available, as well as short descriptions and names in the 'visualize' page! 

