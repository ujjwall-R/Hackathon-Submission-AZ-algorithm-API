import pandas as pd
from storage import DBStorage


def GetRecommendations():
    # runs the model for recommendation generation to generate the generations
    df = pd.empty()
    return df


def AddRecommendations():
    # addrows in the recommendation
    storage = DBStorage()
    storage.insert_row()


def RetrainRecommendationModel():
    # retrains the model
    print('Retrain recommendation model')


def ViewTracker():  # Track total number of Views from the application
    # assist in retraining
    print('Track total number of Views from the application')
