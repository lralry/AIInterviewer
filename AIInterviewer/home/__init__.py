from flask import Blueprint,render_template
home = Blueprint("home",__name__)
@home.route('/')
def aiinterviewer():
    return render_template("web.html")