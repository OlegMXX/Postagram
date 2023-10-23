from rest_framework.permissions import IsAuthenticated

from core.abstract.viewsets import AbstractViewSet
from core.user.serializers import UserSerializer
from core.user.models import User


class UserViewSet(AbstractViewSet):
    http_method_names = ('patch', 'get') #the only methods allowed
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        method to get a list of users by GET-request
        """
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    def get_object(self):
        """
        method to get one user with GET or PUT request on /user/id/ endpoint
        """
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

