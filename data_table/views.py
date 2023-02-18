from django.shortcuts import render

# Create your views here.
from django_tables2 import SingleTableView

from .models import DataTable
from .table import ReviewTable


class ReviewsListView(SingleTableView):
    model = DataTable
    table_class = ReviewTable
    template_name = 'tutorial/table.html'