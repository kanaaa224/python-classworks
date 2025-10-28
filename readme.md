仮想環境を作成
```
python -m venv venv
```

仮想環境を有効化
```
source venv/bin/activate
```

（Windows環境はVSCodeのcmdで（PowerShellではない））
```
venv\Scripts\activate.bat
```

仮想環境の無効化
```
deactivate
```

パッケージをインストール
```
pip install -r requirements.txt
```

パッケージ情報確認
```
pip list
```

パッケージ情報書き出し
```
pip freeze > requirements.txt
```