# 株価可視化アプリ

## 簡単な説明
株価を表を用いて可視化するツールです。表示する日数、株価をサイドバーを利用して調整することができます。
また表示する会社を選択し追加、削除することが可能です。

## ライブラリ
利用しているライブラリで重要なものをピックアップして説明します。
### streamlit
streamlitはPythonのみで簡単にWebアプリを作成できるオープンソースのライブラリです。簡単なコードでUIを作成することができ、データの可視化に向いています。

[streamlit公式ドキュメント](https://docs.streamlit.io/)

### yfinance
yfinanceはティッカーシンボルから各企業の株価や財務情報などの株価データを収集することのできるライブラリです。


## インストール
```
git clone https://github.com/kytym/stockapp.git

pip install -r requirements.text
```

## 使い方
コマンドラインで以下のコードを実行してください
```
streamlit run stockapp.py
```
