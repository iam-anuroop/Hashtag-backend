from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SocialMediaPost
import re
from collections import Counter
from datetime import datetime
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils import timezone

 
class ManageHashtags(APIView):
    @swagger_auto_schema(
        tags=["Get top Hashtag"],
        operation_description="Takes two parameter start,end dates and return the most used hashtags btween the dates",
        responses={200: "success", 400: "errors"},
        manual_parameters=[
            openapi.Parameter(
                'start_date',
                openapi.IN_QUERY,
                description='Start date (YYYY-MM-DD)',
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
            ),
            openapi.Parameter(
                'end_date',
                openapi.IN_QUERY,
                description='End date (YYYY-MM-DD)',
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
            ),
        ],
    )
    def get(self,request):
        try:
            start_date = request.query_params.get('start_date')
            end_date = request.query_params.get('end_date')
            start_date = timezone.make_aware(datetime.strptime(start_date, "%Y-%m-%d"))
            end_date = timezone.make_aware(datetime.strptime(end_date, "%Y-%m-%d"))
            posts = SocialMediaPost.objects.filter(dateTime__range=(start_date, end_date))

            count_hashtag = Counter()
            for post in posts:
                hashtags = re.findall(r'#\w+', post.content)
                count_hashtag.update(hashtags)
            top_hashtags = count_hashtag.most_common(5)
            return Response({"top_hashtags": top_hashtags},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg":"something went wrong"},status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
