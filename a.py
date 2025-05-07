import streamlit as st

# プログラミング言語の選択
options = ["Python", "Java", "C++", "JavaScript"]
language = st.selectbox("プログラミング言語を選択してください", options)

# 言語に基づく特徴の表示
if language == "Python":
    st.write("Pythonは、シンプルで読みやすい構文を持つ高水準プログラミング言語です。")
elif language == "Java":
    st.write(
        "Javaは、オブジェクト指向プログラミング言語で、プラットフォームに依存しない特性を持っています。"
    )
elif language == "C++":
    st.write("C++は、低レベルのメモリ操作が可能な高性能プログラミング言語です。")
elif language == "JavaScript":
    st.write("JavaScriptは、ウェブ開発において広く使用されるスクリプト言語です。")
