import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Region, Iso, Site

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # name,description,justification,year,longtitude,latitude,area,category,state,region,iso

    for row in reader:
        print(row)
        name = row[0]
        description = row[1]
        justi = row[2]

        # valid year
        try:
            year = int(row[3])
        except:
            year = None
        # valid longtitude
        try:
            longi = float(row[4])
        except:
            longi = None
        # valid latitude
        try:
            lati = float(row[5])
        except:
            lati = None
        # valid area
        try:
            area = float(row[6])
        except:
            area = None
        cate = row[7]
        state = row[8]
        region = row[9]
        iso = row[10]
        
        cate, created_cat = Category.objects.get_or_create(name=cate)
        state, created_st = State.objects.get_or_create(name=state)
        region, created_reg = Region.objects.get_or_create(name=region)
        iso, created_iso = Iso.objects.get_or_create(name=iso)
        site = Site(name=name, description=description, justification=justi, year=year, longitude=longi, latitude=lati, area_hectares=area, category=cate, state=state, region=region, iso=iso)
        site.save()
