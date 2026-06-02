<h1 align="center">🍔 AI Food Classification & Nutrition Analysis System</h1>

<p align="center">
  <b>Deep Learning Based Food Recognition & Nutrition Analysis Web Application</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-green">
  <img src="https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange">
  <img src="https://img.shields.io/badge/Redis-Database-red">
  <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
The <b>AI Food Classification & Nutrition Analysis System</b> is a Deep Learning powered web application that identifies food items from images and provides detailed nutritional information.
</p>

<p>
The system supports multiple CNN architectures:
</p>

<ul>
<li>🧠 Custom CNN</li>
<li>🧠 VGG16</li>
<li>🧠 ResNet50</li>
</ul>

<hr>

<h2>🚀 Features</h2>

<ul>
<li>📷 Upload Food Images</li>
<li>🤖 Multiple Model Selection</li>
<li>⚡ Real-Time Predictions</li>
<li>📊 Accuracy, Precision, Recall & F1 Score</li>
<li>🥗 Nutrition Information Retrieval</li>
<li>💾 Redis Database Integration</li>
<li>🎨 Modern Responsive UI</li>
<li>🔄 Session-Based Image Storage</li>
</ul>

<hr>

<h2>🛠 Technologies Used</h2>

<table>
<tr>
<th>Category</th>
<th>Technology</th>
</tr>

<tr>
<td>Frontend</td>
<td>HTML, CSS, JavaScript</td>
</tr>

<tr>
<td>Backend</td>
<td>Flask</td>
</tr>

<tr>
<td>Deep Learning</td>
<td>TensorFlow, Keras</td>
</tr>

<tr>
<td>Database</td>
<td>Redis</td>
</tr>

<tr>
<td>Programming Language</td>
<td>Python</td>
</tr>

</table>

<hr>

<h2>📂 Project Structure</h2>

<pre>
AI_Food_Classification/
│
├── app.py
├── food_data.json
│
├── CustomCNN_classification_weights.weights.h5
├── vgg16_food_classification_weights.weights.h5
├── resnet50_food_classification_weights.weights.h5
│
├── Custom_CNN_metrics.json
├── VGG_16_metrics.json
├── ResNet50_metrics.json
│
├── get_data_from_redis.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   ├── uploads/
│   └── images/
│
└── requirements.txt
</pre>

<hr>

<h2>⚙ Installation</h2>

<h3>1️⃣ Clone Repository</h3>

<pre>
git clone https://github.com/yourusername/AI-Food-Classification.git

cd AI-Food-Classification
</pre>

<h3>2️⃣ Create Virtual Environment</h3>

<pre>
python -m venv venv
</pre>

<h3>Activate Environment</h3>

<b>Windows</b>

<pre>
venv\Scripts\activate
</pre>

<b>Linux / Mac</b>

<pre>
source venv/bin/activate
</pre>

<h3>3️⃣ Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>🔥 Start Redis Server</h2>

<pre>
redis-server
</pre>

Verify:

<pre>
redis-cli ping
</pre>

Output:

<pre>
PONG
</pre>

<hr>

<h2>▶ Run Application</h2>

<pre>
python app.py
</pre>

Open:

<pre>
http://127.0.0.1:5000
</pre>

<hr>

<h2>🧠 Deep Learning Models</h2>

<table>
<tr>
<th>Model</th>
<th>Description</th>
</tr>

<tr>
<td>Custom CNN</td>
<td>Lightweight CNN built from scratch</td>
</tr>

<tr>
<td>VGG16</td>
<td>Transfer Learning Architecture</td>
</tr>

<tr>
<td>ResNet50</td>
<td>Residual Deep Neural Network</td>
</tr>

</table>

<hr>

<h2>📊 Performance Metrics</h2>

<ul>
<li>✅ Accuracy</li>
<li>✅ Precision</li>
<li>✅ Recall</li>
<li>✅ F1 Score</li>
</ul>

<hr>

<h2>🥗 Nutrition Analysis</h2>

<p>
The system retrieves nutrition information from Redis:
</p>

<ul>
<li>Calories</li>
<li>Protein</li>
<li>Carbohydrates</li>
<li>Fats</li>
<li>Fiber</li>
</ul>

<hr>

<h2>📸 Application Workflow</h2>

<ol>
<li>Upload Food Image</li>
<li>Select Deep Learning Model</li>
<li>Run Prediction</li>
<li>Identify Food Item</li>
<li>Fetch Nutrition Data</li>
<li>Display Results & Metrics</li>
</ol>

<hr>

<h2>🎯 Future Enhancements</h2>

<ul>
<li>📱 Mobile App Integration</li>
<li>🥗 Personalized Diet Recommendation</li>
<li>📹 Real-Time Camera Detection</li>
<li>☁ AWS Deployment</li>
<li>🤖 AI Meal Planner</li>
<li>📈 Health Analytics Dashboard</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p>
Kareti Haritha
  Developed using Flask, TensorFlow, CNN, VGG16, ResNet50, and Redis.
</p>

<hr>

<h2>📜 License</h2>

<p>
MIT License
</p>

<p align="center">
⭐ Star this repository if you found it useful!
</p>
