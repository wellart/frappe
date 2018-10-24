from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Tugas"),
			"icon": "octicon octicon-briefcase",
			"items": [
				{
					"type": "doctype",
					"name": "ToDo",
					"label": _("To Do"),
					"description": _("Documents assigned to you and by you."),
				},
				{
					"type": "doctype",
					"name": "Event",
					"label": _("Calendar"),
					"link": "List/Event/Calendar",
					"description": _("Event and other calendars."),
				},
				{
					"type": "doctype",
					"name": "Note",
					"description": _("Private and public Notes."),
				},
			]
		},
		{
			"label": _("Buku Alamat"),
			"icon": "octicon octicon-book",
			"items": [
				{
					"type": "doctype",
					"name": "Contact",
					"description": _("Database of potential customers."),
				},
				{
					"type": "doctype",
					"name": "Address",
					"description": _("All Addresses."),
				},
			]
		},
	]
