import os
from flask import Flask, request, abort, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from models import setup_db, db, Question, Category


def pagination(request):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10

    return start, end

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    # Set up CORS
    CORS(app, resources={'/': {'origins': '*'}})

    @app.after_request
    def after_request(response):

        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/categories')
    def get_categories():
        categories = Category.query.all()
        data = {}
        for category in categories:
            data[category.id] = category.type

        return jsonify({
            'success': True,
            'categories': data
        })

    @app.route('/questions')
    def get_questions():

        data_questions = []
        data_category = {}
        categories = Category.query.all()
        questions = Question.query.all()
        paginate = pagination(request)

        for question in questions:
            data_questions.append({
                'id': question.id,
                'question': question.question,
                'answer': question.answer,
                'difficulty': question.difficulty,
                'category': question.category,
            })

        for category in categories:
            data_category[category.id] = category.type

        return jsonify({
            'success': True,
            'questions': data_questions[min(paginate):max(paginate)],
            'total_questions': len(questions),
            'categories': data_category
        })

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            Question.query.get(question_id).delete()
            return jsonify({
                'success': True,
                'deleted': question_id
            })

        except:
            abort(422)

    @app.route('/questions/create', methods=['POST'])
    def create_question():
        data = request.get_json()
        try:
            new_question = Question(
                question=data.get('question'),
                answer=data.get('answer'),
                difficulty=data.get('difficulty'),
                category=data.get('category'),
            )
            new_question.insert()

        except:
            abort(422)
        
        return jsonify({
            'success': True,
            'total_questions': len(Question.query.all())
        })

    @app.route('/questions/search', methods=['POST'])
    def search_question():
        data = request.get_json()
        data_questions = []
        data_category = {}
        
        try:
            search_term = data.get('searchTerm')

            if search_term == '':
                abort(422)

            questions = Question.query.filter(
                Question.question.ilike(f'%{search_term}%')).all()
            
            paginate = pagination(request)

            for question in questions:
                data_questions.append({
                    'id': question.id,
                    'question': question.question,
                    'answer': question.answer,
                    'difficulty': question.difficulty,
                    'category': question.category,
                })

        except:
            abort(422)
        
        return jsonify({
            'success': True,
            'questions': data_questions[min(paginate):max(paginate)],
            'total_questions': len(Question.query.all()),
        })

    @app.route('/categories/<int:category_id>/questions')
    def get_questions_by_category(category_id):

        data_questions = []
        category = Category.query.filter_by(id=category_id).one_or_none()
        questions = Question.query.filter_by(category=category_id).all()
        paginate = pagination(request)

        for question in questions:
            data_questions.append({
                'id': question.id,
                'question': question.question,
                'answer': question.answer,
                'difficulty': question.difficulty,
                'category': question.category,
            })

        return jsonify({
            'success': True,
            'questions': data_questions[min(paginate):max(paginate)],
            'total_questions': len(questions),
            'current_category': category.type
        })

    @app.route('/quizzes', methods=['POST'])
    def get_random_quiz_question():

        data = request.get_json()
        previous_questions = data.get('previous_questions')
        quiz_category = data.get('quiz_category')

        if quiz_category['id'] == 0:
            questions = Question.query.all()

        else:
            questions = Question.query.filter_by(
                category=quiz_category['id']).all()

        
        questions = [question.format()
                     for question in questions if question.id not in previous_questions]


        return jsonify({
            'success': True,
            'question': random.choice(questions),
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    return app
