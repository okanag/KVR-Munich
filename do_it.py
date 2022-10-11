from termin_api import CityHall
import worker

appointments = worker.get_available_appointments(CityHall, 'Antrag Personalausweis')
if len(appointments) > 0:
    for caption, date, time in appointments:
        print('The nearest appointments at %s are on %s:\n%s' % (
            caption, date, '\n'.join(time)))
        print('Please book your appointment here: %s' % CityHall.get_frame_url())
else:
    print("No appointment found.")