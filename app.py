from flask import Flask, render_template, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

FRUIT_TREES = {
    'Loquat': {'ripeness_months': [4, 5, 6], 'fruit_type': 'loquat'},
    'Fig': {'ripeness_months': [6, 7, 8, 9], 'fruit_type': 'fig'},
    'Apple': {'ripeness_months': [8, 9, 10], 'fruit_type': 'apple'},
    'Plum': {'ripeness_months': [6, 7, 8], 'fruit_type': 'plum'},
    'Cherry': {'ripeness_months': [5, 6, 7], 'fruit_type': 'cherry'},
    'Pear': {'ripeness_months': [8, 9, 10], 'fruit_type': 'pear'},
    'Persimmon': {'ripeness_months': [10, 11, 12], 'fruit_type': 'persimmon'},
    'Apricot': {'ripeness_months': [6, 7], 'fruit_type': 'apricot'},
    'Peach': {'ripeness_months': [6, 7, 8], 'fruit_type': 'peach'},
    'Olive': {'ripeness_months': [10, 11, 12], 'fruit_type': 'olive'},
    'Citrus': {'ripeness_months': [11, 12, 1, 2, 3], 'fruit_type': 'citrus'},
    'Orange': {'ripeness_months': [11, 12, 1, 2, 3], 'fruit_type': 'citrus'},
    'Lemon': {'ripeness_months': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 'fruit_type': 'citrus'},
    'Grapefruit': {'ripeness_months': [12, 1, 2, 3, 4], 'fruit_type': 'citrus'},
    'Mulberry': {'ripeness_months': [5, 6, 7], 'fruit_type': 'mulberry'},
    'Walnut': {'ripeness_months': [9, 10], 'fruit_type': 'walnut'},
}

def is_fruit_tree(species_name):
    if not species_name:
        return None
    species_upper = species_name.upper()
    for fruit_type in FRUIT_TREES.keys():
        if fruit_type.upper() in species_upper:
            return fruit_type
    return None

def is_ripe(fruit_type, current_month):
    if fruit_type in FRUIT_TREES:
        return current_month in FRUIT_TREES[fruit_type]['ripeness_months']
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/fruit-trees')
def get_fruit_trees():
    current_month = datetime.now().month
    
    url = "https://data.sfgov.org/resource/tkzw-k3nq.json"
    params = {
        '$limit': 5000,
        '$where': 'latitude IS NOT NULL AND longitude IS NOT NULL'
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        trees = response.json()
        
        fruit_trees = []
        for tree in trees:
            species = tree.get('qspecies', '')
            fruit_type = is_fruit_tree(species)
            
            if fruit_type:
                lat = tree.get('latitude')
                lon = tree.get('longitude')
                
                if lat and lon:
                    ripe = is_ripe(fruit_type, current_month)
                    fruit_trees.append({
                        'id': tree.get('treeid'),
                        'species': species,
                        'fruit_type': fruit_type,
                        'address': tree.get('qaddress', 'Unknown'),
                        'latitude': float(lat),
                        'longitude': float(lon),
                        'is_ripe': ripe,
                        'plant_date': tree.get('plantdate'),
                        'caretaker': tree.get('qcaretaker', 'Unknown')
                    })
        
        return jsonify({
            'trees': fruit_trees,
            'total': len(fruit_trees),
            'current_month': current_month
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
