
from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Load COMPAS dataset (replace with your dataset path)
df = pd.read_csv('cox-violent-parsed_filt_usable.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_plot')
def generate_plot():
    # Data analysis and visualization
    gender_counts = df['sex'].value_counts()
    age_counts = df['age_cat'].value_counts()
    race_counts = df['race'].value_counts()
    
    recidivism_counts = df[['is_violent_recid', 'is_recid', 'event']].apply(pd.Series.value_counts)
    
    # Plot 1: Gender Distribution
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    gender_counts.plot(kind='bar', color='skyblue')
    plt.title('Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    
    # Plot 2: Age Category Distribution
    plt.subplot(2, 2, 2)
    age_counts.plot(kind='bar', color='lightcoral')
    plt.title('Age Category Distribution')
    plt.xlabel('Age Category')
    plt.ylabel('Count')
    
    # Plot 3: Race Distribution
    plt.subplot(2, 2, 3)
    race_counts.plot(kind='bar', color='lightgreen')
    plt.title('Race Distribution')
    plt.xlabel('Race')
    plt.ylabel('Count')
    
    # Plot 4: Recidivism Counts
    plt.subplot(2, 2, 4)
    recidivism_counts.plot(kind='bar', stacked=True)
    plt.title('Recidivism Counts')
    plt.xlabel('Recidivism Type')
    plt.ylabel('Count')
    
    # Adjust layout
    plt.tight_layout()

    # Convert plot to base64-encoded string
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_str = base64.b64encode(img_buffer.read()).decode('utf-8')
    
    # Clear the plot for reuse
    plt.clf()

    return render_template('plot.html', img_str=img_str)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
=======
from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Load COMPAS dataset (replace with your dataset path)
df = pd.read_csv('cox-violent-parsed_filt_usable.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_plot')
def generate_plot():
    # Data analysis and visualization
    gender_counts = df['sex'].value_counts()
    age_counts = df['age_cat'].value_counts()
    race_counts = df['race'].value_counts()
    
    recidivism_counts = df[['is_violent_recid', 'is_recid', 'event']].apply(pd.Series.value_counts)
    
    # Plot 1: Gender Distribution
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    gender_counts.plot(kind='bar', color='skyblue')
    plt.title('Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    
    # Plot 2: Age Category Distribution
    plt.subplot(2, 2, 2)
    age_counts.plot(kind='bar', color='lightcoral')
    plt.title('Age Category Distribution')
    plt.xlabel('Age Category')
    plt.ylabel('Count')
    
    # Plot 3: Race Distribution
    plt.subplot(2, 2, 3)
    race_counts.plot(kind='bar', color='lightgreen')
    plt.title('Race Distribution')
    plt.xlabel('Race')
    plt.ylabel('Count')
    
    # Plot 4: Recidivism Counts
    plt.subplot(2, 2, 4)
    recidivism_counts.plot(kind='bar', stacked=True)
    plt.title('Recidivism Counts')
    plt.xlabel('Recidivism Type')
    plt.ylabel('Count')
    
    # Adjust layout
    plt.tight_layout()

    # Convert plot to base64-encoded string
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_str = base64.b64encode(img_buffer.read()).decode('utf-8')
    
    # Clear the plot for reuse
    plt.clf()

    return render_template('plot.html', img_str=img_str)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
