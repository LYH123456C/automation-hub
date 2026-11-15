import streamlit as st

st.set_page_config(page_title="自动化全能 AI 矩阵", page_icon="🌌", layout="centered")

st.title("🌌 自动化全能 AI 控制台")
st.write("欢迎回来，LYH。请选择你需要调用的专家智能体：")

st.divider()

# 分为两列，放置两个核心按钮
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 自控原理导师")
    st.write("支持劳斯判据计算、微积分画图、文件/截图解析。")
    st.link_button("进入自控导师", "https://control-agent-v3-vh2twxzrcwricl9vnqgl2g.streamlit.app", use_container_width=True)

with col2:
    st.subheader("🏭 PLC 编程专家")
    st.write("支持西门子/三菱代码生成、语法自检、文档分析。")
    st.link_button("进入 PLC 专家", "https://plc-expert-yh.streamlit.app", use_container_width=True)

st.divider()

# 预留的未来扩展区
st.subheader("🧠 多学科问答中枢 (开发中...)")
st.info("未来将支持：高数辅导、大学英语、电力电子技术等学科。")
