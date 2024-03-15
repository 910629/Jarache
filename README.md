# **Jarache Django Application**
[Jarache Django Application](https://github.com/910629/Jarache)

This Django application showcases Jarache Khunyeli's skills in various areas:
* Building and querying Django databases
* Implementing user login, registration, and authentication using Django's built-in modules
* Demonstrating HTML and CSS styling abilities

It also affords users the opportunity to give feedback on Jarache's skills.

## Table of Contents
1. Installation
 * Prerequisites
 * Installation Methods
  * Direct Installation (Without Docker; using IDE)
  * Using Docker Playground
  * Using Docker (Desktop Application)
 * Running the Application
  * Direct Execution (Without Docker; using IDE)
  * Using Docker Playground
  * Using Docker (Deskop Application)

2. Usage
 * Navigation
  * Navigating *Jarache Khunyeli's Bio*
  * Navigating *Mike Store - Online Store*
  * Navigating *Poll - Jarache's Skills*

3. Credits
 * Contributions
 * Licenses

## Installation
 ### Prerequisites:
  #### Using IDE/Docker Desktop App:
   __Python__: This application requires Python version 3.10 or higher. 
   You can download and install Python from the official website: [Download Python](https://www.python.org/downloads/)

  #### Using Docker Playground:
   Although this application requires python version 3.10 or higher, Docker Playground provides a pre-configured Python environment.
 
 ### Installation Methods:
  #### Direct Installation (Without Docker; using IDE):
   1. Install Python (see Prerequisites for link).
   2. Clone the *Jarache* repository.
    ''' 
    git clone https://github.com/910629/Jarache 
    '''

  #### Using Docker Playground:
   1. Within the Docker Playground terminal, use Git commands to clone your repository.
    ''' 
    git clone https://github.com/910629/Jarache 
    '''

  #### Using Docker (Desktop Application):
   1. Install Docker: If you don't have Docker installed, download and install it from the official website: 
   [Docker:get started](https://www.docker.com/get-started)

 ### Running the Application
  #### Direct Execution (Without Docker; using IDE):
   1. After successful installation, you can run the development server using:
    '''
    python manage.py runserver
    '''
    This will start the Django development server, typically accessible at http://127.0.0.1:8000/ in your web browser.

  #### Using Docker Playground:
   1. Navigate to the project directory:
    '''
    cd Jarache
    '''
   2. Run the development server:
    '''
    python manage.py runserver
    '''
   This will start the Django development server within the container. Docker Playground will typically display the assigned port for accessing the application (usually in the logs or UI).

  #### Using Docker (Deskop Application):
   1. Run the container:
    '''
    docker run -p 8000:8000 jarache_image
    '''
    This command runs the built Docker image (Jarache_image) and maps the container's port 8000 (where Django runs) to your host machine's port 8000.
   2. Access the application:
    The application should now be accessible in your web browser at http://localhost:8000/.

## Usage
 ### Navigating *Jarache Khunyeli's Bio*
  Once the application is running and you've accessed it, you will have landed on the *Jarache Khunyeli's Bio* page.
  Please analyze the page and elements before clicking on any links.

  ![Bio screenshot](data/screenshots/bio_scr.jpg)

  To access Jarache's experimental online store's page, click on *store website*.

  ![Store link screenshot](data/screenshots/storesitelink_scr.jpg)

  To access Jarache's skills poll page, click on *poll*.

  ![Poll link screenshot](data/screenshots/pollsitelink_scr.jpg)

  The page also provides links to Jarache's LinkdIn and GitHub profiles.

  ![Social & Repo links](data/screenshots/sociallinks_scr.jpg)

 ### Navigating *Mike Store - Online Store*
  If on *Jarache Khunyeli's Bio* you clicked on *store website*, This is the page you will be seeing:
  Please analyse the page and all its elements befor clicking on any links.
  **Note: You will not be able to purchase any products as yet, since the page is only being used for display purposes.**

  ![Store screenshot](data/screenshots/storesite_scr.jpg)

  Once you've analyzed the page and all its elements, you can scroll to the bottom of the page.
  You'll notice that it also features a form which captures user's details:
  **Note: For display purposes only.**

  ![Store form screenshot](data/)





  * Navigating *Poll - Jarache's Skills*