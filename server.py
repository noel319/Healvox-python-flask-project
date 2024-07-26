from app import create_app

app = create_app(debug=True)

if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1', port=8000)