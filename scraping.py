
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')

# assigning variable to look for the div tag & its class (i.e div.list_text)
# can reference this variable when looking to filter search even further
slide_elem = news_soup.select_one('div.list_text')

# Identify latest news article's title
slide_elem.find('div', class_='content_title').text

# OR other option do to the above + assigning variable
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit Space Images URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
# Don't want to be too specific as the src will be different every time the page is updated
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_link = 'https://spaceimages-mars.com/' + img_url_rel
img_link

#OR 
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# Import Pandas Module 
import pandas as pd

# Visit Galaxy Facts website
url = 'https://galaxyfacts-mars.com/'
browser.visit(url)

# Convert the first table pandas finds in the html to a dataframe, using pd.read_html and 
# index referencing (i.e [0])
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# Convert df back to html format so the table can be live in the web app
# use pandas .to_html() function
df.to_html()

# Quit Browser 
browser.quit()

