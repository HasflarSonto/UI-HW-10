from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photography.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    lesson_number = db.Column(db.Integer)
    quiz_answers = db.Column(db.String(500))  # Store as JSON string

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/learn/<int:lesson_number>')
def learn(lesson_number):
    # If we've completed all lessons, redirect to quiz intro
    if lesson_number > 4:  # Assuming 4 lessons total
        return redirect(url_for('quiz_intro'))
    
    # Special case for exposure lesson
    if lesson_number == 2:
        return render_template('exposure.html')
    
    return render_template('learn.html', lesson_number=lesson_number)

@app.route('/quiz-intro')
def quiz_intro():
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
@app.route('/api/progress', methods=['POST'])
def track_progress():
    data = request.json
    progress = UserProgress(
        lesson_number=data.get('lesson_number'),
        quiz_answers=data.get('quiz_answers', '{}')
    )
    db.session.add(progress)
    db.session.commit()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 