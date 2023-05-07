import os

from django.contrib import admin
from django.db.models import Count
from django.http import HttpResponse
from .models import Car, ServiceRequest, RentalRequest, RentalHistory, ServiceHistory
from EV_chargers import settings
from datetime import datetime
from django.shortcuts import render

import csv
import matplotlib.pyplot as plt
import base64
import io




def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    response.write(u'\ufeff'.encode('utf8'))

    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'


def rental_history_diagrams(modeladmin, request, queryset):
    rental_data = RentalHistory.objects.values('car_id__car_full_name').annotate(count=Count('car_id__car_full_name'))

    labels = []
    sizes = []

    for data in rental_data:
        labels.append(data['car_id__car_full_name'])
        sizes.append(data['count'])

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    filename = f'rental_history_{datetime.now().strftime("%d-%m-%Y")}'
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    filepath = filepath.replace('\\', '/')
    plt.savefig(filepath)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    img_dgrm = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')

    return render(request, template_name='analytics.html', context={'path': img_dgrm})

rental_history_diagrams.short_description = 'Diagram to png'


class CarAdmin(admin.ModelAdmin):
    actions = [export_to_csv]


class RentalHistoryAdmin(admin.ModelAdmin):
    actions = [rental_history_diagrams]


admin.site.register(Car, CarAdmin)
admin.site.register(ServiceRequest)
admin.site.register(RentalRequest)
admin.site.register(RentalHistory, RentalHistoryAdmin)
admin.site.register(ServiceHistory)