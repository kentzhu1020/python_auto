# Overview

   This is an automation testing framework. it use MVC to setup the structure. Test suite is used to organize each module,
   integration,end to end, or smoke parts to achieve the business logic
   
####Model
* Database visiting
* Common utility functions
* Report and logs

####Views
* It's an object repository for each page on the web/mobile.
 
####Controller
* Controller is a bridge for the page object and business logic. it try to find the element one the page the achieve each action
on that page

####Dependency
In order to complete the automation testing framework. We need to install/have some pro-conditions below

In order to show the code. It's much suggested to install [pycharm](https://www.jetbrains.com/pycharm/download/)

**Mac**

**1** Python 2.7.* (Already installed)

**2** Selenium [WebDriver](https://pypi.python.org/pypi/selenium)

**3** Chrome Driver/Firefox 

*  Download [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
*  From the Go menu select Go To Folder
*  Type /usr/bin and press enter

**4** Safari (if you want to run the test suite for safari compatibility)

* The prebuilt SafariDriver extension(SafariSriver.safariextz) can be downloaded from [here](http://selenium-release.storage.googleapis.com/index.html?path=2.48/)
(the link is listed in the [Getting Started section of the SafariDriver Selenium Wiki](https://github.com/SeleniumHQ/selenium/wiki/SafariDriver#getting-started). 
Download it, double-click it, and click **Trust** when prompted.

* open Safari

* go to Preferences

* click on the Extensions tab

* Make sure Enable WebDriver is checked

* Close Safari

**5** [Pylab](https://pypi.python.org/pypi/pylab)

**6** nmap brew intall nmap Or download [nmap](https://nmap.org/download.html)

**Windows**

**1** [Python 2.7.*](https://www.python.org/getit/windows/)

**2** Selenium [WebDriver](https://pypi.python.org/pypi/selenium)

**3** Chrome Driver/Firefox 

* Download [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* %HOMEPATH%\Local Settings\Application Data\Google\Chrome\Application\chrome.exe

**4** Pylab 
Intall below 3 packages

* [numpy](http://sourceforge.net/projects/numpy/files/NumPy/1.7.0/)
* [matplotlab](http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.1.1/)
* [scipy](http://sourceforge.net/projects/scipy/files/scipy/0.12.0/)

**5** [nmap](https://nmap.org/download.html)




    


 
    