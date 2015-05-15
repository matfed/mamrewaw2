from django.test import TestCase
from models import *
from datetime import datetime

# Create your tests here.
class FileNamesTest(TestCase):
    def test_recording_content_file_name(self):
        set = RecordingSet.objects.create(title="set", date=datetime.strptime("2015-03-01", "%Y-%m-%d"))
        recording = Recording.objects.create(title="title", content="content", type="type", set=set)
        self.assertEqual(recording_content_file_name(recording, 'name.mp3'), 'blog/recordings/20150301/title.mp3')

    def test_recording_content_file_name(self):
        post = Post.objects.create(
            title="title", 
            date=datetime.strptime("2015-03-01", "%Y-%m-%d"),
            img="img",
            lead="lead",
            text="text")

        self.assertEqual(post_img_file_name(post, 'name.jpg'), 'blog/photos/1/main.jpg')