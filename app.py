from flask import Developer-2

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
<<<<<<< HEAD
print("app is running on 4000")
=======
>>>>>>> 19ffa64366bac1cf552862847e4c60777cd130ec
