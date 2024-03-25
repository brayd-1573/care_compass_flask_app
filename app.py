from flask import Flask, request, jsonify
import tips_model

app = Flask(__name__)

@app.route('/predict_disease', methods=['POST'])
def predict_disease():
    data = request.json
    symptoms = data['symptoms']
    result = tips_model.run_model(symptoms)  # Call model function
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
