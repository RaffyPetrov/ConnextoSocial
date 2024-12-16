roject Setup

Follow the steps below to set up the project locally:
1. Clone the Repo

First, clone the repository to your local machine:

git clone https://github.com/RaffyPetrov/ConnextoSocial.git

2. Open the Project Directory

Navigate to the project folder:

cd your-repo-name

3. Install Dependencies

Install the required dependencies using pip:

pip install -r requirements.txt

4. Update Database Settings

Update the database configuration in the settings.py file. Modify the DATABASES setting with your PostgreSQL credentials:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "your_db_name",
        "USER": "your_username",
        "PASSWORD": "your_password",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

5. Run Migrations

Apply the database migrations to set up your database schema:

python manage.py migrate

6. Run the Project Locally

Start the Django development server to run the project:

python manage.py runserver

Once the server is running, you can access the project by navigating to http://127.0.0.1:8000/ in your browser.
