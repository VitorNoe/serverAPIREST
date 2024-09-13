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

    def create_lead(self, name, email, telefone, latitude, longitude, temperature, interest):
        lead = Lead(name=name, email=email, telefone=telefone, latitude=latitude, longitude=longitude, temperature=temperature, interest=interest)
        self.db.session.add(lead)
        self.db.session.commit()

    def get_lead_by_id(self, lead_id):
        return Lead.query.get_or_404(lead_id)

    def get_leads(self, page, per_page, search_name):
        query = Lead.query
        if search_name:
            query = query.filter(Lead.name.ilike(f"%{search_name}%"))
        return query.paginate(page=page, per_page=per_page, error_out=False)

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