# app/__init__.py

from flask import Flask

# 先ほど作成したmain_views.pyからbp(Blueprintオブジェクト)をインポート
from .views import main_views

def create_app():
    # Flaskアプリケーションのインスタンスを作成
    app = Flask(__name__)

    # 作成したBlueprintをアプリケーションに登録
    app.register_blueprint(main_views.bp)

    # 設定済みのアプリケーションインスタンスを返す
    return app
