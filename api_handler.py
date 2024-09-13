from flask import Flask, jsonify, request
from lead_service import LeadService
from flask_jwt_extended import jwt_required

class LeadAPIHandler:
    def __init__(self, app, db):
        self.app = app
        self.lead_service = LeadService(db)
        
        # Definição das rotas
        self.app.add_url_rule('/leads', view_func=self.get_leads, methods=['GET'])
        self.app.add_url_rule('/leads/<int:id>', view_func=self.get_lead, methods=['GET'])
        self.app.add_url_rule('/leads', view_func=self.create_lead, methods=['POST'])
        self.app.add_url_rule('/leads/<int:id>', view_func=self.update_lead, methods=['PUT'])
        self.app.add_url_rule('/leads/<int:id>', view_func=self.delete_lead, methods=['DELETE'])

    # Métodos com jwt_required devem ser usados dessa forma para métodos da classe
    @jwt_required()
    def create_lead(self):
        data = request.json
        required_fields = ['name', 'email', 'telefone', 'latitude', 'longitude', 'temperature', 'interest']
        
        # Validação dos campos obrigatórios
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Campos obrigatórios faltando."}), 400
        
        # Criação do lead
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

    @jwt_required()
    def update_lead(self, id):
        data = request.json
        
        # Buscar lead pelo ID
        lead = self.lead_service.get_lead_by_id(id)
        if not lead:
            return jsonify({"error": "Lead não encontrado."}), 404
        
        # Atualização dos dados do lead
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

    @jwt_required()
    def delete_lead(self, id):
        # Buscar lead pelo ID
        lead = self.lead_service.get_lead_by_id(id)
        if not lead:
            return jsonify({"error": "Lead não encontrado."}), 404
        
        # Deletar lead
        self.lead_service.delete_lead(id)
        return jsonify({"message": "Lead deletado com sucesso!"}), 200

    @jwt_required()
    def get_leads(self):
        leads = self.lead_service.get_all_leads()
        return jsonify(leads), 200

    @jwt_required()
    def get_lead(self, id):
        lead = self.lead_service.get_lead_by_id(id)
        if not lead:
            return jsonify({"error": "Lead não encontrado."}), 404
        return jsonify(lead), 200