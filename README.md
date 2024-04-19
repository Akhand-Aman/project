## Python Project : A Flask Web Application which displays table data and basic information for Noble Laureates in HTML



### Description
This Flask web application demonstrates how to display a table and basic information on a webpage using HTML. The table is generated dynamically using data retrieved from an SQLite database in Python. The application uses Flask, a lightweight web framework for Python, to serve the HTML content. The website displays the dataset of Noble Laureates in Physics from 2015 onwards.

### Features
- Displays table dynamically generated from SQLite database
- Includes basic information on the webpage

### Prerequisites
Before running the application, make sure you have following installed:
- Python (version 3.x)
- Flask (install via `pip install flask`)
- SQLite3 (install via`pip install sqlite3)
- Pandas (install via `pip install pandas`)

### Usage
1. Clone or download this repository to your local machine
2. Clone the repository [https://github.com/Akhand-Aman/project].git
3. Install the required dependencies using the command: pip install -r requirements.txt
4. Navigate to the folder where you downloaded this repository.
5. Configure the database path In the app.py file, locate the database configuration section. By default, it may look like this: r'C:\Users\AmanS\OneDrive\Documents\GitHub\project\Database'
6. Change 'path/to/your/database.db' to the desired path where you want to store your database file. For example: DATABASE_PATH = 'data/Noble_Prize_Laureates.db'
8. Run the Flask application by executing the following command:
    ```
    python app.py
    ```
9. Open your web browser and go to `http://localhost:5000` to view the application.

### Files
- `app.py`: Main Flask application file containing routes and logic.
- `templates/about.html`: HTML template file detailing the source of the data and   definition of each variable.
- `templates/data_table.html`: HTML template file table webpage.
- `templates/index_links.html`: HTML template file for the main webpage containing links to other webpages.
- `Database/Physics_laureates.csv`: The csv file containing data about Noble Laureates in Physics since its inception.
- `Database/Physics_laureates_since 2015.csv`: The csv file containing data about Noble Laureates in Physics from 2015 onwards.
- `Noble_Prize_Laureates.db`: The database file containing the data.

### Refrences
http://www.nobelprize.org/nobel_organizations/nobelmedia/nobelprize_org/developer/
https://public.opendatasoft.com/explore/dataset/nobel-prize-laureates/table/?disjunctive.category
