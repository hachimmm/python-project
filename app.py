from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr  # Import absolu

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    try:
        data = request.get_json()
        height = float(data['height'])  # en mètres
        weight = float(data['weight'])  # en kg
        bmi = calculate_bmi(height, weight)
        return jsonify({'bmi': round(bmi, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    try:
        data = request.get_json()
        height = float(data['height'])  # en cm
        weight = float(data['weight'])  # en kg
        age = int(data['age'])         # en années
        gender = data['gender']        # 'male' ou 'female'
        bmr = calculate_bmr(height, weight, age, gender)
        return jsonify({'bmr': bmr})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "version": "1.0.0"}), 200