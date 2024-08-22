from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-matlab', methods=['POST'])
def run_matlab():
    # Ambil data dari request
    name = request.json.get('name', '')
    age = request.json.get('age', '')
    num1 = request.json.get('num1', 0)
    num2 = request.json.get('num2', 0)

    # Path ke skrip MATLAB
    matlab_script = os.path.join(os.getcwd(), 'matlab', 'script.m')
    
    # Jalankan MATLAB script
    try:
        result = subprocess.run(
            ['matlab', '-batch', f"result = script({num1}, {num2}); disp(result)"], 
            capture_output=True, text=True
        )
        output = result.stdout.strip()
    except Exception as e:
        output = str(e)
    
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
