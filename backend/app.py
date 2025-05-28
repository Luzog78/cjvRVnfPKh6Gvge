from flask import Flask, render_template, jsonify
import os

app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    log_message = f"Current working directory: {os.getcwd()}"
    app.logger.info(log_message)
    return render_template('../frontend/index.html'), 200

@app.route('/health')
def health():
    return jsonify({"status": True}), 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page Not Found"}), 400

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
