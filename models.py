from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"


class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

class CropWeatherAdvice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop = db.Column(db.String(80), nullable=False)
    weather = db.Column(db.String(120), nullable=False)
    weather_hi = db.Column(db.String(120))
    advice_en = db.Column(db.Text)
    advice_hi = db.Column(db.Text)

    def __repr__(self):
        return f"<CropWeatherAdvice {self.crop} - {self.weather}>"

