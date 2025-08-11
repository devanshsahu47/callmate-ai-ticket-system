# 🤖 CallMate – AI-Powered Ticket Management System  

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)  
![Django](https://img.shields.io/badge/Django-4.0+-green?logo=django)  
![License](https://img.shields.io/badge/License-MIT-yellow)  
![Status](https://img.shields.io/badge/Status-Active-success)  

> **AI-driven customer support solution** that automates ticket categorization, sentiment analysis, and priority handling for faster response times and improved customer satisfaction.  

---

## 📌 Table of Contents  
1. [Overview](#-overview)  
2. [Core Features](#-core-features)  
3. [Tech Stack](#-tech-stack)  
4. [Project Structure](#-project-structure)  
5. [Getting Started](#-getting-started)  
6. [Future Enhancements](#-future-enhancements)  

---

## 📖 Overview  
CallMate is a **Django-based ticket management platform** enhanced with **Machine Learning** and **NLP**.  
It automatically categorizes incoming tickets, analyzes sentiment, and prioritizes issues to ensure the **most urgent cases are resolved first**.

---

## 🚀 Core Features
- **Automated Categorization** – Classifies tickets into *Billing*, *Technical*, *General*, *Complaint*.  
- **Sentiment Analysis** – Uses **NLTK’s VADER** to detect tone (*Positive*, *Negative*, *Neutral*).  
- **Dynamic Priority Scoring** – Combines urgency level & sentiment score for ranking.  
- **Prioritized Dashboard** – Sorted ticket list for instant access to critical issues.  
- **One-Click Agent Assignment** – Bulk-assign tickets to agents by category.  
- **Responsive UI** – Built with **Bootstrap 5** for a seamless experience.  

---

## 🛠 Tech Stack  

**Backend:** Django  
**Frontend:** HTML, Bootstrap 5, Django Templates  
**Database:** SQLite 3  
**ML & NLP:** Scikit-learn, NLTK (VADER), Joblib  
**Language:** Python  

---

## 🛠 5. How to Run the Project

Since the project is not deployed, you can run it locally by following these steps:

---

### **Step 1 – Clone the Repository**
```bash
git clone <your-repository-url>
cd callmate-project
```

### **Step 2 – Set Up a Virtual Environment**
# For macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
# For Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```

### **Step 3 – Install Required Packages**
```bash
pip install -r requirements.txt
```

### **Step 4 – Train the Machine Learning Model**
```bash
python tickets/train_model.py
```

### **Step 5 – Run Database Migrations**
```bash
python manage.py migrate
```

### **Step 6 – Start the Development Server**
```bash
python manage.py runserver
```

---

## 🚀 Future Enhancements
- **User Authentication** – Add secure login for customers and agents to enable personalized access and role-based features.  
- **Real-time Updates** – Implement Django Channels or integrate React/Vue for live dashboard refresh when new tickets arrive.  
- **Advanced Analytics** – Build a dedicated analytics dashboard to track KPIs like category distribution, resolution time, and agent performance.  
- **Email Notifications** – Send automated emails to customers when a ticket is submitted and to agents when assigned.  
- **Enhanced ML Model** – Retrain using a larger, more diverse dataset for higher accuracy and broader category prediction.  
- **Database Upgrade** – Switch from SQLite to PostgreSQL for better scalability and production readiness.  
