import pandas as pd
from jinja2 import Template

# Load data from CSV
data = pd.read_csv('data.csv')

# Define HTML template
template = Template("""
<!DOCTYPE html>
<html>
<head>
    <title>Static Page Example</title>
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
            width: 200px;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
        }
        .card h3 {
            margin-top: 0;
        }
    </style>
</head>
<body>
    <div class="container">
    {% for item in data %}
        <div class="card">
            <h3>{{ item['title'] }}</h3>
            <p>{{ item['description'] }}</p>
        </div>
    {% endfor %}
    </div>
</body>
</html>
""")

# Render HTML with data
html_content = template.render(data=data.to_dict(orient='records'))

# Save HTML to file
with open('output.html', 'w') as file:
    file.write(html_content)

print('Static HTML page generated successfully!')