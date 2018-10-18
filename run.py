"""
module run
"""

from api.v1 import app

if __name__ == '__main__':
    app.run(debug=True)
