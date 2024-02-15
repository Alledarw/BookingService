

-- Insert service values
INSERT INTO "service" ("service_code", "service_name", "description", "image", "price", "time_in_minutes", "is_active")
VALUES 
    ('S001', 'Haircut', 'Price determined upon selection of time and stylist', 'https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/klippning.svg', 200, 45, TRUE),
    ('S002', 'Balayage Creative Color', 'Price determined upon selection of time and stylist', 'https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/balayage.svg', 2000, 120, TRUE),
    ('S003', 'Hair Extensions', 'Special offer: Get 20% off on your first visit', 'https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/Klippochfa%CC%88rg.svg', 1500, 180, TRUE),
    ('S004', 'Men Haircut', 'Quick and stylish haircut for men', 'https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/sk%C3%A4gg.svg', 150, 30, TRUE),
    ('S005', 'Coloring', 'Transform your look with professional coloring', 'https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/f%C3%A4rgning.svg', 800, 90, TRUE),
    ('S006', 'Styling', 'Perfect your hairstyle with professional styling', 'https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/permanent.svg', 300, 60, TRUE),
    ('S007', 'Event Hairstyle', 'Create a memorable event hairstyle for special occasions', 'https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/salongskur_2.svg', 1200, 90, TRUE),
    ('S008', 'Eyelash Extensions', 'Achieve longer and fuller lashes', 'https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/fransarobryn.svg', 600, 60, TRUE);


-- Insert staff values
INSERT INTO "staff" ("staff_code", "staff_name", "image", "description")
VALUES 
    ('Staff001', 'John Doe', 'https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/upps%C3%A4ttning.svg', 'Senior Stylist'),
    ('Staff001', 'Alice Smith', 'https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/upps%C3%A4ttning.svg', 'Color Specialist'),
    ('Staff001', 'Bob Johnson', 'https://voady-files.s3.eu-west-1.amazonaws.com/voadyicons/categories/upps%C3%A4ttning.svg', 'Junior Stylist');




-- Insert staff_relate_service values
INSERT INTO "staff_relate_service" ("srs_id", "service_id", "staff_id")
VALUES 
    (1, 1, 1),
    (2, 1, 3),
    (15, 2, 3),
    (16, 2, 1),
    (3, 3, 2),
    (4, 3, 1),
    (5, 3, 3),
    (6, 4, 3),
    (7, 4, 1),
    (8, 5, 2),
    (9, 6, 3),
    (10, 6, 1),
    (11, 6, 2),
    (12, 7, 3),
    (13, 7, 1),
    (14, 8, 2);


INSERT INTO appointment_scheduling (srs_id, booking_code, start_at, end_at, booked_date, is_booked, created, updated)
VALUES
  (15, 'ABC123', '10:30', '11:59', '2024-02-20', true, NOW(), NOW()),
  (15, 'DEF456', '09:00', '10:29', '2024-02-20', true, NOW(), NOW()),
  (15, 'GHI789',  '15:00','16:30', '2024-02-20', true, NOW(), NOW()),
  (15, 'JKL012', '12:00', '13:29', '2024-02-18', true, NOW(), NOW()),
  (16, 'MNO345', '13:30', '14:59', '2024-02-18', true, NOW(), NOW()),
  (15, 'PQR678', '15:00', '16:29', '2024-02-17', false, NOW(), NOW()),
  (15, 'STU901', '10:30', '11:59', '2024-02-17', false, NOW(), NOW()),
  (16, 'VWX234', '15:00', '16:29', '2024-02-16', false, NOW(), NOW()),
  (15, 'YZA567', '09:00', '10:29', '2024-02-15', false, NOW(), NOW()),
  (16, 'BCD890', '16:30', '17:59', '2024-02-15', false, NOW(), NOW());



-- Inserted example data into the tables
-- INSERT INTO staff (shop_name, name) VALUES
--   ('HairSalon', 'Florinel'),
--   ('HairSalon', 'Sirahj'),
--   ('HairSalon', 'Nurhan');

-- INSERT INTO service (service_name, description, image, price, time_in_minutes, is_active, created) VALUES
--   ('Haircut', 'Includes shampoo and styling', 'haircut.jpg', 500, 30, true, NOW()),
--   ('Perm', 'Curl or wave your hair', 'perm.jpg', 900, 90, true, NOW()),
--   ('Extensions', 'Add length and volume to your hair', 'extensions.jpg', 1200, 120, true, NOW());


