import re
from models import Lead, db

class LeadService:
    def __init__(self, db):
        self.db = db

    # Validação de email usando regex
    @staticmethod
    def is_valid_email(email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    # Validação de telefone usando regex
    @staticmethod
    def is_valid_telefone(telefone):
        regex = r'^\(\d{2}\) \d{4,5}-\d{4}$'  # Corrigido o regex
        return re.match(regex, telefone) is not None

    # Verifica se o email já existe no banco
    @staticmethod
    def is_unique_email(email):
        return Lead.query.filter_by(email=email).first() is None

    # Criação de lead com validações de email e telefone
    def create_lead(self, name, email, telefone, latitude, longitude, temperature, interest):
        # Verificar se o email é válido
        if not self.is_valid_email(email):
            raise ValueError("Email inválido.")

        # Verificar se o telefone é válido
        if not self.is_valid_telefone(telefone):
            raise ValueError("Telefone inválido.")

        # Verificar se o email já existe
        if not self.is_unique_email(email):
            raise ValueError("O email já está sendo usado por outro lead.")

        # Criar lead
        lead = Lead(
            name=name, 
            email=email, 
            telefone=telefone, 
            latitude=latitude, 
            longitude=longitude, 
            temperature=temperature, 
            interest=interest
        )
        self.db.session.add(lead)
        self.db.session.commit()

    # Busca lead pelo ID com erro 404 se não encontrado
    def get_lead_by_id(self, lead_id):
        return Lead.query.get_or_404(lead_id)

    # Paginação de leads com opção de busca por nome
    def get_leads(self, page, per_page, search_name=None):
        query = Lead.query
        if search_name:
            query = query.filter(Lead.name.ilike(f"%{search_name}%"))
        return query.paginate(page=page, per_page=per_page, error_out=False)

    # Atualização de lead
    def update_lead(self, lead_id, name, email, telefone, latitude, longitude, temperature, interest):
        lead = self.get_lead_by_id(lead_id)

        # Atualizar os campos, mantendo valores antigos caso não sejam fornecidos
        lead.name = name or lead.name
        lead.email = email or lead.email
        lead.telefone = telefone or lead.telefone
        lead.latitude = latitude or lead.latitude
        lead.longitude = longitude or lead.longitude
        lead.temperature = temperature or lead.temperature
        lead.interest = interest or lead.interest

        self.db.session.commit()

    # Deleção de lead
    def delete_lead(self, lead_id):
        lead = self.get_lead_by_id(lead_id)
        self.db.session.delete(lead)
        self.db.session.commit()