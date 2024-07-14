import pandas as pd
from jinja2 import Template
import os

# List of CSV files
csv_files = ['appliancerepair.csv','Housecleaning.csv','pestcontrol.csv']

# HTML template
template_str = ("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://kit.fontawesome.com/17fedfb487.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="sample.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
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
            width: 100%;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
        }
        .card h3 {
            margin-top: 0;
        }
    </style>
</head>
<body>
    <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-white px-4 border-bottom">
        <div class="container-fluid">
          <a class="navbar-brand fs-1" href="#">Hyderabd-<span class="text-primary">Info</span></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ms-auto mb-2 mb-lg-0 fs-5 text-center">
              <li class="nav-item">
                <a class="nav-link" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link active text-primary" href="petshops_dilsukhnagar.html">PetShops</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="Acmechanic_dilsukhnagar.html">AcMechanics</a>
              </li>
              <li class="nav-item">
                <a class="dropdown-item" href="clinics_dilsuknagar.html">Clinics</a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  More
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li><a class="dropdown-item" href="beautyparlour_dilsukhnagar.html">BeautyParlours</a></li>
                  <li><a class="dropdown-item" href="Gyms_dilsukhnagar.html">Gyms</a></li>
                  <li><a class="dropdown-item" href="schools_dilsukhnagar.html">Schools</a></li>
                  <li><a class="dropdown-item" href="petshops_dilsukhnagar.html">PetShops</a></li>
                  <li><a class="dropdown-item" href="Carpenters_dilsukhnagar.html">Carpenter</a></li>
                  <li><a class="dropdown-item" href="Electrician_dilsukhnagar.html">Electrician</a></li>
                </ul>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Contact Us</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
                    
    <section>
    <div class="container my-5 justify-content-center">
        <h1>AC MECHANICS IN DILSHUKHNAGAR</h1>
        <div class="row">
            <div class="col-md-4">
                <div class="dummy-content my-5">
                    <P>Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto recusandae, at cupiditate accusantium illum vel est id soluta facere voluptatem ratione alias molestiae tempora possimus blanditiis, eveniet, minus deserunt consequuntur ex vero praesentium ipsam totam hic dignissimos. Aperiam hic cum reiciendis fuga. Et laudantium incidunt magni officia libero, quaerat rem asperiores. A fugiat molestiae nisi ipsam maiores quaerat veritatis, repellat dolorum non! Sed in tenetur quisquam quas autem ratione voluptatum unde, enim nesciunt maiores a. Maxime obcaecati aliquid eaque nobis ullam aliquam? Inventore culpa delectus nulla reprehenderit molestias enim sapiente magni? Aut consequatur repellat, dicta tempore mollitia et pariatur obcaecati.</P>
                </div>
            </div>
            <div class="col-md-8">
                <div id="data-container" class="row justify-content-end">
                    <div class="col-12 mb-4 float-right">
                        {% for item in data %}
                        <div class="card">
                            <h5>{{ item['Companyname'] }}</h5>
                            <p>Phone: {{ item['Phone'] }}</p>
                            <p>Address: {{ item['Address'] }}</p>
                        </div>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
    </div>
    </section>
                    

    <footer class="py-3 mt-4 footer">
      <ul class="nav justify-content-center border-bottom pb-3 mb-3">
        <li class="nav-item"><a href="homepage.html" class="nav-link px-2 text-light ">Home</a></li>
        <li class="nav-item"><a href="#ABOUT" class="nav-link px-2 text-light">about</a></li>
        <li class="nav-item"><a href="contact.html" class="nav-link px-2 text-light">contact</a></li>
      </ul>
      <p class="text-center text-light">&copy; 2024 spark technologies</p>
    </footer>
                    
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init();
    </script>
</body>
</html>
""")

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
