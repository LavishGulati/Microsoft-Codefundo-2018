## How to Use the Project
1. Download and extract repo
2. Ensure Django version 1.9.4 is installed `pip3 install django==1.9.4`
3. Run command `python3 manage.py migrate`
4. Run command `python3 manage.py runserver`

# Microsoft codefundo++ 2018
Project Name: 404 Disaster Not Found <br>
Team Name: 404 Brain Not Found <br>
Team Members: Lavish Gulati, Mayank Baranwal, Chirag Gupta <br>
Organization: Indian Institute of Technology Guwahati


## Project Description

Inspired by the recent Kerala floods and the growing number of natural calamities that wreak havoc on our society, we aim to utilize technology as a means to improve the quality of lives of people living in vulnerable areas. <br>
The various domains of the project are discussed below:

#### 1. Prediction
* To build an early warning system by detecting upcoming natural calamities (with special emphasis on cyclones). Computer vision will be used to detect the formation of cyclones using real time satellite imagery.

#### 2. Prevention
* Once a natural disaster is eminent, our project aims to identify vulnerable areas which are at the greatest risk of harm. These include low lying areas and crowded, underdeveloped places where evacuation could be difficult.
* Latest alerts will be posted in the form of short snippets by summarizing alerts from various media outlets on upcoming disasters.

#### 3. Management
* We will construct a platform to coordinate rescue efforts and allow disaster victims to communicate their needs to the rescuers
* An additional extension can include a GSM module that can send news updates on the disaster and tips to affected areas.


## Implementation
The above mentioned domains will be implemented on a web-based platform where the latest prediction alerts, management aspects and prevention techniques will be published.  

* #### Datasets To Be Used
    * [Archived Cyclone Images](http://satellite.imd.gov.in/archive/)
* #### Technologies
    * APIs To Be Used:
        * [Custom View API](https://azure.microsoft.com/en-us/services/cognitive-services/custom-vision-service/)
        * [Computer Vision API](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/)
* #### Hardware To Be Used:
    * sim900A GSM/GPRS Module
