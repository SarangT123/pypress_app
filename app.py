from pypress import app
from flask_pwa import PWA
if __name__ == '__main__':
    PWA(app)
    app.run(debug=True)
