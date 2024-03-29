from .models import loanarrears
from django.db.models import OuterRef, Subquery , F
from django.db.models import Max

class loanarrearsuils:
    @classmethod
    def filter_by_assigned_location(cls , location):
            return loanarrears.filter_by_assigned_location(location)
        
    @classmethod
    def filter_by_loanaddress(cls , location):
            return loanarrears.filter_by_loanaddress(location).exclude(monthly_arrears = 0)
        
    @classmethod
    def filter_by_location_and_price(cls ,location, pricemax, pricemin):
        queryset = loanarrears.objects.all()

        if location:
            queryset = queryset.filter(loan_id__username__address__icontains=location)

        if pricemax:
            queryset = queryset.filter(monthly_arrears__lte=pricemax)

        if pricemin:
            queryset = queryset.filter(monthly_arrears__gt=pricemin)
            
        queryset = queryset.values('loan_id').distinct()

        return queryset
    
    @classmethod
    def filter_by_assigned_staff(cls, staffName):
        
        subquery = loanarrears.objects.filter(loan_id=OuterRef('loan_id'), staff__name__icontains=staffName).order_by('loan_id')
        queryset = loanarrears.objects.annotate(latest_id=Subquery(subquery.values('id')[:1]))
        queryset = queryset.filter(id=F('latest_id')).order_by('loan_id__branch_location').exclude(monthly_arrears = 0)
        return queryset
    
    
    @classmethod
    def filter_by_loan_id(cls):
        return loanarrears.objects.filter(id__in=loanarrears.objects.values('loan_id').annotate(max_id=Max('id')).values('max_id')).exclude(monthly_arrears = 0)