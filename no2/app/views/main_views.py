# app/views/main_views.py

# render_template: HTMLファイルをレンダリングする関数
# Blueprint: Blueprintを作成するクラス
from flask import Blueprint, render_template

# Blueprintオブジェクトを作成
# 'main'はBlueprintの名前、__name__はURL生成で必要
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # templatesフォルダ内のindex.htmlをレンダリングする
    return render_template('index.html')
