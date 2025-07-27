from flask import render_template
from app.main import main_bp

@main_bp.route("/")
def home():
    return render_template("main/home.html")

@main_bp.route("/sobre")
def about():
    return render_template("main/about.html") 