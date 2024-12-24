import gpxpy

class Activity:

    def __init__(self):
        self.type = 'Cycle Commuting'

    def importActivity(self, file_path):
        gpx_file = open(file_path, 'r')
        gpx = gpxpy.parse(gpx_file)

class Commute:
    def __init__(self, startLatitude, startLongitude, endLatitude, endLongitude, startRadius_m=100, endRadius_m=100):
        # NOTES
        # 1. Need to do something to parse the direction; commutes are saved as separate entries, but start/end locations flip
        # 2. Pull out date/time information for the start/end of each commute leg
        # 3. Pull out durations
        # 4. Pull out bicycle used; maybe infer from activity type?
        # 5. Possibly correlate with some weather plugin (unless that's included in the GPX file natively?

        # define the start and end locations of the commute
        self.startLatLong = [startLatitude, startLongitude]
        self.endLatLong = [endLatitude, endLongitude]

        # define the rough distances from the start and end locations that will be considered commute rides
        self.startRadius_m = startRadius_m
        self.endRadius_m = endRadius_m
