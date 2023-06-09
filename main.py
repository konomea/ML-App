from flask import Flask, redirect, render_template, request, url_for
import numpy as np
import pickle

import db

model = pickle.load(open('c:/Users/vmadmin/Documents/ML App/model/classifier.pkl', 'rb'))


#initialize
app = Flask(__name__)
# db.init()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == "POST":
        #collect information from request.form['id']
        name = request.form['name']
        hp = int(request.form['hp'])
        attack = int(request.form['attack'])
        defense = int(request.form['defense'])
        speed = int(request.form['speed'])
        sp_attack = int(request.form['sp_attack'])
        sp_defense = int(request.form['sp_defense'])

        desc = request.form['desc']
        img = request.form['img']
        
        # issue that these aren't named but model takes named features, look into later
        x = [[hp, attack, defense, speed, sp_attack, sp_defense]]
        y_pred = model.predict(x) #USE MODEL TO GIVE INPUTS HERE
        
        x = {
            "hp": hp, "name": name, "attack": attack, "defense": defense, "speed": speed,
            "sp_attack": sp_attack, "sp_defense": sp_defense, 
            "desc": desc, "img": img, "cluster": int(y_pred)
        }
        db.insert(x)
        
        return render_template('results.html', stats = x)
    
    else:
        return render_template('form.html')

@app.route('/record/<id>')
def record(id):
    row = db.get_pokemon_from_id(id)
    x = {
            "hp": row["hp"], "name": row["name"], "attack": row["attack"], "defense": row["defense"], "speed": row["speed"],
            "sp_attack": row["sp_attack"], "sp_defense": row["sp_defense"], 
            "desc": row["desc"], "img": row["img"], "cluster": row["cluster"]
        }
    return render_template('results.html', stats = x)

@app.route('/model_info')
def model_info():
    return render_template('model.html')
    
@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/history')
def history():
    rows = db.get_pokemon()
    html = ""
    for row in rows:
        html += f"""
        <div class='col-md-4 col-xl-3'>
            <div class='card'>
                <img src="{row['img']}" class='card-img-top'>
                <div class='card-body'>
                    <h5 class='card-title'>{row['name']}</h5>
                    <p class='card-text'>{row['cluster']}</p>
                    <div class='d-flex justify-content-center'>
                        <a href='{{{{url_for('record', id={row['id']})}}}}' class='btn btn-dark-gradient'>Full Results</a>
                    </div>
                </div>
            </div>
        </div>"""
    
    f = open('templates/history_cards.html', 'w')
    f.write(html)
    f.close()
    return render_template('history.html')
    
@app.route('/visualize', methods=['GET'])
def visualize():
    return render_template('visualize.html')

if __name__=="__main__":
    app.run(debug=True)