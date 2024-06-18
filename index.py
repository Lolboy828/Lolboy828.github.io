from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_command():
    if request.method == 'POST':
        data = request.json
        if 'command' in data:
            if data['command'] == 'ban':
                # Perform ban action
                return jsonify({'message': 'Player banned successfully!'}), 200
            else:
                return jsonify({'error': 'Invalid command.'}), 400
        else:
            return jsonify({'error': 'Command not provided.'}), 400
    else:
        return jsonify({'error': 'Method not allowed.'}), 405

if __name__ == '__main__':
    app.run(debug=True)
