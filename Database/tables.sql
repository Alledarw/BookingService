DROP TABLE IF EXISTS "staff_relate_service";
DROP TABLE IF EXISTS "service";
DROP TABLE IF EXISTS "staff";
-- DROP TABLE IF EXISTS "client_profile_relate_schedul";
-- DROP TABLE IF EXISTS "client_profile";
DROP TABLE IF EXISTS "appointment_scheduling";

-- Sprint 1
-- Create the service table
CREATE TABLE "service" (
  "id" SERIAL PRIMARY KEY,
  "service_code" VARCHAR(10) NOT NULL,
  "service_name" VARCHAR(255) NOT NULL,
  "description" VARCHAR(255),
  "image" VARCHAR(255),
  "price" INT,
  "time_in_minutes" INT,
  "is_active" BOOLEAN,
  "updated" TIMESTAMP,
  "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Create the staff table
CREATE TABLE "staff" (
  "id" SERIAL PRIMARY KEY,
  "staff_code" VARCHAR(10) NOT NULL,
  "staff_name" VARCHAR(255) NOT NULL,
  "image" VARCHAR(255),
  "description" VARCHAR(50) NOT NULL,
  "updated" TIMESTAMP,
  "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the staff_relate_service table
CREATE TABLE "staff_relate_service" (
  "srs_id" SERIAL PRIMARY KEY,
  "service_id" INT,
  "staff_id" INT,
  UNIQUE (service_id, staff_id),
  FOREIGN KEY (service_id)  REFERENCES service(id),
  FOREIGN KEY (staff_id)  REFERENCES staff(id)
);


-- Sprint 2
CREATE TABLE "appointment_scheduling" (
  "id" SERIAL PRIMARY KEY,
  "srs_id" INT,
  "booking_code" VARCHAR(20),
  "start_at" VARCHAR(5),
  "end_at" VARCHAR(5),
  "email" VARCHAR(200),
  "booked_date" DATE,
  "is_booked" bool,
  "created" TIMESTAMP,
  "updated" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sprint 3
-- CREATE TABLE "client_profile" (
--   "id" SERIAL PRIMARY KEY,
--   "email" VARCHAR(100),
--   "password" VARCHAR(50),
--   "first_name" VARCHAR(100),
--   "last_name" VARCHAR(100),
--   "phone" VARCHAR(20),
--   "profile_image" VARCHAR(255),
--   "created" datetime,
--   "updated" datetime
-- );
 
-- CREATE TABLE "client_profile_relate_schedul" (
--   "appointment_id" INT,
--   "client_id" INT,
--   FOREIGN KEY (appointment_id)  REFERENCES appointment_scheduling(id)
--   FOREIGN KEY (client_id)  REFERENCES client_profile(id)
-- );