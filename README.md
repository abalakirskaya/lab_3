# lab_3
Python application for creating HTML map with locations of Twitter users` friends using folium, flask and geopy.
## Information
The application was made to create HTML map, using the data about user in Twitter. User should enter the name in Twitter and program will upload information about his friends using Twitter API. Then program (task_2) will write this information in 'data.json' file. Another program (task_3) will situate locations of friends on the wed-map('Map.html').
#### Libraries
In application are used:
  - string
  - geopy
  - folium
  - urllib
  - json
  - ssl
  - standart Python libraries
#### The structure of the project
  - __task_2.py__ - the main application of the project, which you should run, which will write the information about users` friends in 'data.json' file
  - __task_3.py__ - the main application of the project, which you should run, which will made the web-map ('Map.html')
  - __Map.html__ - html file with the map
  - __data.json__ - file with information about users` friends
  - __hidden.py__ - file with the keys to Twitter API
  - __oauth.py__, __twurl.py__ - files with additional functions
  - __web.py__ - file to run project in pythonanywhere.com

#### License of using
  - Download the 'lab_3' project (_all files!_)
  - Run the task_2 (or task_3) in Python runner 
  - Then enter the user`s name in which you are interested in
  - Open the data.json (or Map.html)
#### HTML structure
  __There are some the most common tags in html map file:__
  - \<!DOCTYPE html> - Defines the document type
  - \<body> - Defines the document's body
  - \<script> - 	Defines a client-side script
  - \<style> - Defines style information for a document
  - \<div> - Defines a section in a document
  - \<head> - Defines information about the document
#### Summary
  Using Twitter API program gets information from Twitter. The first program can get any information about Twitter users which you enter and write it to the file. The second program takes this information and creates a web-map with locations of the friends of this user. The problem of my program is that you can`t get on the step back and you see the map with the locations of all friends of all users which you entered.
