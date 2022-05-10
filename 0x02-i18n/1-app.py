#!/usr/bin/env python3
"""A Basic Flask app.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config_class = Config
app.config['LANGUAGES'] = Config.LANGUAGES
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index():
    """The home/index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
