A simple To-Do List Web Application built using Django, Python, and HTML/CSS, designed to help users manage their daily tasks efficiently. The application allows users to add new tasks, update existing ones, mark them as completed, and delete them once finished. It also includes a basic user authentication system so each user can maintain their own task list securely.
🚀 Features

➕ Add new tasks with title and description

✏️ Edit and update tasks

✅ Mark tasks as completed

❌ Delete tasks once finished

🔐 User authentication (secure login/logout)

🗂️ Separate task lists for each user

# Clone the repository  
git clone https://github.com/your-username/todo-list-django.git  

# Navigate to the project folder  
cd todo-list-django  

# Create virtual environment & activate  
python -m venv venv  
source venv/bin/activate   # Linux/Mac  
venv\Scripts\activate      # Windows  

# Install dependencies  
pip install -r requirements.txt  

# Apply migrations  
python manage.py migrate  

# Create superuser (optional for admin access)  
python manage.py createsuperuser  

# Run the server  
python manage.py runserver  
