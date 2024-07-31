from flask import Flask, render_template
from routes import init_routes

app = Flask(__name__)
app.config.from_object('config.Config')

init_routes(app)

@app.route('/')
def home():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)