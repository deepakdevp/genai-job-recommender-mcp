# 🧑‍💼 GenAI Job Recommender

Unlock your career potential! Upload your resume and get personalized job recommendations, skill gap analysis, and a future roadmap—all powered by AI.

---

## 🚀 Features

- **Landing Page with Animation:** Modern UI with Lottie animation and branding.
- **Resume Parsing:** Upload your resume (PDF) and extract text automatically.
- **AI-Powered Analysis:**
  - Resume summary highlighting key skills and experience
  - Skill gap analysis
  - Personalized future roadmap
- **Job Recommendations:**
  - Fetches jobs from LinkedIn and Naukri using Apify
  - Card-style job display with icons and branding
- **Downloadable Reports:** Download skill gap and roadmap as a PDF.
- **Tabbed Layout:** Clean navigation for summary, gaps, roadmap, and jobs.
- **Animated & Visual UI:** Emojis, icons, and Lottie animations for a delightful experience.

---

## 🛠️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/genai-job-recommender-mcp.git
   cd genai-job-recommender-mcp
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Or, if using `uv`:
   ```bash
   uv pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root with the following:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   APIFY_KEY=your_apify_api_key
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

---

## ⚙️ Environment Variables

- `OPENAI_API_KEY` — Your OpenAI API key for GPT-4o access
- `APIFY_KEY` — Your Apify API key for job scraping

---

## 📦 Dependencies

- streamlit
- openai
- pymupdf
- python-dotenv
- apify-client
- streamlit-lottie
- fpdf

---

## 🖥️ Usage

1. Launch the app with `streamlit run app.py`.
2. Upload your resume (PDF).
3. View the AI-generated summary, skill gaps, and roadmap in the tabs.
4. Download the skill gap + roadmap as a PDF.
5. Click "Get Job Recommendations" to fetch jobs from LinkedIn and Naukri.
6. Browse jobs in card-style format with direct links.

---

## 📁 Project Structure

```
├── app.py                # Streamlit app
├── src/
│   ├── helper.py         # Resume parsing & OpenAI helpers
│   ├── jobs_api.py       # Job fetching logic (LinkedIn, Naukri)
├── assets/               # Lottie animations, icons
├── requirements.txt
├── README.md
└── .env                  # (not committed) API keys
```

---

## 🙏 Credits
- [Streamlit](https://streamlit.io/)
- [OpenAI](https://openai.com/)
- [Apify](https://apify.com/)
- [LottieFiles](https://lottiefiles.com/) for animations

---

## 📬 Contact
For questions, suggestions, or contributions, open an issue or reach out to the maintainer.
