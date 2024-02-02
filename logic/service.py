 
class service: 

    def get_all_services():
        return {
            "services": [
                {
                "service_id": "1",
                "service_name": "Klippning",
                "description": "Priset fastställs vid val av tid och utförare",
                "image": "https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/klippning.svg",
                "price": "200",
                "time_in_minutes": "45",
                "staff": [
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
                "staff": [
                    {
                    "staff_id": "1",
                    "staff_name": "Lee"
                    }
                ]
                }
            ]
            }
