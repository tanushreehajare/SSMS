# 📚 Somaiya Stationary Management System (SSMS)

A robust Django-powered web application revolutionizing stationary requisition and distribution for educational institutions — built specifically for KJSIT AI&DS department. SSMS bridges the gap between administrators and faculty, ensuring seamless, transparent, and efficient stationary management.

---

## 🚀 Features

- 📝 **Faculty Portal**
  - Request stationary items directly
  - Track past requisitions and assigned items
  - Profile dashboard with transparent history

- 🛠️ **Admin Panel**
  - Manage faculty profiles and roles
  - Track stationary availability in real-time
  - Assign items with date, recipient, and quantity logs
  - Store bills and generate custom reports

- 📊 **Reports & Insights**
  - Generate data-driven reports on usage trends and allocations
  - Visualize consumption patterns for informed decision-making
  - Support for tailored parameters to refine analysis

---

## 🛠️ Tech Stack

| Frontend | Backend | Database |
|----------|---------|----------|
| HTML/CSS | Django  | SQLite   |

---

## 📸 Screenshots  
> ![Dashboard Screenshot](link-to-image)  
> ![Report Generation](link-to-image)

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/SSMS.git

# Navigate to project directory
cd SSMS

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
