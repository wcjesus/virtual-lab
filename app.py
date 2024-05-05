# app.py

from flask import Flask, render_template, request, send_file
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    frequency = request.form['frequency']
    amplitude = request.form['amplitude']

    # Call the Fortran executable to generate data
    subprocess.run(["./sine_data", frequency, amplitude])

    # Read data from file
    data = np.loadtxt('data.txt')
    x = data[:, 0]
    y = data[:, 1]

    # Generate plot
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('Plot')

    # Save plot as image
    plot_path = 'static/plot.png'
    plt.savefig(plot_path)
    plt.close()

    return render_template('index.html', plot_path=plot_path)

@app.route('/plot_image')
def plot_image():
    return send_file('static/plot.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
