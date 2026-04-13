from flask import Flask, render_template, request, jsonify
# ಇಲ್ಲಿ zefame ಲೈಬ್ರರಿ ಇರಬೇಕು
try:
    from zefame import Zefame
except ImportError:
    Zefame = None

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Running! Create index.html in templates folder to see UI."

@app.route('/boost', methods=['POST'])
def boost_reel():
    if not Zefame:
        return jsonify({"error": "Zefame module not installed!"})
        
    video_url = request.form.get('url')
    boost_type = request.form.get('type')
    
    try:
        service_id = 237 if boost_type == 'views' else 234
        zefame = Zefame(video_url, service_id)
        status = zefame.send_boost()
        return jsonify({"status": "Success" if status else "Failed"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
