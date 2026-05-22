# AI BI Copilot

AI-powered Business Intelligence platform that automatically transforms CSV datasets into:

- 📊 Interactive dashboards
- 📈 AI-generated charts
- 📌 KPI metrics
- 🧠 AI insights
- 💬 Natural language data Q&A

Built with:
- Python
- OpenAI API
- Pandas
- Plotly
- Streamlit

---

# 🚀 Features

- Automatic schema detection
- AI-generated dashboard planning
- KPI computation
- Interactive Plotly charts
- Streamlit dashboard UI
- Ask questions directly to your data

---

# 📁 Project Structure

```bash
ai-bi-engine/
│
├── app/
│   ├── ai/
│   ├── data/
│   ├── visualization/
│   ├── utils/
│   └── ui/
│
├── datasets/
├── outputs/
├── tests/
│
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/ai-bi-engine.git

cd ai-bi-engine
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

```txt
openai
pandas
plotly
streamlit
python-dotenv
numpy
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini
```

---

# ▶️ Run Application

```bash
streamlit run app/ui/streamlit_app.py
```

App runs at:

```bash
http://localhost:8501
```

---

# 🧠 How It Works

1. Upload CSV dataset
2. Detect column roles
3. Compute KPIs
4. Generate AI dashboard plan
5. Render charts
6. Ask questions about the data

---

# 📊 Example AI Dashboard 


<p align="center">
  <img src="https://raw.githubusercontent.com/chrisProj91/AI-BI-Copilot/main/assets/image.png" width="1000" style="border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.2);" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/chrisProj91/AI-BI-Copilot/main/assets/image(1).png" width="1000" style="border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.2);" />
</p>
---

# 🖥️ UI Modes

## 📊 Auto Dashboard
Automatically generates:
- KPIs
- Charts
- Insights

## 🔍 Explore Data
- Dataset preview
- Summary statistics

## 💬 Ask AI
Ask questions directly to your dataset.

---

# 🧱 Core Modules

| Module | Purpose |
|---|---|
| `loader.py` | CSV loading |
| `schema_detector.py` | Column role detection |
| `metric_engine.py` | KPI calculations |
| `dashboard_planner.py` | AI dashboard generation |
| `chart_renderer.py` | Plotly chart rendering |
| `insights_generator.py` | AI dataset Q&A |

---

# 📈 Supported Charts

- Bar
- Line
- Pie

---

# 🛡️ Validation

Dashboard JSON validation ensures:
- valid structure
- required fields
- valid chart definitions

---

# 🔮 Future Improvements

- Excel support
- SQL database support
- PDF reports
- Advanced chart types
- Dashboard export
- Multi-page dashboards

---

# 📌 Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| Visualization | Plotly |
| AI | OpenAI API |
| Data | Pandas |

---

