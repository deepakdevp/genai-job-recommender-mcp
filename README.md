<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/deepakdevp/genai-job-recommender-mcp">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">GenAI Job Recommender</h3>

  <p align="center">
    Unlock your career potential! Upload your resume and get personalized job recommendations, skill gap analysis, and a future roadmap—all powered by AI.
    <br />
    <a href="#about-the-project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#usage">View Demo</a>
    ·
    <a href="https://github.com/deepakdevp/genai-job-recommender-mcp/issues">Report Bug</a>
    ·
    <a href="https://github.com/deepakdevp/genai-job-recommender-mcp/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project



GenAI Job Recommender is a modern, AI-powered web app that helps users:
- Parse and summarize their resume
- Identify skill gaps and receive a personalized roadmap
- Get job recommendations from LinkedIn and Naukri
- Download skill gap and roadmap as a PDF
- Enjoy a beautiful, animated, and user-friendly interface

### Features
* Resume parsing (PDF)
* AI-powered summary, skill gap analysis, and roadmap (OpenAI GPT-4o)
* Job recommendations from LinkedIn and Naukri (Apify)
* Card-style job display with icons and branding
* Downloadable PDF reports
* Animated UI with Lottie

### Built With
* [Streamlit](https://streamlit.io/)
* [OpenAI](https://openai.com/)
* [Apify](https://apify.com/)
* [LottieFiles](https://lottiefiles.com/)
* [FPDF](https://pyfpdf.github.io/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
* Python 3.8+
* pip (or uv)

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/deepakdevp/genai-job-recommender-mcp.git
   cd genai-job-recommender-mcp
   ```
2. Install dependencies
   ```sh
   pip install -r requirements.txt
   # or
   uv pip install -r requirements.txt
   ```
3. Set up environment variables
   Create a `.env` file in the project root with:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   APIFY_KEY=your_apify_api_key
   ```
4. Run the app
   ```sh
   streamlit run app.py
   ```

<!-- USAGE EXAMPLES -->
## Usage

1. Launch the app with `streamlit run app.py`.
2. Upload your resume (PDF).
3. View the AI-generated summary, skill gaps, and roadmap in the tabs.
4. Download the skill gap + roadmap as a PDF.
5. Click "Get Job Recommendations" to fetch jobs from LinkedIn and Naukri.
6. Browse jobs in card-style format with direct links.

_For more examples, please refer to the [Documentation](#)_

<!-- ROADMAP -->
## Roadmap
- [ ] Add support for DOCX resumes
- [ ] Add more job sources (Indeed, Monster, etc.)
- [ ] User authentication and profile saving
- [ ] Enhanced analytics and reporting
- [ ] Mobile-friendly UI
- [ ] ...and more! See [open issues](https://github.com/deepakdevp/genai-job-recommender-mcp/issues)

<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact
Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/deepakdevp/genai-job-recommender-mcp](https://github.com/deepakdevp/genai-job-recommender-mcp)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [LottieFiles](https://lottiefiles.com/)
* [Font Awesome](https://fontawesome.com)

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/deepakdevp/genai-job-recommender-mcp.svg?style=for-the-badge
[contributors-url]: https://github.com/deepakdevp/genai-job-recommender-mcp/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/deepakdevp/genai-job-recommender-mcp.svg?style=for-the-badge
[forks-url]: https://github.com/deepakdevp/genai-job-recommender-mcp/network/members
[stars-shield]: https://img.shields.io/github/stars/deepakdevp/genai-job-recommender-mcp.svg?style=for-the-badge
[stars-url]: https://github.com/deepakdevp/genai-job-recommender-mcp/stargazers
[issues-shield]: https://img.shields.io/github/issues/deepakdevp/genai-job-recommender-mcp.svg?style=for-the-badge
[issues-url]: https://github.com/deepakdevp/genai-job-recommender-mcp/issues
[license-shield]: https://img.shields.io/github/license/deepakdevp/genai-job-recommender-mcp.svg?style=for-the-badge
[license-url]: https://github.com/deepakdevp/genai-job-recommender-mcp/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/deepak-dev-panwar-166187135/
[product-screenshot]: images/screenshot.png
