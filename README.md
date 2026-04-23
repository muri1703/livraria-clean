## Arquitetura Clean

Este projeto foi refatorado para Clean Architecture, garantindo:

- Separação clara entre domínio, casos de uso e infraestrutura
- Aplicação do princípio DIP (Dependency Inversion Principle)
- Persistência desacoplada utilizando arquivo TXT
- Backend independente de tecnologia de banco de dados

## Como rodar

### Backend
cd backend

venv\Scripts\activate

python app.py

### Frontend
cd frontend

npm install

npm run dev
