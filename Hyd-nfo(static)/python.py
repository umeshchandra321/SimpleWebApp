import pandas as pd
from jinja2 import Template
import os

# List of CSV files
csv_files = [
    'Dental_clinics.csv', 
    'Pharmacies.csv', 
    'Physiotherapy.csv'
]

# HTML template
template_str = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{ page_title }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .container {
            display: flex;
            flex-wrap: wrap;
        }
        .card {
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 16px;
            margin: 8px;
            width: 300px;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
        }
        .card h3 {
            margin-top: 0;
        }
        .card p {
            margin-bottom: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
    {% for item in data %}
        <div class="card">
            <h3>{{ item['Companyname'] }}</h3>
            <p>Phone: {{ item['Phone'] }}</p>
            <p>Address: {{ item['Address'] }}</p>
        </div>
    {% endfor %}
    </div>
</body>
</html>
"""

# Create Jinja2 template
template = Template(template_str)

# Loop through each CSV file and generate an HTML file
for csv_file in csv_files:
    print(f"Processing file: {csv_file}")
    try:
        # Load data from CSV
        data = pd.read_csv(csv_file)

        # Debug print to check loaded data
        print("Loaded data:")
        print(data)

        # Filter rows where Address contains '500060'
        filtered_data = data[data['Address'].str.contains('500060', na=False)]

        # Debug print to check filtered data
        print("Filtered data:")
        print(filtered_data)

        # Extract the base name of the file without extension for the page title
        page_title = os.path.splitext(csv_file)[0].replace('_', ' ').title()

        # Render HTML with data
        html_content = template.render(data=filtered_data.to_dict(orient='records'), page_title=page_title)

        # Create output HTML file name based on CSV file name
        output_file = f"{os.path.splitext(csv_file)[0]}.html"

        # Save HTML to file with UTF-8 encoding
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)

        print(f'Static HTML page generated successfully for {csv_file}!')
    except Exception as e:
        print(f"Error processing file {csv_file}: {e}")
