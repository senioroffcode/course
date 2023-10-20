from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_200_OK

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create_direction(request):
     user = request.user
     if user.status in [2, 4]:
          direction = Direction.objects.create(
               name=request.POST.get('name'),
               duration = request.POST.get('duration'),
               payment  = request.POST.get('payment'),
          )
          data = {
             "Direction": DirectionSerializer(direction).data,
              "success":True
         }
     else:
          data = {
               "success": False,
               "message": "You do`nt have permission to do this"
          }

     return Response(data, status=HTTP_201_CREATED )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_direction(request):
     direction = Direction.objects.all()
     serialized_data = DirectionSerializer(direction, many=True).data
     return Response(serialized_data, status=HTTP_200_OK)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def change_direction(request):
     user = request.user
     if user.status in [2, 4]:
          name = request.POST.get('name'),
          duration = request.POST.get('duration'),
          payment = request.POST.get('payment'),
          direction = Direction.objects.get(id=pk),
          if name is not None:
               direction.name = name
          if duration is not None:
               direction.duration = duration
          if payment is not None:
               direction.payment = payment
          direction.save()
          serialized_data = DirectionSerializer(direction).data
          direction = Direction.objects.create(
               name=request.POST.get('name'),
               duration=request.POST.get('duration'),
               payment=request.POST.get('payment'),
          )
          data = {
               "Direction": DirectionSerializer(direction).data,
               "success": True
          }
     else:
          data = {
               "success": False,
               "message": "You do`nt have permission to do this"
          }

     return Response(data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def delete_direction(request, pk):
     Direction.objects.all(id=pk).delete()
     return Response(
          status=HTTP_204_NO_CONTENT
     )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create_student(request):
     name = request.name
     if name.status in [2, 5]:
          student = Student.objects.create(
               status=request.POST.get('status'),
               full_name=request.POST.get('full_name'),
               phone=request.POST.get('phone'),
               extra_phone=request.POST.get('extra_phone'),
               region=request.POST.get('region'),
               address=request.POST.get('address'),
               created_at=request.POST.get('created_at'),
               debt=request.POST.get('debt'),
          )
          data = {
               "Student": StudentSerializer(student).data,
               "success": True
          }
     else:
          data = {
               "success": False,
               "message": "ERROR!"
          }

     return Response(data, status=HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_students(request):
     student = Student.objects.all()
     serialized_data = (student).data
     return Response(serialized_data, status=HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_student(request):
     students = Students.objects.all()
     serialized_data = (students).data
     return Response(serialized_data, status=HTTP_200_OK)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def change_student(request):
          name = request.name
          if name.status in [3, 6]:
               status = request.POST.get('status'),
               full_name = request.POST.get('full_name'),
               phone = request.POST.get('phone'),
               extra_phone = request.POST.get('extra_phone'),
               region = request.POST.get('region'),
               address = request.POST.get('address'),
               created_at = request.POST.get('created_at'),
               debt = request.POST.get('debt'),
               student = Student.objects.get(id=pk),
               if status is not None:
                    Student.status = status
               if full_name is not None:
                    Student.full_name = full_name
               if phone is not None:
                    Student.phone = phone
               if extra_phone is not None:
                    Student.extra_phone = extra_phone
               if region is not None:
                    Student.region = region
               if address is not None:
                    Student.address = address
               if created_at is not None:
                    Student.created_at = created_at
               if debt is not None:
                    Student.debt = debt
               student.save()
               serialized_data = StudentSerializers(direction).data
               student = Student.objects.create(
                    full_name=request.POST.get('full_name'),
                    phone=request.POST.get('phone'),
                    extra_phone=request.POST.get('extra_phone'),
                    region=request.POST.get('region'),
                    address=request.POST.get('address'),
                    created_at=request.POST.get('created_at'),
                    debt=request.POST.get('debt'),
               )
               data = {
                    "Student": StudentSerializers(student).data,
                    "success": True
               }
          else:
               data = {
                    "success": False,
                    "message": "ERROR!"
               }

          return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create_group(request):
     user = request.user
     if user.status in [1, 4]:
          group = Group.objects.create(
               status=request.POST.get('direction'),
               full_name=request.POST.get('mentor'),
               phone=request.POST.get('students'),
               created_at=request.POST.get('created_at'),
          )
          data = {
               "Group": GroupSerializers(group).data,
               "success": True
          }
     else:
          data = {
               "success": False,
               "message": "ERROR!"
          }

     return Response(data, status=HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_groups(request):
     groups = Groups.objects.all()
     serialized_data = (groups).data
     return Response(serialized_data, status=HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_group(request):
     group = Group.objects.all()
     serialized_data = (group).data
     return Response(serialized_data, status=HTTP_200_OK)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def change_group(request):
     users = request.users
     if users.status in [3, 6]:
          direction = request.POST.get('direction'),
          mentor = request.POST.get('mentor'),
          students = request.POST.get('students'),
          created_at = request.POST.get('created_at'),
          group = Group.objects.get(id=pk),
          if status is not None:
               Group.direction = status
          if full_name is not None:
               Group.mentor = full_name
          if phone is not None:
               Group.students = phone
          if created_at is not None:
               Group.created_at = created_at
          Group.save()
          serialized_data = GroupSerializers(direction).data
          group = Group.objects.create(
               direction=request.POST.get('direction'),
               mentor=request.POST.get('mentor'),
               students=request.POST.get('students'),
               created_at=request.POST.get('created_at'),
          )
          data = {
               "Group": GroupSerializers(group).data,
               "success": True
          }
     else:
          data = {
               "success": False,
               "message": "ERROR!"
          }

     return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def add_student_to_group(request):
     user = request.user
     if user.status in [2, 4]:
          group = Group.objects.create(
               direction=request.POST.get('direction'),
               mentor=request.POST.get('mentor'),
               students=request.POST.get('students'),
               created_at=request.POST.get('created_at')
          )
          data = {
               "Group": GroupSerializers(group).data,
               "success": True
          }
     else:
          data = {
               "success": False,
               "message": "ERROR!"
          }

     return Response(data, status=HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def remove_student_in_group(request):
     student.objects.all(id=pk).delete()
     return Response(
          status=HTTP_204_NO_CONTENT
     )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create_region(request):
     user = request.user
     if user.status in [1]:
          region = Region.objects.create(
          name=request.POST.get('name'),
          )
          data = {
               "Region": RegionSerializers(group).data,
               "success": True
          }
     else:
          data = {
               "success": False,
               "message": "ERROR!"
          }

     return Response(data, status=HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_region(request):
     region = Region.objects.all()
     serialized_data = (region).data
     return Response(serialized_data, status=HTTP_200_OK)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def change_region(request):
     users = request.users
     if users.status in [3, 6]:
          name = request.POST.get('name'),
          region = Region.objects.get(id=pk),
          if status is not None:
               Region.name = status
          region.save()
          serialized_data = RegionSerializers(direction).data
          region = Region.objects.create(
               name=request.POST.get('name'),
          )
          data = {
               "region": RegionSerializers(region).data,
               "success": True
          }
     else:
          data = {
               "success": False,
               "message": "ERROR!"
          }

     return Response(data)
# xato


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create_payment(request):
     user = request.user
     if user.status in [1, 3]:
          payment = Payment.objects.create(
               name=request.POST.get('student'),
               money=request.POST.get('money'),
               group=request.POST.get('group'),
               created_at=request.POST.get('created_at'),
          )
          data = {
               "Payment": PaymentSerializers(direction).data,
               "success": True
          }
     else:
          data = {
               "success": False,
               "message": "You do`nt have permission to do this"
          }

     return Response(data, status=HTTP_201_CREATED)
# xato


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_payment(request):
          payment = Payment.objects.all()
          serialized_data = PaymentSerializers(payment, many=True).data
          return Response(serialized_data, status=HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def change_payment(request):
     user = request.user
     if user.status in [1, 4]:
          payment = Payment.objects.create(
               name=request.POST.get('student'),
               money=request.POST.get('money'),
               group=request.POST.get('group'),
               created_at=request.POST.get('created_at'),
          )
          data = {
               "Payment": PaymentSerializers(group).data,
               "success": True
          }
     else:
          data = {
               "success": False,
               "message": "ERROR!"
          }

     return Response(data, status=HTTP_201_CREATED)
# xato

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_payment_by_student(request):

     return Response('ss')

@api_view([''])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_unpayment_student(request):

     return Response('ss')