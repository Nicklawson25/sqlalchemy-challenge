##### README
---

# Climate Analysis and Flask API

## Project Overview

This project involves analyzing climate data for Honolulu, Hawaii, to provide insights for planning a vacation. Using Python, SQLAlchemy, Pandas, and Matplotlib, a basic climate analysis is conducted to understand precipitation trends and station activity. Additionally, a Flask API is developed to provide access to various climate-related data through defined routes.

## Project Components

### Part 1: Climate Data Analysis

1. **Precipitation Analysis**: Analyzes the precipitation data for the last 12 months to identify patterns and trends.
2. **Station Analysis**: Identifies the most active weather stations and analyzes temperature observations for the most active station.

### Part 2: Flask API Development

1. **Home Route (`/`)**: Lists all available routes of the API.
2. **Precipitation Route (`/api/v1.0/precipitation`)**: Returns the precipitation data for the last 12 months in JSON format.
3. **Stations Route (`/api/v1.0/stations`)**: Returns a list of weather stations.
4. **Temperature Observations Route (`/api/v1.0/tobs`)**: Provides temperature observations for the most active station for the previous year.
5. **Temperature Statistics Routes (`/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`)**: Returns the minimum, average, and maximum temperatures for a given date range.

## File Structure

```
.
├── app.py                  # Flask API script
├── climate_analysis.ipynb  # Jupyter Notebook containing the climate analysis code
├── hawaii_measurements.csv # CSV file with measurement data
├── hawaii_stations.csv     # CSV file with station data
├── hawaii.sqlite           # SQLite database with climate data
└── README.md               # Project overview and instructions
```

## Setup Instructions

### Prerequisites

Ensure you have the following Python libraries installed:
- Flask
- SQLAlchemy
- Pandas
- Matplotlib

You can install them using pip:

```bash
pip install flask sqlalchemy pandas matplotlib
```

### Running the Climate Analysis

1. Open the `climate_analysis.ipynb` file in Jupyter Notebook.
2. Run the cells sequentially to perform the data analysis and visualization.
3. Ensure that the `hawaii_measurements.csv`, `hawaii_stations.csv`, and `hawaii.sqlite` files are in the same directory or update the file paths accordingly.

### Running the Flask API

1. Ensure that the database file `hawaii.sqlite` is accessible in the specified path in `app.py`.
2. Run the Flask application from the command line:

   ```bash
   python app.py
   ```

3. Access the API in your web browser at `http://127.0.0.1:5000/`.

## API Endpoints

- **`/`**: Displays all available API routes.
- **`/api/v1.0/precipitation`**: Returns a JSON dictionary of precipitation data for the last 12 months.
- **`/api/v1.0/stations`**: Returns a JSON list of all weather stations.
- **`/api/v1.0/tobs`**: Returns a JSON list of temperature observations for the most active station for the last year.
- **`/api/v1.0/<start>`**: Returns a JSON list of the minimum, average, and maximum temperatures from the given start date to the latest date in the dataset.
- **`/api/v1.0/<start>/<end>`**: Returns a JSON list of the minimum, average, and maximum temperatures for the specified date range.

## Project Summary

This project provides valuable insights into the climate of Honolulu, Hawaii, using historical weather data. By developing a Flask API, users can access these insights dynamically, making it a useful tool for planning weather-dependent activities.

## License

This project is for educational purposes.

---

