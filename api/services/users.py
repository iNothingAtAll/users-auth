from sqlmodel import Session

from api.schemas import Usuario
from api.models import UserCreate, UserUpdate


# Servicio para manejar operaciones relacionadas con usuarios
class UserService:
    def __init__(self, session: Session):
        self.session = session


    # Método para crear un nuevo usuario
    def create_user(self, user_data: UserCreate):
        user = Usuario(**user_data.model_dump())
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user


    # Método para obtener un usuario por su ID
    def get_user(self, user_id):
        return self.session.get(Usuario, user_id)


    # Método para actualizar la información de un usuario existente
    def update_user(self, user_id, user_data: UserUpdate):
        user = self.session.get(Usuario, user_id)
        if user:
            for key, value in user_data.model_dump().items():
                setattr(user, key, value)
            self.session.commit()
        return user


    # Método para deshabilitar un usuario
    def disable_user(self, user_id):
        user = self.session.get(Usuario, user_id)
        if user:
            user.activo = False
            self.session.commit()
        return user