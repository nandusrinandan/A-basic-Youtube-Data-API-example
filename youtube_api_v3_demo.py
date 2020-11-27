from apiclient.discovery import build
import pprint as pp
import matplotlib.pyplot as plt
import numpy as np

api_key = "Insert your API key here"
youtube = build('youtube', 'v3', developerKey=api_key)

res1 = youtube.channels().list(part='statistics', forUsername="PewDiePie").execute()
pp.pprint(res1['items'][0]['statistics'])
pewdiepie = res1['items'][0]['statistics']
res2 = youtube.channels().list(part='statistics', forUsername="tanmay316").execute()
pp.pprint(res2['items'][0]['statistics'])
tanmay = res2['items'][0]['statistics']
res3 = youtube.channels().list(part='statistics', forUsername="RavenGrimm").execute()
pp.pprint(res3['items'][0]['statistics'])
keyush = res3['items'][0]['statistics']
res4 = youtube.channels().list(part='statistics', forUsername="AddictedA1").execute()
pp.pprint(res4['items'][0]['statistics'])
carryminati = res4['items'][0]['statistics']
res5 = youtube.channels().list(part='statistics', forUsername="MrSuicideSheep").execute()
pp.pprint(res5['items'][0]['statistics'])
suicidesheep = res5['items'][0]['statistics']

plot1 = plt.figure(1)
height = [int(pewdiepie['subscriberCount']),int(tanmay['subscriberCount']),int(keyush['subscriberCount']),int(carryminati['subscriberCount']),int(suicidesheep['subscriberCount'])]
bars = ('PewdiePie', 'Tanmay Bhat', 'Keyush the Stunt Dog', 'CarryMinati', 'Mr.Suicidesheep')
y_pos = np.arange(len(bars))
plt.barh(y_pos, height)
plt.yticks(y_pos, bars)
plt.title('Subscribers')

plot2 = plt.figure(2)
height2 = [int(pewdiepie['viewCount']),int(tanmay['viewCount']),int(keyush['viewCount']),int(carryminati['viewCount']),int(suicidesheep['viewCount'])]
bars2 = ('PewdiePie', 'Tanmay Bhat', 'Keyush the Stunt Dog', 'CarryMinati', 'Mr.Suicidesheep')
y_pos2 = np.arange(len(bars))
plt.barh(y_pos2, height2)
plt.yticks(y_pos2, bars2)
plt.title('View Count')

plt.show()
