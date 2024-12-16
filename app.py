from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

def load_formulas(category):
    try:
        with open(f'formulas/{category}.json', 'r', encoding='utf-8') as file:
            formulas = json.load(file)
        return formulas
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    category = request.args.get('category', 'math').lower()

    formulas = load_formulas(category)
    results = []

    for formula in formulas:
        if query in formula['name'].lower() or query in formula['explanation'].lower():
            results.append(formula)

    return render_template('index.html', results=results, query=query, category=category)

if __name__ == '__main__':
    app.run(debug=True)
