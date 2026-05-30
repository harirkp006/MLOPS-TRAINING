from flask import Flask, render_template, request
from ultralytics import YOLO
import os

app = Flask(__name__)

model = YOLO(r"C:\Users\dell\Desktop\EVE\runs\detect\train\weights\best.pt")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    print(request.files)   # Debug

    if "file" not in request.files:
        return "No video uploaded"

    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    upload_path = os.path.join("uploads", file.filename)
    file.save(upload_path)

    print("Uploaded:", file.filename)

    results = model.predict(
        source=upload_path,
        save=True,
        conf=0.25
    )

    return "Prediction Completed Successfully!"


if __name__ == "__main__":
    app.run(debug=True)