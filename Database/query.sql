SELECT JSON_BUILD_OBJECT(
                            'id', id,
                            'srs_id', srs_id,
                            'booking_code', booking_code,
                            'start_at', start_at,
                            'end_at', end_at,
                            'booked_date', booked_date,
                            'email', email,
                            'is_booked', is_booked
                            ) AS json_data
                            FROM appointment_scheduling where srs_id IN (2, 5, 6, 9, 12, 15);


SELECT JSON_BUILD_OBJECT(
                        'srs_id', srs_id
                        ) AS json_data
                        FROM staff_relate_service where staff_id = 3