def convert_to_si(radius,mass): 
  for i in range(0,len(radius)-1): 
    radius[i] = radius[i]*6.957e+8 
    mass[i] = mass[i]*1.989e+30 

import pandas as pd
import csv
import plotly.express as px
import matplotlib as plt
f=pd.read_csv('star_with_gravity.csv')
rows=[]
star_data_rows = rows[1:]

name1=[]
star_data=name1[1:]
gravity=[]
mass=f['Mass'].to_list()
radius =f['Radius'].to_list()
star_name=[]
for i in star_data:
  mass.append(star_data[3])
  radius.append(star_data[4])
  name1.append(star_data[1])

star_gravity=[]

for index,name in enumerate(star_name):
  g=convert_to_si(radius,mass)
  print(g)
  
  star_gravity.append(g)
final_dict={}

for index,star_data in enumerate(star_data_rows):
  features_list=[]
  gravity=convert_to_si(radius,mass)
  try:
    if gravity>100 and gravity<350:
      features_list.append('gravity')
  except:
    pass
  
  try:
    if star_data[3]>=100:
      features_list.append("keep")
  except:
    pass  




  final_dict[index]=features_list

print(final_dict)
  