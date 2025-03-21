### **🔹 Load Testing Suite**
This repository contains **load testing scripts** for evaluating web application performance using **JMeter, Locust, and k6**.  

### **🛠 Tools Used**
- **Apache JMeter** (`.jmx`) – GUI-based performance testing  
- **Locust** (`Python`) – Python-based load testing with a web UI  
- **k6** (`JavaScript`) – CLI-based load testing for DevOps & CI/CD  

---

## **🚀 How to Use Each Tool**

### **1️⃣ JMeter**
**Location**: `test_plan.jmx`  
**Steps**:
1. Open **Apache JMeter** (`jmeter.bat` on Windows, `jmeter` on macOS/Linux).
2. Load `test_plan.jmx` and run the test.
3. View results in the **Results Tree** panel.

---

### **2️⃣ Locust**
**Location**: `locustfile.py`  
**Steps**:
1. Install dependencies:  
   ```sh
   pip install -r locust/requirements.txt
   ```
2. Start Flask API (if testing locally):  
   ```sh
   python locust/app.py
   ```
3. Run Locust:  
   ```sh
   locust -f locust/locustfile.py
   ```
4. Open **http://localhost:8089** in your browser to monitor test results.

---

### **3️⃣ k6**
**Location**: `load_test.js`  
**Steps**:
1. Install **k6** (if not installed):  
   ```sh
   brew install k6  # macOS
   choco install k6  # Windows
   ```
2. Run the test:  
   ```sh
   k6 run k6/load_test.js
   ```
3. View results in the terminal.

---

## **📊 When to Use Which Tool?**
| Tool   | Best For |
|--------|----------|
| **JMeter** | GUI-based testing, large-scale scenarios |
| **Locust** | Python-based, real user simulation, Web UI |
| **k6** | CLI-based, lightweight, CI/CD integration |

This repository provides **multiple load testing options** so you can choose the right tool based on your use case.
