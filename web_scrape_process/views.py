from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
from .stores.SephoraScrapper import SephoraScrapper
import multiprocessing
import time
from products.models import Product
from django.contrib.auth import get_user_model 
# Create your views here.

def processURL(url):
    scrapperObject = SephoraScrapper()
    scrapperObject.openWindow(url)
    review = scrapperObject.getReviews()
    scrapperObject.closeWindow()

    return review


class GetInfoFromURL(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        User = get_user_model()
        body = json.loads(request.body)
        print(body)
        url = body["url"]
        user_mail = body["email"]
        productInfoDict, similarProductsList = [], []

        try:
            scrapperObject = SephoraScrapper()
            scrapperObject.openWindow(url)
            productInfoDict = scrapperObject.getProductInfo()
            similarProductsList = scrapperObject.getSimilarProducts()
            scrapperObject.closeWindow()
        except:
            scrapperObject.closeWindow()
            return Response(status=400, data={
                'message': 'Error in processing data.'
            })
        Product.objects.create(
            name=productInfoDict["Product Name"],
            user=User.objects.get(email=user_mail),
            brand=productInfoDict["Brand Name"],
            #images=productInfoDict["Image Links"],
            rating=productInfoDict["Avg Rating"],
            reviews=productInfoDict["No of Reviews"],
            likes=productInfoDict["Likes"],
            size=productInfoDict["Size"],
            quantity=productInfoDict["Quantity"],
            cost=productInfoDict["Cost"]
        )
        return Response({
            'productInfo': productInfoDict,
            'similarProducts': similarProductsList
        })

class GetReviewFromURLs(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        body = json.loads(request.body)
        urls = body["urls"]
        outputs = []

        try:
            pool = multiprocessing.Pool()
            pool = multiprocessing.Pool(processes=10)
            outputs = pool.map(processURL, urls)
        except:
            return Response(status=400, data={
                'message': 'Error in processing data.'
            })

        return Response({
            "reviewList": outputs
        })