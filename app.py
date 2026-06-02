from flask import Flask,render_template,request,session,url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from get_data_from_redis import get_nutrition_data
import os
import json
import uuid
import numpy as np


app = Flask(__name__)

# SECRET KEY

app.secret_key = "food_classifier_secret_key"

# CONFIG

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

IMG_SIZE = 224

# LOAD FOOD CLASSES

with open("food_data.json", "r") as file:
    food_data = json.load(file)

class_names = food_data["classes"]

# LOAD MODELS

custom_model = load_model(
    "CustomCNN_classification_weights.weights.h5",
    compile=False
)

vgg_model = load_model(
    "vgg16_food_classification_weights.weights.h5",
    compile=False
)

resnet_model = load_model(
    "resnet50_food_classification_weights.weights.h5",
    compile=False
)

# LOAD METRICS

with open("Custom_CNN_metrics.json", "r") as f:
    custom_metrics = json.load(f)

with open("VGG_16_metrics.json", "r") as f:
    vgg_metrics = json.load(f)

with open("ResNet50_metrics.json", "r") as f:
    resnet_metrics = json.load(f)

# HOME

@app.route("/")
def home():

    return render_template(
        "index.html",
        image_path=session.get("uploaded_image"),
        selected_model="custom",
        classes=[
            x.replace("_", " ").title()
            for x in class_names
        ]
    )

# PREDICT

@app.route("/predict", methods=["POST"])
def predict():

    try:

        filepath = session.get("filepath")
        image_path = session.get("uploaded_image")

        # NEW IMAGE UPLOAD

        if "image" in request.files:

            file = request.files["image"]

            if file and file.filename != "":

                extension = os.path.splitext(
                    file.filename
                )[1]

                filename = (
                    str(uuid.uuid4()) + extension
                )

                filepath = os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    filename
                )

                file.save(filepath)

                image_path = url_for(
                    "static",
                    filename=f"uploads/{filename}"
                )

                session["filepath"] = filepath
                session["uploaded_image"] = image_path

        # IMAGE CHECK

        if not filepath:

            return render_template(
                "index.html",
                error="Please upload an image first.",
                classes=[
                    x.replace("_", " ").title()
                    for x in class_names
                ]
            )

        # IMAGE PREPROCESSING

        img = image.load_img(
            filepath,
            target_size=(IMG_SIZE, IMG_SIZE)
        )

        img_array = image.img_to_array(img)

        img_array = np.expand_dims(
            img_array,
            axis=0
        )

        img_array = img_array / 255.0

        # MODEL SELECTION

        selected_model = request.form.get(
            "model",
            "custom"
        )

        if selected_model == "custom":

            model = custom_model
            metrics = custom_metrics
            model_used = "Custom CNN"

        elif selected_model == "vgg":

            model = vgg_model
            metrics = vgg_metrics
            model_used = "VGG16"

        elif selected_model == "resnet":

            model = resnet_model
            metrics = resnet_metrics
            model_used = "ResNet50"

        else:

            model = custom_model
            metrics = custom_metrics
            model_used = "Custom CNN"

        # PREDICTION

        predictions = model.predict(img_array)

        predicted_index = np.argmax(
            predictions
        )

        prediction_raw = class_names[
            predicted_index
        ]

        prediction = prediction_raw.replace(
            "_",
            " "
        ).title()

        confidence = round(
            float(np.max(predictions)) * 100,
            2
        )

        # NUTRITION

        nutrition = get_nutrition_data(
            prediction_raw
        )

        if nutrition is None:

            nutrition = {
                "calories": "N/A",
                "protein": "N/A",
                "carbs": "N/A",
                "fats": "N/A",
                "fiber": "N/A"
            }

        # METRICS

        accuracy = round(
            float(
                metrics.get(
                    "accuracy",
                    0
                )
            ) * 100,
            2
        )

        report = metrics.get(
            "classification_report",
            {}
        )

        class_metric = report.get(
            prediction_raw,
            {}
        )

        precision = round(
            float(
                class_metric.get(
                    "precision",
                    0
                )
            ) * 100,
            2
        )

        recall = round(
            float(
                class_metric.get(
                    "recall",
                    0
                )
            ) * 100,
            2
        )

        f1_score = round(
            float(
                class_metric.get(
                    "f1-score",
                    0
                )
            ) * 100,
            2
        )

        return render_template(

            "index.html",

            prediction=prediction,
            confidence=confidence,

            image_path=image_path,

            nutrition=nutrition,

            model_used=model_used,

            accuracy=accuracy,
            precision=precision,
            recall=recall,
            f1_score=f1_score,

            selected_model=selected_model,

            classes=[
                x.replace("_", " ").title()
                for x in class_names
            ]
        )

    except Exception as e:

        return render_template(

            "index.html",

            error=str(e),

            image_path=session.get(
                "uploaded_image"
            ),

            classes=[
                x.replace("_", " ").title()
                for x in class_names
            ]
        )

# CLEAR IMAGE

@app.route("/clear-image")
def clear_image():

    session.pop(
        "uploaded_image",
        None
    )

    session.pop(
        "filepath",
        None
    )

    return render_template(
        "index.html",
        classes=[
            x.replace("_", " ").title()
            for x in class_names
        ]
    )

# MAIN

if __name__ == "__main__":
    app.run(debug=True)