from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from rooms.models import Room, Topic, Message
import random
from faker import Faker

fake = Faker()
User = get_user_model()


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        # Create 10 users
        users = []
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="password123"
            )
            users.append(user)

        # Create 15 topics
        topics = [Topic.objects.create(name=fake.word()) for _ in range(15)]

        # Create 20 rooms with random topics and users
        rooms = []
        for _ in range(20):
            room = Room.objects.create(
                host=random.choice(users),
                topic=random.choice(topics),
                name=fake.sentence(nb_words=3),
                description=fake.paragraph()
            )
            room.participants.set(random.sample(users, random.randint(1, 10)))
            rooms.append(room)

        # Create random messages for each room
        for room in rooms:
            for _ in range(random.randint(5, 25)):
                Message.objects.create(
                    user=random.choice(users),
                    room=room,
                    body=fake.text()
                )

        print('Successfully populated the database.')
