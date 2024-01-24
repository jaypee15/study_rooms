<div align="center">
<img width="30%" src="https://user-images.githubusercontent.com/72341453/134747028-7e2d90cc-a92f-4f66-815e-54a0d50cca54.PNG">

# Study Rooms
</div>

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/jaypee15/StudyBud.git

```

--> Move into the directory where we have the project files : 
```bash
cd StudyBud

```

--> Create a virtual environment.:
```bash
# Create virtual env first
python -m venv .venv

```

--> Activate the virtual environment :
```bash
.venv\scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

--> Run Migrations
```
Python manage.py migrate

```
--> To add mock data using the faker library
```
# Run the populate.py manage.py command
python manage.py populate

```
--> Run Tests using coverage
```
coverage run manage.py test rooms

```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```


> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Feed Home
</p>
<img src="https://user-images.githubusercontent.com/72341453/134747262-0a92233d-8010-40f8-84c5-8d94895aac44.PNG">
</td> 
<td width="50%">
<br>
<p align="center">
  Room Conversation Preview
</p>
<img src="https://user-images.githubusercontent.com/72341453/134747155-3ca5b55f-b064-4741-aeae-abe90bddf41e.PNG">  
</td>
</table>

