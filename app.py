from flask import Flask, request, render_template
import os, csv, time

app = Flask(__name__)

csv_data = {}
csvfile = 'upcsvfile.csv'
print("Loading CSV data...")
with open(csvfile, 'r') as file:
    csvreader = csv.reader(file, delimiter=",")
    for row in csvreader:
        csv_data[row[0]] = row[1] # Define the upload folder
@app.route('/', methods=['POST'])
def upload_file():
    #global csvreader
    start = time.time()
    if 'inputFile' not in request.files:
        return 'No file part'
    file = request.files['inputFile']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = file.filename
        fname=os.path.splitext(os.path.basename(filename))

        rows = []

    result = csv_data.get(fname[0], None)
    result = fname[0] + ":" + result if result else "Record Not Found"
    return result
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
