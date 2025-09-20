# Python Flask講座：note風ブログサイト開発 🚀

これは、ブログで連載しているPython Flask講座の公式ソースコードリポジトリです。

**[🔗 なおくんのブログ | Flask講座](https://nao-kun.com/?cat=56)**

この講座では、PythonのWebフレームワーク**Flask**を使い、**note風のブログサイト**をゼロから構築していきます。Webの仕組みといった基礎の基礎から、Stripeを使った決済機能の実装、そしてDockerを用いた本番環境へのデプロイまで、Webアプリケーション開発の全工程を体系的に学びます。

## ✨ 完成するアプリケーションの主な機能

この講座を最後まで進めると、以下の機能をすべて備えたWebアプリケーションが完成します。

  - **アカウント機能:**
      - ユーザー登録・ログイン・ログアウト
      - Googleアカウントによるソーシャルログイン
      - メールアドレスによる本登録・パスワード再設定
  - **記事投稿機能:**
      - 記事の作成・編集・削除 (CRUD)
      - タグによる記事の分類
  - **ソーシャル機能:**
      - 記事へのコメント投稿
      - 非同期通信による「いいね」機能
  - **収益化機能:**
      - **Stripe連携**による有料記事の単体販売
      - **サブスクリプション**による月額メンバーシップ機能
  - **管理者機能:**
      - ユーザーや投稿を管理するための専用画面

## 🛠️ 使用技術 (技術スタック)

  - **バックエンド:** Python 3.12, Flask
  - **データベース:** PostgreSQL, Redis
  - **ライブラリ:** Flask-SQLAlchemy, Flask-Migrate, Flask-Login, Celery, Stripe, Authlib
  - **フロントエンド:** HTML, CSS, JavaScript (Ajax/fetch API)
  - **インフラ・デプロイ:** Gunicorn, Nginx, Docker, GitHub Actions (CI/CD)

## 🚀 環境構築と実行方法

このプロジェクトをあなたのローカル環境で動かすための手順です。

1.  **リポジトリをクローン**

    ```bash
    git clone https://github.com/あなたのユーザー名/リポジトリ名.git
    cd リポジトリ名
    ```

2.  **Python仮想環境の構築**
    本講座ではPython `3.12.7` を使用します。`venv`を使って仮想環境を構築・有効化してください。

    ```bash
    # Windows (cmd)
    py -3.12 -m venv venv
    .\venv\Scripts\activate

    # macOS (Terminal)
    python3.12 -m venv venv
    source venv/bin/activate
    ```

3.  **依存ライブラリのインストール**

    ```bash
    pip install -r requirements.txt
    ```

4.  **環境変数の設定**
    `.env.example` ファイルをコピーして `.env` という名前のファイルを作成し、ファイル内の項目（`SECRET_KEY`やデータベース接続情報、StripeのAPIキーなど）をあなた自身の環境に合わせて編集してください。

    ```bash
    # Windows (cmd)
    copy .env.example .env

    # macOS (Terminal)
    cp .env.example .env
    ```

    **注意:** `.env` ファイルは、APIキーなどの機密情報を含むため、絶対にGitでバージョン管理しないでください。`.gitignore`に`.env`が含まれていることを確認してください。

5.  **データベースのセットアップ**
    ローカル環境にPostgreSQLがインストールされ、起動していることを確認してください。`.env`ファイルに設定したデータベース名で、空のデータベースを作成しておく必要があります。
    その後、以下のコマンドでテーブルを作成・更新します。

    ```bash
    flask db upgrade
    ```

6.  **アプリケーションの実行**

    ```bash
    flask run
    ```

    ブラウザで `http://127.0.0.1:5000` にアクセスしてください。

## 📚 講座の進め方とソースコードの参照方法

このリポジトリは、講座の各回の終了時点でのソースコードを**Gitのタグ**を使って管理しています。学習中につまずいた時や、特定の回の完成形を確認したい時にご活用ください。

**1. タグの一覧を表示する**
以下のコマンドで、利用可能な全てのタグ（`part-01`など）を確認できます。

```bash
git tag
```

**2. 特定の回の状態に切り替える**
例えば、第5回の終了時点のコードを確認したい場合は、以下のコマンドを実行します。

```bash
git checkout tags/part-05-login
```

**注意:** この状態でコードを編集すると「detached HEAD」状態になります。最新の状態に戻るには `git checkout main` (または `master`) を実行してください。

### 各回のタグと対応記事

| タグ (Tag) | 対応する講座記事 |
| :--- | :--- |
| `part-01-hello-world` | 第1回: Webはどのように動くのか？ |
| `part-02-project-structure` | 第2回: Flaskプロジェクトの始動と設計思想 |
| `part-03-database` | 第3回: データベースの世界へようこそ |
| `part-04-user-model` | 第4回: ユーザーモデルと認証の基礎 |
| `part-05-login` | 第5回: セッションとログイン管理 |
| `part-06-crud` | 第6回: 記事投稿機能(CRUD)の実装 |
| `part-07-comments` | 第7回: コメント機能とリレーションシップ |
| `part-08-tags` | 第8回: タグ機能と多対多リレーションシップ |
| `part-09-ajax-like` | 第9回: Ajaxによる非同期「いいね」機能 |
| `part-10-stripe-single` | 第10回: Stripeによる記事単体決済 |
| `part-11-stripe-subscription`| 第11回: Stripeによるメンバーシップ機能 |
| `part-12-n-plus-1` | 第12回: データベースのパフォーマンス改善 |
| `part-13-celery` | 第13回: バックグラウンドタスク |
| `part-14-oauth` | 第14回: 外部サービスとの連携 (OAuth認証) |
| `part-15-caching` | 第15回: さらなる高速化 (キャッシュの導入) |
| `part-16-production-server` | 第16回: 本番環境のアーキテクチャ |
| `part-17-docker-cicd` | 第17回: DockerとCI/CDによるデプロイ自動化 |

## 📄 ライセンス
このプロジェクトはMITライセンスです。

## ✍️ 著者・ブログ

  - **著者:** なおくん
  - **ブログ:** [なおくんのブログ](https://nao-kun.com/)
