### REVIEW TECH STACK - MIGRATE TO JAVA OR GO
next tasj

# Product Catalog Application

This is a simple web application that serves a product catalog using Flask. The application displays a list of products with their details, allowing users to view and interact with the catalog.

## Project Structure

```
product-catalog-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates
│   │   └── catalog.html
│   └── static
│       ├── styles.css
│       └── script.js
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd product-catalog-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To start the Flask development server, run the following command:

```
python run.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

Once the server is running, navigate to the homepage to view the product catalog. The catalog displays a list of products, each with a name, description, and price.

## Contributing

Feel free to submit issues or pull requests if you would like to contribute to the project.
