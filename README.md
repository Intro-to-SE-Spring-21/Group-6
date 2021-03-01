# Group-6
Description
-----------------
A Twitter-like application created in Python, Django, and SQLite. Written for Intro to Software Engineering at Mississippi State University, Spring 2021.

The site is hosted on Heroku at https://swe2021-twitter.herokuapp.com/. 

Objective
-----------------
To create a Twitter-like webpage. This includes being able to post microblogs similar to tweets, "favoriting" or "liking" tweets, and following certain users to add their specific tweets to an account's feed.

Core Features
-----------------
* Posting tweets
* Liking tweets
* Following users to see their future tweets

Languages
-----------------
* SQLite
* Python
* Django

Team Members
---------------
```
Team Lead: Caden Austin

Github Email: Cadenbryant@hotmail.com

MSU ID: CBA169 
```
```
Front-End: Darrion Robinson

Github Email: dr1374@msstate.edu

MSU ID: dr1374
```
```
???: Connor Hicks

Github Email: connorhicks@outlook.com

MSU ID: ch3083 
```
```
???: Bryan Alston

Github Email: bma1701@gmail.com

MSU ID: bma271
```

Running
---------------
Code can be pushed to heroku by pushing as a subtree. This must be ran by someone with an administrative account in the heroku portal however.
```
git subtree push --prefix TwitterClone heroku master
```
If you wish to run locally
```
cd TwitterClone
pip3 install -r requirements.txt
python3 manage.py runserver
```
