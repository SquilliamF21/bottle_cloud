from flask import Flask

app = Flask(__name__)

# Initialize an empty variable to store file content
file_content = ""

def load_file_content():
    global file_content
    try:
        with open('file.txt', 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        file_content = "File not found."

# Call this function during app startup
load_file_content()

@app.route('/')
def index():
    return f"File.txt: {file_content}"

if __name__ == '__main__':
    app.run(debug=True)