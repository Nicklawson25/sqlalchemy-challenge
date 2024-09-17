# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt


# Setup Flask
app = Flask(__name__)

# Setup database connection
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# References to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Helper function to create session
def get_session():
    return Session(engine)

# Home route
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = get_session()
    # Calculate the date 1 year ago from the last data point in the database
    latest_date = session.query(func.max(Measurement.date)).scalar()
    year_ago = dt.datetime.strptime(latest_date, '%Y-%m-%d') - dt.timedelta(days=365)

    # Query for the last 12 months of precipitation data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()
    session.close()

    # Convert results to a dictionary
    precip_data = {date: prcp for date, prcp in results}
    return jsonify(precip_data)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    session = get_session()
    # Query all stations
    results = session.query(Station.station).all()
    session.close()

    # Convert list of tuples into normal list
    stations_list = list(map(lambda x: x[0], results))
    return jsonify(stations_list)

# Temperature observations route for the most active station
@app.route("/api/v1.0/tobs")
def tobs():
    session = get_session()
    # Calculate the date 1 year ago from the last data point in the database
    latest_date = session.query(func.max(Measurement.date)).scalar()
    year_ago = dt.datetime.strptime(latest_date, '%Y-%m-%d') - dt.timedelta(days=365)

    # Find the most active station
    most_active_station = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()[0]

    # Query the dates and temperature observations of the most-active station for the previous year
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station).\
        filter(Measurement.date >= year_ago).all()
    session.close()

    # Convert the results into a list
    tobs_list = [{date: temp} for date, temp in results]
    return jsonify(tobs_list)

# Temperature stats for start date
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temp_stats(start, end=None):
    session = get_session()

    # Create base query with dynamic filtering based on start and end date
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results = session.query(*sel).filter(Measurement.date >= start).all()
    else:
        results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    session.close()

    # Convert results into a dictionary
    temp_data = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    return jsonify(temp_data)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
