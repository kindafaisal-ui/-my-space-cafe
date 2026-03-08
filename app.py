import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, static_folder='demo')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('demo', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('demo', filename)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    content_type = data.get('type', 'instagram')
    topic = data.get('topic', 'My Space Cafe')
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return jsonify({'error': 'OPENAI_API_KEY not configured'}), 500
    prompts = {
        'instagram': f"You are the brand voice for My Space Cafe. Write an Instagram caption for: {topic}. Short, emotional, max 3 hashtags.",
        'tiktok': f"You are the brand voice for My Space Cafe. Write a TikTok script for: {topic}. Include HOOK, VIDEO DIRECTION, VOICEOVER, CLOSING LINE.",
        'story': f"You are the brand voice for My Space Cafe. Write a brand story paragraph for: {topic}. Poetic but grounded. 3-4 sentences."
    }
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            max_tokens=400,
            messages=[{'role': 'user', 'content': prompts.get(content_type, prompts['instagram'])}]
        )
        return jsonify({'result': response.choices[0].message.content, 'type': content_type})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'ok'})


@app.route("/api/voice", methods=["POST"])
def generate_voice():
    try:
        from openai import OpenAI; import io
        client=OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        data=request.get_json()
        text=data.get("text","Welcome to My Space.")
        resp=client.audio.speech.create(model="tts-1",voice="nova",input=text)
        buf=io.BytesIO()
        [buf.write(chunk) for chunk in resp.iter_bytes()]
        buf.seek(0)
        from flask import send_file; return send_file(buf,mimetype="audio/mpeg",as_attachment=False)
    except Exception as e: return jsonify({"error":str(e)}),500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
