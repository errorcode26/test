
from app import create_app
import os

if __name__ == '__main__':
    app = create_app()
    # Disable debug mode and reloader to avoid issues in background
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
