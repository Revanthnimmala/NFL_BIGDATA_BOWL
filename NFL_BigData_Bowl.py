# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 08:49:09 2019

@author: vkaus
"""
import pandas as pd


    
old_data=pd.read_csv(r'train.csv')#509762 rows before dropping null values
old_data=old_data.dropna()#375786 rows after dropping null values


old_data.shape # rows * columns in a dataset

old_data.dtypes # data types of a data frame

old_data.columns # printing column names


###################################################### Data Preprocessing for All Players   ###############################################

old_data=old_data.drop(columns=['PlayId','NflId','DisplayName','JerseyNumber','NflIdRusher','PlayerBirthDate','PlayerCollegeName','Stadium','Season','GameClock','PossessionTeam','FieldPosition','NflIdRusher','OffenseFormation', 'OffensePersonnel',
                                'DefensePersonnel', 'PlayDirection', 'TimeHandoff','TimeSnap', 'PlayerBirthDate',
       'PlayerCollegeName', 'Position', 'HomeTeamAbbr', 'VisitorTeamAbbr','Week', 'Stadium', 'Location', 'StadiumType', 'Turf', 'GameWeather','WindDirection']) #Removing columns which are text.



new_csv=old_data.to_csv(r'C:\Users\vkaus\OneDrive\Desktop\Kaggle\NFL_Final.csv',header=True)#Converting the dataframe into a csv file which is used in R for modeling


new_data=pd.read_csv(r'NFL_Final.csv')

new_data.dtypes

new_data=new_data.drop(columns=['Unnamed: 0'])

new_data = new_data.drop(columns=['OffensePersonnel','DefensePersonnel','Location','StadiumType']) 


# Preprocessing windspeed column with replacements
new_data['WindSpeed']=new_data['WindSpeed'].replace('10mph','10')
new_data['WindSpeed']=new_data['WindSpeed'].replace('10-20','15')
new_data['WindSpeed']=new_data['WindSpeed'].replace('11-17','14')
new_data['WindSpeed']=new_data['WindSpeed'].replace('12-22','17')
new_data['WindSpeed']=new_data['WindSpeed'].replace('12mph','12')
new_data['WindSpeed']=new_data['WindSpeed'].replace('13 MPH','13')
new_data['WindSpeed']=new_data['WindSpeed'].replace('14-23','18')
new_data['WindSpeed']=new_data['WindSpeed'].replace('15 gusts up to 25','20')
new_data['WindSpeed']=new_data['WindSpeed'].replace('4 MPh','4')
new_data['WindSpeed']=new_data['WindSpeed'].replace('6 mph','6')
new_data['WindSpeed']=new_data['WindSpeed'].replace('7 MPH','7')
new_data['WindSpeed']=new_data['WindSpeed'].replace('E','8')
new_data['WindSpeed']=new_data['WindSpeed'].astype(float)


# Preprocessing WindDirection column
new_data['WindDirection']=new_data['WindDirection'].replace('8','E')
new_data['WindDirection']=new_data['WindDirection'].replace('From ESE','ESE')
new_data['WindDirection']=new_data['WindDirection'].replace('From NNE','NNE')
new_data['WindDirection']=new_data['WindDirection'].replace('From NNW','NNW')
new_data['WindDirection']=new_data['WindDirection'].replace('From S','S')
new_data['WindDirection']=new_data['WindDirection'].replace('From SSE','SSE')
new_data['WindDirection']=new_data['WindDirection'].replace('From SSW','SSW')
new_data['WindDirection']=new_data['WindDirection'].replace('From SW','SW')
new_data['WindDirection']=new_data['WindDirection'].replace('From W','W')
new_data['WindDirection']=new_data['WindDirection'].replace('From WSW','WSW')
new_data['WindDirection']=new_data['WindDirection'].replace('from W','W')
new_data['WindDirection']=new_data['WindDirection'].replace('N-NE','NNE')
new_data['WindDirection']=new_data['WindDirection'].replace('W-NW','WNW')
new_data['WindDirection']=new_data['WindDirection'].replace('W-SW','WSW')
new_data['WindDirection']=new_data['WindDirection'].replace('North/Northwest','NNW')
new_data['WindDirection']=new_data['WindDirection'].replace('East','E')
new_data['WindDirection']=new_data['WindDirection'].replace('East North East','ENE')
new_data['WindDirection']=new_data['WindDirection'].replace('East Southeast','ESE')
new_data['WindDirection']=new_data['WindDirection'].replace('North','N')
new_data['WindDirection']=new_data['WindDirection'].replace('Northeast','NE')
new_data['WindDirection']=new_data['WindDirection'].replace('North East','NE')
new_data['WindDirection']=new_data['WindDirection'].replace('NorthEast','NE')
new_data['WindDirection']=new_data['WindDirection'].replace('Northwest','NW')
new_data['WindDirection']=new_data['WindDirection'].replace('s','S')
new_data['WindDirection']=new_data['WindDirection'].replace('South','S')
new_data['WindDirection']=new_data['WindDirection'].replace('South Southeast','SSE')
new_data['WindDirection']=new_data['WindDirection'].replace('South Southwest','SSW')
new_data['WindDirection']=new_data['WindDirection'].replace('Southeast','SE')
new_data['WindDirection']=new_data['WindDirection'].replace('Southwest','SW')
new_data['WindDirection']=new_data['WindDirection'].replace('SouthWest','SW')
new_data['WindDirection']=new_data['WindDirection'].replace('West','W')
new_data['WindDirection']=new_data['WindDirection'].replace('West-Southwest','WSW')
new_data['WindDirection']=new_data['WindDirection'].replace('West-Northwest','WNW')
new_data['WindDirection']=new_data['WindDirection'].replace('West Northwest','WNW')
new_data['WindDirection']=new_data['WindDirection'].astype(str)

#Preprocessing Turf Column
new_data['Turf'] = new_data['Turf'].replace('Artifical','Artificial')
new_data['Turf'] = new_data['Turf'].replace('FieldTurf','Field Turf')
new_data['Turf'] = new_data['Turf'].replace('FieldTurf 360','Field Turf')
new_data['Turf'] = new_data['Turf'].replace('FieldTurf360','Field Turf')
new_data['Turf'] = new_data['Turf'].replace('grass','Grass')
new_data['Turf'] = new_data['Turf'].replace('Natural','Natural Grass')
new_data['Turf'] = new_data['Turf'].replace('Natural grass','Natural Grass')
new_data['Turf'] = new_data['Turf'].replace('Naturall Grass','Natural Grass')
new_data['Turf'] = new_data['Turf'].astype(str)

#Preprocessing GameWeather column
new_data['GameWeather']=new_data['GameWeather'].replace('Clear and cold','Clear and Cool')
new_data['GameWeather']=new_data['GameWeather'].replace('Clear and sunny','Clear and Sunny')
new_data['GameWeather']=new_data['GameWeather'].replace('Clear skies','Clear')
new_data['GameWeather']=new_data['GameWeather'].replace('Clear Skies','Clear')
new_data['GameWeather']=new_data['GameWeather'].replace('cloudy','Cloudy')
new_data['GameWeather']=new_data['GameWeather'].replace('Cloudy and cold','Cloudy and Cool')
new_data['GameWeather']=new_data['GameWeather'].replace('Cloudy with periods of rain, thunder possible. Winds shifting to WNW, 10-20 mph.','Rain Chance')
new_data['GameWeather']=new_data['GameWeather'].replace('Cloudy, 50% change of rain','Rain Chance')
new_data['GameWeather']=new_data['GameWeather'].replace('Cloudy, fog started developing in 2nd quarter','Cloudy, fog')
new_data['GameWeather']=new_data['GameWeather'].replace('Cloudy, light snow accumulating 1-3"','Cloudy, snow')
new_data['GameWeather']=new_data['GameWeather'].replace('Coudy','Cloudy')
new_data['GameWeather']=new_data['GameWeather'].replace('Cold','Cool')
new_data['GameWeather']=new_data['GameWeather'].replace('Mostly cloudy','Mostly Cloudy')
new_data['GameWeather']=new_data['GameWeather'].replace('Mostly Coudy','Mostly Cloudy')
new_data['GameWeather']=new_data['GameWeather'].replace('Mostly sunny','Mostly Sunny')
new_data['GameWeather']=new_data['GameWeather'].replace('Mostly Sunny Skies','Mostly Sunny')
new_data['GameWeather']=new_data['GameWeather'].replace('Partly cloudy','Partly Cloudy')
new_data['GameWeather']=new_data['GameWeather'].replace('Partly Clouidy','Partly Cloudy')
new_data['GameWeather']=new_data['GameWeather'].replace('Partly sunny','Partly Sunny')
new_data['GameWeather']=new_data['GameWeather'].replace('Party Cloudy','Partly Cloudy')
new_data['GameWeather']=new_data['GameWeather'].replace('Rain Chance 40%','Rain Chance')
new_data['GameWeather']=new_data['GameWeather'].replace('Rain likely, temps in low 40s.','Rain Chance')
new_data['GameWeather']=new_data['GameWeather'].replace('Rain shower','Rainy')
new_data['GameWeather']=new_data['GameWeather'].replace('Scattered Showers','Showers')
new_data['GameWeather']=new_data['GameWeather'].replace('Sun & clouds','Sunny and cold')
new_data['GameWeather']=new_data['GameWeather'].replace('Sunny and clear','Clear and Sunny')
new_data['GameWeather']=new_data['GameWeather'].replace('Sunny Skies','Sunny')
new_data['GameWeather']=new_data['GameWeather'].replace('Sunny, highs to upper 80s','Sunny')
new_data['GameWeather']=new_data['GameWeather'].replace('Rain','Rainy')
new_data['GameWeather']=new_data['GameWeather'].astype(str)



#Converting Preprocessed data into modeling dataset where we train our models and split data into train and test
new_csv=new_data.to_csv(r'C:\Users\vkaus\OneDrive\Desktop\Kaggle\Final_NFL.csv',header=True)

