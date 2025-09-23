# run.py

# appフォルダの__init__.pyからcreate_app関数をインポート
from app import create_app

# create_app関数を実行して、アプリケーションインスタンスを作成
app = create_app()

# このファイルが直接実行された場合にのみ、開発サーバーを起動
if __name__ == '__main__':
    app.run(debug=True)
