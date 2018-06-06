# Mission to Mars

![mission_to_mars](Images/mission_to_mars.jpg)


In this project, I have built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines of how I have completed this project:

## Scraping

I completed my initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

### NASA Mars News

* I have also scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest News Title and Paragragh Text. Assign the text to variables that you can reference later.

### JPL Mars Space Images - Featured Image

* Obtained the recent image from the HTML page.

* Used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable.

### Mars Weather

* To find the weather, I visited the Mars Weather twitter account and scraped the latest Mars weather tweet from the page. 

### Mars Facts

* I then visited the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.


### Mars Hemisperes

* Visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* Saved both the image url string for the full resolution hemipshere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image url string and the hemisphere title to a list. 
