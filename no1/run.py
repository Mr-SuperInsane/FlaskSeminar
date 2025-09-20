# run.py

# 1. FlaskライブラリからFlaskクラスをインポート
from flask import Flask

# 2. Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# 3. 特定のURLへのアクセスと、実行する関数を結びつける
@app.route('/')
def hello_world():
    # 4. ブラウザに表示する文字列を返す
    return 'Hello, World!'
