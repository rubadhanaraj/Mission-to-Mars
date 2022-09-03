# Mission-to-Mars
## Overview
The purpose of this project is create a Mars data web app which will scrape needed data from multiple websites. The scraped data will be stored in NoSQL Mongo database using python scripts and displayed in the newly created web page using HTML and Flask applications. Using Bootstrap, a responsive web app was created which can be viewed through any device.The software used for this projects are MongoDB, Python 3.7, Visual Studio Code and Flask application. The objective of this project is to
* Gain familiarity with and use HTML elements, as well as class and id attributes, to identify content for web scraping.
* Use BeautifulSoup and Splinter to automate a web browser and perform a web scrape.
* Create a MongoDB database to store data from the web scrape.
* Create a web application with Flask to display the data from the web scrape.
* Create an HTML/CSS portfolio to showcase projects.
* Use Bootstrap components to polish and customize the portfolio.
Robin wants to update the web app with Mars's hemisphere images which are available in another scrape friendly web page. 

## Results
To scrape full-resolution images of Mars’s hemispheres and the titles of those images from another website, BeautifulSoup and Splinter has been used.  

![image](https://user-images.githubusercontent.com/108298416/188289012-1dc370db-e48b-4c2b-98b2-22a7b6c8eb61.png)

The Mission_to_Mars_Challenge.ipynb file was exported as a Python file and scraping.py file has been updated with new code by defining a scrape_all() function and a new dictionary was created in the data dictionary to hold a list of dictionaries with the URL string and title of each hemisphere image. All data have been retreived by running the app.py file. HTML file was updated to access the database, and retrieve the img_url and title as it loops through the dictionary in the database using {% for hemisphere in mars.hemispheres %}.

![image](https://user-images.githubusercontent.com/108298416/188288806-3b63e4a6-9c44-465b-8f7d-00aa14bbad88.png)

![image](https://user-images.githubusercontent.com/108298416/188289341-bd30d9c5-48ce-407a-b043-345921852397.png)

## Summary
* Using Bootstrap 3 grid system the HTML file was updated to ensure that the website is mobile responsive.

![image](https://user-images.githubusercontent.com/108298416/188289147-e665f15d-bcbd-4f7d-812b-bd785971b42a.png)

* The facts table has been customized as striped table using the following Bootstrap 3 components.

![image](https://user-images.githubusercontent.com/108298416/188289235-3c9f145f-8979-41df-8c74-85d212e6a50b.png)

* The background colour of the body is changed by updating the HTML file

![image](https://user-images.githubusercontent.com/108298416/188289256-8092d8ec-f173-4e54-ac6f-f23fa3b400ab.png)

* The hemisphere images were added as thumbnails using Bootstrap 3 components.

![image](https://user-images.githubusercontent.com/108298416/188289217-74d1aa7c-52a7-4147-8965-208d21c0ebe4.png)

![image](https://user-images.githubusercontent.com/108298416/188289373-0779c765-f712-4d6c-980c-4c72b3a81e98.png)




