import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC # "Support Vector Classifier"
def reg(file,impacts,outcome,inps):
    data = pd.read_csv('/content/exam dataset ml.csv')
    X = data[impacts]
    Y = data[outcome]
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    nx = [inps]
    pred = linear_regressor.predict(nx)
    return pred

def classify(file,impacts,outcome,inps):
    data = pd.read_csv('/content/exam dataset ml.csv')
    X = data[impacts]
    Y = data[outcome]
    Y=Y.round()
    clf = SVC(kernel='linear') 
    clf.fit(X,Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred

def inputu(a):
    print("Bot: please enter the following data for me to predict")
    knowledge_transfer=int(input("knowledge transfer: "))
    health_condition = int(input("health condition: "))
    availability = int(input("availability: "))
    preparation = int(input("preparation: "))
    
    if(a=="regression"):
        p = reg('examdatasetml.csv',["KT","HC","AV","PREP"],"RS",[knowledge_transfer,health_condition,availability,preparation])
        print("Bot : The outcome is: ",float(p[0]))
    if((a=="classification")or(a=="classify")): 
        p = classify('examdatasetml.csv',["KT","HC","AV","PREP"],"RD",[knowledge_transfer,health_condition,availability,preparation])
        print("Bot :The outcome is: ",float(p[0]))
print("Bot: Hello.How can I help you?")
msg=input("You: ")
print("Bot: I  can help you in predicting whether you are ready for the exam and how much!")
print("Bot:Do you want me to the predict data ?")
y=input("You : ")
if("yes" in y):
    print("BOT: please enter 'predict' :")
    c=input("You:")
    if "predict" in c:
          print("Bot : I can predict regression and classification for you")
          print("Bot :please enter the model that I can help you with in predicting your data : ")
          a=input("You: ")
          inputu(a)
    else:
      print("Sorry we don't predict this kind of data ")
else:
    print( "Bot: It's ok. Thank you")