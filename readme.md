# Photography Learning Platform

A web-based interactive platform to teach the basics of photography, including Rule of Thirds, Exposure, Hue, and Saturation. The app features lessons, interactive tutorials, and a quiz to reinforce learning.

## Features

- **Step-by-step lessons** on core photography concepts
- **Interactive tutorials** with visual guides and instructions
- **Quiz section** to test your understanding
- **Progress tracking** for quiz answers
- **Responsive design** for desktop and mobile

## Project Structure

```
.
├── app.py                  # Flask backend application
├── requirements.txt        # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── js/
│   │   └── main.js         # Common JavaScript logic
│   ├── data/
│   │   ├── lessons.json    # Lesson content and tutorial steps
│   │   └── quiz.json       # Quiz questions and answers
│   └── images/
│       ├── ...             # Lesson, tutorial, and quiz images
│       └── quiz/
│           └── ...         # Quiz-specific images
├── templates/
│   ├── base.html           # Base template
│   ├── home.html           # Home/landing page
│   ├── learn.html          # Standard lesson page
│   ├── tutorial.html       # Interactive tutorial page
│   ├── exposure.html       # Exposure lesson
│   ├── hue.html            # Hue lesson
│   ├── saturation.html     # Saturation lesson
│   ├── quiz.html           # Quiz page
│   ├── quiz_intro.html     # Quiz introduction
│   └── results.html        # Quiz results
└── ...
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```
   The app will start on `http://localhost:5001`.

4. **Open in your browser:**
   - Go to `http://localhost:5001` to start learning!

## Dependencies

- Flask==3.0.2
- Flask-SQLAlchemy==3.1.1
- python-dotenv==1.0.1

## How It Works

- **Lessons** are loaded from `static/data/lessons.json` and rendered dynamically.
- **Tutorials** use step-by-step instructions and images, with special styling for certain images (e.g., Rule of Thirds tutorial image is always 100% width).
- **Quiz** questions are loaded from `static/data/quiz.json`. User answers are tracked and results are shown at the end.
- **Progress API**: `/api/progress` allows tracking and retrieving quiz progress.

## Customization

- Add or edit lessons in `static/data/lessons.json`.
- Add new quiz questions in `static/data/quiz.json`.
- Place new images in `static/images/` or `static/images/quiz/` as needed.
- Adjust styles in `static/css/style.css`.

## License

MIT License (or specify your license here)
