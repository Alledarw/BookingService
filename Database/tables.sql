DROP TABLE "staff_relate_service";
DROP TABLE "service";
DROP TABLE "staff";

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
  "updated" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Create the staff table
CREATE TABLE "staff" (
  "id" SERIAL PRIMARY KEY,
  "staff_code" VARCHAR(10) NOT NULL,
  "staff_name" VARCHAR(255) NOT NULL,
  "image" VARCHAR(255),
  "description" VARCHAR(50) NOT NULL,
  "updated" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
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





-- -- Create tables based on the ER-diagram
-- CREATE TABLE "staff" (
--   "id" SERIAL PRIMARY KEY,
--   "shop_name" VARCHAR(100) NOT NULL,
--   "name" VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE "service" (
--   "id" SERIAL PRIMARY KEY,
--   "service_name" VARCHAR(100) NOT NULL,
--   "description" VARCHAR(100),
--   "image" VARCHAR(100),
--   "price" INT,
--   "time_in_minutes" INT,
--   "is_active" bool,
--   "created" TIMESTAMP
-- );

-- CREATE TABLE "opening_hours" (
--   "id" SERIAL PRIMARY KEY,
--   "start_at" VARCHAR(20),
--   "end_at" VARCHAR(20),
--   "is_allow_book" bool
-- );

-- CREATE TABLE "appointment_time_slot" (
--   "id" SERIAL PRIMARY KEY,
--   "appointment_id" INT,
--   "staff_time_slot_id" INT
-- );

-- CREATE TABLE "staff_time_slot" (
--   "id" SERIAL PRIMARY KEY,
--   "staff_id" INT,
--   "slot_date" DATE,
--   "start_at" VARCHAR(20),
--   "end_at" VARCHAR(20)
-- );

-- CREATE TABLE "client_profile" (
--   "id" SERIAL PRIMARY KEY,
--   "email" VARCHAR(100),
--   "password" VARCHAR(50),
--   "first_name" VARCHAR(100),
--   "last_name" VARCHAR(100),
--   "phone" VARCHAR(20),
--   "profile_image" VARCHAR(255),
--   "created" TIMESTAMP
-- );

-- CREATE TABLE "appointment_scheduling" (
--   "id" SERIAL PRIMARY KEY,
--   "client_id" INT,
--   "service_id" INT,
--   "staff_id" INT,
--   "booking_code" VARCHAR(20),
--   "start_at" VARCHAR(5),
--   "end_at" VARCHAR(5),
--   "booked_date" DATE,
--   "is_booked" bool,
--   "created" TIMESTAMP
-- );

-- CREATE TABLE "appointment_scheduling_log" (
--   "id" SERIAL PRIMARY KEY,
--   "service_id" INT,
--   "staff_id" INT,
--   "place_id" INT,
--   "booked_date" DATE,
--   "start_at" VARCHAR(20),
--   "end_at" VARCHAR(20),
--   "is_booked" bool,
--   "created" TIMESTAMP
-- );

-- -- Foreign key references
-- ALTER TABLE "appointment_scheduling" ADD FOREIGN KEY ("staff_id") REFERENCES "staff" ("id");
-- ALTER TABLE "appointment_scheduling" ADD FOREIGN KEY ("service_id") REFERENCES "service" ("id");
-- ALTER TABLE "appointment_scheduling" ADD FOREIGN KEY ("client_id") REFERENCES "client_profile" ("id");

-- ALTER TABLE "appointment_time_slot" ADD FOREIGN KEY ("staff_time_slot_id") REFERENCES "staff_time_slot" ("id");
-- ALTER TABLE "appointment_time_slot" ADD FOREIGN KEY ("appointment_id") REFERENCES "appointment_scheduling" ("id");

-- ALTER TABLE "staff_time_slot" ADD FOREIGN KEY ("staff_id") REFERENCES "staff" ("id");
