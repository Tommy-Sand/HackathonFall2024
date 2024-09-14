from django.test import TestCase, Client
from django.urls import reverse
from .models import User, Job, JobApplication
import json

class JobApplicationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(name="Moeid", resume="Moeid's resume")
        self.job = Job.objects.create(company_name="uofa", position="comp sci", description="A great job")
        self.url = reverse('apply', args=[self.job.id, self.user.name])

    def test_apply_to_job_success(self):
        response = self.client.post(self.url, data=json.dumps({
            'send_date': '2024-09-15T12:00:00Z',
            'interview_date': '2024-09-20T12:00:00Z',
            'accept_date': '2024-09-25T12:00:00Z',
            'status': 'I',
            'resume': 'My resume content...'
        }), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.content)
        self.assertEqual(response_data['message'], f"Applied to job {self.job.id} successfully.")
        self.assertIn('application', response_data)
        self.assertEqual(response_data['application']['user'], self.user.name)
        self.assertEqual(response_data['application']['job'], self.job.id)