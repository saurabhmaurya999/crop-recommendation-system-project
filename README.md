
# 🌾 Crop Recommendation System

A Machine Learning–based **Crop Recommendation System** that suggests the most suitable crop to grow based on soil and environmental parameters. The project includes model training and a Flask web application for user interaction.

---

## 🚀 Features

* Predicts the best crop using ML
* Flask-based web interface
* Uses real agricultural dataset
* Simple and beginner-friendly project structure

---

## 📂 Project Structure

```
crop-recommendation-system-project/
│
├── app.py                         # Flask application
├── crop_recommendation_model.pkl  # Trained ML model
├── Crop_Recommendation.ipynb      # Model training notebook
├── Crop_recommendation.csv        # Dataset
├── templates/                     # HTML files
│   └── index.html
├── static/                        # CSS, images, JS
└── README.md
```

---

## 🧠 Machine Learning

* Algorithm: (e.g., Random Forest / Decision Tree)
* Input Features:

  * Nitrogen (N)
  * Phosphorus (P)
  * Potassium (K)
  * Temperature
  * Humidity
  * pH
  * Rainfall
* Output: **Recommended Crop**

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Flask
* HTML, CSS

---

## ▶️ How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/saurabhmaurya999/crop-recommendation-system-project.git
```

2. Install required libraries

```bash
pip install flask numpy pandas scikit-learn
```

3. Run the Flask app

```bash
python app.py
```

4. Open browser and go to

```
http://127.0.0.1:5000/
```

---

## 📸 Output

The system displays the **recommended crop** based on user input values.

---

## 🎯 Use Case

Helpful for:

* Farmers
* Agriculture students
* Smart farming applications

---

## 👤 Author

**Saurabh Maurya**
B.Sc. (Hons) Computer Science & Data Analytics
IIT Patna

---

## ⭐ Future Improvements

* Add fertilizer recommendation
* Deploy on cloud (Render / Railway)
* Improve UI with Bootstrap

---

⭐ If you like this project, don’t forget to star the repository!
