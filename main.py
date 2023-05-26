from flask import Flask, render_template, request
import pickle

# get model

#initialize
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply', methods=['POST'])
def apply():
    if request.method == "POST":
        #collect information from request.form['id']
        
        #put fields into this to be collected later
        #x = np.array([])
        y_pred = None #USE MODEL TO GIVE INPUTS HERE
        
        return render_template('results.html', prediction = y_pred)
    
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
    