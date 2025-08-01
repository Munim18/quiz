from flask import Flask, render_template, request
app = Flask(__name__)

from openai import OpenAI  
OPENAI_API_KEY =  'API  KEYHERE'
def get_chat(prompt):
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    reply = response.choices[0].message.content.strip()
    print("Prompt:", prompt)
    print("Response:", reply)
    return reply

@app.route('/bitswits.ai/', methods=['GET', 'POST'])
def bitswits_ai():
    if request.method == 'POST':
        user_prompt = request.form['prompt']
        print('User Prompt is : ', user_prompt)

        chat_response = get_chat(user_prompt)
        return render_template('bitswits_output.html', response=chat_response , user_prompt= user_prompt)
    else:
        return render_template('bitswitsai.html')

if __name__ == "__main__":
    app.run()


