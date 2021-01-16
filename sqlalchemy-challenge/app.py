import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///./Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)


@app.route("/")
def welcome():
    """Listing all available api routes."""
    return (
        f"Welcome to the Hawaii Weather Stations API page!<br/><br/>"
        f"Available Routes:<br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
            )


@app.route("/api/v1.0/precipitation")
def precipitation():
    
    session = Session(engine)

        # Query precipitation by date
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Convert results to dictionary
    output = []
    for date, prcp in results:
        results2 ={}
        results2['date'] = date
        results2['precipitation'] = prcp
        output.append(results2)
    
    return jsonify(output)


@app.route("/api/v1.0/stations")
def stations():

    session = Session(engine)

    # Query stations
    results = session.query(Station.station).all()

    session.close()

    # Convert results to list
    output = list(np.ravel(results))
    
    return jsonify(output)


@app.route("/api/v1.0/tobs")
def temperature():

    session = Session(engine)

    # Query temperature by date for the past year from 08/23/2017 for most active station.
   
    results = session.query(Measurement.date, Measurement.tobs)\
                .filter(Measurement.date >= (dt.date(2017, 8, 23) - dt.timedelta(days=365)))\
                .filter(Measurement.station == 'USC00519281').order_by(Measurement.date).all()

    session.close()

    # Convert results to dictionary
    temps = []
    for date, tobs in results:
        results2 = {}
        results2['date'] = date
        results2['temperature'] = tobs
        temps.append(results2)
    
    return jsonify(temps)


@app.route("/api/v1.0/<start>")
def start_date(start):
    
    session = Session(engine)
    
   
    results = session.query(Measurement.date, func.min(Measurement.tobs),func.max(Measurement.tobs), func.avg(Measurement.tobs))\
        .filter(Measurement.date >= start).all()

    session.close()

    # Convert results to dictionary
    summaries = []
    for date, tmin,tmax,tavg in results:
        results2 = {}
        results2['date'] = date
        results2['TMIN'] = tmin
        results2['TAVG'] = tavg
        results2['TMAX'] = tmax
        summaries.append(results2)

    return jsonify(summaries)


    



if __name__ == '__main__':
    app.run(debug=True)
