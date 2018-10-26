# Store-manager-2

Store Manager is a web application that helps store owners manage sales and product inventory
records. This application is meant for use in a single store.
[![Build Status](https://travis-ci.org/e-ian/Store-manager-2.svg?branch=ft_challenge_2)](https://travis-ci.org/e-ian/Store-manager-2)
[![Coverage Status](https://coveralls.io/repos/github/e-ian/Store-manager-2/badge.svg?branch=ft_challenge_2)](https://coveralls.io/github/e-ian/Store-manager-2?branch=ft_challenge_2)
[![Maintainability](https://api.codeclimate.com/v1/badges/92702517d537517d9d3c/maintainability)](https://codeclimate.com/github/e-ian/Store-manager-2/maintainability)

# Getting started.

These instructions will help you set and run the application on your local machine.

# Prerequisites

The following are required to enable you get started!

* Serverside Framework: Flask Python Framework
* Testing Framework: Pytest
* API development environment: Postman
* GIT
* IDE/Text editor(Vs Code preferred)
* Python 3.6

# Project links:

## User interface: 
* The project user interface pages are hosted on gh-pages and can be accessed on this link: (https://e-ian.github.io/Store-Manager/UI/index.html). 
* The code for the UI templates can be accessed using this link: (https://github.com/e-ian/Store-Manager/tree/feat-UI)

## API endpoints: 
* The code for the endpoints can be accessed using this link: (https://github.com/e-ian/Store-manager-2/tree/ft_challenge_2)

# Installation.
* Clone the remote repository to your local machine using this command:

```git clone https://github.com/e-ian/Store-manager-2.git``` 

* You can access the project on your local machine by using git bash commands `cd` to navigate the directory and `code .` if using Vs Code to open the code on your local machine.

* Create a virtual environment.

```virtualenv venv```

* Install a virtual environment.

```pip install virtualenv``` 

* Activate your virtual environment.

```venv\Scripts\activate```

* Install dependencies.

To install all required dependencies for the project, use the command:

```pip install -r requirements.txt```

* Install Postman.


# Project features/ functionality

## Interface

* Store attendant can search and add products to buyer's cart.
* Store attendant can see his/her sale records but can’t modify them.
* App should show available products, quantity and price.
* Store owner can see sales and can filter by attendants.
* Store owner can add, modify and delete products.

# API Endpoints

|   Method | Route                           | Functionality             |
|----------|:-------------------------------:|--------------:            |
| POST     | "/api/v1/products"              | Create a product          |
| POST     | "/api/v1/sales"                 | Create a sale order       |
| GET      | "/api/v1/products"              | Fetches all products      |
| GET      | "/api/v1/products/<product_id>" | Fetches a single product  |
| GET      | "/api/v1/sales"                 | Fetches all sales         |
| GET      | "/api/v1/sales/<sale_id>"       | Fetches single sale record|



# Running unittests.

* Install pytest from terminal

`pip install pytest`

* Test your endpoints in the terminal

`pytest tests/test_api.py`

* To run tests and get coverage report

`pytest tests --cov=api --cov-report term-missing`

# Deployment

The app has been hosted on heroku and can be accessed using the following link (https://eian.herokuapp.com/)

# Author:

Emmanuel Ogwal











