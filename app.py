import streamlit as st
import pandas as pd
import plotly.express as px

# CSVファイルのアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=['csv'])
if uploaded_file is not None:
    # データの読み込み
    df = pd.read_csv(uploaded_file)

    # TimestampをDatetime型に変換（タイムスタンプの形式に応じてformatを調整してください）
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%Y-%m-%d %H:%M:%S')

    # グラフの表示
    st.header("Tilt Angleの折れ線グラフ")
    fig = px.line(df, x='Timestamp', y='Tilt Angle', title='Tilt Angle')
    st.plotly_chart(fig)

    # CSVデータの閲覧
    st.header("CSVデータの閲覧")
    st.write(df)
