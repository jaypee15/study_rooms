from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase
from rooms.models import Room, Topic, Message
from django.utils import timezone
from django.urls import reverse
import time

User = get_user_model()


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@email.com", password="testpassword"
        )
        self.user2 = get_user_model().objects.create_user(
            username="testuser2", email="testuser2@email.com", password="testpassword2"
        )

        self.topic = Topic.objects.create(name="Test Topic")
        self.room = Room.objects.create(
            host=self.user,
            topic=self.topic,
            name="Test Room",
            description="Test Room Description",
        )
        self.room.participants.set([self.user, self.user2])

        self.message = Message.objects.create(
            user=self.user, room=self.room, body="Test Message Body"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@email.com")
        self.assertEqual(self.user.bio, None)
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(isinstance(self.user, User))

    def test_password_hashing(self):
        self.assertNotEqual(self.user.password, "testpassword")
        self.assertTrue(self.user.check_password("testpassword"))

    def test_change_password(self):
       # Change the user's password and ensure it's hashed
        new_password = 'newtestpassword'
        self.user.set_password(new_password)
        self.user.save()

        # Ensure the new password is hashed
        self.assertNotEqual(self.user.password, new_password)
        self.assertTrue(self.user.check_password(new_password))

    def test_authenticate(self):
       # Test with correct password
        self.assertIsNotNone(authenticate(username="testuser", password="testpassword"))

        # Test with incorrect password
        self.assertIsNone(authenticate(username="testuser", password="wrongpassword"))

    def test_topic_creation(self):
        self.assertEqual(self.topic.name, "Test Topic")
        self.assertTrue(isinstance(self.topic, Topic))

    def test_topic_string_representation(self):
        expected_str = "Test Topic"
        self.assertEqual(str(self.topic), expected_str)

    def test_room_creation(self):
        self.assertEqual(self.room.host, self.user)
        self.assertEqual(self.room.topic, self.topic)
        self.assertEqual(self.room.name, "Test Room")
        self.assertEqual(self.room.description, "Test Room Description")
        self.assertTrue(isinstance(self.room, Room))
        self.assertEqual(list(self.room.participants.all()), [self.user, self.user2])
        self.assertEqual(list(self.user.participants.all()), [self.room])
        self.assertEqual(list(self.topic.room_set.all()), [self.room])


        # Test the created and updated timestamps
        self.assertIsNotNone(self.room.created)
        self.assertIsNotNone(self.room.updated)
        self.assertEqual(self.room.created, self.room.updated)

        # Update the room name
        original_updated = self.room.updated
        time.sleep(0.1)
        self.room.name = "Updated Room Name"
        self.room.save()
        self.assertEqual(self.room.name, "Updated Room Name")

        # Check if the updated field is modified
        self.assertGreater(self.room.updated, original_updated)

    def test_room_string_representation(self):
        expected_str = "Test Room"
        self.assertEqual(str(self.room), expected_str)

    def test_message_creation(self):
        self.assertEqual(self.message.user, self.user)
        self.assertEqual(self.message.room, self.room)
        self.assertEqual(self.message.body, "Test Message Body")
        self.assertTrue(isinstance(self.message, Message))

        # Test the created and updated timestamps
        self.assertIsNotNone(self.message.created)
        self.assertIsNotNone(self.message.updated)
        self.assertEqual(self.message.created, self.message.updated)

        # Update the message body
        original_updated = self.message.updated
        time.sleep(0.1)
        self.message.body = "Updated Message Body"
        self.message.save()

        self.assertEqual(self.message.body, "Updated Message Body")

        # Check if the updated field is modified
        self.assertGreater(self.message.updated, original_updated)

    def test_message_string_representation(self):
        expected_str = "Test Message Body"
        self.assertEqual(str(self.message), expected_str)
