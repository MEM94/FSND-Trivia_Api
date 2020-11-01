# FSND-Trivia_Api
## Introduction

Trivia is a application that display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.

## Instructions
## Full Stack Trivia API Frontend

## Getting Setup

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

npm install

## Required Tasks

## Running Your Frontend in Dev Mode run:

npm start

To view it in the browser open [http://localhost:3000](http://localhost:3000).
 


## Full Stack Trivia API Backend

## Getting Setup

1- Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
psql trivia < trivia.psql

2- Initialize and activate a virtualenv using:
python -m virtualenv env
source env/bin/activate
Note - In Windows, the env does not have a bin directory. Therefore, you'd use the analogous command shown below:
source env/Scripts/activate

3- Install the dependencies:
pip install -r requirements.txt

4- Run the development server:
export FLASK_APP=flaskr
export FLASK_ENV=development
python3 __init__.py


## Endpoints
GET  '/categories'
GET  '/questions'
GET  '/categories/<int:category_id>/questions'
POST '/questions/create'
POST '/quizzes'
DELETE '/questions/<int:question_id>'

### GET '/categories'
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.
- curl -X GET http://127.0.0.1:5000/categories

{
   '1' : "Science",
   '2' : "Art",
   '3' : "Geography",
   '4' : "History",
   '5' : "Entertainment",
   '6' : "Sports"
}

### GET '/questions'
- Request Arguments: None
- Returns: Returns a list of categories and questions, total of questions.
- curl -X GET http://127.0.0.1:5000/questions 


{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 31
}

### GET '/categories/<int:category_id>/questions'
- Request Arguments: None
- Returns: Returns a object of questions that belong to a category Id.
- curl -X GET http://127.0.0.1:5000/categories/1/questions


{
  "current_category": "Science",
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "22",
      "category": 1,
      "difficulty": 2,
      "id": 24,
      "question": "\u0643\u064a\u0641 \u062a\u0642\u062f\u064a\u0645 \u0628\u0644\u0627\u063a \u0644\u0645\u0634\u0631\u0648\u0639 \u0631\u0639\u062f1"
    },
    {
      "answer": "22",
      "category": 1,
      "difficulty": 1,
      "id": 30,
      "question": "\u0643\u064a\u0641 \u062a\u0642\u062f\u064a\u0645 \u0628\u0644\u0627\u063a \u0644\u0645\u0634\u0631\u0648\u0639 \u0631\u0639\u062f1"
    },
    {
      "answer": "111",
      "category": 1,
      "difficulty": 1,
      "id": 31,
      "question": "Test"
    },
    {
      "answer": "111",
      "category": 1,
      "difficulty": 1,
      "id": 32,
      "question": "Test"
    },
    {
      "answer": "111",
      "category": 1,
      "difficulty": 3,
      "id": 34,
      "question": "Test1"
    },
    {
      "answer": "22",
      "category": 1,
      "difficulty": 1,
      "id": 36,
      "question": "test6666655"
    }
  ],
  "success": true,
  "total_questions": 9
}

### POST '/questions/create'
- Request Arguments: None
- Returns: An object of question id, status if it is success or not and total of questions.
- curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/questions/create  -d '{"question":"Test","answer":"Test","category":"1","difficulty":"1"}'

{
    "question_id": 1,
    "success": true, 
    "total_questions": 19
}

### POST '/quizzes'
- Request Arguments: None
- Returns: An object of random questions within the given category, if provided, and that is not one of the previous questions.

{
    "success": true, 
    "question": "What is the largest lake in Africa?"
}

### DELETE '/questions/<int:question_id>'
- Request Arguments: None
- Returns: An object of question id deleted, status if it is success or not and total of questions.
- curl -X DELETE http://127.0.0.1:5000/questions/50

{
  "deleted": 50,
  "success": true
}

## Testing
To run the tests, run

dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py






