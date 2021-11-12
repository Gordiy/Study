from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"\


@app.route("/login", methods=['POST'])
def login():
    if request.POST.username and request.POST.password:
        pass


if __name__ == "__main__":
  app.run()