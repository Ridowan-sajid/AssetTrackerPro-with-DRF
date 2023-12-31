from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, GadgetUser, Gadget
from .serializers import CompanySerializer, GadgetUserSerializer, GadgetSerializer

# Company
# There are 3 feature:
# 1. Company creation
# 2. Company Login
# 3. Company Logout

class CompanyCreate(GenericAPIView,CreateModelMixin):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class CompanyLogin(APIView):
    def post(self,request):
        company_code=request.data.get("company_code")
        company = Company.objects.get(company_code=company_code)

        if company is not None:
            request.session['authenticated_company_id'] = company.id
            return Response({"message":"Login Successful"},status=status.HTTP_200_OK)
        else:
            return Response({"message":"Invalid Username Or Password"},status=status.HTTP_401_UNAUTHORIZED)

class CompanyLogout(APIView):
    def get(self, request):
        if 'authenticated_company_id' in request.session:
            del request.session['authenticated_company_id']
        return Response({"message": "Logged out"}, status=status.HTTP_200_OK)



# Gadget User
# There are 6 feature:
# 1. User Creation
# 2. Get User List
# 3. Delete User
# 4. Update User
# 5. Retrieve individual user
# 6. Delete any User

# All this action can be done by Company after logged in by company_code

class UserCreateList(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = GadgetUser.objects.all()
    serializer_class = GadgetUserSerializer

    def post(self,request,*args,**kwargs):
        authenticated_company_id = request.session.get('authenticated_company_id')
        company_instance = Company.objects.get(pk=authenticated_company_id)
        serializer = self.get_serializer(data=request.data)
        print(company_instance)
        if authenticated_company_id:
            if serializer.is_valid():
                serializer.validated_data['company'] = company_instance
                print(serializer)
                serializer.save()
                return Response({'message': 'Created successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'You have given some invalid data'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'message': 'You are not authorized.'}, status=status.HTTP_403_FORBIDDEN)

    def get(self,request,*args,**kwargs):
        authenticated_company_id = request.session.get('authenticated_company_id')
        if authenticated_company_id:
            return self.list(request, *args, **kwargs)
        else:
            return Response({'message': 'You are not authorized.'}, status=status.HTTP_403_FORBIDDEN)


class UserDeleteUpdateRetrieve(GenericAPIView,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin):
    queryset = GadgetUser.objects.all()
    serializer_class = GadgetUserSerializer

    def get(self,request,*args,**kwargs):
        authenticated_company_id = request.session.get('authenticated_company_id')
        if authenticated_company_id:
            return self.retrieve(request, *args, **kwargs)
        else:
            return Response({'message': 'You are not authorized.'}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, *args, **kwargs):
        authenticated_company_id = request.session.get('authenticated_company_id')
        if authenticated_company_id:
            return self.update(request, *args, **kwargs)
        else:
            return Response({'message': 'You are not authorized.'}, status=status.HTTP_403_FORBIDDEN)


    def delete(self, request, *args, **kwargs):
        authenticated_company_id = request.session.get('authenticated_company_id')
        if authenticated_company_id:
            return self.destroy(request, *args, **kwargs)
        else:
            return Response({'message': 'You are not authorized.'}, status=status.HTTP_403_FORBIDDEN)

# Gadget
# There are 6 feature:
# 1. Gadget Creation
# 2. Get Gadget List
# 3. Delete Gadget
# 4. Update Gadget
# 5. Retrieve individual Gadget
# 6. Delete any Gadget

# All this action can be done by Company after logged in by company_code

class GadgetCreateList(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer

    def post(self,request,*args,**kwargs):
        authenticated_company_id = request.session.get('authenticated_company_id')
        if authenticated_company_id:
            return self.create(request, *args, **kwargs)
        else:
            return Response({'message': 'You are not authorized.'}, status=status.HTTP_403_FORBIDDEN)


    def get(self,request,*args,**kwargs):
        authenticated_company_id = request.session.get('authenticated_company_id')
        if authenticated_company_id:
            return self.list(request, *args, **kwargs)
        else:
            return Response({'message': 'You are not authorized.'}, status=status.HTTP_403_FORBIDDEN)


class GadgetDeleteUpdateRetrieve(GenericAPIView,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin):
    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer

    def get(self,request,*args,**kwargs):
        authenticated_company_id = request.session.get('authenticated_company_id')
        if authenticated_company_id:
            return self.retrieve(request, *args, **kwargs)
        else:
            return Response({'message': 'You are not authorized.'}, status=status.HTTP_403_FORBIDDEN)


    def put(self, request, *args, **kwargs):
        authenticated_company_id = request.session.get('authenticated_company_id')
        if authenticated_company_id:
            return self.update(request, *args, **kwargs)
        else:
            return Response({'message': 'You are not authorized.'}, status=status.HTTP_403_FORBIDDEN)


    def delete(self, request, *args, **kwargs):
        authenticated_company_id = request.session.get('authenticated_company_id')
        if authenticated_company_id:
            return self.destroy(request, *args, **kwargs)
        else:
            return Response({'message': 'You are not authorized.'}, status=status.HTTP_403_FORBIDDEN)

# To use this application a company first have to register their self with company title, and a secret
# company_code which will be used for login. After register company can logged In by that company_code.
# After logged In company can create as many user as the company wants. After that The company can
# update, delete or retrieve any user from database. And after creating user the company can
# assign one or multiple gadget with relevant information of that gadget to any user and company
# can set a time for using that gadget. So, that company can see the checked out and return time.
# Company can update, delete and retrieve any gadget info from database.

# I used company based on models not based on user though I can create company based on user and can use
# the django's default authentication but in my opinion it seems company and user are quite different.
# And Company is being authenticated based on session
# After logged In a session will be created for that company. If the company logged out session will be
# destroyed.

# I used postgreSQL for database. Because sqlite3 is not suitable or reliable for bigger project.

