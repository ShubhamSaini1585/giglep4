from datetime import datetime, timedelta
from calendar import HTMLCalendar

from django.http import request
from .models import Event
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		# events = Event.objects.filter(author)
		events_per_day = events.filter(date__day=day)
		d = ''
		
		if len(events_per_day) > 1:
			d += f'<li class="event-big"><a href="{ reverse_lazy("cal:event-list", kwargs={"slug_year": self.year, "slug_month": self.month, "slug_day": day}) }">{len(events_per_day)} events</a></li>'
			d += f'<li class="event-small"><a href="{ reverse_lazy("cal:event-list", kwargs={"slug_year": self.year, "slug_month": self.month, "slug_day": day}) }">..</a></li>'

		else:
			for event in events_per_day:
				d += f'<li class="event-big"><a href="{ reverse_lazy("cal:event_detail", args=(event.pk,)) }">{event.title}</a></li>'
				d += f'<li class="event-small"><a href="{ reverse_lazy("cal:event_detail", args=(event.pk,)) }"> . </a></li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr class="rb-txt"> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, user, withyear=True):
		events = Event.objects.filter(date__year=self.year, date__month=self.month, author=user)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal