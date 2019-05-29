from myapp.models import Review
from myapp.serializers import ReviewSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Review.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# class TaskListApi(generics.RetrieveUpdateDestroyAPIView):
#     queryset = TaskList.objects.all()
#     serializer_class = TaskListSerializer2

#
# class TasksListApi(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#
# class TaskApi(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#


