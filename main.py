from flask import Flask, render_template, request, jsonify, current_app
import os
import json

app = Flask(__name__)




def resource_meets_criteria(resource, distance, tags):
    # Convert distance to float for comparison and handle None or empty string
    selected_distance = float(distance) if distance else float('inf')
    
    # Ensure the resource's distance is within the selected range
    resource_distance = float(resource.get('distance', 0))
    if resource_distance > selected_distance:
        return False

    # Ensure the resource has all the selected tags
    resource_tags = set(resource.get('tags', []))
    for tag in tags:
        if tag not in resource_tags:
            return False

    return True


tag_colors = {
    "Recycling Center": "#f8c0c0",  # Was #e57373
    "Local Trading": "#f8bad4",     # Was #f06292
    "Store or Business": "#dcb6e0", # Was #ba68c8
    "Service": "#c7b3e5",           # Was #9575cd
    "Older Technology": "#bfc9f2",  # Was #7986cb
    "Newer Technology": "#a6d7f7",  # Was #64b5f6
    "Consumer Hardware": "#9edff9", # Was #4fc3f7
    "General Hardware": "#9ee9eb",  # Was #4dd0e1
    "Government": "#9edeca",        # Was #4db6ac
    "Individual": "#b3e6c1",        # Was #81c784
    "Paid": "#d2e9b1",              # Was #aed581
    "Free": "#e9f5b2",              # Was #dce775
}



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/resources')
def resources():
    distance = request.args.get('distance', None)
    tags = request.args.getlist('tags') if 'tags' in request.args else []
    if isinstance(tags, str):  # In case tags come as a comma-separated string
        tags = tags.split(',')

    # Construct the path to resources.JSON relative to the Flask app root
    resources_path = os.path.join(current_app.root_path, 'static', 'resources.JSON')

    with open(resources_path) as f:
        resources_data = json.load(f)

    # Filter resources based on criteria
    filtered_resources = [resource for resource in resources_data if resource_meets_criteria(resource, distance, tags)]

    # Pass the tag_colors dictionary to the template
    return render_template('resources.html', resources=filtered_resources, tag_colors=tag_colors)

@app.route('/lesson1')
def lesson1():
    return render_template('lesson1.html')

@app.route('/lesson2')
def lesson2():
    return render_template('lesson2.html')

@app.route('/lesson3')
def lesson3():
    return render_template('lesson3.html')

if __name__ == '__main__':
    app.run(debug=True)
