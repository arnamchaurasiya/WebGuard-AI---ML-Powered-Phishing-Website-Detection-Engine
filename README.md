# 🛡️ WebGuard AI — ML-Powered Phishing Website Detection Engine

**Live Demo:** [webguard-ai-ml-powered-phishing-website-detection-engine-gyk.streamlit.app](https://webguard-ai-ml-powered-phishing-website-detection-engine-gyk.streamlit.app/)

**WebGuard AI** is a real-time cybersecurity product component designed to identify and classify phishing websites using machine learning and content-based feature extraction. Built with enterprise security in mind, this detection engine can be integrated into broader **EDR, SIEM, or DLP** solutions to provide predictive analytics and automated threat detection, enabling **SOAR** platforms to orchestrate rapid responses against malicious web traffic.

## 🛠️ Features & Cybersecurity Alignment

- **🔍 AI/ML Threat Detection**: Automatically detects phishing websites with a 98% F1-Score using a multi-model approach (Random Forest, Decision Tree, Neural Networks). Maps directly to **AI/ML-based security use cases**.
- **📊 Advanced Anomaly Detection**: Extracts 43 content-based features dynamically by parsing HTML/DOM structures instead of just analyzing URLs, simulating deep **threat analysis and vulnerability research**.
- **⚙️ High-Fidelity Classification**: Trained on a custom dataset of 31,600 websites (16,100 Legitimate, 15,500 Phishing).
- **🌐 Real-Time Analytics Dashboard**: User-friendly Streamlit web application providing instant phishing verdicts, designed for SOC analyst workflows.

## 🖥️ Tech Stack

WebGuard AI leverages scalable tools tailored for cybersecurity product engineering:

- **[Python](https://www.python.org/)**: Core backend logic and ML orchestration.
- **[Scikit-learn](https://scikit-learn.org/)**: Machine learning library used to build the predictive analytics models.
- **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)**: Used for deep web scraping and content-based feature extraction from live targets.
- **[Streamlit](https://streamlit.io/)**: Framework for the real-time interaction and reporting dashboard.
- **[Pandas](https://pandas.pydata.org/)** & **[Numpy](https://numpy.org/)**: Data processing, manipulation, and correlation analysis.

## 📁 Directory Structure

```text
WebGuard-AI/
├── datasets/               # Structured dataset files for model training
├── images/                 # Image assets for the web dashboard
├── pages/                  # Reporting and Contact modules
├── style/                  # UI Styling and CSS
├── trained_models/         # Serialized ML models for fast inference
├── 1_🔎_Home.py            # Main application entry point
├── data_collector.py       # Live data collection and scraping logic
├── feature_extraction.py   # Code for extracting the 43 security features
├── features.py             # Feature definitions
├── machine_learning.py     # Script for training, cross-validation, and evaluation
├── ml_app_screen.py        # Core application logic and rendering
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.12+ (Recommended)
- Dependencies listed in `requirements.txt`

### Installation & Deployment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/arnamchaurasiya/WebGuard-AI---ML-Powered-Phishing-Website-Detection-Engine.git
   cd WebGuard-AI---ML-Powered-Phishing-Website-Detection-Engine
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application locally:**
   ```bash
   streamlit run "1_🔎_Home.py"
   ```

### Usage Workflow

- Navigate to `http://localhost:8501`.
- Input a suspicious URL into the scanning engine.
- The system will fetch the HTML content, extract security features, and feed them into the ML classifier.
- Receive a real-time verdict (Legitimate or Phishing) to simulate an automated alert triage process.

## 🔍 Model Details & Analytics

WebGuard AI utilizes 6 different machine learning classifiers implemented with k-fold cross-validation (k=5). Performance metrics (Accuracy, Precision, Recall, F1-Score) are calculated to ensure minimal false positives—a critical requirement for **SIEM and EDR** products. **Random Forest** and **Decision Tree** Classifiers demonstrated the best performance, effectively distinguishing threats based on content structure.

## 🔗 Useful Links

- [Live Application](https://webguard-ai-ml-powered-phishing-website-detection-engine-gyk.streamlit.app/)
- [Original Dataset Source](https://www.kaggle.com/datasets/yuvistrange/content-based-features-phishing-and-legit-websites)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
