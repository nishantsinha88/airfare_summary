import requests
import pandas as pd

City1 = input("\nEnter Origin City: ")
City1MMT = City1.replace(" ","_")
City1GoIB = City1.replace(" ","-")
City2 = input("\nEnter Destination City: ")
City2MMT = City2.replace(" ","_")
City2GoIB = City2.replace(" ","-")

Internat = input("\nIs this an international route (Y/N): ")

headerMMT = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

# ~~~~~~~~~~~~~ Make My Trip ~~~~~~~~~~~~~~~~~~~~

if Internat in ['Y', 'y']:
    urlMMT = 'https://www.makemytrip.com/international-flights/' + City1MMT + '-' + City2MMT + '-cheap-airtickets.html'
if Internat in ['N', 'n']:
    urlMMT = 'https://www.makemytrip.com/flights/'+City1MMT+'-'+City2MMT+'-cheap-airtickets.html'

rMMT = requests.get(urlMMT, headers=headerMMT)
dfMMT = pd.read_html(rMMT.text)[0]

print("\n\n"+City1+" - "+ City2 + " - Make My Trip \n\n"+dfMMT.iloc[0:(len(dfMMT.index)-1),0:(len(dfMMT.columns)-1)].to_string())

# ~~~~~~~~~~~~~ GoIbibo ~~~~~~~~~~~~~~~~~~~~

dfGoIB = pd.read_html("https://www.goibibo.com/flights/"+City1GoIB+"-to-"+City2GoIB+"-flights/", header=0)[0]
dfGoIB = dfGoIB[::-1]
dfGoIB = dfGoIB[['Cheapest Fares', 'Fare (INR)', 'Date', 'Airline', 'Departure', 'Arrival']]
print("\n\n"+City1+" - "+ City2 + " - Goibibo\n")
print(dfGoIB[dfGoIB.columns[0:6]].to_string())
