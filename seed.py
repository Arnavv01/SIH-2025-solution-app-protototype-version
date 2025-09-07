from app import app, db
from models import Crop

with app.app_context():
    if Crop.query.count() == 0:
        crops = ["Wheat", "Rice", "Maize", "Sugarcane", "Cotton"]
        for name in crops:
            crop = Crop(name=name)
            db.session.add(crop)
        db.session.commit()
        print("Mock crops added!")
    else:
        print("Crops already exist in DB.")