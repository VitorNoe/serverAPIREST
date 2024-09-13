import random
from models import Lead, db

def generate_leads():
    names = ['John Doe', 'Jane Smith', 'Chris Johnson', 'Patricia Brown', 'Michael Williams']
    emails = ['john.doe@example.com', 'jane.smith@example.com', 'chris.johnson@example.com', 'patricia.brown@example.com', 'michael.williams@example.com']
    telefones = ['(12) 3456-7890', '(98) 7654-3210', '(55) 6666-7777', '(88) 9999-0000', '(44) 5555-6666']
    interests = ['Tecnologia', 'Saúde', 'Educação', 'Marketing', 'Design']

    # Garantir unicidade de emails
    existing_emails = set(Lead.query.with_entities(Lead.email).all())
    existing_emails = {email[0] for email in existing_emails}

    for _ in range(100):
        name = random.choice(names)
        email = random.choice(emails)
        
        # Garantir unicidade de email
        while email in existing_emails:
            email = random.choice(emails)
        existing_emails.add(email)

        telefone = random.choice(telefones)
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        temperature = random.uniform(10, 40)
        interest = random.choice(interests)
        
        lead = Lead(name=name, email=email, telefone=telefone, latitude=latitude, longitude=longitude, temperature=temperature, interest=interest)
        db.session.add(lead)
    
    db.session.commit()
    print("Leads fictícios gerados e adicionados ao banco de dados com sucesso!")

generate_leads()