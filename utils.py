import random
from models import Lead, db

def generate_leads():
    names = ['John Doe', 'Jane Smith', 'Chris Johnson', 'Patricia Brown', 'Michael Williams']
    emails = ['john.doe@example.com', 'jane.smith@example.com', 'chris.johnson@example.com', 'patricia.brown@example.com', 'michael.williams@example.com']
    telefones = ['123456789', '987654321', '555666777', '888999000', '444555666']
    interests = ['Tecnologia', 'Saúde', 'Educação', 'Marketing', 'Design']

    for _ in range(100):
        name = random.choice(names)
        email = random.choice(emails)
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