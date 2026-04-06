from flask import Flask

# Flask app initialize ki
app = Flask(__name__)


# Rule: Function se pehle 2 khali lines honi chahiye (E302 fix)
@app.route('/')
def home():
    return "Hello! Ye mera simple portfolio server hai."


# Rule: Function ke baad 2 khali lines honi chahiye (E305 fix)
if __name__ == '__main__':
    # host='0.0.0.0' taaki ye network par access ho sake
    app.run(debug=True, host='0.0.0.0', port=5000)
