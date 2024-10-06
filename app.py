import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd
import random
import webbrowser
import threading
from jinja2 import Template
import os

app = FastAPI()

# Bootstrap static files serving
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load data from the xlsx file
def load_data():
    # 'data.xlsx'는 실행 파일과 같은 디렉토리에 있는 엑셀 파일
    file_path = os.path.join(os.path.dirname(__file__), 'data.xlsx')
    df = pd.read_excel(file_path, engine='openpyxl')
    return df[['name', 'email']].dropna()

# Randomly select 60 emails
def select_random_emails(df, count=60):
    random_state_value = random.randint(1, 10000)
    selected = df.sample(n=count, random_state=random_state_value)
    return selected['email'].tolist()

@app.get("/", response_class=HTMLResponse)
async def get_index():
    df = load_data()
    emails = df['email'].tolist()
    total_count = len(emails)
    with open(os.path.join(os.path.dirname(__file__), "static/index.html"), "r", encoding='utf-8') as f:
        template_content = f.read()
    template = Template(template_content)
    return template.render(
        emails=emails, 
        total_count=total_count, 
        selected_emails=None, 
        draw_done=False
    )

@app.post("/draw", response_class=HTMLResponse)
async def draw_random_emails():
    df = load_data()
    selected_emails = select_random_emails(df)
    with open(os.path.join(os.path.dirname(__file__), "static/index.html"), "r", encoding='utf-8') as f:
        template_content = f.read()
    template = Template(template_content)
    return template.render(
        emails=[], 
        total_count=0, 
        selected_emails=selected_emails, 
        draw_done=True
    )

# 서버 시작 후 웹 브라우저를 자동으로 열기 위한 함수
def open_browser():
    webbrowser.open("http://localhost:8000")

# 메인 실행 함수
def run():
    # 웹 서버를 실행하고 웹 브라우저를 엽니다.
    threading.Timer(1.25, open_browser).start()  # 1.25초 후에 브라우저를 엽니다.
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    run()
