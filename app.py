from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    books = [
        {
        'title': 'キセキの大逆転',
        'price': 1200,
        'arrival_day': '2024年3月14日'
        },
        {
        'title': '常識を疑え',
        'price': 1420,
        'arrival_day': '2024年3月15日'
        },
        {
        'title': 'GitHUB',
        'price': 2200,
        'arrival_day': '2024年3月17日'
        },
        {
        'title': 'PythonAnyWhere',
        'price': 2420,
        'arrival_day': '2024年3月17日'
        }        
    ]
    return render_template('index.html', books=books)

@app.route('/form')
def form():
    return render_template('form.html')

# if __name__=='__main__':
#    app.run('0.0.0.0', 5500, debug=True)
