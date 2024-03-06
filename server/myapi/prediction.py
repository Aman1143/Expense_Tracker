import pickle
import spacy
# import pandas as pd
# import json

def predict_mpg(config):
    ##loading the model from the saved file
    # pkl_filename = "model.pkl"
    # with open(pkl_filename, 'rb') as f_in:
    #     model = pickle.load(f_in)

    # if type(config) == dict:
    #     df = pd.DataFrame(config)
    # else:
    #     df = config
    
    # y_pred = model.predict(df)
    
    # if y_pred == 0:
    #     return 'Extremely Weak'
    # elif y_pred == 1:
    #     return 'Weak'
    # elif y_pred == 2:
    #     return 'Normal'
    # elif y_pred == 3:
    #     return 'Overweight'
    # elif y_pred == 4:
    #     return 'Obesity'
    # elif y_pred == 5:
    #     return 'Extreme Obesity'
    pass

def helper(text):
    clf = open("clf.pkl", 'rb')
    clf = pickle.load(clf)
    nlp = spacy.blank("en")
    vectorizer = pickle.load(open("vector.pickel", "rb"))
    doc = nlp(text)
    amount = -1
    for token in doc:
        if(token.is_digit):
            amount = str(token)
            break
    
    # return amount
    d = dict()
    d['class'] = clf.predict(vectorizer.transform([text]))[0]
    d['amount'] = amount
    
    if d['class']==0:
        return 'Spent '+amount
    elif d['class']==1:
        return 'Earned '+amount
    else:
        return 'Limit '+amount

