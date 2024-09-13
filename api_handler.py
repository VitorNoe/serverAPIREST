from flask import Flask, jsonify, request
from lead_service import LeadService

class LeadAPIHandler:
    def __init__(self, app, db):
        self.app = app
        self.lead_service = LeadService(db)
        
        # Rotas da API
        self.app.add_url_rule('/leads', view_func=self.get_leads, methods=['GET'])
        self.app.add_url_rule('/leads/<int:id>', view_func=self.get_lead, methods=['GET'])
        self.app.add_url_rule('/leads', view_func=self.create_lead, methods=['POST'])
        self.app.add_url_rule('/leads/<int:id>', view_func=self.update_lead, methods=['PUT'])
        self.app.add_url_rule('/leads/<int:id>', view_func=self.delete_lead, methods=['DELETE'])

    # Retorna todos os leads com paginação e pesquisa
    def get_leads(self):
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)
        search_name = request.args.get('search_name', default='', type=str)

        leads_pagination = self.lead_service.get_leads(page, per_page, search_name)
        leads = [lead.as_dict() for lead in leads_pagination.items]
        
        return jsonify({
            'leads': leads,
            'total': leads_pagination.total,
            'page': leads_pagination.page,
            'per_page': leads_pagination.per_page,
            'pages': leads_pagination.pages
        }), 200

    # Retorna um lead específico
    def get_lead(self, id):
        lead = self.lead_service.get_lead_by_id(id)
        if lead:
            return jsonify(lead.as_dict()), 200
        else:
            return jsonify({"error": "Lead não encontrado."}), 404

    # Cria um novo lead
    def create_lead(self):
        data = request.json
        required_fields = ['name', 'email', 'telefone', 'latitude', 'longitude', 'temperature', 'interest']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Campos obrigatórios faltando."}), 400
        
        self.lead_service.create_lead(
            name=data['name'],
            email=data['email'],
            telefone=data['telefone'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            temperature=data['temperature'],
            interest=data['interest']
        )
        return jsonify({"message": "Lead criado com sucesso!"}), 201

    # Atualiza um lead existente
    def update_lead(self, id):
        data = request.json
        lead = self.lead_service.get_lead_by_id(id)
        if not lead:
            return jsonify({"error": "Lead não encontrado."}), 404
        
        self.lead_service.update_lead(
            lead_id=id,
            name=data.get('name', lead.name),
            email=data.get('email', lead.email),
            telefone=data.get('telefone', lead.telefone),
            latitude=data.get('latitude', lead.latitude),
            longitude=data.get('longitude', lead.longitude),
            temperature=data.get('temperature', lead.temperature),
            interest=data.get('interest', lead.interest)
        )
        return jsonify({"message": "Lead atualizado com sucesso!"}), 200

    # Deleta um lead
    def delete_lead(self, id):
        lead = self.lead_service.get_lead_by_id(id)
        if not lead:
            return jsonify({"error": "Lead não encontrado."}), 404
        
        self.lead_service.delete_lead(id)
        return jsonify({"message": "Lead deletado com sucesso!"}), 200