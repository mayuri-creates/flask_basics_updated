"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using Flask with all pages working.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template, abort, request

# =========================
# Initialize Flask App
# =========================
app = Flask(__name__)

# =========================
# Personal Info & Data
# =========================
PERSONAL_INFO = {
    'name': 'Mayuri',
    'title': 'Python & Flask Developer',
    'bio': 'I am an MCA graduate learning backend development using Flask and Python.',
    'email': 'mayurimahajan252@gmail.com',
    'github': 'https://github.com/mayuri-creates',
    'linkedin': 'https://www.linkedin.com/in/mayuri-mahajan-a44378244/',
}

SKILLS = [
    {'name': 'Python', 'level': 85},
    {'name': 'Flask', 'level': 70},
    {'name': 'HTML/CSS', 'level': 80},
    {'name': 'JavaScript', 'level': 55},
    {'name': 'SQL', 'level': 65},
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'My portfolio built using Flask.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Student Management System', 'description': 'CRUD app using Flask and SQLite.', 'tech': ['Python', 'Flask', 'SQLite'], 'status': 'In Progress'},
    {'id': 3, 'name': 'Blog Platform', 'description': 'Simple blog with authentication.', 'tech': ['Flask', 'SQL', 'HTML'], 'status': 'In Progress'},
]

BLOG_POSTS = [
    {'id': 1, 'title': 'Learning Flask', 'content': 'Flask is a lightweight Python web framework...', 'date': '2025-01-05'},
    {'id': 2, 'title': 'Why I Love Python', 'content': 'Python is simple, powerful, and versatile...', 'date': '2025-01-10'},
    {'id': 3, 'title': 'My First Web App', 'content': 'Building my first Flask app was exciting...', 'date': '2025-01-15'},
]

# =========================
# ROUTES
# =========================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO, page_title=f"Home | {PERSONAL_INFO['name']}")

@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS, page_title=f"About | {PERSONAL_INFO['name']}")

@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS, page_title=f"Projects | {PERSONAL_INFO['name']}")



@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in PROJECTS if p['id'] == project_id), None)

    if project is None:
        abort(404)

    return render_template(
        'project_detail.html',
        project=project,
        project_id=project_id,
        info=PERSONAL_INFO,
        page_title=f"{project['name']} | {PERSONAL_INFO['name']}"
    )



@app.route('/blog')
def blog():
    return render_template('blog.html', info=PERSONAL_INFO, posts=BLOG_POSTS, page_title=f"Blog | {PERSONAL_INFO['name']}")

@app.route('/skill/<skill_name>')
def skill_projects(skill_name):
    matched_projects = [
        project for project in PROJECTS
        if skill_name.lower() in [tech.lower() for tech in project['tech']]
    ]
    message = None
    if not matched_projects:
        message = f"No projects found using {skill_name.title()}."
    return render_template('skill.html', info=PERSONAL_INFO, skill=skill_name.title(), projects=matched_projects, message=message, page_title=f"{skill_name.title()} Projects | {PERSONAL_INFO['name']}")

@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO, page_title=f"Contact | {PERSONAL_INFO['name']}")

# =========================
# Run the App
# =========================
if __name__ == '__main__':
    app.run(debug=True)
