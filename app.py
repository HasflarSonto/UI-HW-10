from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Simple list to store quiz answers
quiz_answers = []

timestamps = []

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/learn/<int:lesson_number>')
def learn(lesson_number):

    # user goes into lesson

    timestamps.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    print(timestamps)


    # If we've completed all lessons, redirect to quiz intro
    if lesson_number > 4:  # Assuming 4 lessons total
        return redirect(url_for('quiz_intro'))
    
    # Special case for exposure lesson
    if lesson_number == 2:
        return render_template('exposure.html')
    
    return render_template('learn.html', lesson_number=lesson_number)

@app.route('/quiz-intro')
def quiz_intro():
    # Clear previous answers when starting a new quiz
    quiz_answers.clear()
    return render_template('quiz_intro.html')

@app.route('/quiz/<int:question_number>')
def quiz(question_number):
    # If we've completed all questions, redirect to results
    if question_number > 5:  # Assuming 5 questions total
        return redirect(url_for('results'))
    return render_template('quiz.html', question_number=question_number)

@app.route('/results')
def results():
    return render_template('results.html')

# API Routes
@app.route('/api/progress', methods=['GET', 'POST'])
def track_progress():
    if request.method == 'POST':
        data = request.json
        question_number = data.get('question_number')
        answer = data.get('answer')
        
        # Get the correct answer from quiz.json
        with open('static/data/quiz.json', 'r') as f:
            import json
            quiz_data = json.load(f)
            correct_answer = next(q['correctAnswer'] for q in quiz_data['questions'] if q['number'] == question_number)
            
            # Store 1 for correct answer, 0 for incorrect
            quiz_answers.append(1 if answer == correct_answer else 0)
            
        return jsonify({'status': 'success'})
    else:
        # GET request to retrieve all progress
        return jsonify(quiz_answers)

if __name__ == '__main__':
    app.run(debug=True) 