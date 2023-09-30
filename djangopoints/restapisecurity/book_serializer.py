
from rest_framework.serializers import ModelSerializer
from restapisecurity.models import Book

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'         #all
        #fields = ('id','price','name','qty','publication','author')    #only these
        #exclude = ('id','price') #except these