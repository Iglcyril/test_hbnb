C#26 🎓 – HBnB Team Project – Part 2
🏠 Overview

This project is Part 2 of the HBnB application developed at Holberton School.
It focuses on implementing the Business Logic layer and exposing it through a RESTful API built with Flask and Flask-RESTx.

The goal is to design a clean, modular backend architecture using layered principles and the Facade pattern.

🎯 Objectives

Build a modular Flask application structure

Implement core business models:

User

Place

Review

Amenity

Create RESTful CRUD endpoints

Implement a Facade layer to connect API and business logic

Use an in-memory repository (extensible to database later)

Implement unit and integration tests

🗂️ Project Structure
hbnb/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── basemodel.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   └── facade.py
│   ├── persistence/
│   │   └── repository.py
├── tests/
├── run.py
├── config.py
├── requirements.txt
🧱 Architecture

The application follows a layered architecture:

🔹 API Layer (Presentation)

Built with Flask + Flask-RESTx

Handles HTTP requests and responses

Provides Swagger documentation

🔹 Business Logic Layer

Contains entity definitions

Handles validations and relationships

Manages object behavior

🔹 Persistence Layer

In-memory repository

Abstracted for future database integration

🔹 Facade Layer

Central access point between API and business logic

Simplifies interactions between layers

🏗️ Implemented Features
👤 Users

Create user

Get all users

Get user by ID

Update user

Password is stored securely and not returned in API responses.

🏷️ Amenities

Create amenity

List amenities

Get amenity by ID

Update amenity

🏠 Places

Create place (linked to owner and amenities)

List places

Get place by ID (includes related data)

Update place

📝 Reviews

Create review

List reviews

Get review by ID

Update review

Delete review

🚀 Running the Project
1️⃣ Install dependencies
pip3 install -r requirements.txt
2️⃣ Run the server
python3 run.py

Server runs on:

http://localhost:5000

Swagger documentation available at:

http://localhost:5000/api/v1/
🧪 Running Tests

Run all unit tests:

export PYTHONPATH=$PYTHONPATH:$(pwd)
python3 -m unittest discover tests
🔎 Example API Usage

Create a user:

curl -X POST http://localhost:5000/api/v1/users/ \
-H "Content-Type: application/json" \
-d '{"first_name":"Alice","last_name":"Doe","email":"alice@example.com"}'

List users:

curl http://localhost:5000/api/v1/users/
📌 Technical Stack

Python 3

Flask

Flask-RESTx

unittest

📚 Concepts Used

Layered architecture

REST API design

Facade Design Pattern

Object-Oriented Programming

Data serialization

👥 Team

Holberton School – HBnB Project
C#26 Cohort

Si tu veux, je peux te faire :

🔥 Une version plus “pro” orientée portfolio

🎯 Une version plus courte pour évaluation Holberton

💣 Une version optimisée pour recruteurs (cybersécurité / backend focus)

Tu veux laquelle ?

un peu plus complète

Parfait 👌
Voici une version plus complète, plus professionnelle, tout en restant claire et lisible pour ton repo holbertonschool-hbnb/part2/hbnb.

C#26 🎓 – HBnB Team Project – Part 2
🏠 Overview

HBnB is a backend web application inspired by AirBnB, developed as part of the Holberton School curriculum.

This second part focuses on building:

The Business Logic Layer

The RESTful API (Presentation Layer)

A clean and modular backend architecture

The project is built using Python, Flask, and Flask-RESTx, following layered architecture principles and applying the Facade Design Pattern.

🎯 Project Goals

By the end of Part 2, the application supports:

Modular Flask application structure

Object modeling with relationships

RESTful CRUD endpoints

In-memory persistence layer

Separation of concerns (API / Business / Persistence)

Data validation and serialization

Unit and integration testing

🧱 Architecture Overview

The application follows a layered architecture to ensure scalability and maintainability.

🔹 1. API Layer (Presentation)

Built with Flask and Flask-RESTx

Defines REST endpoints

Handles request parsing and response formatting

Automatically generates Swagger documentation

Location:

app/api/v1/
🔹 2. Business Logic Layer

Contains all domain models and application logic.

Implemented Models:

BaseModel

id (UUID)

created_at

updated_at

User

first_name

last_name

email

password (not exposed in API)

Place

title

description

price

latitude / longitude

owner (User relationship)

amenities (Many-to-Many)

Amenity

name

Review

text

rating

linked to User and Place

Location:

app/models/
🔹 3. Persistence Layer

In-memory repository implementation

Abstracted storage layer

Easily replaceable with database (PostgreSQL, MySQL, etc.)

Location:

app/persistence/repository.py
🔹 4. Facade Layer

The Facade pattern is used to:

Centralize business operations

Decouple API from model logic

Provide a clean service interface

Location:

app/services/facade.py
🗂️ Project Structure
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   └── v1/
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── basemodel.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   └── facade.py
│   ├── persistence/
│   │   └── repository.py
├── tests/
├── run.py
├── config.py
├── requirements.txt
🚀 API Endpoints

All routes are prefixed with:

/api/v1/
👤 Users
Method	Endpoint	Description
POST	/users/	Create a user
GET	/users/	List users
GET	/users/<id>	Get user by ID
PUT	/users/<id>	Update user

⚠️ Passwords are stored but never returned in API responses.
🚫 DELETE not implemented.

🏷️ Amenities

| Method | Endpoint | Description |
|--------|----------|------------ |
| POST | amenities | Create |
| GET	| amenities | List all |
| GET	| amenities/<id> | Retrieve one |
| PUT	| amenities/<id> | Update |

🏠 Places
Method	Endpoint	Description
POST	/places/	Create place
GET	/places/	List all places
GET	/places/<id>	Retrieve place (with owner & amenities)
PUT	/places/<id>	Update
📝 Reviews
Method	Endpoint	Description
POST	/reviews/	Create
GET	/reviews/	List
GET	/reviews/<id>	Retrieve
PUT	/reviews/<id>	Update
DELETE	/reviews/<id>	Delete

✅ DELETE available only for Reviews.

🧪 Testing
✅ Run Unit Tests
export PYTHONPATH=$PYTHONPATH:$(pwd)
python3 -m unittest discover tests
▶️ Running the Application
1️⃣ Install dependencies
pip3 install -r requirements.txt
2️⃣ Start the server
python3 run.py

Server will run on:
```code
http://localhost:5000
```

Swagger documentation:
```code
http://localhost:5000/api/v1/
```
🧪 Example cURL Request

Create a user:
```bash
curl -X POST http://localhost:5000/api/v1/users/ \
-H "Content-Type: application/json" \
-d '{"first_name":"Alice","last_name":"Doe","email":"alice@example.com"}'
```
🛠️ Technologies Used

Python 3

Flask

Flask-RESTx

unittest

UUID

RESTful API principles