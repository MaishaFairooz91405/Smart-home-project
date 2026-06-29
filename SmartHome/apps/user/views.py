# from rest_framework.response import Response
# from rest_framework.views import APIView
# from room.serializer import User
# from .serializer import UserSerializer
#
#
# class AvailableUsersAPIView(APIView):
#
#
#     def get(self, request):
#         users = User.objects.exclude(id=request.user.id)
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
