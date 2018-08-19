from tests import BaseTestCase

import json

from flask import jsonify

class RequestTestmodels(BaseTestCase):
    def test_get_all_questions(self):
        response=self.test_client.post(
        '/api/v1/questions', data= json.dumps(self.request_data),content_type='application/json')
        response=self.test_client.get(
            '/api/v1/questions', data=json.dumps(self.request_data),content_type='application/json'
        )
        self.assertEqual(response.status_code,200)
        
    def test_get_a_question(self):
        response=self.test_client.post(
            '/api/v1/questions', data=json.dumps(self.request_data), content_type='application/json')
        response=self.test_client.get(
            '/api/v1/question/1', content_type='application/json'
        )
        self.assertEqual(response.status_code,404)

    def test_add_a_question(self):
        response=self.test_client.post(
            '/api/v1/questions', data = json.dumps(self.request_data),content_type='application/json')
        self.assertEqual(response.status_code,200)
        self.assertIn(
            "Hello Rhytah! Question successfully added", str(response.data)
        )

    def test_add_an_answer(self):
        
        response=self.test_client.post(
            '/api/v1/questions/1/answers', data = json.dumps(self.request_data),content_type='application/json')
        self.assertEqual(response.status_code,200)
        self.assertIn(
            'Great job! answer added to question 1', str(response.data)
        )

