from tinydb import TinyDB, Query

class FormDatabase:
    def __init__(self, db_path='forms.json'):
        self.db = TinyDB(db_path)
    
    def add_template(self, template):
        if 'name' not in template:
            raise ValueError("Шаблон должен содержать поле 'name'")
        
        fields = {k: v for k, v in template.items() if k != 'name'}
        self.db.insert({
            'name': template['name'],
            'fields': fields
        })
    
    def find_matching_template(self, input_fields):
        Form = Query()
        
        for template in self.db.all():
            template_fields = template['fields']
            match = True
            
            for field_name, field_type in template_fields.items():
                if field_name not in input_fields:
                    match = False
                    break
                
                if input_fields[field_name] != field_type:
                    match = False
                    break
            
            if match:
                return template['name']
        return None