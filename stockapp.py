import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st


def main():
    st.title("株価可視化アプリ")
    st.sidebar.write("""
    # 株価
    株価可視化ツールです。以下のオプションから表示日数を指定できます。
    """)

    #サイドバーの設定
    st.sidebar.write("""
    # 表示日数選択
    """)

    days = st.sidebar.slider("日数", 1, 50, 25)

    st.write(f"""
    ### 過去 **{days}日間** の株価
    """)
    
    st.sidebar.write("""
    # 範囲指定
    """)

    ymin, ymax = st.sidebar.slider(
        "範囲を指定してください",
        0, 1500, (0, 1500)
    )

    #ティッカーシンボルの設定
    tickers = {
        "apple": "AAPL",
        "meta":"META",
        "google": "GOOGL",
        "microsoft": "MSFT",
        "amazon": "AMZN",
        "tesla": "TSLA",
        "nvidia": "NVDA"
    }

    df = get_data(days,tickers)

    #表示する会社の選択,削除
    companies = st.multiselect(
        "会社名を選択してください",
        list(df.index),
        ["google","amazon","meta","apple"]
    )

    #株価データの可視化
    if not companies:
        st.error("少なくとも一社を選択してください")
    else:
        data = df.loc[companies]
        st.write("### 株価（USD）", data.sort_index())
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["Date"]).rename(
            columns={"value": "Stock Prices(USD)"}
        )

        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x="Date:T",
                y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                color="Name:N"
            )
        )
        st.altair_chart(chart, use_container_width=True )


#株価データの作成、編集
def get_data(days, tickers):
    df= pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f"{days}d")
        #hist.index = hist.index.strftime("%d %B %Y")
        hist = hist[["Close"]]
        hist.columns= [company]
        hist = hist.T
        hist.index.name = "Name"
        df = pd.concat([df,hist])
    return df


if __name__ == "__main__":
    main()
