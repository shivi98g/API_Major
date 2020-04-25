

import requests
import pandas as pd


filename = "./Data_AB_E.csv"
#print("Imported Task1 Data:  data_AB_E")
dataset = pd.read_csv(filename)

signals_all = dataset.drop(columns=['y'])  # drop 1st and last column as they are not rqd

#dataset=dataset.drop(columns=['Unnamed: 0'])

labels_all = dataset['y']  # add last column to output


signal=''
for i in range((signals_all.shape[0])):
    signal=(list(signals_all.iloc[i, :]))



label_string_sent=''
label_sent=labels_all[0]

if(label_sent==2):
    label_string_sent='Unhealthy Person'
else :
    label_string_sent = 'Healthy Person'


print('Sent Label: '+label_string_sent)
print("EEG Signal Sent ")
print(signal)

resp = requests.post("http://localhost:5000/web",json={'data':signal} )

print("Predicted value :")
print(resp.json())