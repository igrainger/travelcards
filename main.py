from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__, static_url_path='/static')

# Specify the path to your JSON file
json_file_path = 'cities.json'

# Read JSON data from the file
with open(json_file_path, 'r') as json_file:
    city_data = json.load(json_file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_city_data', methods=['POST'])
def get_city_data():
    city_name_1 = request.form['city_name_1']
    city_name_2 = request.form['city_name_2']

    # Search for data for City 1
    city_info_1 = next(
        (city for city in city_data if city['city'].lower() == city_name_1.lower()),
        None)

    # Search for data for City 2
    city_info_2 = next(
        (city for city in city_data if city['city'].lower() == city_name_2.lower()),
        None)

    if city_info_1 and city_info_2:
        return render_template('result.html', city_info_1=city_info_1, city_info_2=city_info_2)
    else:
        error_message = f"Data not found for one or both cities: {city_name_1}, {city_name_2}"
        return render_template('result.html', error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)
