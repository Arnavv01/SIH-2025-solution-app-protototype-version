from app import app, db
from models import CropWeatherAdvice

with app.app_context():
    advice_list = [
        # Wheat
        {"crop": "Wheat", "weather": "Rain (excess)", "weather_hi": "अत्यधिक वर्षा",
         "advice_en": "Ensure quick drainage; delay irrigation; apply split nitrogen after drying; monitor fungal diseases.",
         "advice_hi": "तेज़ जल निकासी करें; सिंचाई टालें; मिट्टी सूखने पर नाइट्रोजन डालें; फफूंदी रोग पर नज़र रखें।"},
        {"crop": "Wheat", "weather": "Dry (deficit)", "weather_hi": "सूखा",
         "advice_en": "Conserve moisture (mulch/zero-till); irrigate at critical stages; use drought-tolerant varieties.",
         "advice_hi": "नमी बचाएँ (मल्च/जीरो-टिल); आवश्यक अवस्थाओं पर सिंचाई करें; सूखा-सहिष्णु किस्में अपनाएँ।"},
        {"crop": "Wheat", "weather": "Hot (heat-wave)", "weather_hi": "गर्मी की लहर",
         "advice_en": "Advance sowing; irrigate during grain-filling; adopt heat-tolerant varieties.",
         "advice_hi": "समय पर बुवाई करें; दाने भरते समय सिंचाई करें; गर्मी-सहिष्णु किस्में लें।"},
        {"crop": "Wheat", "weather": "Cold (frost)", "weather_hi": "पाला",
         "advice_en": "Pre-dawn irrigation on frost nights; avoid hoeing; protect seedlings with straw/sprinklers.",
         "advice_hi": "पाले की रातों में भोर से पहले हल्की सिंचाई करें; गुड़ाई न करें; पौधों को पुआल/स्प्रिंकलर से ढकें।"},

        # Rice
        {"crop": "Rice", "weather": "Rain (excess)", "weather_hi": "अत्यधिक वर्षा",
         "advice_en": "Strengthen bunds/drains; reduce water depth; replant gaps; apply potash/zinc; monitor pests.",
         "advice_hi": "मेड़ व नालियाँ मजबूत करें; पानी की गहराई कम रखें; खाली जगहों में पुनः रोपाई करें; पोटाश/जिंक डालें; कीटों पर नज़र रखें।"},
        {"crop": "Rice", "weather": "Dry (deficit)", "weather_hi": "सूखा",
         "advice_en": "Careful AWD; irrigate at PI/flowering; use short-duration/drought-tolerant varieties.",
         "advice_hi": "AWD सावधानी से करें; पुष्पन पर सिंचाई करें; कम अवधि व सूखा-सहिष्णु किस्में अपनाएँ।"},
        {"crop": "Rice", "weather": "Hot (heat-wave)", "weather_hi": "गर्मी की लहर",
         "advice_en": "Maintain 5–7 cm water at flowering; apply potassium foliar spray; shade nursery.",
         "advice_hi": "फूल आने पर 5–7 सेमी पानी रखें; पोटाश का छिड़काव करें; नर्सरी पर छाया दें।"},
        {"crop": "Rice", "weather": "Cold (cold spell)", "weather_hi": "ठंड की लहर",
         "advice_en": "Keep deeper water layer; delay transplanting in severe cold; avoid herbicides on stressed crop.",
         "advice_hi": "अत्यधिक ठंड में गहरी पानी की परत रखें; रोपाई देर से करें; ठंड से प्रभावित फसल पर खरपतवारनाशी का उपयोग न करें।"},

        # Maize
        {"crop": "Maize", "weather": "Rain (excess)", "weather_hi": "अत्यधिक वर्षा",
         "advice_en": "Plant on raised beds; drain quickly; re-sow patches; monitor foliar diseases.",
         "advice_hi": "ऊँची क्यारियों पर बोआई करें; पानी तुरंत निकालें; धुली हुई जगहों में पुनः बुवाई करें; रोगों पर नज़र रखें।"},
        {"crop": "Maize", "weather": "Dry (deficit)", "weather_hi": "सूखा",
         "advice_en": "Mulch; irrigate at tasseling/silking and grain fill; use drought-tolerant hybrids.",
         "advice_hi": "मल्च करें; रेशमी अवस्था व दाना भरने पर सिंचाई करें; सूखा-सहिष्णु संकर लें।"},
        {"crop": "Maize", "weather": "Hot (heat-wave)", "weather_hi": "गर्मी की लहर",
         "advice_en": "Irrigate frequently at tasseling/silking; mulch; apply foliar micronutrients if advised.",
         "advice_hi": "रेशमी अवस्था पर बार-बार सिंचाई करें; मल्च करें; आवश्यकता अनुसार सूक्ष्म पोषक तत्वों का छिड़काव करें।"},
        {"crop": "Maize", "weather": "Cold (cold spell)", "weather_hi": "ठंड की लहर",
         "advice_en": "Sow after soils warm; mulch seedlings; avoid over-irrigation in cloudy/cool weather.",
         "advice_hi": "मिट्टी गर्म होने पर बोआई करें; पौधों को मल्च से ढकें; ठंडे मौसम में अधिक सिंचाई न करें।"},

        # Cotton
        {"crop": "Cotton", "weather": "Rain (excess)", "weather_hi": "अत्यधिक वर्षा",
         "advice_en": "Drain excess water; stake plants; apply potassium/magnesium foliar feed; monitor pests/diseases.",
         "advice_hi": "अतिरिक्त पानी निकालें; पौधों को सहारा दें; पोटाश/मैग्नीशियम का छिड़काव करें; कीट/रोग पर नज़र रखें।"},
        {"crop": "Cotton", "weather": "Dry (deficit)", "weather_hi": "सूखा",
         "advice_en": "Use drip/skip-furrow irrigation; mulch; irrigate at square/boll development; avoid excess N.",
         "advice_hi": "ड्रिप या स्किप-फरो सिंचाई करें; मल्च करें; वर्ग निर्माण व बोली अवस्था पर सिंचाई करें; अधिक नाइट्रोजन न डालें।"},
        {"crop": "Cotton", "weather": "Hot (heat-wave)", "weather_hi": "गर्मी की लहर",
         "advice_en": "Light, frequent irrigations; maintain mulch; use growth regulators only as recommended.",
         "advice_hi": "हल्की, बार-बार सिंचाई करें; मल्च रखें; ग्रोथ रेगुलेर केवल सलाह पर प्रयोग करें।"},
        {"crop": "Cotton", "weather": "Cold (cold spell)", "weather_hi": "ठंड की लहर",
         "advice_en": "Delay sowing until soils warm; protect seedlings; avoid irrigation during cold spells.",
         "advice_hi": "मिट्टी गर्म होने पर बोआई करें; पौधों की रक्षा करें; ठंड में सिंचाई न करें।"},

        # Sugarcane
        {"crop": "Sugarcane", "weather": "Rain (excess)", "weather_hi": "अत्यधिक वर्षा",
         "advice_en": "Drain fields; re-erect lodged canes; apply split N & potash after drainage; monitor red rot.",
         "advice_hi": "खेत से पानी निकालें; गिरे हुए गन्ने को सीधा करें; पानी निकलने पर नाइट्रोजन व पोटाश दें; लाल सड़न पर नज़र रखें।"},
        {"crop": "Sugarcane", "weather": "Dry (deficit)", "weather_hi": "सूखा",
         "advice_en": "Trash mulching; drip/frequent irrigation; control weeds; avoid heavy tillage.",
         "advice_hi": "मल्चिंग करें; ड्रिप/बार-बार सिंचाई करें; खरपतवार नियंत्रित करें; भारी जुताई न करें।"},
        {"crop": "Sugarcane", "weather": "Hot (heat-wave)", "weather_hi": "गर्मी की लहर",
         "advice_en": "Maintain steady soil moisture with frequent irrigations; mulch; avoid waterlogging after irrigation.",
         "advice_hi": "नियमित अंतराल पर सिंचाई करें; मल्च रखें; सिंचाई के बाद जलभराव से बचें।"},
        {"crop": "Sugarcane", "weather": "Cold (frost)", "weather_hi": "पाला",
         "advice_en": "Light irrigation before frost; retain trash mulch; avoid late heavy nitrogen; use tolerant ratoon varieties.",
         "advice_hi": "पाले से पहले हल्की सिंचाई करें; मल्च बनाए रखें; देर से नाइट्रोजन न दें; सहिष्णु किस्में लें।"},
    ]

    for entry in advice_list:
        db.session.add(CropWeatherAdvice(**entry))
    db.session.commit()
    print("CropWeatherAdvice table seeded successfully!")
