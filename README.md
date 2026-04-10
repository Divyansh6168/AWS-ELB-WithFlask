# 🚀 AWS ELB with Flask (Load Balancing Demo)

## 📌 Project Overview
This project demonstrates deploying a Python Flask application on multiple AWS EC2 instances and distributing traffic using an Elastic Load Balancer (ELB).

---

## 🧠 Architecture

User → ELB → EC2 Instances (Flask Apps)

---

## 🛠️ Tech Stack
- Python (Flask)
- AWS EC2
- AWS Elastic Load Balancer (ELB)
- GitHub

---

## ⚙️ Steps Performed

### 1. Create Flask App
```python
from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from {socket.gethostname()}"

app.run(host="0.0.0.0", port=5000)
```

---

### 2. Launch EC2 Instances
- Created 2 EC2 instances
- Enabled ports: 22, 80, 5000

---

### 3. Setup Environment
```bash
sudo yum update -y
sudo yum install python3 -y
pip3 install flask
```

---

### 4. Run Flask App
```bash
python3 app.py
```

---

### 5. Create Target Group
- Protocol: HTTP
- Port: 5000
- Added both EC2 instances

---

### 6. Create Load Balancer
- Type: Application Load Balancer
- Listener: HTTP (80)
- Attached Target Group

---

### 7. Access ELB
Open:
http://<ELB-DNS>

Refresh to see traffic routed across instances.

---

## 🎯 Outcome
- Successfully implemented load balancing
- Traffic distributed across EC2 instances
- Basic fault tolerance achieved

---

## 🚀 Future Improvements
- Auto Scaling Group
- HTTPS
- Docker
- CI/CD

---

## 👨‍💻 Author
Divyansh Rawat
