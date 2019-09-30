import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/merg_dt.sqlite"

db = SQLAlchemy(app)


# Create our database model
class Crime(db.Model):
    __tablename__ = 'crime'

    id = db.Column(db.Integer, primary_key=True)
    Areaname = db.Column(db.String)
    sixteen_plus_unemployed = db.Column(db.Float)
    income_per_capital = db.Column(db.Integer)
    crime_no = db.Column(db.Integer)

    def __repr__(self):
        return '<Crime %r>' % (self.name)


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")


@app.route("/income")
def income_data():
    """Return ward name, income, unemployment and crime incidence number"""

    # Query for the data
    results = db.session.query(Crime.Areaname, Crime.income_per_capital, Crime.sixteen_plus_unemployed, Crime.crime_no).order_by(Crime.income_per_capital.desc()).all()


    # Create lists from the query result
    ward_name = [result[0] for result in results]
    income = [int(result[1]) for result in results]
    unemployment = [int(result[2]) for result in results]
    crime = [int(result[3]) for result in results]

    # Generate the plot trace
    trace = {
        "x": ward_name,
        "y": income,
        "type": "bar"
    }
    return jsonify(trace)

@app.route("/unemployment")
def unemployment_data():
    """Return ward name, income, unemployment and crime incidence number"""

    # Query for the data
    results = db.session.query(Crime.Areaname, Crime.income_per_capital, Crime.sixteen_plus_unemployed, Crime.crime_no).order_by(Crime.income_per_capital.desc()).all()


    # Create lists from the query result
    ward_name = [result[0] for result in results]
    income = [int(result[1]) for result in results]
    unemployment = [int(result[2]) for result in results]
    crime = [int(result[3]) for result in results]
    print(str(ward_name))

    # Generate the plot trace
    trace = {
        "x": ward_name,
        "y": unemployment,
        "type": "bar"
    }
    return jsonify(trace)

@app.route("/crime")
def crime_data():
    """Return ward name, income, unemployment and crime incidence number"""

    # Query for the data
    results = db.session.query(Crime.Areaname, Crime.income_per_capital, Crime.sixteen_plus_unemployed, Crime.crime_no).order_by(Crime.income_per_capital.desc()).all()


    # Create lists from the query result
    ward_name = [result[0] for result in results]
    income = [int(result[1]) for result in results]
    unemployment = [int(result[2]) for result in results]
    crime = [int(result[3]) for result in results]
    print(str(ward_name))

    # Generate the plot trace
    trace = {
        "x": ward_name,
        "y": crime,
        "type": "bar"
    }
    return jsonify(trace)

@app.route("/merged")
def merged_data():
    """Return ward name, income, unemployment and crime incidence number"""

    # Query for the data
    results = db.session.query(Crime.Areaname, Crime.income_per_capital, Crime.sixteen_plus_unemployed, Crime.crime_no).order_by(Crime.income_per_capital.desc()).all()


    # Create lists from the query result
    ward_name = [result[0] for result in results]
    income = [int(result[1]) for result in results]
    unemployment = [int(result[2]) for result in results]
    crime = [int(result[3]) / 10 for result in results]

    # Generate the plot trace
    trace = {
        "x": unemployment,
        "y": income,
        "mode": "markers",
        "marker": {"size": crime},
        "type": "scatter"
    }
    return jsonify(trace)

if __name__ == '__main__':
    app.run(debug=True)