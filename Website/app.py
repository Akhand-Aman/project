from flask import Flask, render_template
import sqlite3
import pathlib 

base_path = pathlib.Path(r'C:\Users\AmanS\OneDrive\Documents\GitHub\project\Database')
db_name = "Noble_Prize_Laureates.db"
db_path = base_path / db_name
print(db_path)



app = Flask(__name__, template_folder=r'C:\Users\AmanS\OneDrive\Documents\GitHub\project\templates')

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    laureates = cursor.execute("SELECT * FROM Physics_Laureates_2015onwards").fetchall()
    con.close()

    return render_template("data_table.html", Physics_Laureates=laureates)





@app.route('/')
def map():
    # Load the CSV file
    df = pd.read_csv('Laureates_all.csv')
    
    # Create a Folium map centered around Europe
    m = folium.Map(location=[51.1657, 10.4515], zoom_start=3)

    # Add markers for each Nobel laureate
    for _, row in df.iterrows():
        folium.Marker([row['lat'], row['long']], 
                      popup=f"{row['Firstname']} - {row['Year']} {row['Category']}",
                      icon=folium.Icon(color='blue')).add_to(m)

    # Save map to a temporary file
    m.save('templates/map.html')

    # Render the HTML template
    return render_template('map.html')




if __name__=="__main__":
    app.run(debug=True)
