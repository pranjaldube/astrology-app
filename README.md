# India Today Astrology App
## Introduction

This repository contains the code for the backend setup of the India Today Astrology app as a part of their recruitment process for internship.

### Relevant Links

- [Problem Statement](https://docs.google.com/document/d/10dP7KHRoT3K97t1dliecDtlj9Q5-xR8E0gCxUUopWac/edit)

## Table Of Content
- [Development Environment](#development-environment)
- [Dependencies](#dependencies)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Models](#models)

## Development Environment
Download the following
```bash
- python version: python3.9.7 windows-64    # https://www.python.org/downloads/release/python-397/
- PostgreSql version 13.4         #https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
- text editor: VSCode    	# https://code.visualstudio.com/download
- terminal: Windows Terminal     		# https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701
```

## Dependencies
Install the following Python packages
```bash
pip install django
pip install djangorestframework
pip install psycopg2
```
## Prerequisites
-Open the PostgreSQL shell. You can find the PSQL Shell in the Start Menu.
-The shell will prompt you for Server, Database, Port, and Username details. Set it to default by clicking on the Enter button in the keyboard without providing any value. Finally, the shell will prompt you for the Password. Provide the password that you used during the PostgreSQL installation.
-Create a PostgreSQL database via the following steps:
```bash
CREATE DATABASE indiatoday;
CREATE USER kesha WITH PASSWORD '1234';
ALTER ROLE kesha SET client_encoding TO 'utf8';
ALTER ROLE kesha SET default_transaction_isolation TO 'read committed';
ALTER ROLE kesha SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE helloworld TO kesha;
```
To make sure that you have connected to the PostgreSQL database.
```bash
python manage.py makemigrations
python manage.py migrate
```
## Usage
```bash
git clone https://github.com/pranjaldube/astrology-app.git
cd 
go run main.go     
#, or build the program and run the executable
go build
./iitk-coin
# , or build docker image and run docker container
docker build -t iitk-coin .
docker run --rm -it -p 8080:8080 iitk-coin
```

Output should look like

```
2021/06/20 23:59:40 User Database opened and table created (if not existed) successfully!
2021/06/20 23:59:40 Transaction Database opened and table created (if not existed) successfully!
2021/06/20 23:59:40 Wallet Database opened and table created (if not existed) successfully!
2021/06/20 23:59:40 Serving at 8080
```

## Endpoints
POST requests take place via `JSON` requests. A typical usage would look like

```bash
curl -d '<json-request>' -H 'Content-Type: application/json' http://localhost:8080/<endpoint>
```

- `/login` : `POST`
```json
{"name":"<name>", "rollno":"<rollno>", "password":"<password>"}
```

- `/signup` : `POST`
```json
{"rollno":"<rollno>", "password":"<password>"}
```

- `/reward` : `POST`
```json
{"rollno":"<rollno>", "coins":"<coins>"}
```

- `/transfer` : `POST`
```json
{"sender":"<senderRollNo>", "receiver":"<receiverRollNo>", "coins":"<coins>"}
```

GET requests:

- `/secretpage` : `GET`
```bash
curl http://localhost:8080/secretpage
```

- `/balance` : `GET`
```bash
curl http://localhost:8080/balance?rollno=<rollno>
```

## Models

-  User
```go
	Name     string `json:"name"`
	Rollno   string  `json:"rollno"`
	Password string `json:"password"`
```

- RewardPayload
```go
	Rollno string `json:"rollno"`
	Coins  int64 `json:"coins,string"`
```

- TransferPayload
```go
	SenderRollno   string `json:"sender"`
	ReceiverRollno string `json:"receiver"`
	Coins          int64 `json:"coins,string"`
```
