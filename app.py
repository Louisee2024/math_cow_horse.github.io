from flask import Flask, jsonify
import os

app = Flask(__name__)
counter_file = 'count.txt'

# Initialize the counter file
if not os.path.exists(counter_file):
    with open(counter_file, 'w') as f:
        f.write('0')

@app.route('/visit', methods=['GET'])
def visit():
    # Read and update the counter
    with open(counter_file, 'r+') as f:
        count = int(f.read().strip())
        count += 1
        f.seek(0)
        f.write(str(count))
        f.truncate()
    return jsonify({'visits': count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

