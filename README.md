Overview

This project is a Django REST Framework (DRF) API for managing company data including employees, departments, attendance, and performance.
It demonstrates core backend concepts such as CRUD operations, token-based authentication, and Swagger documentation for easy API testing.

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/ayah692/employee-api.git
cd employee-api

2️⃣ Create and Activate a Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup Environment Variables
cp .env.example .env

5️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Seed the Database (create admin + sample data)
python manage.py seed_data

7️⃣ Run the Development Server
python manage.py runserver


Once the server starts, visit:
👉 Swagger UI: http://127.0.0.1:8000/swagger/

🧾 Usage
🔐 Get Authentication Token
curl -X POST http://127.0.0.1:8000/api-token-auth/ \
-H "Content-Type: application/json" \
-d '{"username":"admin","password":"adminpass"}'


You’ll receive a token like this:

{"token": "your_token_here"}


Use it in your API requests:

Authorization: Token your_token_here

📡 Example Endpoints
Method	Endpoint	Description
GET	/api/employees/	List employees
POST	/api/employees/	Create employee
GET	/api/departments/	List departments
POST	/api/departments/	Create department
GET	/api/attendance/	View attendance
GET	/api/performance/	View performance
💡 Technologies Used

Python 3

Django 5

Django REST Framework (DRF)

drf-yasg (Swagger UI)

SQLite (default database)
