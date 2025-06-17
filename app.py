import argparse
from database import FormDatabase
from validators import detect_field_type

def main():
    parser = argparse.ArgumentParser(description='Сопоставление шаблонов форм')
    parser.add_argument('command', choices=['get_tpl'], help='Команда для выполнения')
    
    args, unknown_args = parser.parse_known_args()
    
    input_fields = {}
    for arg in unknown_args:
        if arg.startswith('--'):
            field_arg = arg[2:]
            if '=' in field_arg:
                field_name, field_value = field_arg.split('=', 1)
                input_fields[field_name] = field_value
    
    detected_fields = {name: detect_field_type(value) for name, value in input_fields.items()}
    
    db = FormDatabase()
    template_name = db.find_matching_template(detected_fields)
    
    if template_name:
        print(template_name)
    else:
        print('{')
        for i, (name, ftype) in enumerate(detected_fields.items()):
            print(f'  {name}: {ftype}' + (',' if i < len(detected_fields) - 1 else ''))
        print('}')

if __name__ == '__main__':
    main()

    