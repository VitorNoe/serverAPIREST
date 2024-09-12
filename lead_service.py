import re
from models import Lead, db

class LeadService:
	def __init__(self, db):
		self.db = db

	@staticmethod
	def is_valid_email(email):
		regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
		return re.match(regex, email) is not None

	@staticmethod
	def is_valid_telefone(telefone):
		regex = r'^\(\d{2}\) \d{4, 5}-\d{4}$'
		return re.match(regex, telefone) is not None

	@staticmethod
	def is_unique_email(email):
		return Lead.query.filter_by(email=email).first() is None

	@staticmethod
	def create_lead(data):
		name = data.get('name')
		email = data.get('email')
		telefone = data.get('telefone')
		latitude = data.get('latitude')
		longitude = data.get('longitude')
		temperature = data.get('temperature')
		interest = data.get('interest')

	def create_lead(self, name, email, telefone, latitude, longitude, temperature, interest):
		lead = Lead(name=name, email=email, telefone=telefone, latitude=latitude, longitude=longitude, temperature=temperature, interest=interest)
		self.db.session.add(lead)
		self.db.session.commit()

	def get_all_leads(self):
		return Lead.query.all()

	def get_lead_by_id(self, lead_id):
		return Lead.query.get_or_404(lead_id)

	def update_lead(self, lead_id, name, email, telefone, latitude, longitude, temperature, interest):
		lead = self.get_lead_by_id(lead_id)
		lead.name = name
		lead.email = email
		lead.telefone = telefone
		lead.latitude = latitude
		lead.longitude = longitude
		lead.temperature = temperature
		lead.interest = interest
		self.db.session.commit()

	def delete_lead(self, lead_id):
		lead = self.get_lead_by_id(lead_id)
		self.db.session.delete(lead)
		self.db.session.commit()