import os, random

from flask import Flask, render_template, request, redirect, url_for


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    @app.route('/myPage/')
    def hello():
        with open("flaskr/scores.txt") as f:
            data = f.read().split('\n')
        return render_template("index.html", fin=data[0], flm=data[1], mcd=data[2])

    @app.route('/compTest/')
    def comp_test():
        return render_template("comp.html")

    @app.route('/get-post', methods=["POST", "GET"])
    def login():
        y = open("flaskr/questions.txt", 'r')
        q = y.read().split('\n')
        y.close()
        x = open("flaskr/answers.txt", 'r')
        a = x.read().split('\n')
        x.close()
        q_num = random.randint(0, len(q)-1)
        q = q[q_num]
        a = a[q_num]
        a = a.split(" ; ")
        if request.method == "POST":
            user = request.form["multichoice"]
            if user == "item1":
                chosen = a[0]
            elif user == "item2":
                chosen = a[1]
            elif user == "item3":
                chosen = a[2]
            return f"<h1>{chosen}</h1>"
        else:
            return render_template("get_post_test.html", question=q, item=a)

    @app.route("/<usr>")
    def user_login(usr):
        return f"<h1>{usr}</h1>"

    @app.route("/question-test", methods=["GET", "POST"])
    def question_test():
        with open("flaskr/questions.txt") as q:
            d = q.read().split('\n')
        var = random.randint(0, len(d)-1)
        with open("flaskr/answers.txt") as a:
            d = a.read().split('\n')
        if request.method == "POST":
            an = request.form["question"]
            if an == d[var]:
                an = "yes"
            else:
                an = "no"
            return redirect(url_for("user_login", usr=an))
        else:
            return render_template("question.html", qs=d[var])

    return app
