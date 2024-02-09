class service_db: 
    def __init__(self, db):
        self.db = db

    def query_all_service(self):
        query = """
        SELECT jsonb_build_object(
            'id', id,
            'service_code', service_code,
            'service_name', service_name,
            'description', description,
            'image', image,
            'price', price,
            'time_in_minutes', time_in_minutes,
            'is_active', is_active,
            'updated', updated,
            'created', created
        ) AS json_data
            FROM service;
        """ 
        return self.db.execute_return_attributed(query, fetchall=True)
    

    def query_all_staff(self):
        query = """
        SELECT jsonb_build_object(
                'id', id,
                'staff_code', staff_code,
                'staff_name', staff_name,
                'staff_name', staff_name,
                'image', image
                ) AS json_data
                FROM staff;
          
            """  
        return self.db.execute_return_attributed(query, fetchall=True)
    
    def query_service_relate_staff(self):
        query = """
        SELECT jsonb_build_object(
                'srs_id', srs_id,
                'service_id', service_id,
                'staff_id', staff_id
                ) AS json_data
                FROM staff_relate_service;
            """  
        return self.db.execute_return_attributed(query, fetchall=True)
    



class service: 

    def get_all_services():
        return [
    {
    "service_id": "1",
    "service_name": "Klippning",
    "description": "Priset fastställs vid val av tid och utförare",
    "image": "https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/klippning.svg",
    "price": "200",
    "time_in_minutes": "45",
    "staffs": [
        {
        "staff_id": "1",
        "staff_name": "Lee"
        },
        {
        "staff_id": "2",
        "staff_name": "Nurhan"
        }
    ]
    },
    {
    "service_id": "2",
    "service_name": "Balayage Kreativ Färg",
    "description": "Priset fastställs vid val av tid och utförare",
    "image": "https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/balayage.svg",
    "price": "2000",
    "time_in_minutes": "120",
    "staffs": [
        {
        "staff_id": "3",
        "staff_name": "Florinel"
        }
    ]
    }
]
