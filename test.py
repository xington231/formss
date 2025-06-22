from database import FormDatabase

def initialize_database():
    db = FormDatabase()
    
    db.db.drop_tables()  

    db.add_template({
        "name": "Форма пользователя",
        "email": "email",
        "phone": "phone"
    })
    
    db.add_template({
        "name": "Форма заказа",
        "customer": "text",
        "order_date": "date",
        "contact": "phone"
    })
    
    print("База данных успешно инициализирована с тестовыми шаблонами")

if __name__ == "__main__":
    initialize_database()