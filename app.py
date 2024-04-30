from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_content():
    user_input = request.json.get('topic')
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=f"Write a blog post about {user_input}",
      max_tokens=150
    )
    return jsonify({"content": response['choices'][0]['text']})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
