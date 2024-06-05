# 株価可視化アプリ

## 概要
株価を表を用いて可視化するツールです。表示する日数、株価をサイドバーを利用して調整することができます。
また表示する会社を選択し追加、削除することが可能です。

##バージョン
Python 3.12.3

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
cd stockapp
pip install -r requirements.txt
```

## 使い方
コマンドラインで以下のコードを実行してください。実行するとブラウザが起動します。
```
streamlit run stockapp.py
```
