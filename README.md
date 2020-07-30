# izzi
 Test task for IZZI interview

## Requirements
* Python 3

## Running it locally

#### Step 1. Create a new environment.
```
python3 -m venv venv

source venv/bin/activate
```

#### Step 2. Install requirements.
```
python -m pip install -r requirements.txt
```

#### Step 3: Create a database structure
```
python manage.py migrate
```

#### Step 4: Create superuser
```
python manage.py createsuperuser
```

#### Step 5: Run dev server
```
python manage.py runserver
```

## Usage

#### Step 1. Import users from [TestData.csv](TestData.csv).

Go to [**admin panel**](http://127.0.0.1:8000/admin) and log in with your superuser credentials.

Then go to [**Upload File page**](http://127.0.0.1:8000/admin/app/uploadfile/add/) and import `TestData.csv`. Click `Save`

To check is everything going well, go to [**Users page**](http://127.0.0.1:8000/admin/app/user/) and make sure that all users are imported.


#### Step 2. API with users' info.

You can use Postman or your default browser.

To see **all users**, make a GET request to `http://127.0.0.1:8000/users/`. 

**[Link of example with all users.](http://127.0.0.1:8000/users/)**

Also, you can make a request with **a certain date** in `date` param.
To try it, you visit **[this link](http://127.0.0.1:8000/users/?date=2018-05-16)**.

And you could get users with registration dates **between**, **before** or **after** a certain date.

Here are examples:
- [Users with registration **after 2018-05-13**](http://127.0.0.1:8000/users/?datefrom=2018-05-13)
- [Users with registration **before 2018-05-15**](http://127.0.0.1:8000/users/?dateto=2018-05-15)
- [Users with registration **after 2018-05-13 and before 2018-05-15**](http://127.0.0.1:8000/users/?dateto=2018-05-15&datefrom=2018-05-13)
