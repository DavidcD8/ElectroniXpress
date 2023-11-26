#   
#   ElectgroniXpress

## Overview

ElectgroniXpress is a Django-based web application designed for electronics enthusiasts to buy and sell electronic items. This README provides an in-depth look at the key components and configurations used in the application.

## Features

-   User registration and authentication
-   Listing electronic items for sale
-   Buying electronic items
-   Stylish frontend using Bootstrap 4 and Django-Crispy-Forms
-   Cloud storage for images using Amazon S3 and Django-Storages
-   PostgreSQL database for data storage

## Technology

-   Django 4.2.7
-   Django-Allauth 0.58.2
-   Django-Crispy-Forms 2.1
-   Gunicorn 21.2.0
-   PostgreSQL
-   HTML, CSS, JavaScript
-   Amazon S3 (for static files and media storage)

## Requirements

The application requires the following packages and libraries to be installed:

  
* dj-database-url==2.1.0
* Django==4.2.7
* django-allauth==0.58.2
* django-countries==7.5.1
* django-crispy-forms==2.1
* gunicorn==21.2.0
* psycopg2-binary==2.9.9
* whitenoise==6.6.0
* zipp==1.0.0
* boto3==1.28.84 
* django-storages==1.14.2 
* crispy-bootstrap4==2022.1` 

## Getting Started

To set up and run ElectgroniXpress, follow these steps:

1.  Ensure you have Python and pip installed.
    
2.  Create a virtual environment and activate it.
    
3.  Install the required dependencies using the following command:
    
    pip install freeze > requirements.txt
    
4.  Create a `.env` file in the project directory and define the following environment variables:
     * SECRET_KEY=your-secret-key
    *  DATABASE_URL=your-database-url
    
6.  Run the application using the following command:
    
    `python manage.py runserver` 
    
7.  Access the application in your web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
    

## Database

The application uses a PostgreSQL database, configured using the `dj-database-url` package. The database URL is fetched from the `DATABASE_URL` environment variable.

## Static Files and Media

Static files (CSS, JavaScript, etc.) and media files are managed using Amazon S3 for storage. The configuration includes settings for `MEDIA_URL`, `DEFAULT_FILE_STORAGE`, `STATIC_URL`, and `STATICFILES_STORAGE`.

## Security

The application includes security measures such as CSRF protection and password validation. Ensure that the environment variables are kept secret and the application is not run in debug mode in a production environment.

## Credits & Acknowledgments

-   Code Institute: Thanks to the Code Institute for providing project classes instrumental in developing ElectgroniXpress.
-   Django: The web framework used to build this application.
-   Amazon S3: The cloud-based platform used for managing static files and media.
-   dj-database-url: A package for configuring the database using environment variables.
-   Bootstrap: The front-end framework for styling the application.
-   Python: The programming language used to write the application's logic.
-   GitHub: The platform used for version control and collaboration.
 

## Deployment

### Prepare Your Project

1.  Ensure your project has the necessary files: requirements.txt to list required Python packages and a "Procfile" to specify how Heroku should run your app.

 
### Deploy to Heroku

1.  If you don't have a Heroku account, sign up at Heroku.
    
2.  Use the Heroku CLI to log in:

    
3.  Create a new Heroku app with a name of your choice:
     
4.  Connect your Heroku app to your GitHub repository from the Heroku dashboard.
    
5.  Enable automatic deployment from your desired branch.
    
6.  Set environment variables like `SECRET_KEY`, `DEBUG`, and others in the Heroku app settings.
    
7.  Trigger a manual deployment from the Heroku dashboard or let Heroku automatically deploy when changes are pushed to the connected GitHub repository.
    

### Deployed Link

[ElectgroniXpress on Heroku](https://onlineshopfirst-9d7d819c65b1.herokuapp.com/home.html)

## Manual Testing

### Project Overview

-   **Project Name:** ElectgroniXpress
-   **Testing Scope:** Functionality, Usability, and Responsiveness
-   **Testing Goals:** Ensure that the website functions as expected, is user-friendly, and responsive on different devices and screen sizes.

### Test Plan

#### Functional Testing

**Test Case 1: User Registration**

1.  Navigate to the registration page.
2.  Fill in valid registration details.
3.  Click the "Register" button.
4.  Verify that the user is redirected to the profile page.
    -   _Expected Outcome:_ User registration is successful.

**Test Case 2: Add Creation**

1.  Log in as an admin.
2.  Navigate to the "Sell Item" page.
3.  Fill in the Item details.
4.  Click the "Add Item" button.
5.  Verify that the new Item appears on the Listings page.
    -   _Expected Outcome:_ Item listed is successful.  
 
#### Usability Testing

**Test Case 3: Navigation and User Experience**

1.  Navigate through the website as a new user.
2.  Assess the intuitiveness of the navigation menu.
3.  Evaluate the readability and layout of content.
    -   _Expected Outcome:_ The website is user-friendly and intuitive.

#### Responsiveness Testing

**Test Case 4: Mobile Device Compatibility**

1.  Access the website on various mobile devices.
2.  Check for layout issues and readability.
    -   _Expected Outcome:_ The website is responsive and displays correctly on mobile devices.

### Test Results

#### Functional Testing:

-   Test Case 1: Passed
-   Test Case 2: Passed

#### Usability Testing:

-   Test Case 3: Passed

#### Responsiveness Testing:

-   Test Case 4: Passed

## Bugs Fixed

- 'User' object has no attribute 'profile'
    * SOLUTION: Modifying the signal to create and save profile   

- Forbidden CSRF verification failed
   * SOLUTION: Added URL to CSRF_TRUSTED_ORIGINS =[]

## Code Validator Results


