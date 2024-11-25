from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    first_name = 'Kimbo'
    content = 'This is bold text'

    favorite_pets = ['Frodek', 'Kajtek', 'Pajka', 'Lilka']
    return render_template('index.html', my_name=first_name, content=content, favorite_pets=favorite_pets)


# second endpoint
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# CUSTOM ERROR PAGES

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html', e=e), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)