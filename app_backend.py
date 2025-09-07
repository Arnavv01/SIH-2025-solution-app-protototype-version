from flask import Flask, jsonify, request
from extensions import db
from models import Crop, Feedback, Contact, User, CropWeatherAdvice
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Backend is running! 🚀"

@app.route('/api/crops', methods=['GET'])
def get_crops():
    crops = Crop.query.all()
    return jsonify([{"id": c.id, "name": c.name} for c in crops])

@app.route('/api/contact', methods=['POST'])
def add_contact():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    if not name or not email or not message:
        return jsonify({"error": "Name, email and message are required"}), 400
    contact = Contact(name=name, email=email, message=message)
    db.session.add(contact)
    db.session.commit()
    return jsonify({"message": "Contact form submitted successfully!"}), 201

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return {"error": "Name and email are required"}, 400
    if User.query.filter_by(email=email).first():
        return {"error": "User with this email already exists"}, 400
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return {"message": "User created successfully!", "user_id": user.id}, 201

@app.route('/api/feedback', methods=['POST'])
def add_feedback():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    if not name or not email or not message:
        return {"error": "All fields are required"}, 400
    feedback = Feedback(name=name, email=email, message=message)
    db.session.add(feedback)
    db.session.commit()
    return {"message": "Feedback submitted successfully!"}, 201

@app.route('/api/advice', methods=['GET'])
def get_advice():
    crop = request.args.get("crop")
    weather = request.args.get("weather")
    
    if not crop or not weather:
        return {"error": "Crop and weather are required"}, 400
    
    crop_norm = crop.strip().lower()
    weather_norm = weather.strip().lower()
    
    advice = CropWeatherAdvice.query.filter(
        db.func.lower(db.func.trim(CropWeatherAdvice.crop)) == crop_norm,
        db.func.lower(db.func.trim(CropWeatherAdvice.weather)) == weather_norm
    ).first()
    
    if not advice:
        return {"error": "No advice found"}, 404
    
    return {
        "crop": advice.crop,
        "weather": advice.weather,
        "weather_hi": advice.weather_hi,
        "advice_en": advice.advice_en,
        "advice_hi": advice.advice_hi
    }

if __name__ == "__main__":
    app.run(debug=True)
