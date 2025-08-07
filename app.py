import streamlit as st
from src.helper import extract_text_from_pdf, call_openai
from src.jobs_api import fetch_linkedin_jobs, fetch_naukri_jobs

st.title("Job Recommender")

st.subheader("Enter your job description")
job_description = st.text_area("Job Description")

st.subheader("Enter your resume")
resume = st.file_uploader("Upload your resume", type=["pdf", "docx"])

st.subheader("Enter your job description")

file_to_upload = st.file_uploader("Upload your resume", type=["pdf", "docx"])

if file_to_upload:
  with st.spinner("Extracting text from resume..."):
    resume_text = extract_text_from_pdf(file_to_upload)

  with st.spinner("Summarizing resume..."):
    resume_summary = call_openai(f"Summarize the following resume highlighting the key skills and experience. {resume_text}" )

  with st.spinner("Finding skill gaps..."):
    skill_gaps = call_openai(f"Analyze the following resume and identify the skill gaps,certifications,projects,experience,education {resume_summary}" )

  with st.spinner("Forming future roadmap to fill the skill gaps..."):
    future_roadmap = call_openai(f"Go though the resume summary and skill gaps and form a future roadmap to fill the skill gaps. resume summary: {resume_summary}/n/n skill gaps: {skill_gaps}" )

  # Display the resume summary, skill gaps and future roadmap in the UI
  st.subheader("Resume Summary")
  st.write(resume_summary)
  st.subheader("Skill Gaps")
  st.write(skill_gaps)
  st.subheader("Future Roadmap")
  st.write(future_roadmap)

  if st.button("🔎Get Job Recommendations"):
    with st.spinner("Fetching job recommendations..."):
        keywords = call_openai(
            f"Based on this resume summary, suggest the best job titles and keywords for searching jobs. Give a comma-separated list only, no explanation.\n\nSummary: {summary}",
            max_tokens=100
        )

        search_keywords_clean = keywords.replace("\n", "").strip()

        st.success(f"Extracted Job Keywords: {search_keywords_clean}")

        with st.spinner("Fetching jobs from LinkedIn and Naukri..."):
            linkedin_jobs = fetch_linkedin_jobs(search_keywords_clean, rows=60)
            naukri_jobs = fetch_naukri_jobs(search_keywords_clean, rows=60)

    if linkedin_jobs:
            for job in linkedin_jobs:
                st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}*")
                st.markdown(f"- 📍 {job.get('location')}")
                st.markdown(f"- 🔗 [View Job]({job.get('link')})")
                st.markdown("---")
    else:
        st.warning("No LinkedIn jobs found.")

    st.markdown("---")
    st.header("💼 Top Naukri Jobs (India)")

    if naukri_jobs:
        for job in naukri_jobs:
            st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}*")
            st.markdown(f"- 📍 {job.get('location')}")
            st.markdown(f"- 🔗 [View Job]({job.get('url')})")
            st.markdown("---")
    else:
        st.warning("No Naukri jobs found.")