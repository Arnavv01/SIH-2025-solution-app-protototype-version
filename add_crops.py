from app import app, db
from models import Crop

with app.app_context():
    extra_crops = ["Rice", "Maize", "Sugarcane", "Cotton"]
    
    for name in extra_crops:
        if not Crop.query.filter_by(name=name).first():  # check if crop already exists
            db.session.add(Crop(name=name))
    
    db.session.commit()
    print("Extra crops added!")
