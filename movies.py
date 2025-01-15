# Name: Mohmmad Parvez
# Collaborators: https://youtu.be/JH0eRpB3g_0?si=K02Aas2ywB0P36Yh
                #https://youtube.com/shorts/R4IP0qTZWz8?si=mkttOL-G3arR3GRT
# Comments:     https://youtu.be/Re-TqK9-FYE?si=8RIi8ionCo5yWtzU
    
import pandas as pd



df = pd.read_csv("movies.csv") #Creating a dataframe
del df["Running Time"]
del df["Budget (in $)"]
del df["International Sales (in $)"] #Removing certain columns

df["Domestic Opening(in $)"]= df["Domestic Opening (in $)"].astype(classmethod(int())) #Changing to int type

df["Multiplier"] = df["Domestic Sales (in $)"] / df["Domestic Opening (in $)"] #Adding new Column

def df(leggiest_movies):
    if df["Multiplier"] > 9 and df["Multiplier"] < 251:
        return df["Multiplier"]
    
def df(r_rated):
    return df["Licence"] == "R"

def df(pre_2000):
    return df["Year"] < 2000

def df(non_action):
   return "Action" not in df["Genre"]
    
    



