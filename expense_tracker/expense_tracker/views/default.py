""" Views for the Expense Tracker app """

from pyramid.response import response

def home_page(request):
    """ View for the home route """
    return Response("This is my first view!")