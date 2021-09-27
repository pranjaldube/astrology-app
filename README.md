# India Today Astrology App
## Introduction

This repository contains the code for the **Backend setup** of the India Today Astrology app as a part of their recruitment process for internship.

### Relevant Links

- [Problem Statement](https://docs.google.com/document/d/10dP7KHRoT3K97t1dliecDtlj9Q5-xR8E0gCxUUopWac/edit)

## Table Of Content
- [Development Environment](#development-environment)
- [Dependencies](#dependencies)
- [Setup](#setup)
- [Usage](#usage)
- [Models](#models)
- [URL Endpoints](#url-endpoints)
- [Images](#images)

## Development Environment
```bash
- python version: python3.9.7 windows-64    # https://www.python.org/downloads/release/python-397/
- PostgreSql version 13.4         			# https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
- text editor: VSCode    					# https://code.visualstudio.com/download
- terminal: Windows Terminal     			# https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701
```

## Dependencies
Install the following Python packages
```bash
pip install -r requirements.txt
```
## Prerequisites

Clone the repository

```
git clone https://github.com/pranjaldube/astrology-app.git
cd indiaToday
```

- Open the PostgreSQL shell. You can find the PSQL Shell in the Start Menu.
- The shell will prompt you for Server, Database, Port, and Username details. Set it to default by clicking on the Enter button in the keyboard without providing any value. Finally, the shell will prompt you for the Password. Provide the password that you used during the PostgreSQL installation.
- Create a PostgreSQL database via the following steps (here, `kesha` and `1234` are dummy user credentials):

```bash
CREATE DATABASE indiatoday;
CREATE USER kesha WITH PASSWORD '1234';
ALTER ROLE kesha SET client_encoding TO 'utf8';
ALTER ROLE kesha SET default_transaction_isolation TO 'read committed';
ALTER ROLE kesha SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE indiatoday TO kesha;
```
To make sure that you have connected and uploaded schema to the PostgreSQL database.
```bash
python manage.py makemigrations
python manage.py migrate
```
Load the dummy database to PostgreSQL with

```
python manage.py loaddata dumpdata.json
```

## Usage

Run the server

```bash
python manage.py runserver
```

The app will be served at <http://127.0.0.1:8000/home>

You should also create superuser to view **Django-admin dashboard**

```
python manage.py createsuperuser
```

And login with your credentials at <http://127.0.0.1:8000/admin> to view all the tables and their data.

## Models

Defined in `indiaToday/astroApp/models.py`.

- `AstrologerDetails`
- `Reports`
- `BannerOffers`
- `Horoscopes`
- `Questions`
- `Testimonials`

## URL Endpoints

Defined in `indiaToday/astroApp/urls.py` and methods defined in `indiaToday/astroApp/views.py`

`/home`: GET request to <http://127.0.0.1:8000/home> returns combined GET request data from all 6 APIs below, each designed for specific model as mentioned in the problem statement. 

- `/astro_data`: List of all astrologers and their details.

- `/questions_data`: Get question categories from API and show them in the dropdown list.

- `/horoscopes_data`: Get all horoscopes list from API

- `/banneroffers_data` : Get details from API of the images and redirection screen when clicked.

- `/reports_data`: List of all the reports.

- `/testimonials_data`: Get customer feedback and show them in the horizontal list.

  > __*NOTE*__ : Although the 6 APIs would be used to retrieve data (hence the GET method), but they have been equipped additionally with POST, PUT and DELETE methods.

## Images

Sample images of use case goes here.

![](assets\admin.png)

![](assets/astro_data)

![](assets/banneroffers_data)

![](assets/home)

![](assets/horoscopes_data)

![](assets/questions_data)

![](assets/reports_data)

![](assets/testimonials_data)