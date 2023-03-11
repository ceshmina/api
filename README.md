# api

個人用のAPIです。

## development

事前にリポジトリ直下に `.env` ファイルを設置し、以下のように記述してください。値は一例です。

```
FLASK_SECRET_KEY={適当な文字列}
GOOGLE_APPLICATION_CREDENTIALS=../config/account/api-test.json
OPENAI_API_KEY={OpenAIのAPIキー}
PORT=80
```

以下コマンドで起動し、[localhost:8090](http://localhost:8090) で動作確認できます。

データベース (Firestore) に接続するには、テスト環境のサービスアカウントキーを `config/account/api-test.json` に配置してください。

```
docker compose up flask-dev
```

## test

### local

```
docker compose run --rm test
```

### CI

`dev` ブランチにプッシュ/マージ時、GitHub Actionsでテストが実行されます。

## lint

### local

```
docker compose run --rm flake8
docker compose run --rm mypy
```

### CI

`dev` ブランチにプッシュ/マージ時、GitHub Actionsでflake8/mypyが実行されます。

## deployment

### local

以下コマンドでテスト環境同等のビルドをローカルで行い、[localhost:8091](http://localhost:8091) で動作確認できます。

```
docker compose up flask
```

### test

`dev` ブランチにプッシュ/マージすると、Cloud Build/Cloud Runによって [dev.api.ceshmina.com](https://dev.api.ceshmina.com) にデプロイされます。

### production

`main` ブランチにマージすると、Cloud Build/Cloud Runによって [api.ceshmina.com](https://api.ceshmina.com) にデプロイされます。
