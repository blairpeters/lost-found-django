
# Lost & Found - Django Web Application

## 1. Project Overview

Lost & Found is a web-based application built with Django that allows users to report lost and found items.

The platform provides a centralized place where users can post information about items they have lost or found, view details of items posted by others, and contact the respective item owners to facilitate recovery.

The application uses authentication and role-based access control to ensure that users can only perform actions they are authorized to perform.

## 2. Features

### User Authentication
- Users must log in to access the application.
- New users can register for an account if they do not already have one.
- Unauthenticated users are redirected to the login page.
- Authenticated users can log out of their accounts.

### Posting Lost and Found Items
Logged-in users can post items by completing a form containing the following fields:

| Field | Description |
|---|---|
| Title | Name or title of the lost/found item |
| Description | Detailed description of the item |
| Picture | An image of the item (optional) |
| Status | Select whether the item is Lost, Found or claimed |
| Location | Where the item was lost or found |
| Contact | Contact information for reaching the person who posted the item |

### Viewing Items
- Users can view all items posted on the platform.
- Items are displayed in a card layout.
- Each card displays the item's title, category, status, location and picture (if available).
- Users can click the **View Details** button to access more information about a particular item.

### Editing Items
- Users can only edit items that they have personally posted.
- The Edit Item button is only displayed to the owner of an item.
- Django backend validation ensures that users cannot edit items belonging to other users.

### Deleting Items
- Only superusers have permission to delete items.
- Normal users cannot delete items, regardless of whether they posted them.
- A confirmation message is displayed before an item is permanently deleted.
- Deletion is handled through a POST request with CSRF protection.

## 3. Technologies Used

- Python
- Django
- SQLite3
- HTML5
- CSS3
- Bootstrap 5
- Django Authentication System

## 4. Project Setup and Installation

Follow these steps to clone the repository and run the project locally.

### Step 1: Clone the Repository

Open your terminal and run:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project directory:

```bash
cd lost_and_found
```

### Step 2: Create a Virtual Environment

Create an isolated Python environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### Step 3: Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### Step 4: Apply Database Migrations

Run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates and updates the database tables required by the application.

### Step 5: Create a Superuser

To access administrative features, create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to provide a username, email address and password.

Only this superuser account will have permission to delete items through the application.

### Step 6: Start the Development Server

Run:

```bash
python manage.py runserver
```

Open your browser and visit:

http://127.0.0.1:8000/

You can also access the Django administration panel at:

http://127.0.0.1:8000/admin/

## 5. How the Application Works

The application follows this general workflow:

1. A user visits the Lost & Found platform.
2. If the user is not authenticated, they must register or log in.
3. Once authenticated, the user can browse items posted by other users.
4. A user can post a lost or found item by completing the item submission form.
5. The newly posted item appears on the homepage.
6. Users can select **View Details** to see the full information about an item, including its description and contact details.
7. The person who posted an item can edit their own listing.
8. Only a superuser can delete an item.

## 6. Access Control and Permissions

The application implements ownership-based access control and superuser privileges.

| Action | Normal User | Superuser |
|---|---|---|
| View items | Yes | Yes |
| Post an item | Yes | Yes |
| View item details | Yes | Yes |
| Edit own items | Yes | Yes |
| Edit another user's items | No | No |
| Delete items | No | Yes |

## 7. Important Notes

- A user must be authenticated before accessing the application.
- Each item is associated with the user who posted it.
- Users cannot edit listings belonging to other users.
- Only superusers can delete listings.
- The application uses SQLite as its default development database.
- Uploaded images require the appropriate Django media configuration.
- The Django development server is intended for local development and testing, not production deployment.

## 8. Future Improvements

Potential improvements include:

- Search and filter functionality.
- Item category filtering.
- Email notifications when an item is reported.
- Pagination for item listings.
- Improved user profiles.
- Automated matching of lost and found items.



**Developed using Django, Python and Bootstrap.**
