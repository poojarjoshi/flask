from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
     return 'method is %s' %request.method


@app.route('/tuna')
def tuna():
     return '<h2>Tuna is good </h2> '

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', name=username)

@app.route('/post/<int:post_id>')
def post(post_id):
    return 'post id is %s' %post_id

@app.route('/bacon', methods=['GET', 'POST'] )
def bacon():
    if request.method == "POST":
        return 'you are using post'
    else:
        return 'you are using get'

@app.route("/shopping")
def shopping():
    food=["cheese", "tuna" , "beef", "fruits"]
    return render_template("shopping.html",food=food)

if __name__=="__main__":
     app.run(debug=True)
