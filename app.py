import streamlit as st
from src.helper import extract_text_from_pdf, call_openai
from src.jobs_api import fetch_linkedin_jobs, fetch_naukri_jobs
from streamlit_lottie import st_lottie
import json
from fpdf import FPDF
import os

# --- Load Lottie Animation ---
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_resume = load_lottiefile("assets/animation.json")

# --- Landing Section ---
st.set_page_config(page_title="GenAI Job Recommender", page_icon="🧑‍💼", layout="wide")

with st.container():
    left, right = st.columns([2, 1])
    with left:
        st.markdown("""
        # 🧑‍💼 GenAI Job Recommender
        Unlock your career potential! Upload your resume and get personalized job recommendations, skill gap analysis, and a future roadmap—all powered by AI.
        """)
    with right:
        st_lottie(lottie_resume, height=180, key="resume-lottie")

st.markdown("---")

# --- File Upload ---
st.subheader("Upload your Resume")
file_to_upload = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])  # docx not supported in extract_text_from_pdf

resume_summary = skill_gaps = future_roadmap = None
linkedin_jobs = naukri_jobs = None

if file_to_upload:
    with st.spinner("Extracting text from resume..."):
        resume_text = extract_text_from_pdf(file_to_upload)

    with st.spinner("Summarizing resume..."):
        resume_summary = call_openai(f"Summarize the following resume highlighting the key skills and experience. {resume_text}")

    with st.spinner("Finding skill gaps..."):
        skill_gaps = call_openai(f"Analyze the following resume and identify the skill gaps,certifications,projects,experience,education {resume_summary}")

    with st.spinner("Forming future roadmap to fill the skill gaps..."):
        future_roadmap = call_openai(f"Go though the resume summary and skill gaps and form a future roadmap to fill the skill gaps. resume summary: {resume_summary}\n\n skill gaps: {skill_gaps}")

    st.markdown("---")

    # --- Tabs for Results ---
    tabs = st.tabs(["📄 Resume Summary", "🧩 Skill Gaps", "🗺️ Roadmap", "💼 Recommendations"])

    with tabs[0]:
        st.markdown("## 📄 Resume Summary")
        st.info(resume_summary)

    with tabs[1]:
        st.markdown("## 🧩 Skill Gaps")
        st.warning(skill_gaps)

    with tabs[2]:
        st.markdown("## 🗺️ Future Roadmap")
        st.success(future_roadmap)
        # --- Download PDF Button ---
        if st.button("⬇️ Download Skill Gap + Roadmap as PDF"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, f"Skill Gaps:\n{skill_gaps}\n\nFuture Roadmap:\n{future_roadmap}")
            pdf_path = "skill_gap_roadmap.pdf"
            pdf.output(pdf_path)
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="Download PDF",
                    data=f,
                    file_name="skill_gap_roadmap.pdf",
                    mime="application/pdf"
                )
            os.remove(pdf_path)

    with tabs[3]:
        st.markdown("## 💼 Job Recommendations")
        if st.button("🔎 Get Job Recommendations"):
            with st.spinner("Fetching job recommendations..."):
                keywords = call_openai(
                    f"Based on this resume summary, suggest the best job titles and keywords for searching jobs. Give a comma-separated list only, no explanation.\n\nSummary: {resume_summary}",
                    max_tokens=100
                )
                search_keywords_clean = keywords.replace("\n", "").strip()
                st.success(f"Extracted Job Keywords: {search_keywords_clean}")
                with st.spinner("Fetching jobs from LinkedIn and Naukri..."):
                    linkedin_jobs = fetch_linkedin_jobs(search_keywords_clean, rows=60)
                    naukri_jobs = fetch_naukri_jobs(search_keywords_clean, rows=60)

            st.markdown("### 🌐 LinkedIn Jobs")
            if linkedin_jobs:
                for job in linkedin_jobs:
                    st.markdown(f"""
                        <div style='background-color:#f9f9f9; border-radius:10px; padding:16px; margin-bottom:10px; box-shadow:0 2px 8px #eee;'>
                        <b>💼 {job.get('title')}</b> at <i>{job.get('companyName')}</i><br>
                        📍 {job.get('location')}<br>
                        🔗 <a href='{job.get('link')}' target='_blank'>View Job</a>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("No LinkedIn jobs found.")

            st.markdown("### 🇮🇳 Top Naukri Jobs (India)")
            if naukri_jobs:
                for job in naukri_jobs:
                    st.markdown(f"""
                        <div style='background-color:#f1f8e9; border-radius:10px; padding:16px; margin-bottom:10px; box-shadow:0 2px 8px #eee;'>
                        <b>💼 {job.get('title')}</b> at <i>{job.get('companyName')}</i><br>
                        📍 {job.get('location')}<br>
                        🔗 <a href='{job.get('url')}' target='_blank'>View Job</a>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("No Naukri jobs found.")