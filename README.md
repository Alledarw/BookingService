# BookingService

A simple booking service application made in flask.

Prerequisites
Before you begin, ensure you have met the following requirements:

    Python installed (version 3)
    Pip installed
    [Optional] Virtual environment (recommended for isolation)


Installation

    Clone the repository:


    git clone https://github.com/alledarw/bookingservice.git

    Navigate to the project directory:


    cd /your_directory

    Install dependencies:


    pip install -r requirements.txt

Configuration

    Create a .flaskenv file in the project root and configure your environment variables for flask:


    FLASK_APP=app.py
    FLASK_ENV=development  # or production in a production environment
    FLASK_DEBUG=1

    Create a .env file in the project root and configure your environment variables for the databse:


    DB_USER=postgres
    DB_HOST=localhost
    DB_PASSWORD=your_password
    DB_NAME=your_db_name
    DB_PORT=5432

Running the Application

    Activate the virtual environment (if used):


    source venv/bin/activate
 

    Setup tables and dummy data:


    execute tables.sql #to create tables
    execute values.sql #to insert dummy data

    Run the Flask application:


    flask run #to use a different port run: flask run --port=###

   This will start the development server, and you can access the application at http://localhost:5000 in    your web browser.

Running the Pytest

    Run tests in a module 
     
    pytest testfile.py

Contributing
If you'd like to contribute, please fork the repository and create a pull request. We welcome contributions!
