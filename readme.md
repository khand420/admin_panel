# Django Admin Panel

## Overview
This project is a basic administrative panel built using Django. It includes functionalities for user authentication, a dashboard, and partner management.

## Features
- **Admin Login**: Secure login for admin users with authentication.
- **Dashboard**: Overview of the system status and recent activities.
- **Partner Management**:
  - Listing of partners with search/filter functionality.
  - Add new partners with input validation.
  - Edit partner details.
  - View detailed information for individual partners.

## Requirements
- Python 3.x
- Django 3.x or later

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/khand420/admin_panel.git
   cd admin_panel
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install django
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8000/login/` to access the login page.

   - username admin
   - password 123

## Usage
- Log in with your admin credentials.
- Navigate through the dashboard to manage partners.

## Contributing
If you wish to contribute, please fork the repository and submit a pull request.