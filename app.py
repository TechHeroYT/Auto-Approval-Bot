from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TechVJ'


if __name__ == "__main__":
    app.run()

# Don't Remove Credit @hero_botss
# Subscribe YouTube Channel For Amazing Bot @bots_repo
# Ask Doubt on telegram @hero_botss
