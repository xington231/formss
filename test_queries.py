import subprocess
from database import FormDatabase

def run_test_query(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f"Команда: {command}")
    print("Вывод:")
    print(result.stdout)
    print("-----")

if __name__ == '__main__':
    db = FormDatabase('test_forms.json')
    
    db.db.truncate()  
    
    db.add_template({
        "name": "Данные пользователя",
        "login": "email",
        "tel": "phone"
    })
    db.add_template({
        "name": "Форма заказа",
        "customer": "text",
        "order_date": "date",
        "contact": "phone"
    })
    
    test_queries = [
        'py app.py get_tpl --login=test@example.com --tel="+7 123 456 78 90"',
        'py app.py get_tpl --customer="Иван" --order_date=2023-12-31 --contact="+7 987 654 32 10"',
        'py app.py get_tpl --login=test@example.com --tel=invalid',
        'py app.py get_tpl --unknown_field=2023-12-31',
        'py app.py get_tpl --customer="Иван" --order_date=31.12.2023'
    ]
    
    for query in test_queries:
        run_test_query(query)