from flask import Flask, render_template, request
import numpy as np
import pickle

# get model; what is rb?
model = pickle.load(open('c:/Users/vmadmin/Documents/ML App/model/classifier.pkl', 'rb'))


#initialize
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
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

        
        # #put fields into this to be collected later
        x = [[hp, attack, defense, speed, sp_attack, sp_defense]]
        y_pred = model.predict(x) #USE MODEL TO GIVE INPUTS HERE
        
        
        return render_template('results.html', prediction = y_pred, stats = x, name = name)
    
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
    