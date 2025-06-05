# 📝 Taskly - Advanced To-Do List App

Taskly is a modern, full-featured to-do list web application built with **Python Django**.  
It helps users manage tasks efficiently with category labels, status tracking, deadlines, and a stylish UI.


## 🚀 Features

- 🗂️ Create, edit, and delete tasks
- 🔄 Mark tasks as `Incomplete`, `Ongoing`, or `Completed`
- 📅 Set task due dates and view them clearly
- 📊 Dashboard with:
  - Summary cards (Total, Completed, Pending)
  - Progress bar
  - Category breakdown
  - High priority highlights
  - Recent activity
- 🏷️ Label tasks by categories (e.g., Work, Personal, Urgent)
- 🌙 Dark mode toggle (optional)
- 🎨 Fully customized UI using modern CSS styles and hover effects
- 📦 Session-based user system for task isolation (optional authentication can be added)

---

## 📂 Project Structure

Taskly/
├── taskly/ # Main Django project settings
│ └── settings.py # Configurations
├── todo/ # Core app for task management
│ ├── models.py # Task and Category models
│ ├── views.py # All views
│ ├── templates/ # HTML templates
│ └── static/ # CSS, JS, and images
├── manage.py
└── README.md # You're here!


## ⚙️ Setup Instructions

Follow these steps to run Taskly locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Nalgirkar123/Taskly.git
cd Taskly
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
