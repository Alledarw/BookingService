-- Inserted example data into the tables
INSERT INTO staff (shop_name, name) VALUES
  ('HairSalon', 'Florinel'),
  ('HairSalon', 'Sirahj'),
  ('HairSalon', 'Nurhan');

INSERT INTO service (service_name, description, image, price, time_in_minutes, is_active, created) VALUES
  ('Haircut', 'Includes shampoo and styling', 'haircut.jpg', 500, 30, true, NOW()),
  ('Perm', 'Curl or wave your hair', 'perm.jpg', 900, 90, true, NOW()),
  ('Extensions', 'Add length and volume to your hair', 'extensions.jpg', 1200, 120, true, NOW());
