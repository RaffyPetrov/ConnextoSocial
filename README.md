**Project Setup**

**1. Clone the repo**

  git clone https://github.com/RaffyPetrov/ConnextoSocial.git

**2. Open the project**

**3. Install dependencies**

**pip install -r requirements.txt**

**4. Change DB settings in settings.py**

  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql",
          "NAME": "your_db_name",
          "USER": "your_username",
          "PASSWORD": "your_pass",
          "HOST": "127.0.0.1",
          "PORT": "5432",
      }
  }

  5. Run the migrations

python manage.py migrate

**6. Run the project**

python manage.py runserver
