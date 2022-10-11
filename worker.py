# -*- coding: utf-8 -*-
import datetime

import termin_api
from termin_api import Buro


def get_available_appointments(department: Buro, termin_type):

    appointments = termin_api.get_termins(department, termin_type)
    if appointments is None:
        print(
            f'Seems like appointment title <{termin_type}> is not accepted by the '
            f'buro <%s> any more:' % department.get_name())
        return None

    # list of tuples: (caption, date, time)
    available_appointments = []
    for k, v in appointments.items():
        caption = v['caption']
        first_date = None
        for date in v['appoints']:
            if v['appoints'][date]:
                first_date = date

                next_in = (datetime.datetime.strptime(first_date, '%Y-%m-%d').date() - datetime.date.today()).days
                print(f'Soonest appt at {caption} is {next_in} days from today')

                break

        if first_date:
            available_appointments.append((caption, first_date, v['appoints'][first_date]))

    return available_appointments
