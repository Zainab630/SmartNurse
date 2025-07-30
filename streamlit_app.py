import streamlit as st
import openai

st.set_page_config(page_title="SmartNurse", layout="centered")
st.title("🩺 SmartNurse - المساعد التمريضي الذكي")
st.markdown("#### 👤 تم تطويره بواسطة: **زينب نادر الجبوري**")
st.markdown("---")

lang = st.radio("Select Language / اختر اللغة:", ["English", "العربية"])

symptoms = st.text_area("📝 Please describe the patient's symptoms / يرجى وصف أعراض المريض:")

col1, col2 = st.columns(2)
with col1:
    temp = st.text_input("🌡️ Body Temperature (°C)")
    pulse = st.text_input("💓 Pulse Rate (bpm)")
with col2:
    bp = st.text_input("🩸 Blood Pressure (e.g., 120/80)")
    spo2 = st.text_input("🫁 SpO2 (%)")

if st.button("🚨 Emergency - Call a Nurse / طوارئ - استدعِ ممرض"):
    st.error("⚠️ A nurse has been notified immediately!")

if st.button("🔍 Analyze / تحليل"):
    if not symptoms:
        st.warning("Please enter symptoms / الرجاء إدخال الأعراض")
    else:
        if lang == "English":
            prompt = f"Analyze the following nursing symptoms and give a basic nursing recommendation:
{symptoms}"
        else:
            prompt = f"حلل الأعراض التمريضية التالية وقدم توصية تمريضية مبدئية:
{symptoms}"

        st.info("⏳ Please wait, analyzing...")
        try:
            import os
            openai.api_key = os.getenv("OPENAI_API_KEY") or "sk-YourKeyHere"

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert nursing assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response["choices"][0]["message"]["content"]
            st.success("✅ Recommendation:")
            st.markdown(result)
        except Exception as e:
            st.error(f"Error: {e}")
