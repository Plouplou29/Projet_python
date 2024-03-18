#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 
# permet d'importer le module pour les graphiques/courbes...


# ### Récolte des données météo des villes voulues

# In[2]:


import json
import urllib
key="f23dcaf9b7ae8ff919d486adb295dce8" # clé permettant d'accéder aux données

myrequest1="https://api.openweathermap.org/data/2.5/weather?q=Vinon&units=metric&appid=f23dcaf9b7ae8ff919d486adb295dce8"
url1=urllib.request.urlopen(myrequest1)
data1=json.loads(url1.read().decode())
print(data1) #data de Vinon

myrequest2="https://api.openweathermap.org/data/2.5/weather?lat=42.5611&lon=0.0834&units=metric&appid=f23dcaf9b7ae8ff919d486adb295dce8"
url2=urllib.request.urlopen(myrequest2)
data2=json.loads(url2.read().decode())
print(data2) #data du Pic du Midi

myrequest3="https://api.openweathermap.org/data/2.5/weather?q=75014&units=metric&appid=f23dcaf9b7ae8ff919d486adb295dce8"
url3=urllib.request.urlopen(myrequest3)
data3=json.loads(url3.read().decode())
print(data3) #data de Paris

myrequest4="https://api.openweathermap.org/data/2.5/weather?q=Lynde&units=metric&appid=f23dcaf9b7ae8ff919d486adb295dce8"
url4=urllib.request.urlopen(myrequest4)
data4=json.loads(url4.read().decode())
print(data4) #data de Lynde

myrequest5="https://api.openweathermap.org/data/2.5/weather?q=Bischwiller&units=metric&appid=f23dcaf9b7ae8ff919d486adb295dce8"
url5=urllib.request.urlopen(myrequest5)
data5=json.loads(url5.read().decode())
print(data5) #data de Bischwiller

myrequest6="https://api.openweathermap.org/data/2.5/weather?q=Corte&units=metric&appid=f23dcaf9b7ae8ff919d486adb295dce8"
url6=urllib.request.urlopen(myrequest6)
data6=json.loads(url6.read().decode())
print(data6) #data de Porte

myrequest7="https://api.openweathermap.org/data/2.5/weather?q=Nantes&units=metric&appid=f23dcaf9b7ae8ff919d486adb295dce8"
url7=urllib.request.urlopen(myrequest7)
data7=json.loads(url7.read().decode())
print(data7) #data de Nantes

myrequest8="https://api.openweathermap.org/data/2.5/weather?q=Orelle&units=metric&appid=f23dcaf9b7ae8ff919d486adb295dce8"
url8=urllib.request.urlopen(myrequest8)
data8=json.loads(url8.read().decode())
print(data8) #data de Nantes

myrequest9="https://api.openweathermap.org/data/2.5/weather?lat=48.3904&lon=-4.4861&units=metric&appid=f23dcaf9b7ae8ff919d486adb295dce8"
url9=urllib.request.urlopen(myrequest9)
data9=json.loads(url9.read().decode())
print(data9) #data de Brest


# ### Isolation des données de couvertuge nuageuse pour chacune des villes 

# In[3]:


clouds1=data1['clouds']
clouds2=data2['clouds']
clouds3=data3['clouds']
clouds4=data4['clouds']
clouds5=data5['clouds']
clouds6=data6['clouds']
clouds7=data7['clouds']
clouds8=data8['clouds']
clouds9=data9['clouds']
c1=clouds1['all']
c2=clouds2['all']
c3=clouds3['all']
c4=clouds4['all']
c5=clouds5['all']
c6=clouds6['all']
c7=clouds7['all']
c8=clouds8['all']
c9=clouds9['all']
y1=[c1,c2,c3,c4,c5,c6,c7,c8,c9]


# In[4]:


print(y1)


# ### Isolation des données d'humidité  pour chacune des villes 

# In[5]:


main1=data1['main']
main2=data2['main']
main3=data3['main']
main4=data4['main']
main5=data5['main']
main6=data6['main']
main7=data7['main']
main8=data8['main']
main9=data9['main']
h1=main1['humidity']
h2=main2['humidity']
h3=main3['humidity']
h4=main4['humidity']
h5=main5['humidity']
h6=main6['humidity']
h7=main7['humidity']
h8=main8['humidity']
h9=main9['humidity']
y2=[h1,h2,h3,h4,h5,h6,h7,h8,h9]


# In[6]:


print(y2)


# ### Isolation des données de visibilité pour chacune des villes 

# In[7]:


v1=data1['visibility']//100
v2=data2['visibility']//100
v3=data3['visibility']//100
v4=data4['visibility']//100
v5=data5['visibility']//100
v6=data6['visibility']//100
v7=data7['visibility']//100
v8=data8['visibility']//100
v9=data9['visibility']//100
y3=[v1,v2,v3,v4,v5,v6,v7,v8,v9]


# ### Création du graphique

# In[8]:


r1=range(len(y1))  
# pour définir le nombre de colonnes pour la couverture nuageuse 
r2=[x+0.2 for x in r1] 
#pour définir le nombre de colonnes pour le taux d'humidité
#avec un espacement par rapport à la première colonne
r3=[x+0.4 for x in r1] 
#pour définir le nombre de colonnes pour la visibilité 
#avec un espacement par rapport à la première et la deuxième colonne

plt.figure(figsize=(15,9), dpi=200)
plt.bar(r1, y1, width=0.2, color=['red']) 
#Création de la première barre (absisse, position, largeur de colonne,couleur)
plt.bar(r2, y2, width=0.2, color=['blue']) 
#Création de la deuxième barre (absisse, position, largeur de colonne,couleur)
plt.bar(r3, y3, width=0.2, color=['green']) 
#Création de la troisième barre (absisse, position, largeur de colonne,couleur)
plt.title("Comparaison des conditions d'observation :") # Titre du graphique
plt.xticks([r+0.4/2 for r in range(len(y1))],['Vinon','Pic du Midi','Paris',
            'Lynde','Bischwiller','Corte','Nantes','Orelle','Brest']) 
            #Étiquettes des villes
plt.legend(labels=['Couverture nuageuse (%)',"Taux d'humidité (%)",
                   'Visibilité sur 10km (%)'],bbox_to_anchor = (1.42, 1), 
           loc = 'upper right', prop = {'size': 20}) 
#Création de la légende
#correspondance de chaque barre,position de la légende, taille de police


# ### Calcul du taux d'humidité moyen et de la couverture nuageuse moyenne

# In[9]:


Taux_humidite=[h1,h2,h3,h4,h5,h6,h7,h8,h9]

somme1=sum(Taux_humidite) 
#Effectue la somme de tous les taux d'humidité sur les villes choisies
moyenne1=round(somme1/9,1) 
#Calcule la moyenne sur l'ensemble des villes choisies
print("Taux d'humidité moyen:",moyenne1,'%')

Couverture_nuageuse=[c1,c2,c3,c4,c5,c6,c7,c8,c9]
somme2=sum(Couverture_nuageuse) 
#Effectue la somme de toutes les couvertures nuageuses sur les villes choisies
moyenne2=round(somme2/9,1) 
#Calcule la moyenne sur l'ensemble des villes choisies
print('Couverture nuageuse moyenne:',moyenne2,'%')


# In[10]:


from turtle import *


# ### Tracé de la Corse et de la France avec turtle

# In[11]:


reset()
speed(100)
up()
goto(-200,0)
forward(200)
left(70)
down()
forward(140)
left(100)
forward(50)
right(20)
forward(70)
right(20)
forward(40)
right(10)
forward(20)
left(80)
forward(50)
left(70)
forward(50)
right(40)
forward(50)
right(56)
forward(40)
right(30)
forward(25)
left(30)
forward(20)
left(120)
forward(25)
right(20)
forward(30)
right(95)
forward(30)
right(25)
forward(35)
left(40)
forward(30)
left(65)
forward(15)
left(10)
forward(30)
left(85)
forward(40)
right(40)
forward(65)
right(40)
forward(65)
right(10)
forward(70)
right(50)
forward(20)
left(130)
forward(150)
left(30)
forward(30)
left(70)
forward(30)
right(60)
forward(30)
right(50)
forward(35)
right(10)
forward(20)
left(30)
forward(15)
left(45)
forward(60)
left(80)
forward(70)
goto(0,0)
up()
goto(0,0)
pensize(0.5)
goto(200,-220)
down()
right(195)
forward(25)
right(15)
forward(30)
right(35)
forward(15)
left(35)
forward(8)
right(10)
forward(40)
right(40)
forward(15)
right(90)
forward(18)
left(45)
forward(18)
right(105)
forward(8)
left(80)
forward(12)
right(90)
forward(15)
left(110)
forward(20)
right(95)
forward(18)
left(100)
forward(12)
right(110)
forward(20)
left(120)
forward(15)
right(80)
forward(15)
right(50)
forward(10)
left(35)
forward(12)
right(30)
forward(30)
right(50)
forward(20)
left(10)
forward(12)
right(80)
forward(5)
left(140)
forward(50)
right(80)
forward(12)
right(95)
forward(30)
left(24)
forward(45)


# ### Création des fonctions pour les différentes conditions d'observation 

# In[12]:


def cercle_vert(c):
    down()
    fillcolor('green')
    begin_fill()
    circle(c)
    end_fill()
def cercle_jaune(c):
    down()
    fillcolor('yellow')
    begin_fill()
    circle(c)
    end_fill()
def cercle_orange(c):
    down()
    fillcolor('orange')
    begin_fill()
    circle(c)
    end_fill()
def cercle_rouge(c):
    down()
    fillcolor('red')
    begin_fill()
    circle(c)
    end_fill()


# ### Création des cercles des villes et paramétrage de leurs couleurs selon les données

# In[13]:


up()
goto(-110,10) # Vinon
if h1>=40 and h1<=60 and c1<=50 and v1>=90:
    cercle_vert(10)
elif h1<=40 or h1>=60 and c1<=50 and v1>=90:
    cercle_jaune(10)
elif h1>=40 and h1<=60 and c1>=50 and v1>=90:
    cercle_jaune(10)
elif h1>=40 and h1<=60 and c1<=50 and v1<=90:
    cercle_jaune(10)
elif h1<=40 and h1>=60 and c1>=50 and v1>=90:
    cercle_orange(10)
elif h1>=40 and h1<=60 and c1>=50 and v1<=90:
    cercle_orange(10)
elif h1<=40 and h1>=60 and c1<=50 and v1<=90:
    cercle_orange(10)
else:
    cercle_rouge(10)


# In[14]:


up()
goto(-150,-170) # Pic du Midi 
if h2>=40 and h2<=60 and c2<=50 and v2>=90:
    cercle_vert(10)
elif h2<=40 or h2>=60 and c2<=50 and v2>=90:
    cercle_jaune(10)
elif h2>=40 and h2<=60 and c2>=50 and v2>=90:
    cercle_jaune(10)
elif h2>=40 and h2<=60 and c2<=50 and v2<=90:
    cercle_jaune(10)
elif h2<=40 and h2>=60 and c2>=50 and v2>=90:
    cercle_orange(10)
elif h2>=40 and h2<=60 and c2>=50 and v2<=90:
    cercle_orange(10)
elif h2<=40 and h2>=60 and c2<=50 and v2<=90:
    cercle_orange(10)
else:
    cercle_rouge(10)


# In[15]:


up()
goto(-110,95) # Paris
if h3>=40 and h3<=60 and c3<=50 and v3>=90:
    cercle_vert(10)
elif h3<=40 or h3>=60 and c3<=50 and v3>=90:
    cercle_jaune(10)
elif h3>=40 and h3<=60 and c3>=50 and v3>=90:
    cercle_jaune(10)
elif h3>=40 and h3<=60 and c3<=50 and v3<=90:
    cercle_jaune(10)
elif h3<=40 and h3>=60 and c3>=50 and v3>=90:
    cercle_orange(10)
elif h3>=40 and h3<=60 and c3>=50 and v3<=90:
    cercle_orange(10)
elif h3<=40 and h3>=60 and c3<=50 and v3<=90:
    cercle_orange(10)
else:
    cercle_rouge(10)


# In[16]:


up()
goto(-100,200) # Lynde 
if h4>=40 and h4<=60 and c4<=50 and v4>=90:
    cercle_vert(10)
elif h4<=40 or h4>=60 and c4<=50 and v4>=90:
    cercle_jaune(10)
elif h4>=40 and h4<=60 and c4>=50 and v4>=90:
    cercle_jaune(10)
elif h4>=40 and h4<=60 and c4<=50 and v4<=90:
    cercle_jaune(10)
elif h4<=40 and h4>=60 and c4>=50 and v4>=90:
    cercle_orange(10)
elif h4>=40 and h4<=60 and c4>=50 and v4<=90:
    cercle_orange(10)
elif h4<=40 and h4>=60 and c4<=50 and v4<=90:
    cercle_orange(10)
else:
    cercle_rouge(10)


# In[17]:


up()
goto(25,106) # Bischwiller
if h5>=40 and h5<=60 and c5<=50 and v5>=90:
    cercle_vert(10)
elif h5<=40 or h5>=60 and c5<=50 and v5>=90:
    cercle_jaune(10)
elif h5>=40 and h5<=60 and c5>=50 and v5>=90:
    cercle_jaune(10)
elif h5>=40 and h5<=60 and c5<=50 and v5<=90:
    cercle_jaune(10)
elif h5<=40 and h5<=60 and c5>=50 and v5>=90:
    cercle_orange(10)
elif h5>=40 and h5<=60 and c5>=50 and v5<=90:
    cercle_orange(10)
elif h5<=40 and h5>=60 and c5<=50 and v5<=90:
    cercle_orange(10)
else:
    cercle_rouge(10)


# In[18]:


up()
goto(165,-240) # Corte
if h6>=40 and h6<=60 and c6<=50 and v6>=90:
    cercle_vert(10)
elif h6<=40 or h6>=60 and c6<=50 and v6>=90:
    cercle_jaune(10)
elif h6>=40 and h6<=60 and c6>=50 and v6>=90:
    cercle_jaune(10)
elif h6>=40 and h6<=60 and c6<=50 and v6<=90:
    cercle_jaune(10)
elif h6<=40 and h6>=60 and c6>=50 and v6>=90:
    cercle_orange(10)
elif h6>=40 and h6<=60 and c6>=50 and v6<=90:
    cercle_orange(10)
elif h6<=40 and h6>=60 and c6<=50 and v6<=90:
    cercle_orange(10)
else:
    cercle_rouge(10)


# In[19]:


up()
goto(-240,10) # Nantes
if h7>=40 and h7<=60 and c7<=50 and v7>=90:
    cercle_vert(10)
elif h7<=40 or h7>=60 and c7<=50 and v7>=90:
    cercle_jaune(10)
elif h7>=40 and h7<=60 and c7>=50 and v7>=90:
    cercle_jaune(10)
elif h7>=40 and h7<=60 and c7<=50 and v7<=90:
    cercle_jaune(10)
elif h7<=40 and h7>=60 and c7>=50 and v7>=90:
    cercle_orange(10)
elif h7>=40 and h7<=60 and c7>=50 and v7<=90:
    cercle_orange(10)
elif h7<=40 and h7>=60 and c7<=50 and v7<=90:
    cercle_orange(10)
else:
    cercle_rouge(10)


# In[20]:


up()
goto(-10,-70) # Orelle
if h8>=40 and h8<=60 and c8<=50 and v8>=90:
    cercle_vert(10)
elif h8<=40 or h8>=60 and c8<=50 and v8>=90:
    cercle_jaune(10)
elif h8>=40 and h8<=60 and c8>=50 and v8>=90:
    cercle_jaune(10)
elif h8>=40 and h8<=60 and c8<=50 and v8<=90:
    cercle_jaune(10)
elif h8<=40 and h8>=60 and c8>=50 and v8>=90:
    cercle_orange(10)
elif h8>=40 and h8<=60 and c8>=50 and v8<=90:
    cercle_orange(10)
elif h8<=40 and h8>=60 and c8<=50 and v8<=90:
    cercle_orange(10)
else:
    cercle_rouge(10)


# In[21]:


up()
goto(-335,70) # Brest
if h9>=40 and h9<=60 and c9<=50 and v9>=90:
    cercle_vert(10)
elif h9<=40 or h9>=60 and c9<=50 and v9>=90:
    cercle_jaune(10)
elif h9>=40 and h9<=60 and c9>=50 and v9>=90:
    cercle_jaune(10)
elif h9>=40 and h9<=60 and c9<=50 and v9<=90:
    cercle_jaune(10)
elif h9<=40 and h9>=60 and c9>=50 and v9>=90:
    cercle_orange(10)
elif h9>=40 and h9<=60 and c9>=50 and v9<=90:
    cercle_orange(10)
elif h9<=40 and h9>=60 and c9<=50 and v9<=90:
    cercle_orange(10)
else:
    cercle_rouge(10)


# ### Création des étiquettes des villes sur la carte turtle 

# In[22]:


up()
goto(-100,-15)
write(("Vinon"),font=("Arial",15))
goto(190,-250)
write(("Corte"),font=("Arial",15))
goto(-125,-180)
write(("Pic Du Midi"),font=("Arial",15))
goto(-87,90)
write(("Paris"),font=("Arial",15))
goto(-85,180)
write(("Lynde"),font=("Arial",15))
goto(50,100)
write(("Bischwiller"),font=("Arial",15))
goto(-212,0)
write(("Nantes"),font=("Arial",15))
goto(10,-80)
write(("Orelle"),font=("Arial",15))
goto(-315,65)
write(("Brest"),font=("Arial",15))
hideturtle()


# ### Création de la légende sur la carte turtle

# In[23]:


up()
goto(150,190)
down()
setheading(0)
forward(200)
right(90)
forward(300)
right(90)
forward(200)
right(90)
forward(300)
up() # cadre de la légende
goto(170,160)
write(("Légende:"),font=("Arial",17))

goto(190,120) # conditions excellentes
down()
fillcolor('green')
begin_fill()
circle(10)
end_fill()
up()
goto(200,108)
write(("Excellent"),font=("Arial",15))

up()
goto(190,60) # conditions favorables
down()
fillcolor('yellow')
begin_fill()
circle(10)
end_fill()
up()
goto(200,48)
write(("Favorable"),font=("Arial",15))

up()
goto(190,0) # conditions défavorables
down()
fillcolor('orange')
begin_fill()
circle(10)
end_fill()
up()
goto(200,-12)
write(("Défavorable"),font=("Arial",15))

up()
goto(190,-60) # impraticable
down()
fillcolor('red')
begin_fill()
circle(10)
end_fill()
up()
goto(200,-72)
write(("Impraticable"),font=("Arial",15))


# ### Création du titre sur la carte turtle

# In[24]:


up()
goto(-250,270) # titre
write(("Conditions d'observations astronomiques:"),font=("Arial",20))


# ### Création des variables issues du calcul de la différence de température

# In[25]:


e1=main1['temp_max']-main1['temp_min']
e2=main2['temp_max']-main2['temp_min']
e3=main3['temp_max']-main3['temp_min']
e4=main4['temp_max']-main4['temp_min']
e5=main5['temp_max']-main5['temp_min']
e6=main6['temp_max']-main6['temp_min']
e7=main7['temp_max']-main7['temp_min']
e8=main8['temp_max']-main8['temp_min']
e9=main9['temp_max']-main9['temp_min']


# ### Création des listes avec les écarts selon les différentes villes

# In[26]:


villes=['Vinon','Pic du Midi','Paris','Lynde','Bischwiller','Corte','Nantes',
        'Orelle','Brest']
ecarts=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
temp_min=[main1['temp_min'],main2['temp_min'],main3['temp_min'],
          main4['temp_min'],main5['temp_min'],main6['temp_min'],
          main7['temp_min'],main8['temp_min'],main9['temp_min']]
temp_max=[main1['temp_max'],main2['temp_max'],main3['temp_max'],
          main4['temp_max'],main5['temp_max'],main6['temp_max'],
          main7['temp_max'],main8['temp_max'],main9['temp_max']]
print(ecarts)


# ### Création du graphique de la différence de température jour/nuit dans les différentes villes

# In[27]:


for i in range(0,9):
    if ecarts[i]==min(ecarts):
        ville_min=villes[i]
print('Écart minimum:',round(min(ecarts),2),'°C à',ville_min)
plt.figure(figsize=(20,10), dpi=250)
plt.plot(villes,temp_max,'red',linewidth=5)
plt.plot(villes,temp_min,'blue',linewidth=5)
plt.legend(labels=["Température maximum (°C)",'Température minimum (°C)'],
           bbox_to_anchor=(1.35,1),loc='upper right',prop={'size':20})
plt.title("Comparaison des températures minimales et maximales des différentes villes:")


# In[28]:


sys1=data1['sys']
sys2=data1['sys']
sys3=data1['sys']
sys4=data1['sys']
sys5=data1['sys']
sys6=data1['sys']
sys7=data1['sys']
sys8=data1['sys']
sys9=data1['sys']


# In[29]:


rise1=sys1['sunrise']
rise2=sys2['sunrise']
rise3=sys3['sunrise']
rise4=sys4['sunrise']
rise5=sys5['sunrise']
rise6=sys6['sunrise']
rise7=sys7['sunrise']
rise8=sys8['sunrise']
rise9=sys9['sunrise']
rise_m=(rise1+rise2+rise3+rise4+rise5+rise6+rise7+rise8+rise9)/9
print(round(rise_m))


# In[30]:


set1=sys1['sunset']
set2=sys2['sunset']
set3=sys3['sunset']
set4=sys4['sunset']
set5=sys5['sunset']
set6=sys6['sunset']
set7=sys7['sunset']
set8=sys8['sunset']
set9=sys9['sunset']
set_m=(set1+set2+set3+set4+set5+set6+set7+set8+set9)/9
print(round(set_m))


# In[31]:


from datetime import datetime
timestamp1 = round(set_m)
set_m_dt=datetime.fromtimestamp(timestamp1)
print('Heure de couché du soleil:',set_m_dt.hour,'h',set_m_dt.minute)


# In[32]:


from datetime import datetime
timestamp2 = round(rise_m)
rise_m_dt=datetime.fromtimestamp(timestamp2)
print('Heure de couché du soleil:',rise_m_dt.hour,'h',rise_m_dt.minute)


# In[33]:


def soleil(n,m):
    up()
    goto(-50,70)
    down()
    color('orange','orange')
    begin_fill()
    dot(24)
    end_fill()
    k=0
    while k<m:
        forward(25)
        goto(-50,70)
        left(360/m)
        k+=1


# In[34]:


goto(0,0)
left(100)
circle(100,160)
up()
soleil(15,8)
up()
goto(-20,-20)
pencolor('black')
setheading(0)
write((set_m_dt.hour),font=("Arial",10))
forward(20)
write(('h'),font=("Arial",10))
forward(10)
write((set_m_dt.minute),font=("Arial",10))
goto(-210,-20)
setheading(0)
write((rise_m_dt.hour),font=("Arial",10))
forward(10)
write(('h'),font=("Arial",10))
forward(10)
write((rise_m_dt.minute),font=("Arial",10))
hideturtle()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




