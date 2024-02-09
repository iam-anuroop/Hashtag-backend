from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class SocialMediaPostAPITestCase(APITestCase):

    def test_get_top_hashtags(self):
        start_date = '2022-01-01'
        end_date = '2022-12-31'

        url = reverse('hashtag')  
        response = self.client.get(url, {'start_date': start_date, 'end_date': end_date})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('top_hashtags' in response.data)

        # expected_result = [
        #     '#AdvoNinja247',
        #     '#HR184',
        #     '#HumanResources113',
        #     '#Follow80',
        #     '#EmployeeFeedback42',
        # ]

        # actual_result = [data[0] for data in response.data.get('top_hashtags', [])]

        # self.assertEqual(actual_result, expected_result)

