import requests

class teamup:
    """Handle Teamup"""

    def __init__(self, teamup_token):
        self.teamup_token = teamup_token

        parent = self

    def get(self, endpoint, payload={}):
        headers = {'Teamup-Token': self.teamup_token}
        response = requests.get('https://api.teamup.com' + endpoint, headers=headers)
        return response.json()


class teamup_calendar:
    """Handle Teamup Calendar"""

    def __init__(self, parent, calendar_key):
        self.parent = parent
        self.calendar_key = calendar_key

    def config(self):
        return self.parent.get('/' + self.calendar_key + '/configuration')

    def events(self, options={'query': '', 'startDate': '', 'endDate': '', 'subcalendarId': '', 'modifiedSince': ''}):
        payload = {
            'query': options['query'],
            'startDate': options['startDate'],
            'endDate': options['endDate'],
            'subcalendarId': options['subcalendarId'],
            'modifiedSince': options['modifiedSince']
        }
        return self.parent.get('/' + self.calendar_key + '/events', payload)

    def event(self, eventId):
        return self.parent.get('/' + self.calendar_key + '/events/' + eventId)

    def event_histroy(self, eventId):
        return self.parent.get('/' + self.calendar_key + '/events/' + eventId + '/history')

    def subs(self):
        return self.parent.get('/' + self.calendar_key + '/subcalendars')

    def sub(self, subcalendarId):
        return self.parent.get('/' + self.calendar_key + '/subcalendars/' + subcalendarId)


if __name__ == "__main__":
    t = teamup('<teamup_token>')
    r = t.get('/check-access')
    print(r)

    c = teamup_calendar(t, '<teamup_calendar>')
    print(c.calendar_key)
    r = c.subs()
    print(r)
