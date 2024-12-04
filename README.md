# ConnextoSocial
This is my social media website for car enthusiasts.
Project setup
1. Clone the repo


  git clone https://github.com/RaffyPetrov/ConnextoSocial.git

2. Open the project
3. Install dependencies


  pip install -r requirements.txt

4. Change DB settings in settings.py

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "connextosocial",
        "USER": "postgres",
        "PASSWORD": "SPn6C01w'*9/",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

5. Run the migrations


  python manage.py migrate

6. Run the project


  python manage.py runserver

