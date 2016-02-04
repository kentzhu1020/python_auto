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

**Mac(iOS)**

**1** Python 2.7.* (Already installed)

**2** Appium

* Install brew and check 

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew -v
```
* Install node and check

```
brew install node
node -v
```
* Install appium

```
sudo chmod -R 777 /usr/local
npm install -g appium
```

* Install python－client－master

```
git clone git@github.com:appium/python-client.git
cd python-client
python setup.py install
```
* Start appium or check 
```
appium &
appium－doctor
```

**4** Build 

```
* cd Downloads/samplecode-master/sample-code/apps/TestApp
* xcodebuild -sdk iphonesimulator 
**BUILD SUCCEEDED**
```
**5** [Pylab](https://pypi.python.org/pypi/pylab)

**6** [Xcode](https://developer.apple.com/xcode/)

**MAC (Android)**

This part have not testes yet.

* Please follow step 1 & 2 as Mac (iOS)
* [Android SDK](https://developer.android.com/sdk/index.html)


**Windows(Android)**
This part have not testes yet.

**1** [Python 2.7.*](https://www.python.org/getit/windows/)

**2** Appium [WebDriver](https://bitbucket.org/appium/appium.app/downloads/)

**3** [Android SDK](https://developer.android.com/sdk/index.html)

**4** ANDROID_HOME: C:\adt-bundle-windows-x86_64-20131030\sdk

**5** Pylab 
Intall below 3 packages

* [numpy](http://sourceforge.net/projects/numpy/files/NumPy/1.7.0/)
* [matplotlab](http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.1.1/)
* [scipy](http://sourceforge.net/projects/scipy/files/scipy/0.12.0/)