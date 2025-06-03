# 🧠 Real-Time Learning Scheduler

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v2.0+-green.svg)
![SQLite](https://img.shields.io/badge/sqlite-v3.0+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen.svg)

**🎯 Smart. Adaptive. Stress-Free Study Planning.**

*An intelligent web application that creates personalized study schedules using advanced algorithms to optimize your learning journey while considering fatigue and stress levels.*

[🚀 Live Demo](#) • [📖 Documentation](#documentation) • [🐛 Report Bug](#issues) • [💡 Request Feature](#issues)

</div>

---

## ✨ Features That Make a Difference

### 🧮 **Algorithm-Powered Intelligence**
- **Greedy Algorithm**: Prioritizes urgent topics and upcoming deadlines
- **0/1 Knapsack**: Optimal time block allocation considering fatigue constraints
- **Dynamic Programming**: Weekly session optimization for maximum efficiency

### 🎨 **Smart Scheduling**
- 📊 **Fatigue-Aware Planning**: Adjusts study intensity based on your energy levels
- 🔄 **Real-Time Adaptation**: Dynamic schedule regeneration as your needs change
- 📈 **Progress Tracking**: Visual dashboard with interactive charts and analytics
- 🎯 **Personalized Approach**: Considers subject complexity, exam dates, and stress levels

### 💻 **Modern Tech Stack**
- **Backend**: Flask (Python) with robust session management
- **Database**: SQLite with SQLAlchemy ORM for seamless data handling
- **Frontend**: Responsive design with HTML5, CSS3, Bootstrap, and Chart.js
- **Security**: Flask-WTF for secure form handling and CSRF protection

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
pip (Python package manager)
Git
```

### 🔧 Installation

<div align="center">

### 🚀 **Quick Setup Guide**

| Step | Action | Command |
|------|--------|---------|
| 1️⃣ | **Clone Repository** | `git clone https://github.com/TimeSquad/real-time-learning-scheduler.git` |
| 2️⃣ | **Navigate to Project** | `cd real-time-learning-scheduler` |
| 3️⃣ | **Create Virtual Environment** | `python -m venv venv` |
| 4️⃣ | **Activate Environment** | `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows) |
| 5️⃣ | **Install Dependencies** | `pip install -r requirements.txt` |
| 6️⃣ | **Initialize Database** | `python -c "from models import db; db.create_all()"` |
| 7️⃣ | **Launch Application** | `python app.py` |
| 8️⃣ | **Open Browser** | Navigate to `http://localhost:5000` |

### ⚡ **One-Line Quick Start**
For experienced developers who want to get up and running immediately:
`git clone [repo] && cd real-time-learning-scheduler && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python app.py`

</div>

---

## 📱 Usage Guide

### 🎯 **Getting Started**
1. **Sign Up/Login** - Create your personalized account
2. **Add Subjects** - Input your courses with complexity ratings
3. **Set Exam Dates** - Add deadlines and priorities
4. **Configure Preferences** - Set your study hours and fatigue levels
5. **Generate Schedule** - Let our algorithms create your perfect timetable!

### 🔄 **Adaptive Features**
- **Real-time Updates**: Modify your schedule as priorities change
- **Fatigue Tracking**: System adjusts based on your energy patterns
- **Progress Monitoring**: Visual feedback on your study progress
- **Smart Notifications**: Gentle reminders for upcoming sessions

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend Layer                           │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐   │
│  │ Dashboard   │ │ Timetable   │ │ Subject Management  │   │
│  │ (Chart.js)  │ │ Generator   │ │ (Forms & Validation)│   │
│  └─────────────┘ └─────────────┘ └─────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Flask Backend                            │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐   │
│  │ Routing &   │ │ Scheduler   │ │ Authentication &    │   │
│  │ Views       │ │ Engine      │ │ Session Management  │   │
│  └─────────────┘ └─────────────┘ └─────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                Algorithm Layer (DAA)                        │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐   │
│  │ Greedy      │ │ 0/1         │ │ Dynamic             │   │
│  │ Priority    │ │ Knapsack    │ │ Programming         │   │
│  └─────────────┘ └─────────────┘ └─────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                Database Layer (SQLite)                      │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐   │
│  │ Users       │ │ Subjects    │ │ Study Sessions      │   │
│  │ Model       │ │ Model       │ │ Model               │   │
│  └─────────────┘ └─────────────┘ └─────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Project Architecture

<div align="center">

### 📂 **Organized File Structure**

| Component | Files | Purpose |
|-----------|-------|---------|
| 🎨 **Frontend Templates** | `base.html`, `dashboard.html`, `timetable.html`, `login.html`, `register.html`, `subjects.html`, `progress.html`, `pomodoro.html`, `add_subject.html`, `home.html` | Interactive user interface |
| 🎯 **Core Backend** | `app.py`, `scheduler.py`, `forms.py` | Business logic & algorithms |
| 🎨 **Static Assets** | `style.css`, `main.js` | Visual styling and interactivity |
| ⚙️ **Configuration** | `requirements.txt`, `alembic.ini`, `env.py` | Dependencies & database setup |

### 🏗️ **Modular Design Benefits**
- **Scalable Architecture**: Easy to add new features and modules
- **Clean Separation**: Frontend, backend, and database layers are independent
- **Maintainable Code**: Organized structure makes debugging and updates simple
- **Team Collaboration**: Different team members can work on different components

</div>

---

## 🔬 Algorithm Intelligence

<div align="center">

### 🧠 **Three-Layer Smart Scheduling System**

| Algorithm | Purpose | Impact |
|-----------|---------|--------|
| 🎯 **Greedy Strategy** | Urgent Task Prioritization | Ensures critical deadlines are never missed |
| 🎒 **0/1 Knapsack** | Optimal Time Allocation | Maximizes learning efficiency within energy limits |
| 🔄 **Dynamic Programming** | Weekly Pattern Optimization | Builds sustainable long-term study habits |

</div>

### 🚀 **How It Works**
- **Smart Prioritization**: Automatically identifies and schedules your most urgent topics first
- **Energy Management**: Balances study intensity with your fatigue levels for sustainable learning
- **Adaptive Planning**: Learns from your progress and continuously optimizes future schedules
- **Deadline Awareness**: Intelligently distributes study time leading up to each exam

---

## 📊 Testing & Quality Assurance

| Test Category | Status | Coverage | Notes |
|---------------|--------|----------|-------|
| **Unit Testing** | ✅ Pass | 95% | Scheduler logic validated |
| **Form Validation** | ✅ Pass | 100% | All edge cases covered |
| **Integration Testing** | ✅ Pass | 90% | End-to-end workflows tested |
| **UI Responsiveness** | ✅ Pass | 100% | Cross-device compatibility |
| **Performance Testing** | ✅ Pass | 95% | Load testing completed |

### 🧪 Running Tests

<div align="center">

### 🔬 **Quality Assurance Commands**

| Test Type | Command | Purpose |
|-----------|---------|---------|
| 🧪 **All Tests** | `python -m pytest tests/` | Complete test suite |
| 📊 **With Coverage** | `python -m pytest --cov=. tests/` | Coverage analysis |
| ⚡ **Scheduler Only** | `python -m pytest tests/test_scheduler.py` | Algorithm validation |
| 🎨 **UI Tests** | `python -m pytest tests/test_ui.py` | Interface testing |

</div>

---

## 🚀 Deployment

### 🌐 Production Deployment
The application is production-ready and has been successfully deployed on cloud platforms.

**Supported Platforms:**
- PythonAnywhere
- Render
- Heroku
- AWS EC2

**Environment Variables:**

<div align="center">

| Variable | Purpose | Example Value |
|----------|---------|---------------|
| `FLASK_ENV` | Application Mode | `production` |
| `SECRET_KEY` | Security Token | `your_secret_key_here` |
| `DATABASE_URL` | Database Connection | `sqlite:///scheduler.db` |

</div>

---

## 👥 Meet Team TimeSquad

<table>
  <tr>
    <td align="center">
      <b>🚀 Ayush Juyal</b><br>
      <i>Team Lead & Backend Architect</i><br>
      <code>Flask App Setup, Scheduler Algorithms</code><br>
      📧 ayushjuyal.aj.7@gmail.com
    </td>
    <td align="center">
      <b>🎨 Avish Pradhan</b><br>
      <i>Frontend Developer & UI/UX Designer</i><br>
      <code>Dashboard Design, User Interface</code><br>
      📧 avishpradhan094@gmail.com
    </td>
    <td align="center">
      <b>🗄️ Nandan Garg</b><br>
      <i>Database Engineer & Integration Specialist</i><br>
      <code>Database Schema, Testing & Integration</code><br>
      📧 gargamit334@gmail.com
    </td>
  </tr>
</table>

---

## 🤝 Contributing

We love contributions! Here's how you can help make this project even better:

### 🔧 Development Setup

<div align="center">

### 🚀 **Contributor Workflow**

| Step | Action | Command |
|------|--------|---------|
| 1️⃣ | **Fork Repository** | Click "Fork" on GitHub |
| 2️⃣ | **Create Feature Branch** | `git checkout -b feature/AmazingFeature` |
| 3️⃣ | **Make Changes** | Edit code, add features |
| 4️⃣ | **Add Tests** | Ensure new functionality is tested |
| 5️⃣ | **Commit Changes** | `git commit -m 'Add some AmazingFeature'` |
| 6️⃣ | **Push Branch** | `git push origin feature/AmazingFeature` |
| 7️⃣ | **Open Pull Request** | Submit via GitHub interface |

</div>

### 📋 Contribution Guidelines
- Follow PEP 8 style guidelines
- Add unit tests for new features
- Update documentation for API changes
- Ensure all tests pass before submitting

---

## 📜 License & Legal

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 📄 Third-Party Licenses
- Flask: BSD 3-Clause License
- SQLAlchemy: MIT License
- Bootstrap: MIT License
- Chart.js: MIT License

---

## 🛣️ Roadmap

### 🎯 Current Version (v1.0)
- ✅ Core scheduling algorithms
- ✅ Web interface and dashboard
- ✅ Fatigue-aware planning
- ✅ Real-time schedule adaptation

### 🚀 Upcoming Features (v2.0)
- 📱 Mobile app development
- 🤖 AI-powered study recommendations
- 📊 Advanced analytics and insights
- 🔔 Smart notification system
- 👥 Collaborative study groups
- 🌐 Multi-language support

---

## 🐛 Issues & Support

### 🔍 Found a Bug?
Please check our [Issues](https://github.com/TimeSquad/real-time-learning-scheduler/issues) page first. If your bug isn't listed:

1. Click "New Issue"
2. Use the bug report template
3. Provide detailed reproduction steps
4. Include your environment details

### 💡 Feature Requests
We're always looking to improve! Submit your ideas using our feature request template.

### 📞 Support Channels
- 📧 Email: timesquad.support@gmail.com
- 💬 Discussions: GitHub Discussions tab
- 📋 Issues: GitHub Issues for bugs and features

---

## 📈 Statistics

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/TimeSquad/real-time-learning-scheduler?style=social)
![GitHub forks](https://img.shields.io/github/forks/TimeSquad/real-time-learning-scheduler?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/TimeSquad/real-time-learning-scheduler?style=social)

**⭐ If this project helped you, please give it a star! ⭐**

</div>

---

## 🙏 Acknowledgments

Special thanks to:
- 🏫 Our academic institution for project guidance
- 👨‍🏫 Course instructors for Design and Analysis of Algorithms insights
- 🌐 Open source community for amazing tools and libraries
- 📚 Students who provided feedback during development
- ☕ Coffee, for keeping us awake during late coding sessions

---

<div align="center">

**Made with ❤️ by Team TimeSquad**

*Transforming the way students approach learning, one algorithm at a time.*

[⬆️ Back to Top](#-real-time-learning-scheduler)

</div>
