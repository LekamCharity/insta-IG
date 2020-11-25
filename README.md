# insta-IG
## Author  
  
[LekamCharity](https://github.com/LekamCharity/insta-IG.git)  
  
# Description  
This is a web application for instagram where users can upload photos and follow other people.

## User Story  
  
* View different photos that interest them  
* Search for different categories   
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.  

## Live Link
https://instaig.herokuapp.com/ 
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/LekamCharity/insta-IG.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd insta-IG pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations  
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8]
* [Django 3.1.3]
* [Heroku]  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  

## Contact Information   
If you have any question or contributions, please email me at [lekamcharity@gmail.com]  

### License
  [MIT](https://github.com/LekamCharity/insta-IG/blob/master/License) Copyright (c) 2020 Lekam Charity
