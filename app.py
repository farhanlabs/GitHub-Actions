from flask import Flask

# Flask app initialize ki
app = Flask(__name__)

# Home route (Main page)
@app.route('/')
def home():
    return "Hello! Ye mera simple portfolio server hai."

# Server ko run karne ke liye code
if __name__ == '__main__':
    # host='0.0.0.0' taaki ye network par access ho sake
    app.run(debug=True, host='0.0.0.0', port=5000)
