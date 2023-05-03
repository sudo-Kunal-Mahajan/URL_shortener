# URL shortener app created using FLASK. 

The app has a single page interface where it takes a URL as user input. Once submitted the tool will create a random string of 10 characters and map it as a shortened URL to the User provided URL. 

The app will then flash a message where the shortened URL will be shown to user. The app will also show 10 latest generate URL on the homepage. 

It uses SQLAlchemy database in backend to store the shortened URLs.

To Run the app, call the _run.py_ file.

***
The configurations are to be stored in _app_configs.py_ file in the _instance_ folder. The required variables are already populated with a random value. (**make sure to change them.**)


***
The Database has following structure:
|shorten_url|full_url|email|created_at|      
|----|-----|-------|-------|     
|asbdu24|https://www.google.com|abc@gmail.com|Timestamp|

The Email ID is set _abc@gmail.com_ as default. Later on Authentication can be added to the tool so that each shortened URL can be mapped to its owner. 

Timestamp is auto populated when a new shortened URL is saved to the database.