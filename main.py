from flask import Flask
import json

app = Flask(__name__)

with open("candidates.json", "r") as file:
    candidates = json.load(file)
    file.close()


@app.route('/')
def profile():
    text = ""
    for i in range(len(candidates)):
        text += f"""Имя кандидата - {candidates[i]["name"]}\nПозиция кандидата - {candidates[i]["position"]}\nНавыки через запятую - {candidates[i]["skills"]}\n \n"""
    return f"<pre>{text}<pre>"

@app.route('/candidate/<x>')
def candidate(x):
    text = f"""Имя кандидата - {candidates[int(x)-1]["name"]}\nПозиция кандидата - {candidates[int(x)-1]["position"]}\nНавыки через запятую - {candidates[int(x)-1]["skills"]}\n \n"""
    return f"<img src={candidates[int(x)-1]['picture']} >\n<pre>{text}<pre>"


app.run(host='127.0.0.2', port=80)
