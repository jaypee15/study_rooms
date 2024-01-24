<div align="center">
<img width="30%" src="https://github.com/jaypee15/study_rooms/blob/master/static/images/study-rooms.png?raw=true">

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
<img src="https://github.com/jaypee15/study_rooms/blob/master/static/images/feed-home.png?raw=true">
</td> 
<td width="50%">
<br>
<p align="center">
  Room Conversation Preview
</p>
<img src="https://github.com/jaypee15/study_rooms/blob/master/static/images/room-conversation.png?raw=true">  
</td>
</table>

