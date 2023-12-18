more_task_and_environment1 = [
    (
        "Identify patients who have had more than three different types of treatments in the past year, listing their name, number of treatments, and the last treatment date.",
        "Patient records in 'patient_details' (includes patient_id, name, dob) linked with 'treatment_records' (patient_id, treatment_type, date_of_treatment)."
    ),
    (
        "Generate a list of employees who have not taken any leave in the current year, sorted by their department and hire date.",
        "'employee' database contains 'employee_info' with fields: emp_id, name, department, hire_date and 'leave_records' with fields: emp_id, leave_start_date, leave_end_date."
    ),
    (
        "Calculate the average duration of stay for guests in each hotel branch, for the last quarter, excluding stays shorter than two days.",
        "'hotels' database: tables include 'branches' (branch_id, location) and 'guest_stays' (stay_id, branch_id, guest_id, check_in_date, check_out_date)."
    ),
    (
        "List all books that have been checked out more than five times but have never been checked out by the same member twice.",
        "Library system with 'book_catalog' (book_id, title) and 'loan_history' (loan_id, book_id, member_id, loan_date)."
    ),
    (
        "Find the most popular product in each category based on the number of times it was ordered, for orders placed in the last six months.",
        "In 'ecommerce_db', 'products' table (product_id, category_id, name), linked to 'orders' table (order_id, product_id, order_date)."
    ),
    (
        "Identify the top 5 busiest flight routes in terms of passenger count for the last financial year.",
        "'airline_data' schema consists of 'flights' (flight_no, route_id, date) and 'passengers' (passenger_id, flight_no, name). 'routes' table (route_id, from_city, to_city)."
    ),
    (
        "Calculate the total sales per region for the last fiscal year, considering only regions that achieved more than $1 million in sales.",
        "Sales department uses 'regional_sales' (region_id, sale_amount, sale_date) and 'regions' (region_id, region_name)."
    ),
    (
        "Report the three most common issues reported in customer feedback for each product category, since the start of the year.",
        "'feedback_system' composed of 'feedback_entries' (feedback_id, customer_id, product_id, issue) and 'product_details' (product_id, category, name)."
    ),
    (
        "List all students who are majoring in Computer Science and have scored an A grade in more than four courses in the previous semester.",
        "University's 'student_portal' with 'student_profiles' (student_id, major, name) and 'grades' (student_id, course_id, grade, semester)."
    ),
    (
        "Find out which day of the week has the highest number of support calls made for IT issues in the last three months.",
        "IT support's 'call_logs' (call_id, issue_id, call_date, resolution_status) and 'issues' (issue_id, description)."
    ),
    (
        "Identify the top 10 students with the highest average marks in mathematics over the last three academic years, including their total number of mathematics courses taken.",
        "In 'education_system', 'students' (student_id, name) linked to 'grades' (student_id, course_id, mark, academic_year) and 'courses' (course_id, subject)."
    ),
    (
        "List the titles of movies that have been rented out every month since the beginning of the year, along with their total number of rentals.",
        "'video_rental_store' database with 'movies' (movie_id, title) and 'rental_history' (rental_id, movie_id, rental_date)."
    ),
    (
        "Calculate the monthly growth rate of new users for each online platform, only considering platforms with more than 10,000 total users.",
        "In 'user_data', 'platforms' (platform_id, name) and 'user_registrations' (user_id, platform_id, registration_date)."
    ),
    (
        "Determine the three most frequently ordered menu items in each restaurant location for the past six months.",
        "'restaurant_chain' system: 'locations' (location_id, address) and 'order_details' (order_id, location_id, menu_item_id, order_date)."
    ),
    (
        "List all vehicles that have been serviced more than 10 times in total but have not been serviced in the last month.",
        "'auto_repair_shop' database contains 'vehicles' (vehicle_id, model) and 'service_records' (record_id, vehicle_id, service_date)."
    ),
    (
        "Identify the three least utilized conference rooms in the office building, based on booking data for the current year.",
        "'office_management' database: 'conference_rooms' (room_id, room_name) and 'bookings' (booking_id, room_id, start_date, end_date)."
    ),
    (
        "Calculate the total volume of products shipped by each supplier in the last quarter, excluding suppliers with less than five shipments.",
        "'supply_chain' system with 'suppliers' (supplier_id, name) and 'shipments' (shipment_id, supplier_id, product_id, shipment_volume, shipment_date)."
    ),
    (
        "Report the average customer satisfaction score for each service representative, only including representatives with more than 50 interactions.",
        "'customer_service' department's 'representatives' (rep_id, name) and 'interactions' (interaction_id, rep_id, customer_id, satisfaction_score)."
    ),
    (
        "List the five most downloaded mobile applications from the online store in the past year, along with their developer names.",
        "'app_store' database: 'applications' (app_id, title, developer_id) and 'downloads' (download_id, app_id, download_date)."
    ),
    (
        "Find the departments with the highest average employee tenure, including only departments with more than 30 employees.",
        "'corporate_db': 'departments' (department_id, department_name) and 'employees' (employee_id, department_id, hire_date, resignation_date)."
    ),
    (
        "Identify the top 5 most frequently booked event types in each venue for the last year, including the number of times each event type was booked.",
        "'event_management' database: 'venues' (venue_id, name) linked with 'bookings' (booking_id, venue_id, event_type, booking_date)."
    ),
    (
        "Calculate the average delay time of flights departing from each airport, only considering airports with more than 100 flights last month.",
        "'air_traffic' system with 'airports' (airport_code, name) and 'flights' (flight_number, departure_airport, scheduled_departure, actual_departure)."
    ),
    (
        "List all products that have been discontinued but were part of more than 50 orders in the past year.",
        "'retail_inventory' database: 'products' (product_id, name, status) and 'order_items' (order_id, product_id, order_date)."
    ),
    (
        "Determine the three departments with the highest number of employee transfers in the past six months.",
        "'human_resources' database: 'departments' (department_id, department_name) and 'employee_transfers' (employee_id, from_department_id, to_department_id, transfer_date)."
    ),
    (
        "Calculate the total number of hours volunteered by each volunteer in the last year, ranking them by the most hours volunteered.",
        "'community_service' database with 'volunteers' (volunteer_id, name) and 'volunteer_hours' (volunteer_id, date, hours)."
    ),
    (
        "Identify the top three most prescribed medications in each clinic for the last quarter, including the total number of prescriptions.",
        "'healthcare_system' with 'clinics' (clinic_id, clinic_name) and 'prescriptions' (prescription_id, clinic_id, medication_id, prescription_date)."
    ),
    (
        "List the names of instructors who have taught more than five different courses but have no courses scheduled for the next semester.",
        "'educational_institute' database: 'instructors' (instructor_id, name) and 'course_schedule' (course_id, instructor_id, semester, scheduled)."
    ),
    (
        "Find the top 10 bestselling authors in the online bookstore, based on the total sales of their books in the past year.",
        "'bookstore' database with 'authors' (author_id, name) and 'book_sales' (book_id, author_id, quantity_sold, sale_date)."
    ),
    (
        "Report the total number of critical incidents reported in each factory location in the last six months.",
        "'industrial_safety' system: 'factories' (factory_id, location) and 'safety_reports' (report_id, factory_id, incident_type, report_date, severity)."
    ),
    (
        "Identify the three most popular payment methods used in the e-commerce platform in the last financial year.",
        "'e_commerce' platform's 'transactions' (transaction_id, amount, payment_method, transaction_date) and 'payment_methods' (method_id, description)."
    ),
    (
        "Identify employees who have not taken any leave in the past year and list their total overtime hours. Include employee name and department.",
        "Employee table with fields - EmployeeID, Name, Department. LeaveRecords table with fields - EmployeeID, LeaveStartDate, LeaveEndDate. Overtime table with fields - EmployeeID, OvertimeHours."
    ),
    (
        "Find the average property prices in each city district, only including districts with more than 20 properties listed. Show district name and average price.",
        "Database includes two tables: PropertyListings (PropertyID, DistrictID, Price) and Districts (DistrictID, DistrictName)."
    ),
    (
        "Extract the list of authors who have published more than 3 books in the genre 'Science Fiction' and list their most recent publication date.",
        "There are multiple tables: Authors (AuthorID, Name), Books (BookID, Title, Genre, PublicationDate), and AuthorBooks (AuthorID, BookID)."
    ),
    (
        "Determine the top 5 suppliers based on the quantity of products supplied this year. Include supplier name, total products, and product categories.",
        "SupplierDetails has SupplierID, Name, and ProductCategories. SupplyRecords holds SupplierID, ProductID, Quantity, and SupplyDate."
    ),
    (
        "Create a report showing the monthly breakdown of sales by region for the current year, excluding regions with less than $10,000 in sales.",
        "SalesData (SaleID, Region, Amount, SaleDate), with SaleDate including dates from the past two years."
    ),
    (
        "List all patients who have missed more than two appointments in the last six months, including their next scheduled appointment.",
        "Patient table contains PatientID, Name. Appointments table includes AppointmentID, PatientID, ScheduledDate, Attended (boolean)."
    ),
    (
        "Show the progression of the average test scores for each grade level from the beginning to the end of the school year.",
        "Tables present: GradeLevels (GradeID, Level), StudentTests (StudentID, GradeID, TestScore, TestDate)."
    ),
    (
        "Identify the top-performing salesperson in each store, based on total sales for the past quarter.",
        "Two main tables: Salesperson (SalespersonID, Name, StoreID) and SalesRecords (RecordID, SalespersonID, SaleAmount, SaleDate)."
    ),
    (
        "Generate a list of all vehicles that have not undergone maintenance in the last year, sorted by vehicle age.",
        "Tables available are Vehicles (VehicleID, Model, Age) and MaintenanceRecords (RecordID, VehicleID, MaintenanceDate)."
    ),
    (
        "Calculate the total and average duration of calls made by each customer in the last month, only including customers with more than 30 calls.",
        "CallLogs (LogID, CustomerID, Duration, CallDate) table holds call records for the last six months."
    ),
    (
        "Identify patients who have missed more than two appointments in the past six months and their last recorded blood pressure reading.",
        "patient_records (patient_id, name, birth_date), appointments (appointment_id, patient_id, appointment_date, status), medical_readings (reading_id, patient_id, reading_type, reading_value, reading_date)"
    ),
    (
        "Generate a summary report showing the total number of hours worked by each employee in the past year, broken down by month.",
        "employee (id, name), timesheet (employee_id, date_worked, hours_worked)"
    ),
    (
        "Find the top 5 most popular books based on checkout frequency in the last three months from a library database.",
        "books (book_id, title, author), checkouts (checkout_id, book_id, checkout_date, return_date)"
    ),
    (
        "List all suppliers who have not provided any products in the last year but were active suppliers the previous year.",
        "suppliers (supplier_id, name, status), supply_history (history_id, supplier_id, product_id, supply_date)"
    ),
    (
        "Calculate the average grade of students in each major, excluding any students who have withdrawn from the program.",
        "students (student_id, name, major, status), grades (grade_id, student_id, course_id, grade)"
    ),
    (
        "Determine which products have seen a price increase of more than 20% over the last six months.",
        "products (product_id, name, current_price), price_history (history_id, product_id, price, date_changed)"
    ),
    (
        "Identify the three least utilized conference rooms in an office building based on booking data from the last quarter.",
        "conference_rooms (room_id, name, capacity), bookings (booking_id, room_id, start_time, end_time)"
    ),
    (
        "Rank departments by the average number of sick days taken by employees last year.",
        "departments (department_id, name), employee_sick_days (record_id, employee_id, department_id, sick_date)"
    ),
    (
        "Create a report showing the monthly trend of customer complaints received, categorized by complaint type.",
        "complaints (complaint_id, customer_id, complaint_type, date_received)"
    ),
    (
        "Determine the flight route with the highest average delay time over the past year.",
        "flights (flight_id, route_id, scheduled_departure, actual_departure), routes (route_id, origin, destination)"
    ),
    (
        "Find the age group with the highest attendance in community events organized by the city council in the last two years.",
        "events (event_id, title, date), attendees (attendee_id, event_id, age_group)"
    ),
    (
        "Calculate the percentage of renewable energy sources used by each city in a region.",
        "cities (city_id, name), energy_usage (usage_id, city_id, source_type, amount_used)"
    ),
    (
        "Identify the most commonly prescribed medication in each hospital department over the last six months.",
        "departments (department_id, name, hospital_id), prescriptions (prescription_id, department_id, medication_id, date_prescribed), medications (medication_id, name)"
    ),
    (
        "Generate a list of all vehicles that have not undergone maintenance in over a year, including the vehicle model and last maintenance date.",
        "vehicles (vehicle_id, model, last_maintenance_date)"
    ),
    (
        "List the top 10 most borrowed authors in a university library and the number of times their books have been borrowed.",
        "authors (author_id, name), books (book_id, title, author_id), borrowings (borrowing_id, book_id, borrowing_date)"
    ),
    (
        "Calculate the total sales generated by each store location in the last financial quarter.",
        "stores (store_id, location), sales (sale_id, store_id, amount, sale_date)"
    ),
    (
        "Find employees who have switched departments more than twice within the last year, including their current department and total number of department changes.",
        "Employee records are stored in 'employee_details' (EmpID, Name, JoinDate) and department changes are logged in 'department_changes' (EmpID, OldDept, NewDept, ChangeDate)."
    ),
    (
        "Identify all books that have not been checked out in the past year from the library database, along with their authors and genres.",
        "The library system comprises 'books' (BookID, Title, Author, Genre) and 'checkouts' (CheckoutID, BookID, CheckoutDate, ReturnDate)."
    ),
    (
        "Generate a report of patients who missed more than three appointments in the last six months, including patient details and appointment dates.",
        "Patient information is in 'patient_info' (PatientID, Name, DOB) and appointment records are in 'appointments' (AppointmentID, PatientID, ScheduledDate, AttendedFlag)."
    ),
    (
        "Aggregate sales data to show monthly sales totals for each salesperson, only including months where they exceeded their sales quota.",
        "Sales data is split across 'monthly_sales' (SalespersonID, Month, TotalSales) and 'sales_targets' (SalespersonID, Month, SalesQuota)."
    ),
    (
        "List all students who are enrolled in courses taught by professors who have won a teaching award in the last 5 years.",
        "Student enrolments are in 'enrollments' (StudentID, CourseID), course details in 'courses' (CourseID, ProfessorID, CourseName), and professor awards in 'professor_awards' (ProfessorID, AwardYear)."
    ),
    (
        "Identify aircraft that have been used more than average and require maintenance, based on flight logs and maintenance records.",
        "Flight information is recorded in 'flight_logs' (FlightID, AircraftID, FlightDate) and maintenance details in 'maintenance_records' (RecordID, AircraftID, MaintenanceDate)."
    ),
    (
        "Extract a list of products that have seen a price increase but a decrease in sales over the past year.",
        "Product pricing history is maintained in 'price_history' (ProductID, Date, Price) and sales figures in 'sales_data' (SalesID, ProductID, SaleDate, QuantitySold)."
    ),
    (
        "Find all movies released in the last 10 years that have not been rented in the past month, including movie titles and release dates.",
        "The movie database has 'movies' (MovieID, Title, ReleaseDate) and rental transactions in 'rentals' (RentalID, MovieID, RentalDate)."
    ),
    (
        "Identify the top 5 most frequently diagnosed illnesses in each hospital department for the current year.",
        "Hospital records are split into 'patient_diagnoses' (DiagnosisID, PatientID, Illness, DiagnosisDate) and 'departments' (DeptID, DeptName, PatientID)."
    ),
    (
        "Create a list of vehicles that have failed more than two emissions tests in the past three years.",
        "Vehicle information is in 'vehicles' (VehicleID, Model, Make) and emissions test results in 'emissions_tests' (TestID, VehicleID, TestDate, PassFail)."
    ),
    (
        "Generate a list of students who have taken the same course multiple times but have never scored above a 'C' grade.",
        "Academic records include 'student_courses' (StudentID, CourseID, Grade) and 'course_catalog' (CourseID, CourseName, Department)."
    ),
    (
        "Identify restaurants that have consistently improved their health inspection scores over the past three inspections.",
        "Inspection data is found in 'health_inspections' (RestaurantID, InspectionDate, Score) and restaurant details in 'restaurants' (RestaurantID, Name, Location)."
    ),
    (
        "Identify employees who have not taken any vacation days in the past year, sorted by department.",
        "Employee table with ID, Name, Department, and VacationDays columns; Vacation table with EmployeeID, StartDate, EndDate."
    ),
    (
        "Find the average time spent by customers on support calls for each product, only including calls longer than 5 minutes.",
        "Database includes a Calls table with columns for CallID, CustomerID, ProductID, Duration, and a Products table with ProductID and Name."
    ),
    (
        "Generate a list of vehicles due for maintenance, based on a maintenance interval of 10,000 miles.",
        "The Vehicle table contains VehicleID, Model, LastMaintenanceMileage, and the TripLog table holds VehicleID, TripDate, MilesDriven."
    ),
    (
        "Create a report of students who have above-average grades but below-average attendance in each class.",
        "Two separate tables: Grades (StudentID, ClassID, Grade) and Attendance (StudentID, ClassID, AttendancePercent)."
    ),
    (
        "List all cities that have more than three suppliers but less than two customers, including the count of suppliers and customers.",
        "Supplier table (SupplierID, City) and Customer table (CustomerID, City), with no direct relationship between them."
    ),
    (
        "Determine the month with the highest number of returned products last year, categorized by product category.",
        "Tables include Returns (ReturnID, ProductID, ReturnDate) and Products (ProductID, Category)."
    ),
    (
        "Calculate the total sales made by employees who joined the company in the last five years, department-wise.",
        "EmployeeDetail table with EmployeeID, JoinDate, Department, and SalesRecord table with EmployeeID, SaleAmount."
    ),
    (
        "Identify the top 10 most frequently booked meeting rooms in the last quarter.",
        "MeetingRoom table containing RoomID, RoomName, and BookingLog table with BookingID, RoomID, BookingDate."
    ),
    (
        "List the top 5 best-selling authors, based on the number of books sold, in the genres of 'Science Fiction' and 'Fantasy'.",
        "A Books table with BookID, AuthorID, Genre, and a Sales table with SaleID, BookID, QuantitySold."
    ),
    (
        "Find the average patient age for each type of medical procedure performed last year.",
        "Patient table with PatientID, BirthDate, and ProcedureLog table with ProcedureID, PatientID, ProcedureDate."
    ),
    ("Calculate the average time spent by customers on each product page in the last month.",
     "In table 'page_visit_logs', columns include visit_id, customer_id, product_id, entry_time, exit_time."),    # Task 2
    ("Identify the top 5 best-selling products in each category for the current year.",
     "Columns in 'sales_data' table are product_id, category_id, quantity_sold, sale_date."),    # Task 3
    ("Generate a report of monthly revenue for each store location.",
     "Relevant columns in 'transactions' include transaction_id, store_id, amount, transaction_date."),    # Task 4
    ("List all employees who have not taken a vacation in the past year.",
     "Fields in 'employee_records' encompass employee_id, employee_name, vacation_days_taken, last_vacation_date."),    # Task 5
    ("Update the inventory to reflect the new stock after recent purchases.",
     "Table 'inventory' holds columns such as product_id, current_stock, last_updated."),    # Task 6
    ("Find all customers who have made more than 10 purchases but have never returned an item.",
     "Within 'customer_purchases', look at columns like customer_id, purchase_count, return_count."),    # Task 7
    ("Determine the average rating for products released in the last year.",
     "Refer to 'product_reviews' with columns including product_id, release_date, rating."),    # Task 8
    ("List the top 10 highest paying customers and their total spending.",
     "Examine 'customer_financials' with fields such as customer_id, total_spent, last_purchase_date."),    # Task 9
    ("Identify employees who have exceeded their sales targets for the last three quarters.",
     "Use 'sales_performance', which contains employee_id, quarterly_target, sales_achieved."),    # Task 10
    ("Calculate the total number of hours worked by each employee last month.",
     "In 'employee_timesheets', columns include employee_id, date, hours_worked."),    # Task 11
    ("Find all orders that were delayed by more than 5 days from their original shipping date.",
     "Columns in 'order_status' include order_id, expected_ship_date, actual_ship_date."),    # Task 12
    ("List the suppliers who have not delivered any products in the last six months.",
     "In 'supplier_deliveries', key columns are supplier_id, product_id, last_delivery_date."),    # Task 13
    ("Update product prices by 5% for all products that haven't been updated in over a year.",
     "Table 'product_pricing' consists of product_id, current_price, last_price_update."),    # Task 14
    ("Generate a list of all active products that are low in stock.",
     "Columns in 'product_inventory' relevant here are product_id, stock_level, status."),    # Task 15
    ("Create a report of all customer complaints received in the last quarter.",
     "Utilize 'customer_complaints' with fields like complaint_id, customer_id, date_received, issue_description."),    # Task 16
    ("Identify the most popular product in each category based on views.",
     "Refer to 'product_views', comprising columns such as product_id, category_id, view_count."),    # Task 17
    ("List all employees who have worked with the company for more than 5 years.",
     "In 'employee_details', consider columns like employee_id, hire_date, current_position."),    # Task 18
    ("Calculate the total revenue generated from top-tier customers this year.",
     "Use 'customer_sales', with fields such as customer_id, customer_tier, purchase_amount, purchase_date."),    # Task 19
    ("Identify products that have consistently received low ratings over the past six months.",
     "Check 'product_feedback' for columns like product_id, review_date, customer_rating."),    # Task 20
    ("Determine the average delivery time for products shipped internationally.",
     "In 'shipping_records', columns to look at are shipment_id, destination_country, dispatch_date, delivery_date."),
    ("Extract all product names and their respective categories from the products table where the stock is below 20.\nIn the products table, relevant columns include product_id, product_name, category, and stock.",
     "In the products table, relevant columns include product_id, product_name, category, and stock."),

    ("List the top 10 most expensive products in the inventory, based on unit price.\nColumns in the inventory table comprise item_id, item_name, unit_price, and quantity_available.",
     "Columns in the inventory table comprise item_id, item_name, unit_price, and quantity_available."),

    ("Find the average age of patients diagnosed with 'Diabetes' from the medical_records table.\nRelevant columns in medical_records include patient_id, diagnosis, age, and last_visit_date.",
     "Relevant columns in medical_records include patient_id, diagnosis, age, and last_visit_date."),

    ("Identify employees who have worked on more than 5 projects in the projects table.\nColumns of interest in the projects table are employee_id, project_id, start_date, end_date.",
     "Columns of interest in the projects table are employee_id, project_id, start_date, end_date."),

    ("Determine the total revenue generated per month in the current year from the sales_data table.\nIncluded columns in sales_data are transaction_id, transaction_date, amount, and customer_id.",
     "Included columns in sales_data are transaction_id, transaction_date, amount, and customer_id."),

    ("List all books that were checked out more than 3 times last month from the library_catalogue table.\nKey columns in library_catalogue include book_id, title, author, times_checked_out.",
     "Key columns in library_catalogue include book_id, title, author, times_checked_out."),

    ("Calculate the total hours worked by each employee last month from the timesheet table.\nTimesheet table includes employee_id, date, hours_worked, and project_code.",
     "Timesheet table includes employee_id, date, hours_worked, and project_code."),
    ("Count the number of products in each category from the product_details table.\nIn the product_details table, columns include product_id, product_name, category, price, stock_quantity.",
     "In the product_details table, columns include product_id, product_name, category, price, stock_quantity."),

    ("Identify patients with appointments scheduled next week in the clinic_schedule table.\nColumns in the clinic_schedule table are patient_id, patient_name, doctor_id, appointment_date, appointment_time.",
     "Columns in the clinic_schedule table are patient_id, patient_name, doctor_id, appointment_date, appointment_time."),

    ("Summarize total sales per month for the current year in the sales_data table.\nIncluded columns in the sales_data table are sales_id, product_id, sale_date, sale_amount.",
     "Included columns in the sales_data table are sales_id, product_id, sale_date, sale_amount."),

    ("List all books issued in the last month from the library_records table.\nFields in the library_records table consist of record_id, book_id, issue_date, return_date, member_id.",
     "Fields in the library_records table consist of record_id, book_id, issue_date, return_date, member_id."),

    ("Determine the average duration of completed projects from the project_management table.\nFeatured columns in the project_management table are project_id, project_name, start_date, end_date, status.",
     "Featured columns in the project_management table are project_id, project_name, start_date, end_date, status."),

    ("Extract the list of employees who have not taken any leave in the current year from the employee_leave_record table.\nAttributes in the employee_leave_record table include employee_id, employee_name, leave_start_date, leave_end_date, leave_type.",
     "Attributes in the employee_leave_record table include employee_id, employee_name, leave_start_date, leave_end_date, leave_type."),
    ("Identify customers with more than three transactions in the last month from the transactions table.\nIn the transactions table, the fields include transaction_id, customer_id, transaction_date, amount.",
     "In the transactions table, the fields include transaction_id, customer_id, transaction_date, amount."),

    ("Extract the list of products that have been discontinued from the product_details table.\nFields in the product_details table encompass product_id, product_name, supplier_id, category_id, quantity_per_unit, unit_price, units_in_stock, units_on_order, reorder_level, discontinued.",
     "Fields in the product_details table encompass product_id, product_name, supplier_id, category_id, quantity_per_unit, unit_price, units_in_stock, units_on_order, reorder_level, discontinued."),

    ("Update the address details for customers who have relocated, in the customer_info table.\nColumns present in the customer_info table are customer_id, customer_name, contact_name, address, city, postal_code, country.",
     "Columns present in the customer_info table are customer_id, customer_name, contact_name, address, city, postal_code, country."),

    ("Generate a report of all employees who have not taken any sick leave this year, using the employee_attendance table.\nContained within the employee_attendance table are columns like employee_id, employee_name, days_present, days_sick, year.",
     "Contained within the employee_attendance table are columns like employee_id, employee_name, days_present, days_sick, year."),

    ("List all suppliers that have not provided any products in the last six months from the supply_chain table.\nThe supply_chain table features columns such as supplier_id, supplier_name, product_id, last_supply_date.",
     "The supply_chain table features columns such as supplier_id, supplier_name, product_id, last_supply_date."),
    ("Identify products with less than 100 units in stock from the inventory table. Columns in inventory include product_id, product_name, category, stock_quantity.",
     "Columns in the inventory table are product_id, product_name, category, stock_quantity."),

    ("List all transactions exceeding $500 in the last month from the transactions table, which has fields transaction_id, customer_id, transaction_date, amount.",
     "Fields in the transactions table: transaction_id, customer_id, transaction_date, amount."),

    ("Update the status of all overdue orders to 'Delayed' in the orders table. This table comprises order_id, customer_id, order_date, due_date, status.",
     "Comprising fields in the orders table: order_id, customer_id, order_date, due_date, status."),

    ("Find the average stay duration of patients admitted this year from the hospital_data table, containing patient_id, admission_date, discharge_date.",
     "Contained columns in hospital_data: patient_id, admission_date, discharge_date."),

    ("Delete records of discontinued product lines from the products table, which includes product_id, product_name, price, status.",
     "Included columns in the products table: product_id, product_name, price, status."),

    ("Count the number of employees per department from the employee_details table, where columns are employee_id, name, department.",
     "Employee_details table columns: employee_id, name, department."),

    ("Select all customers who have not made any purchases in the last year from the customer_records table. It has customer_id, customer_name, last_purchase_date.",
     "Customer_records table fields: customer_id, customer_name, last_purchase_date."),

    ("Update contact information for suppliers in the supplier_info table. This table holds supplier_id, supplier_name, contact_number, email.",
     "Held columns in the supplier_info table: supplier_id, supplier_name, contact_number, email."),

    ("Extract a list of all high priority tasks due next week from the task_manager table, including task_id, task_description, priority, due_date.",
     "Included in the task_manager table: task_id, task_description, priority, due_date."),

    ("Generate a report of all active leases from the property_leases table, which contains lease_id, tenant_id, property_id, start_date, end_date, status.",
     "Property_leases table contains: lease_id, tenant_id, property_id, start_date, end_date, status."),
    ("Identify products with more than 100 units in stock from the inventory table.\nIn the inventory table, the columns include ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued.",
     "Columns in the inventory table: ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued."),

    ("List the details of all active employees who have worked for more than 5 years in the company from the employee_details table.\nIncluded columns in the employee_details table are EmployeeID, FirstName, LastName, Email, PhoneNumber, HireDate, JobID, Salary, CommissionPct, ManagerID, DepartmentID, Status.",
     "Columns in the employee_details table: EmployeeID, FirstName, LastName, Email, PhoneNumber, HireDate, JobID, Salary, CommissionPct, ManagerID, DepartmentID, Status."),

    ("Extract the total sales for each product category from the sales_data table.\nTable sales_data consists of columns: SaleID, ProductID, CategoryID, QuantitySold, SaleDate, SaleAmount.",
     "Column details of sales_data table: SaleID, ProductID, CategoryID, QuantitySold, SaleDate, SaleAmount."),

    ("Find all orders placed in the month of December 2020 from the order_records table.\nColumns present in the order_records table are OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate, ShipVia, Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry.",
     "Order_records table structure: OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate, ShipVia, Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry."),

    ("Update the status of all orders placed before 2018 to 'Archived' in the orders_archive table.\nOrders_archive table fields: OrderID, CustomerID, OrderDate, ShipDate, OrderStatus.",
     "Fields in orders_archive table: OrderID, CustomerID, OrderDate, ShipDate, OrderStatus."),

    ("Generate a report of customer complaints received in the last quarter from the customer_feedback table.\nColumns in the customer_feedback table include FeedbackID, CustomerID, FeedbackDate, FeedbackText, ResolutionStatus.",
     "Customer_feedback table composition: FeedbackID, CustomerID, FeedbackDate, FeedbackText, ResolutionStatus."),

    ("Calculate the average time taken to fulfill orders from the fulfillment_data table.\nFulfillment_data table includes columns: FulfillmentID, OrderID, OrderDate, FulfillmentStartDate, FulfillmentEndDate.",
     "Fulfillment_data table structure: FulfillmentID, OrderID, OrderDate, FulfillmentStartDate, FulfillmentEndDate."),

    ("List all suppliers who have not delivered any products in the last six months from the supplier_records table.\nSupplier_records table columns: SupplierID, SupplierName, ContactName, Address, City, PostalCode, Country, Phone.",
     "Columns of supplier_records table: SupplierID, SupplierName, ContactName, Address, City, PostalCode, Country, Phone."),

    ("Identify all employees who have not taken any leave in the current year from the employee_attendance table.\nEmployee_attendance table columns include EmployeeID, EmployeeName, Department, DateOfJoining, LeaveRecord.",
     "Structure of employee_attendance table: EmployeeID, EmployeeName, Department, DateOfJoining, LeaveRecord."),

    ("Determine the most popular product based on the number of orders from the product_orders table.\nIn the product_orders table, the fields are ProductID, ProductName, OrderID, OrderDate, Quantity.",
     "Product_orders table fields: ProductID, ProductName, OrderID, OrderDate, Quantity."),
    ("Identify products with less than 100 units in stock from the inventory table.\nIn the inventory table, columns include product_id, product_name, category, units_in_stock, and supplier_id.",
     "Columns in the inventory table are product_id, product_name, category, units_in_stock, and supplier_id."),

    ("List all employees who have been with the company for over 5 years in the staff table.\nColumns in the staff table encompass employee_id, name, role, hire_date, and department.",
     "The staff table includes columns such as employee_id, name, role, hire_date, and department."),

    ("Summarize total sales per region from the sales_data table for the current fiscal year.\nColumns present in the sales_data table include sale_id, region, amount, and sale_date.",
     "In the sales_data table, relevant columns are sale_id, region, amount, and sale_date."),

    ("Extract all customer feedback entries received in the last quarter from the feedback table.\nFeedback table's structure consists of feedback_id, customer_id, comments, and date_received.",
     "The feedback table is structured with columns like feedback_id, customer_id, comments, and date_received."),

    ("Update the status of all overdue orders in the orders table to 'Delayed'.\nColumns in the orders table comprise order_id, customer_id, due_date, status, and total_price.",
     "In the orders table, columns include order_id, customer_id, due_date, status, and total_price."),

    ("Retrieve the highest scoring students in each class from the grades table.\nWithin the grades table, columns are structured as grade_id, student_id, class_id, score, and date.",
     "The grades table features columns such as grade_id, student_id, class_id, score, and date."),

    ("Find all suppliers from the USA in the suppliers table.\nThe suppliers table includes supplier_id, supplier_name, contact_name, address, city, country, and phone.",
     "Columns in the suppliers table encompass supplier_id, supplier_name, contact_name, address, city, country, and phone."),

    ("Calculate the average hours worked per week by each employee from the timesheets table.\nTimesheets table's columns include timesheet_id, employee_id, week_starting, hours_worked.",
     "The timesheets table is organized with columns like timesheet_id, employee_id, week_starting, hours_worked."),

    ("List all products that have been discontinued from the products table.\nRelevant columns in the products table are product_id, product_name, supplier_id, category_id, quantity_per_unit, and discontinued.",
     "The products table features columns including product_id, product_name, supplier_id, category_id, quantity_per_unit, and discontinued."),

    ("Identify all transactions exceeding $1000 in the transactions table.\nColumns of the transactions table include transaction_id, account_id, transaction_date, amount, and transaction_type.",
     "The transactions table consists of columns such as transaction_id, account_id, transaction_date, amount, and transaction_type."),
    ("Identify products with stock levels below 20 in the inventory table.\nIn the inventory table, columns include product_id, product_name, category, stock_level, supplier_id.",
     "Columns in the inventory table are product_id, product_name, category, stock_level, supplier_id."),

    ("Summarize the total sales per month for the last year from the sales_data table.\nColumns in the sales_data table encompass sale_id, sale_date, product_id, quantity_sold, sale_amount.",
     "The sales_data table includes columns such as sale_id, sale_date, product_id, quantity_sold, sale_amount."),

    ("List all employees who have a birthday this month from the employee_details table.\nFeatured columns in employee_details include employee_id, name, position, department, birth_date.",
     "Employee details are stored in columns like employee_id, name, position, department, birth_date."),

    ("Extract the top 5 highest selling products from the product_sales table.\nProduct_sales table is structured with columns product_id, product_name, units_sold, total_revenue.",
     "Relevant columns in the product_sales table are product_id, product_name, units_sold, total_revenue."),

    ("Update the contact information of suppliers from the USA in the supplier_info table.\nSupplier_info table fields include supplier_id, supplier_name, contact_name, country, phone.",
     "Fields in the supplier_info table consist of supplier_id, supplier_name, contact_name, country, phone."),

    ("Delete records from the customer_feedback table that are older than two years.\nCustomer_feedback table has columns feedback_id, customer_id, feedback_date, comment.",
     "The customer_feedback table is structured with columns like feedback_id, customer_id, feedback_date, comment."),

    ("Retrieve the average duration of completed projects from the project_data table.\nColumns present in the project_data table are project_id, project_name, start_date, end_date, status.",
     "The project_data table holds columns such as project_id, project_name, start_date, end_date, status."),

    ("Find all transactions over $1000 from the transactions table made in the last month.\nThe transactions table comprises transaction_id, customer_id, transaction_date, amount.",
     "Included in the transactions table are fields like transaction_id, customer_id, transaction_date, amount."),

    ("Calculate the total number of hours worked by each employee last month from the timesheet table.\nTimesheet table columns include timesheet_id, employee_id, date, hours_worked.",
     "In the timesheet table, you'll find columns such as timesheet_id, employee_id, date, hours_worked."),

    ("Select all clients who have not made a purchase in the last six months from the client_records table.\nClient_records table includes columns client_id, client_name, last_purchase_date, total_purchases.",
     "Columns in the client_records table are client_id, client_name, last_purchase_date, total_purchases."),
    ("Identify the most popular product category based on the number of orders in the past month. Database table: product_orders; Columns: product_id, category_id, order_id, order_date.",
     "Database table: product_orders; Columns: product_id, category_id, order_id, order_date."),

    ("Extract a list of all employees with their managers. Database table: employee_hierarchy; Fields include: employee_id, employee_name, manager_id.",
     "Database table: employee_hierarchy; Fields include: employee_id, employee_name, manager_id."),

    ("Calculate the total revenue generated from each product category. Table for reference: sales_data; Column headers are: product_id, category_name, sale_amount.",
     "Table for reference: sales_data; Column headers are: product_id, category_name, sale_amount."),

    ("Fetch the details of customers who have not made any purchases in the last six months. Relevant table: customer_details; Column names include: customer_id, customer_name, last_purchase_date.",
     "Relevant table: customer_details; Column names include: customer_id, customer_name, last_purchase_date."),

    ("List all products that have been out of stock for more than 30 days. Source table: inventory_status; Contains columns: product_id, product_name, stock_status, last_stocked_date.",
     "Source table: inventory_status; Contains columns: product_id, product_name, stock_status, last_stocked_date."),

    ("Identify the top 5 highest earning employees this quarter. Table in use: payroll; Consists of: employee_id, name, quarterly_earnings.",
     "Table in use: payroll; Consists of: employee_id, name, quarterly_earnings."),

    ("Retrieve the average stay duration of guests in each hotel branch. Database table utilized: guest_stays; Columns present: branch_id, guest_id, check_in_date, check_out_date.",
     "Database table utilized: guest_stays; Columns present: branch_id, guest_id, check_in_date, check_out_date."),

    ("Calculate the average test score per class for the current academic year. Table name: academic_scores; Columns include: student_id, class_id, test_score, academic_year.",
     "Table name: academic_scores; Columns include: student_id, class_id, test_score, academic_year."),

    ("Generate a report of overdue library books. Table for querying: library_loans; Fields are: book_id, borrower_id, due_date, return_date.",
     "Table for querying: library_loans; Fields are: book_id, borrower_id, due_date, return_date."),

    ("Find the most frequently visited pages on a website for the last month. Data table: webpage_visits; Columns consist of: page_id, visit_date, visitor_id.",
     "Data table: webpage_visits; Columns consist of: page_id, visit_date, visitor_id."),
    ("Retrieve all employees in the Sales department from the employee_info table.\nThis table has columns: employee_id, employee_name, department.",
     "employee_info table columns: employee_id, employee_name, department."),
    
    ("Find the total revenue generated by the 'Electronics' category in the sales_data table.\nThe table: sales_data, columns: product_id, product_name, category, price, quantity_sold.",
     "sales_data table columns: product_id, product_name, category, price, quantity_sold."),
    
    ("List all the authors who have written more than 5 books from the authors_books table.\nTable: authors_books, columns: author_id, author_name, book_title.",
     "authors_books table columns: author_id, author_name, book_title."),
    
    ("Calculate the average rating of all movies in the movies_ratings table.\nTable: movies_ratings, columns: movie_id, movie_title, rating.",
     "movies_ratings table columns: movie_id, movie_title, rating."),
    
    ("Retrieve the top 10 highest-paid employees from the employee_salary table.\nTable: employee_salary, columns: employee_id, employee_name, salary.",
     "employee_salary table columns: employee_id, employee_name, salary."),
    
    ("Count the number of unique customers who made a purchase in the last month from the customer_orders table.\nTable: customer_orders, columns: customer_id, order_date, total_amount.",
     "customer_orders table columns: customer_id, order_date, total_amount."),
    
    ("Find the most popular product category based on the number of sales in the sales_data table.\nTable: sales_data, columns: product_id, product_name, category, price, quantity_sold.",
     "sales_data table columns: product_id, product_name, category, price, quantity_sold."),
    ("Delete all records with a price higher than $100 from the product_data table.", "The table contains columns: product_id, product_name, price."),
    
    ("Retrieve the names and contact information of customers who placed orders in the last week.", "The relevant tables have columns: customer_name, contact_info, order_date."),
    
    ("Calculate the total revenue generated by the 'Electronics' category in the sales_data table.", "The sales_data table includes columns for product_id, category, price, and quantity_sold."),
    
    ("List all employees in the HR department.", "The employee_data table includes information on employee_id, employee_name, and department."),
    
    ("Find authors who have written more than 5 books.", "The authors_books table contains data on author_id, author_name, and book_title."),
    
    ("Get the average rating of all movies in the movies_ratings table.", "The movies_ratings table includes movie_id, movie_title, and rating columns."),
    
    ("Count the number of unique customers who made a purchase in the last month.", "The customer_orders table contains customer_id, order_date, and total_amount."),
    
    ("Identify the most popular product category based on sales volume.", "The sales_data table includes information on product_id, product_name, category, price, and quantity_sold."),
    ("Delete all orders placed before 2022-01-01 from the orders table.",
     "The orders table contains columns: order_id, order_date, customer_id, total_amount."),
    
    ("Retrieve the names and email addresses of all customers who have made a purchase in the past month from the customers table.",
     "The customers table includes columns: customer_id, customer_name, email, purchase_date."),
    
    ("Calculate the total sales revenue for the 'Electronics' category in the sales_data table.",
     "The sales_data table has columns: product_id, product_name, category, price, quantity_sold."),
    
    ("List all employees in the HR department from the employee_info table.",
     "The employee_info table includes columns: employee_id, employee_name, department."),
    
    ("Count the number of unique products in the inventory table with a quantity greater than 10.",
     "The inventory table contains columns: product_id, product_name, quantity."),
    
    ("Find the average rating of movies in the movie_ratings table.",
     "The movie_ratings table has columns: movie_id, movie_title, rating."),
    
    ("Retrieve the names and addresses of all suppliers in the suppliers table.",
     "The suppliers table includes columns: supplier_id, supplier_name, address."),
    
    ("Summarize the average test scores by subject for students in grade 10.\nTable: student_scores, Columns: StudentID, GradeLevel, Subject, TestScore, TestDate.",
     "Table: student_scores, Columns: StudentID, GradeLevel, Subject, TestScore, TestDate."),

    ("Find the most frequently rented movie genre in 2021.\nDatabase Table: movie_rentals, Fields: RentalID, MovieTitle, Genre, RentalDate.",
     "Database Table: movie_rentals, Fields: RentalID, MovieTitle, Genre, RentalDate."),

    ("List all products that have been discontinued.\nSchema Details: Table - product_catalog, Columns include ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued.",
     "Schema Details: Table - product_catalog, Columns include ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued."),

    ("Retrieve the total number of hours worked by each employee last month.\nStructure: employee_timesheet, Fields include TimesheetID, EmployeeID, WorkDate, HoursWorked.",
     "Structure: employee_timesheet, Fields include TimesheetID, EmployeeID, WorkDate, HoursWorked."),

    ("Calculate the average length of hospital stays for patients over 65 years old.\nDataset: patient_admissions, Attributes: PatientID, AdmissionDate, DischargeDate, Age, Diagnosis.",
     "Dataset: patient_admissions, Attributes: PatientID, AdmissionDate, DischargeDate, Age, Diagnosis."),

    ("Identify customers with more than three late payments in the past year.\nTable Structure: payment_history, Columns: PaymentID, CustomerID, PaymentDate, Amount, LatePayment.",
     "Table Structure: payment_history, Columns: PaymentID, CustomerID, PaymentDate, Amount, LatePayment."),

    ("Determine the most popular travel destinations based on ticket sales.\nInformation Source: travel_tickets, Contains: TicketID, Destination, DepartureDate, ReturnDate, Price.",
     "Information Source: travel_tickets, Contains: TicketID, Destination, DepartureDate, ReturnDate, Price."),

    ("Extract a list of suppliers who have not delivered any products in the last six months.\nTable Reference: supplier_deliveries, Columns Present: SupplierID, ProductID, DeliveryDate, Quantity.",
     "Table Reference: supplier_deliveries, Columns Present: SupplierID, ProductID, DeliveryDate, Quantity."),
    ("For patients with a last visit date in 2021, update their status to 'Inactive'.\nIn the database, patient information is stored in a table named 'patient_records', which includes columns: PatientID, Name, LastVisitDate, Status.",
     "In the 'patient_records' table, columns include PatientID, Name, LastVisitDate, Status."),
    
    ("List all products that have been out of stock for more than 30 days.\nThe product inventory details are maintained in a table called 'inventory', with fields including ProductID, ProductName, StockDate, Quantity.",
     "Fields in the 'inventory' table include ProductID, ProductName, StockDate, Quantity."),
    
    ("Retrieve the average exam scores for students in the Mathematics department.\nStudent exam scores are cataloged in 'exam_scores' table, which has columns like StudentID, Department, ExamScore.",
     "Columns in the 'exam_scores' table include StudentID, Department, ExamScore."),
    
    ("Find the total number of flights delayed due to weather last year.\nFlight information is tracked in the 'flight_status' table, which encompasses FlightID, Date, Status, DelayReason.",
     "The 'flight_status' table encompasses FlightID, Date, Status, DelayReason."),
    
    ("Update the rental status of all books returned this week to 'Available'.\nLibrary book rentals are logged in a table named 'book_rentals', containing BookID, RentalDate, ReturnDate, RentalStatus.",
     "Contained within the 'book_rentals' table are BookID, RentalDate, ReturnDate, RentalStatus."),
    
    ("Count the number of transactions exceeding $500 in the last month.\nTransaction details are recorded in 'transactions' table, featuring columns TransactionID, Date, Amount.",
     "Featured columns in the 'transactions' table include TransactionID, Date, Amount."),
    
    ("Identify employees who have not completed mandatory training courses.\nEmployee training records are in 'training_completion', with fields EmployeeID, CourseID, CompletionStatus, CompletionDate.",
     "Fields in the 'training_completion' include EmployeeID, CourseID, CompletionStatus, CompletionDate."),
    ("List all patients diagnosed with diabetes since 2018.\nIn the 'medical_records' table, columns include PatientID, Diagnosis, DiagnosisDate, Treatment.",
     "Columns in 'medical_records' include PatientID, Diagnosis, DiagnosisDate, Treatment."),

    ("Find all books published by 'Orion Publishing' in the last five years.\nColumns in the 'library_catalog' table are BookID, Title, Author, Publisher, PublishDate.",
     "Table 'library_catalog' has columns BookID, Title, Author, Publisher, PublishDate."),

    ("Retrieve the top 10 highest scoring students in the 2022 final exams.\nHeaders in the 'student_performance' table are StudentID, Name, Subject, Score, ExamYear.",
     "The 'student_performance' table has headers StudentID, Name, Subject, Score, ExamYear."),

    ("Summarize the total working hours per week for each employee.\nFields in 'timesheet' table include EmployeeID, WeekStarting, HoursWorked.",
     "'timesheet' table fields: EmployeeID, WeekStarting, HoursWorked."),

    ("Identify vehicles with more than 100,000 miles serviced in the past year.\nRelevant columns in 'service_records' are VehicleID, Mileage, ServiceDate.",
     "In 'service_records', columns include VehicleID, Mileage, ServiceDate."),

    ("Count the number of flights delayed by over 2 hours last month.\nIncluded in 'flight_logs' table are FlightNumber, ScheduledDeparture, ActualDeparture.",
     "'flight_logs' table includes FlightNumber, ScheduledDeparture, ActualDeparture."),

    ("List all current projects with budgets exceeding $1 million.\nIn 'project_finances' table, columns are ProjectID, ProjectName, Budget, StartDate, EndDate.",
     "'project_finances' table consists of ProjectID, ProjectName, Budget, StartDate, EndDate."),
    ("Retrieve the average score of all students in the 'Mathematics' course.\nIn the database, this information is located in the 'grades' table, which includes columns: StudentID, CourseName, Score, Semester.",
     "In the database, the 'grades' table includes columns: StudentID, CourseName, Score, Semester."),

    ("List all books published after 2010 by 'Orion Publishing Group'.\nRelevant data is stored in the 'books' table, with fields including: BookID, Title, Author, PublishYear, Publisher.",
     "Relevant data is stored in the 'books' table, with fields including: BookID, Title, Author, PublishYear, Publisher."),

    ("Find the number of flights delayed due to weather conditions.\nData regarding flight schedules is contained in the 'flight_status' table, which has headers: FlightNumber, DepartureTime, ArrivalTime, Status, DelayReason.",
     "Data regarding flight schedules is contained in the 'flight_status' table, which has headers: FlightNumber, DepartureTime, ArrivalTime, Status, DelayReason."),

    ("Summarize the total hours worked per employee last month.\nEmployee work records are found in the 'work_hours' table, consisting of columns: EmployeeID, Date, HoursWorked.",
     "Employee work records are found in the 'work_hours' table, consisting of columns: EmployeeID, Date, HoursWorked."),

    ("Identify patients over 65 with high blood pressure.\nPatient medical records are in the 'patient_health' table, featuring columns: PatientID, Age, Condition, LastCheckupDate.",
     "Patient medical records are in the 'patient_health' table, featuring columns: PatientID, Age, Condition, LastCheckupDate."),

    ("Display the top 5 most viewed products on the website this month.\nProduct view statistics are captured in the 'product_views' table, which has the following headers: ProductID, ViewDate, ViewCount.",
     "Product view statistics are captured in the 'product_views' table, which has the following headers: ProductID, ViewDate, ViewCount."),

    ("Calculate the average property prices in 'Downtown' neighborhood last year.\nThis data is available in the 'real_estate_prices' table, including columns: PropertyID, Neighborhood, SalePrice, SaleDate.",
     "This data is available in the 'real_estate_prices' table, including columns: PropertyID, Neighborhood, SalePrice, SaleDate."),

    ("Extract the list of all authors who have published more than 5 books.\nThe 'author_publications' table stores this information, with columns: AuthorID, BookID, PublishDate.",
     "The 'author_publications' table stores this information, with columns: AuthorID, BookID, PublishDate."),
    ("Determine the average time spent by patients in the hospital during 2019, segmented by department.\nIn the database, patient stay information is stored in 'hospital_stays'. Columns include PatientID, AdmitDate, DischargeDate, Department.",
     "Database 'hospital_stays' details patient admissions with columns: PatientID, AdmitDate, DischargeDate, Department."),

    ("Extract the list of products that have been discontinued but still have a remaining stock in any warehouse.\nData about products is found in 'product_inventory'. Relevant columns are ProductID, ProductName, Discontinued, StockQuantity, WarehouseID.",
     "The 'product_inventory' table tracks product details and stock, with columns: ProductID, ProductName, Discontinued, StockQuantity, WarehouseID."),

    ("Identify students who have not enrolled in any courses for the past two semesters but are not listed as graduated.\nStudent enrollment records are in 'student_enrollments', with fields StudentID, CourseID, Semester, Status. Graduation status is in 'student_status', with fields StudentID, Graduated.",
     "Tables involved: 'student_enrollments' (StudentID, CourseID, Semester, Status) and 'student_status' (StudentID, Graduated)."),

    ("Calculate the month-over-month growth rate of sales for each product category since the beginning of last year.\nSales data is stored in 'sales_records'. This table includes SalesID, SaleDate, Category, Amount. Monthly totals should be computed.",
     "'sales_records' table comprises SalesID, SaleDate, Category, Amount, used for analyzing sales growth by category."),

    ("Find the most frequent service issues reported in the last quarter, categorized by product type.\nService issues are logged in the 'service_tickets' table, including TicketID, IssueDate, ProductType, IssueDescription.",
     "In 'service_tickets' (TicketID, IssueDate, ProductType, IssueDescription), analyze common issues by product type."),
    ("For patients diagnosed with diabetes after 2018, list their medication history including dosage and frequency.\nIn the database, patient details are stored in 'patient_details' with columns: PatientID, Name, BirthDate, and medication records in 'medication_history' with columns: PatientID, MedicationName, Dosage, Frequency, StartDate.",
     "Database includes 'patient_details' with columns: PatientID, Name, BirthDate; and 'medication_history': PatientID, MedicationName, Dosage, Frequency, StartDate."),

    ("Extract a list of all books that were checked out more than three times last month, including the borrower's details.\nTables involved: 'book_loans' with BookID, UserID, CheckoutDate, ReturnDate; and 'user_profiles' with UserID, UserName, Address, Email.",
     "Tables: 'book_loans' (BookID, UserID, CheckoutDate, ReturnDate); 'user_profiles' (UserID, UserName, Address, Email)."),

    ("Determine the average duration of calls made by users under 30 from the 'call_records' table, along with their most frequented call destinations.\nRelevant tables: 'call_records' with CallID, UserID, Duration, Destination, Date; 'user_info' with UserID, Name, Age.",
     "Tables: 'call_records' (CallID, UserID, Duration, Destination, Date); 'user_info' (UserID, Name, Age)."),

    ("Identify top-selling products each month in the past year and their respective salesperson details.\nInvolved tables: 'sales_data' comprising ProductID, SalespersonID, SaleAmount, SaleDate; 'salesperson_info' with SalespersonID, Name, Region.",
     "Data spans 'sales_data' (ProductID, SalespersonID, SaleAmount, SaleDate) and 'salesperson_info' (SalespersonID, Name, Region)."),

    ("List all courses that haven't been offered in the last two years but had an enrollment of over 100 students.\nDatabase contains 'course_catalog' with CourseID, Title, LastOfferedDate and 'enrollment_records' with CourseID, EnrollmentCount.",
     "Database structure: 'course_catalog' (CourseID, Title, LastOfferedDate); 'enrollment_records' (CourseID, EnrollmentCount)."),

    ("Calculate the average patient wait time per doctor in the last quarter and compare it with the same period in the previous year.\nTables include 'appointment_records' with DoctorID, PatientID, AppointmentDate, WaitTime and 'doctor_profiles' with DoctorID, Name, Specialty.",
     "Tables available: 'appointment_records' (DoctorID, PatientID, AppointmentDate, WaitTime); 'doctor_profiles' (DoctorID, Name, Specialty).")
]

more_task_and_environment2 = \
[
    ("Calculate the total revenue generated from each product line in the previous fiscal year.",
     "Table: 'financial_records', Columns include 'ProductLineID', 'SaleAmount', 'SaleDate'."),

    ("Determine the number of flights delayed due to weather conditions last winter.",
     "In 'airport_operations', fields are 'FlightID', 'ScheduledDeparture', 'ActualDeparture', 'DelayReason'."),

    ("Summarize customer purchasing trends by age group for the past quarter.",
     "Data found in 'customer_purchases', with fields like 'PurchaseID', 'CustomerAge', 'PurchaseDate', 'Amount'."),

    ("Identify the top-performing sales representatives based on the total sales volume this year.",
     "Sales data captured in 'sales_performance', including 'RepresentativeID', 'TotalSales', 'Year'."),

    ("List the books that have been borrowed the most from the library in the past month.",
     "Library database 'book_loans', fields include 'BookID', 'LoanDate', 'ReturnDate', 'TimesBorrowed'."),

    ("Calculate the average time spent by visitors on each exhibit in the museum.",
     "Visitor logs in 'exhibit_interactions', columns 'ExhibitID', 'VisitorID', 'TimeSpent'."),

    ("Retrieve the list of patients who missed their appointments more than twice last year.",
     "Patient records in 'appointment_history', fields 'PatientID', 'AppointmentDate', 'Status'."),

    ("Assess the yearly growth in the number of active users on the online platform.",
     "User activity stored in 'user_engagement', including 'UserID', 'LastActiveDate', 'SignUpDate'."),

    ("Determine the most common maintenance issues reported for the company fleet vehicles.",
     "Vehicle maintenance data in 'fleet_records', with 'VehicleID', 'IssueType', 'ReportDate'."),

    ("Track the progress of ongoing construction projects and their expected completion dates.",
     "Project details in 'construction_schedule', columns 'ProjectID', 'StartDate', 'ProjectedEndDate'."),

    ("Evaluate the efficiency of different marketing campaigns based on customer conversion rates.",
     "Marketing data in 'campaign_results', fields include 'CampaignID', 'CustomerID', 'ConversionRate', 'CampaignStartDate'."),

    ("Analyze the frequency of network outages in different regions over the past year.",
     "Network data captured in 'outage_reports', including fields like 'RegionID', 'OutageStart', 'OutageEnd', 'Duration'."),

    ("Summarize the average patient satisfaction scores across various hospital departments.",
     "Patient feedback stored in 'hospital_reviews', columns 'DepartmentID', 'PatientID', 'SatisfactionScore', 'ReviewDate'."),

    ("List all properties sold in the downtown area within the last six months.",
     "Real estate transactions in 'property_sales', fields include 'PropertyID', 'SaleDate', 'Location', 'SalePrice'."),

    ("Identify the most common reasons for customer service calls last quarter.",
     "Call center data in 'service_calls', columns 'CallID', 'ReasonForCall', 'CallDate', 'ResolutionTime'."),

    ("Calculate the average daily production output of each manufacturing unit this year.",
     "Production details in 'manufacturing_output', including 'UnitID', 'Date', 'TotalOutput'."),

    ("Assess the frequency and types of medication errors reported in the hospital.",
     "Medical records in 'medication_errors', fields 'ErrorID', 'MedicationID', 'ReportDate', 'ErrorType'."),

    ("Track the average attendance rate of students in online classes this semester.",
     "Educational data stored in 'class_attendance', with columns 'ClassID', 'StudentID', 'AttendanceDate', 'AttendanceStatus'."),

    ("Determine the average repair cost for different types of electronic devices.",
     "Repair records in 'device_repairs', fields include 'DeviceType', 'RepairDate', 'RepairCost'."),

    ("Analyze the change in water consumption patterns in the city over the past five years.",
     "Water usage data in 'consumption_records', including 'ConsumerID', 'Year', 'MonthlyUsage'."),

    ("Summarize the response times of emergency services in various districts.",
     "Emergency response data in 'response_times', columns 'ServiceID', 'DistrictID', 'CallTime', 'ResponseTime'."),

    ("Identify the most frequently visited tourist attractions in the last summer season.",
     "Tourism data in 'attraction_visits', fields 'AttractionID', 'VisitDate', 'VisitorCount'."),
    ("Calculate the total sales volume by region for the previous fiscal year.",
     "Table: regional_sales, Includes: RegionID, SaleAmount, SaleDate, ProductID."),
    
    ("Determine the average age of patients diagnosed with diabetes.",
     "Patient records in: health_data, Fields: PatientID, BirthDate, DiagnosisDate, DiagnosisType."),
    
    ("List the employees who have not taken any sick leave this year.",
     "Sick leave records found in: employee_attendance, Contains: EmployeeID, SickLeaveTaken, Date."),
    
    ("Find the three most frequently visited pages on the website.",
     "Website traffic stored in: web_traffic, With Columns: PageID, VisitCount, VisitDate."),
    
    ("Identify the products with the highest increase in price over the last six months.",
     "Price history in: product_pricing, Columns: ProductID, PriceChangeDate, OldPrice, NewPrice."),
    
    ("Summarize the total duration of customer service calls for each representative.",
     "Call logs in: customer_service_calls, Details: RepresentativeID, CallDuration, CallDate."),
    
    ("Extract the list of books that have been issued more than 50 times in the library.",
     "Library lending data: book_issues, Information: BookID, IssueCount, LastIssuedDate."),
    
    ("Calculate the average number of products sold per transaction last quarter.",
     "Transaction details in: sales_transactions, Contains: TransactionID, NumberOfProducts, SaleDate."),
    
    ("List the departments with more than 10% employee turnover last year.",
     "Employee turnover data: department_turnover, Columns: DepartmentID, TurnoverPercentage, Year."),
    
    ("Identify the customers who have made purchases over $1000 in total.",
     "Customer purchase records: customer_purchases, Includes: CustomerID, TotalPurchaseAmount."),
    ("Sum the total revenue generated from online sales this year.",
     "Table 'online_sales', containing columns: SaleID, ProductID, SaleAmount, SaleDate."),
    
    ("Find employees who have not taken any leave this year.",
     "In 'employee_leave_records', fields include: EmployeeID, LeaveStartDate, LeaveEndDate."),
    
    ("List all products with less than 10 units left in stock.",
     "Inventory details in 'stock_levels', with columns: ProductID, UnitsInStock, LastStockCheckDate."),
    
    ("Determine the number of customer support tickets resolved within 24 hours.",
     "Support ticket log 'customer_support', fields: TicketID, IssueReported, ResolutionTime, Status."),
    
    ("Calculate the average delivery time for orders shipped last month.",
     "Order shipment table 'order_delivery', columns include: OrderID, ShipmentDate, DeliveryDate."),
    
    ("Identify the most commonly prescribed medication in the cardiology department.",
     "Medication records in 'prescriptions', with fields: PrescriptionID, MedicationID, Department, PrescribingDate."),
    
    ("List the employees who have worked on more than three projects this year.",
     "Project assignment details in 'project_assignments', columns: EmployeeID, ProjectID, AssignmentDate."),
    
    ("Display the total number of sold units for each product category.",
     "Sales data stored in 'category_sales', with fields: CategoryID, ProductID, UnitsSold."),
    
    ("Determine the average age of patients admitted to the emergency department.",
     "Patient records in 'emergency_admissions', containing: PatientID, AdmissionDate, BirthDate."),
    
    ("List the top 10 most active users on the platform based on login frequency.",
     "User activity log 'user_logins', columns include: UserID, LoginDate, NumberOfLogins."),

    ("Calculate the total sales for each category in the previous year.",
     "Table: 'yearly_sales', Includes columns: 'CategoryID', 'SaleAmount', 'SaleYear'."),

    ("Identify employees with tenure longer than five years.",
     "Contained in: 'staff_records', Fields: 'ID', 'Name', 'JoiningDate'."),

    ("Rank the top five highest-priced in-stock products.",
     "In the 'inventory_list', with 'ProductPrice', 'StockStatus' among other fields."),

    ("Average customer ratings per service department.",
     "Database: 'service_ratings', Key Columns: 'DeptID', 'CustomerRating'."),

    ("Report weekend transactions from the previous month.",
     "Logs found in 'transaction_history', Key Details: 'TransDate', 'Amount'."),

    ("Monthly new customer acquisition count for the current year.",
     "Data source: 'customer_acquisition', Relevant columns: 'SignUpDate', 'CustomerID'."),

    ("Total items sold by each supplier.",
     "Table: 'supplier_sales', Key information includes 'SupplierName', 'ItemsSold'."),

    ("Most popular product categories based on website views last quarter.",
     "Website data in 'category_views', Fields: 'Category', 'Views', 'Quarter'."),

    ("Total working hours of employees this quarter.",
     "Recorded in 'employee_hours', with 'EmployeeNumber', 'HoursWorked', 'Quarter'."),

    ("Suppliers with no activity for more than 12 months.",
     "Details in 'supplier_activity', including 'SupplierName', 'LastOrderDate'."),

    ("Calculate the total sales by region for the current year.",
     "Table: regional_sales, Columns include: SaleID, Region, SaleAmount, SaleDate"),

    ("Determine the average number of days for order delivery.",
     "Order tracking system: Contains OrderID, DispatchDate, DeliveryDate"),

    ("List all employees who have not taken any sick leave this year.",
     "Employee records: Fields - EmployeeID, Name, SickLeavesTaken"),

    ("Find the top three most frequently ordered products.",
     "Order details table with ProductID, OrderID, Quantity, and OrderDate"),

    ("Retrieve the list of all active clients who have not placed an order in the last six months.",
     "Client activity database: Includes ClientID, LastOrderDate, Status"),

    ("Calculate the average monthly electricity usage for all properties in the database.",
     "Property usage log: Fields cover PropertyID, Month, Year, ElectricityUsed"),

    ("Identify the departments with the highest employee turnover last year.",
     "Human resources database: Includes Department, EmployeeID, JoiningDate, ExitDate"),

    ("Generate a list of books that have been checked out more than 50 times.",
     "Library system: Table contains BookID, Title, TimesCheckedOut"),

    ("Summarize the average customer waiting time by branch for a service company.",
     "Customer service log: Fields - BranchID, CustomerID, WaitingTime, Date"),

    ("List the courses with the highest student enrollment in the past semester.",
     "Academic records: Comprises CourseID, CourseName, EnrollmentNumber, Semester"),

    ("Determine the most viewed product during the holiday season.",
     "Table: holiday_sales, Columns include: ProductID, Views, SaleDate."),
    
    ("Calculate the year-over-year growth in sales for each region.",
     "Database: annual_sales, Tables: Sales2019, Sales2020, Columns in each table: RegionID, TotalSales."),
    
    ("Identify the top three performing sales representatives based on total sales volume.",
     "Schema: sales_performance, Columns: SalesRepID, SalesAmount, SaleDate."),
    
    ("Summarize the monthly electricity usage for each customer.",
     "Energy usage dataset: customer_usage, Fields: CustomerID, Usage, BillingMonth."),
    
    ("List the courses with the highest enrollment in the Spring semester.",
     "Education database: course_enrollment, Tables: Courses, Enrollment, Course fields: CourseID, CourseName, Semester."),
    
    ("Retrieve the history of room bookings for a given conference hall.",
     "Booking system: hall_reservations, Fields: HallID, BookingDate, EventName, CustomerID."),
    
    ("Compute the average time taken to resolve customer complaints.",
     "Customer service data: complaint_resolution, Columns: ComplaintID, ReceivedDate, ResolvedDate."),
    
    ("Extract the list of all medical procedures conducted in the last month.",
     "Hospital records: procedures_conducted, Fields: ProcedureID, PatientID, ProcedureDate."),
    
    ("Analyze the distribution of grades in the final exams across all departments.",
     "Academic records: exam_results, Columns: StudentID, Department, ExamScore, ExamDate."),
    
    ("Assess the flight punctuality performance for each airline last year.",
     "Air travel statistics: flight_data, Fields: AirlineID, FlightDate, ScheduledDeparture, ActualDeparture."),

    ("Calculate the total sales by each product category in the previous year.",
     "Table: sales, with columns including Category, SaleAmount, DateOfSale."),

    ("Identify staff members who joined before 2018.",
     "In the table staff_info, fields include ID, Name, DateJoined."),

    ("Rank the five highest-priced in-stock items.",
     "Inventory table: item_list, containing ItemID, Name, Price, StockQuantity."),

    ("Compute the average customer rating for services offered, categorized by department.",
     "Feedback table: service_ratings, with Department, CustomerRating, DateRecorded."),

    ("Report all transactions from weekends in the past month.",
     "Transaction log table, fields: ID, TransactionDate, TransactionAmount, CustomerID."),

    ("Monthly new customer acquisition counts for the current year.",
     "In the new_customer_data table, columns include CustomerID and DateJoined."),

    ("Aggregate sales volume for each vendor.",
     "Sales records in vendor_sales table, with VendorID, SoldItemID, UnitsSold."),

    ("Identify the most frequently visited product categories on the website for the last quarter.",
     "Web traffic table: site_visits, includes CategoryID, VisitDate, NumberOfVisits."),

    ("Sum up total work hours by each employee for the current quarter.",
     "In the work_schedule table, fields: EmployeeID, DateWorked, Hours."),

    ("List suppliers with no transactions in the past 12 months.",
     "Supplier transaction record: supplier_activity, columns include SupplierID, LastTransactionDate."),

    ("Calculate the standard deviation of daily sales over the past year.",
     "Table: 'daily_sales', Columns: 'SaleDate', 'TotalSales'."),

    ("Determine the correlation between product ratings and sales figures.",
     "Tables: 'product_sales' (Columns: 'ProductID', 'SalesAmount'), 'product_ratings' (Columns: 'ProductID', 'Rating')."),

    ("Identify products whose sales have grown by more than 50% compared to the previous year.",
     "Table: 'annual_sales', Columns: 'ProductID', 'Year', 'SalesAmount'."),

    ("Compute the average time spent by customers on each product page and its impact on sales.",
     "Tables: 'page_visit_duration' (Columns: 'ProductID', 'TimeSpent'), 'product_sales' (Columns: 'ProductID', 'SalesAmount')."),

    ("Find the month-over-month percentage change in new customer sign-ups.",
     "Table: 'customer_signups', Columns: 'SignupDate', 'CustomerID'."),

    ("Calculate the employee performance index based on tasks completed and customer feedback.",
     "Tables: 'employee_tasks' (Columns: 'EmployeeID', 'TaskID', 'CompletionStatus'), 'customer_feedback' (Columns: 'EmployeeID', 'FeedbackScore')."),

    ("Analyze the variance in order processing time across different product categories.",
     "Tables: 'orders' (Columns: 'OrderID', 'ProductCategory', 'ProcessingTime')."),

    ("Determine the three departments with the highest employee turnover rate.",
     "Tables: 'employee_records' (Columns: 'EmployeeID', 'DepartmentID', 'JoinDate', 'LeaveDate')."),

    ("Compute the year-over-year growth rate in total expenses for each department.",
     "Table: 'department_expenses', Columns: 'DepartmentID', 'Year', 'TotalExpenses'."),

    ("Evaluate the seasonal variation in hotel booking cancellations.",
     "Table: 'hotel_bookings', Columns: 'BookingID', 'CancellationDate', 'Season'."),

    ("Assess the linear trend in monthly production output over the past five years.",
     "Table: 'production_data', Columns: 'Month', 'Year', 'Output'."),

    ("Calculate the weighted average customer satisfaction score, considering the number of transactions per customer.",
     "Tables: 'customer_satisfaction' (Columns: 'CustomerID', 'SatisfactionScore'), 'transaction_history' (Columns: 'CustomerID', 'NumberOfTransactions')."),
    
    ("Calculate the standard deviation of monthly sales for each product over the past year.",
     "In the 'monthly_sales' table, key columns include 'ProductID', 'Month', 'Year', 'SalesAmount'."),

    ("Determine the average time spent by customers on support calls last month.",
     "Data is stored in 'customer_support_calls', with fields 'CallID', 'CustomerID', 'CallDuration', 'CallDate'."),

    ("Identify the product category with the highest variability in monthly sales.",
     "Schema: 'product_sales', Columns: 'CategoryID', 'Month', 'SalesVolume'."),

    ("Compute the year-over-year growth rate in sales for each region.",
     "In 'regional_sales', columns include 'RegionID', 'Year', 'TotalSales'."),

    ("Find employees with a performance score variance higher than the department average.",
     "Employee performance data in 'employee_performance', fields 'EmployeeID', 'DepartmentID', 'PerformanceScore'."),

    ("Analyze the trend of ticket response times over the past six months.",
     "Data found in 'support_tickets', columns 'TicketID', 'CreationDate', 'ResolutionDate'."),

    ("Calculate the average age of patients at the time of their first appointment.",
     "Patient records in 'patient_appointments', with 'PatientID', 'BirthDate', 'FirstAppointmentDate'."),

    ("Determine the month with the highest fluctuation in flight ticket prices last year.",
     "Flight pricing data in 'flight_prices', fields include 'FlightID', 'Month', 'TicketPrice'."),

    ("Analyze the variance in weekly working hours for remote vs. office employees.",
     "In 'employee_work_hours', columns are 'EmployeeID', 'WorkType', 'Week', 'HoursWorked'."),

    ("Calculate the standard deviation of order processing times for each product category.",
     "Order processing data in 'order_details', with columns 'OrderID', 'ProductCategory', 'ProcessingTime'."),

    ("Assess the fluctuation in monthly rental prices in different city districts.",
     "Rental market data in 'rental_prices', including 'DistrictID', 'Month', 'RentalPrice'."),

    ("Evaluate the variability in daily foot traffic in shopping malls over the last quarter.",
     "Shopping mall traffic data in 'mall_traffic', fields 'MallID', 'Date', 'VisitorCount'."),
    
    ("Calculate the total sales amount for each product category last year.",
     "Database 'sales_data' contains 'ProductID' (identifier for each product), 'CategoryID' (classifying products into categories), 'SaleDate' (date of sale), and 'SaleAmount' (total value of each sale)."),

    ("Identify employees who have been with the company for more than 5 years.",
     "In the 'employee_details' database, 'EmployeeID' uniquely identifies each employee, 'Name' provides the employee's full name, and 'HireDate' records the date when the employee joined the company."),
    
    ("List the top 5 most expensive products that are in stock.",
     "The 'products' table tracks inventory, including 'ProductID' (unique product identifier), 'ProductName' (name of the product), 'UnitPrice' (price per unit), and 'UnitsInStock' (available quantity in stock)."),
    
    ("Find the average customer satisfaction rating for each service department.",
     "The 'customer_feedback' table includes 'DepartmentID' (identifying various service departments), 'Rating' (customer satisfaction score), and 'FeedbackDate' (date when the feedback was provided)."),
    
    ("Generate a report of all transactions that occurred on weekends last month.",
     "The 'transaction_log' records transactions, with 'TransactionID' (unique identifier for each transaction), 'Date' (date of transaction), 'Amount' (transaction value), and 'CustomerID' (identifying the customer involved)."),
    
    ("Display the number of new customers acquired each month this year.",
     "In 'new_customers', each entry includes 'CustomerID' (unique identifier for customers) and 'AcquisitionDate' (date when the customer was acquired)."),
    
    ("Summarize the total number of items sold by each vendor.",
     "The 'sales_by_vendor' database contains 'VendorID' (identifying each vendor), 'ProductID' (identifying sold products), and 'QuantitySold' (number of units sold by the vendor)."),
    
    ("Identify the most viewed product categories on the website last quarter.",
     "In 'page_views', data includes 'CategoryID' (identifying product category), 'ViewDate' (date of page view), and 'ViewCount' (number of times the category page was viewed)."),
    
    ("Calculate the total hours worked by each employee this quarter.",
     "The 'work_hours' table logs work hours with 'EmployeeID' (employee identifier), 'WorkDate' (date of work), and 'HoursWorked' (total hours worked on that date)."),
    
    ("List all suppliers that have been inactive for over a year.",
     "In 'supplier_status', entries consist of 'SupplierID' (unique identifier for suppliers) and 'LastActivityDate' (date of the supplier's last activity)."),

    ("Calculate the total sales amount for each product category last year.",
     "The 'sales_data' table contains detailed records of each sale, with columns for 'ProductID' identifying the product, 'CategoryID' specifying the product category, 'SaleDate' indicating when the sale occurred, and 'SaleAmount' representing the monetary value of each sale."),
    
    ("Identify employees who have been with the company for more than 5 years.",
     "The 'employee_details' database provides a comprehensive record of all employees, including 'EmployeeID' as a unique identifier for each employee, their 'Name', and 'HireDate' which indicates the date when the employee joined the company."),
    
    ("List the top 5 most expensive products that are in stock.",
     "In the 'products' inventory table, each product is listed with a unique 'ProductID', its 'ProductName', 'UnitPrice' which indicates the cost per unit, and 'UnitsInStock' showing the current stock levels."),
    
    ("Find the average customer satisfaction rating for each service department.",
     "The 'customer_feedback' table records customer ratings for various service departments. It includes 'DepartmentID' for identifying the department, 'Rating' given by customers, and the 'FeedbackDate' marking when the feedback was received."),
    
    ("Generate a report of all transactions that occurred on weekends last month.",
     "The 'transaction_log' database tracks all customer transactions. It includes 'TransactionID' as a unique identifier, 'Date' of the transaction, 'Amount' spent, and 'CustomerID' to link to the customer who made the transaction."),
    
    ("Display the number of new customers acquired each month this year.",
     "The 'new_customers' table logs new customer acquisitions, with 'CustomerID' as a unique identifier for each customer and 'AcquisitionDate' showing when each customer was acquired."),
    
    ("Summarize the total number of items sold by each vendor.",
     "The 'sales_by_vendor' data includes 'VendorID' to identify each vendor, 'ProductID' for the sold products, and 'QuantitySold' which records the number of items sold by that vendor."),
    
    ("Identify the most viewed product categories on the website last quarter.",
     "In the 'page_views' analytics table, webpage views are categorized by 'CategoryID', with 'ViewDate' recording the date of the view and 'ViewCount' tallying the number of times the category page was viewed."),
    
    ("Calculate the total hours worked by each employee this quarter.",
     "The 'work_hours' log tracks employee work hours, with 'EmployeeID' for employee identification, 'WorkDate' indicating the date of work, and 'HoursWorked' showing the duration of work completed by the employee on that day."),
    
    ("List all suppliers that have been inactive for over a year.",
     "The 'supplier_status' table monitors supplier activity. It includes 'SupplierID' as a unique identifier for each supplier and 'LastActivityDate' indicating the last date when the supplier was active."),

    ("Generate a report of employees who have worked at the company for over 10 years.",
     "Database encompasses an 'employee_details' table, with fields such as EmployeeID, Name, JoinDate, Department, Position."),

    ("Calculate the total sales by each salesperson this quarter.",
     "Sales data are recorded in 'sales_records', which contains columns like SalespersonID, SaleAmount, SaleDate, CustomerID."),

    ("Identify products with a price increase of more than 15% compared to last year.",
     "Price history is stored in 'product_pricing', comprising columns ProductID, ProductName, PriceDate, Price."),

    ("List all customers who have not made any purchases in the last year.",
     "Customer purchase history is detailed in 'customer_purchases', including columns CustomerID, PurchaseDate, ProductID, AmountSpent."),

    ("Summarize total donations received by each department this year.",
     "The 'donations' table logs information with columns like DepartmentID, DonationAmount, DonationDate, DonorID."),

    ("Extract data on all properties sold in the last month, including sale price and agent details.",
     "Property sales are detailed in 'property_transactions', which has fields PropertyID, SalePrice, SaleDate, AgentID, BuyerID."),

    ("Retrieve details of all flights that were delayed by more than 2 hours last week.",
     "Flight information is recorded in 'flight_schedule', containing columns FlightNumber, ScheduledDeparture, ActualDeparture, Destination."),

    ("Find all books that have been checked out more than 50 times from the library.",
     "Library transactions are stored in 'book_loans', with columns including BookID, CheckoutDate, ReturnDate, MemberID."),

    ("List the top 5 most prescribed medications in the hospital last month.",
     "Medication prescriptions are documented in 'hospital_prescriptions', encompassing fields like MedicationID, PrescriptionDate, PatientID, DoctorID."),

    ("Determine the number of new memberships registered at the gym each month this year.",
     "Membership registrations are tracked in 'gym_memberships', featuring columns MemberID, RegistrationDate, MembershipType."),
    
    ("Identify employees who have not taken any sick leave in the past year.",
     "Employee attendance is tracked in the 'employee_attendance' database, which includes EmployeeID, Name, SickLeaveTaken, Year."),
    
    ("Calculate the total donation amount received from each donor.",
     "Donor contributions are recorded in the 'donation_ledger', encompassing fields like DonorID, DonationAmount, DonationDate."),
    
    ("List the top 5 most borrowed books from the library.",
     "The 'library_catalog' keeps track of book lending, with columns such as BookID, Title, BorrowDate, ReturnDate."),
    
    ("Find all active projects with a budget exceeding $500,000.",
     "Project details are maintained in 'project_management', containing ProjectID, ProjectName, StartDate, EndDate, Budget, Status."),
    
    ("Determine the average delivery time for orders shipped internationally.",
     "Shipping information is stored in 'global_shipments', which holds data like OrderID, DestinationCountry, DispatchDate, DeliveryDate."),
    
    ("Identify customers who have made more than five purchases but never returned an item.",
     "Customer purchase history is cataloged in 'purchase_records', featuring fields such as CustomerID, PurchaseDate, ReturnStatus."),
    
    ("Calculate the total hours of overtime worked by each department in the last quarter.",
     "Departmental overtime records are available in 'overtime_tracker', with columns including DepartmentID, EmployeeID, OvertimeHours, Quarter."),
    
    ("List all events scheduled in the conference hall for the next month.",
     "Upcoming events are scheduled in the 'event_planner', which includes fields like EventID, EventName, Venue, StartDate, EndDate."),
    
    ("Determine the number of patients treated for each type of illness last year.",
     "Patient treatment records are kept in 'medical_records', encompassing columns such as PatientID, IllnessType, TreatmentDate, RecoveryStatus."),

    ("Calculate the total revenue generated from each product category last quarter.",
     "Database Schema: SalesData, incorporating tables like Categories (CategoryID, CategoryName) and Sales (SaleID, ProductID, SaleDate, SaleAmount), where ProductID in Sales references Products in the Categories table."),

    ("Identify employees who have worked with the company for over 5 years.",
     "Employee records are stored in the EmployeeDetails database, which includes tables such as Employees (EmployeeID, Name, JoiningDate, DepartmentID) and Departments (DepartmentID, DepartmentName)."),

    ("Generate a list of all books that have not been checked out in the last year.",
     "Library Database: Comprising tables like Books (BookID, Title, Author) and BookLoans (LoanID, BookID, CheckoutDate, ReturnDate), with BookID in BookLoans linking to Books."),

    ("Count the number of flights delayed by more than 2 hours this month.",
     "Flight Information System: Contains FlightRecords (FlightID, ScheduledDeparture, ActualDeparture) and Airlines (AirlineID, AirlineName), with FlightID in FlightRecords connected to specific Airlines."),

    ("List the top 10 customers based on their purchase amount in the last 6 months.",
     "Customer Purchase Database: Includes Customer (CustomerID, Name, MembershipDate) and PurchaseHistory (PurchaseID, CustomerID, PurchaseDate, Amount), with CustomerID in PurchaseHistory referencing Customers."),

    ("Find the average customer satisfaction rating for each product line.",
     "Product Feedback Database: Consists of ProductLines (ProductLineID, LineName) and CustomerFeedback (FeedbackID, ProductLineID, Rating), where ProductLineID in CustomerFeedback correlates to ProductLines."),

    ("Retrieve the names of all patients who have not visited the clinic in the past year.",
     "Clinic Patient Management System: Includes PatientRecords (PatientID, Name, LastVisit) and Appointments (AppointmentID, PatientID, AppointmentDate), with PatientID in Appointments linked to PatientRecords."),

    ("Determine the total number of hours spent on project development by each team last month.",
     "Project Management Database: Encompassing Team (TeamID, TeamName) and ProjectHours (RecordID, TeamID, DateLogged, Hours), where TeamID in ProjectHours refers to teams in Team."),

    ("Identify all suppliers that have provided more than 50 different products.",
     "Supplier Product Catalog: Comprises Supplier (SupplierID, SupplierName) and Products (ProductID, SupplierID, ProductName), with SupplierID in Products referencing Suppliers."),

    ("Extract the list of all courses that had less than 10 students enrolled last semester.",
     "Educational Institution Database: Contains Courses (CourseID, CourseName, Semester) and Enrollments (EnrollmentID, CourseID, StudentID), with CourseID in Enrollments linked to Courses."),
    
    ("Count the number of employees in each department.\nData is organized in the 'department_employees' dataset, which is structured with columns such as DepartmentID, EmployeeID, and EmploymentDate.",
     "In the 'department_employees' dataset, columns are DepartmentID, EmployeeID, EmploymentDate."),

    ("Calculate the total sales for each product category last year.\nSales data is recorded in 'sales_records' which is structured with fields ProductID, CategoryID, SaleDate, and SaleAmount.",
     "Fields in 'sales_records' include ProductID, CategoryID, SaleDate, and SaleAmount."),

    ("Identify the most commonly prescribed medication for each illness.\nPrescription data is stored in 'medication_prescriptions', containing columns MedicationID, Illness, PrescriptionDate, and Dosage.",
     "The 'medication_prescriptions' database includes columns such as MedicationID, Illness, PrescriptionDate, and Dosage."),

    ("List the top 5 highest-rated restaurants in each city.\nRestaurant ratings are compiled in 'restaurant_reviews', featuring fields like RestaurantID, City, Rating, and ReviewDate.",
     "Columns in 'restaurant_reviews' encompass RestaurantID, City, Rating, and ReviewDate."),

    ("Summarize the total duration of calls made by each customer last month.\nCall records are kept in 'customer_calls', with columns including CustomerID, CallDate, Duration.",
     "The 'customer_calls' table is composed of columns such as CustomerID, CallDate, Duration."),

    ("Find the average property price in each neighborhood.\nProperty listings are in 'real_estate_prices', which includes fields like PropertyID, Neighborhood, Price, and ListingDate.",
     "The 'real_estate_prices' database is outlined with fields like PropertyID, Neighborhood, Price, and ListingDate."),

    ("Identify the most frequently used shipping route for each supplier.\nShipping information is stored in 'supplier_shipments', containing columns SupplierID, RouteID, ShipmentDate, and Quantity.",
     "In the 'supplier_shipments' table, columns include SupplierID, RouteID, ShipmentDate, and Quantity."),

    ("List the courses with the highest enrollment in each academic department.\nCourse enrollment data is in 'department_enrollments', featuring fields DepartmentID, CourseID, EnrollmentNumber, and Semester.",
     "The structure of 'department_enrollments' involves fields such as DepartmentID, CourseID, EnrollmentNumber, and Semester."),

    ("Calculate the total hours spent on each project by employees.\nProject work logs are in 'employee_projects', with columns EmployeeID, ProjectID, WorkHours, and LogDate.",
     "Columns in 'employee_projects' are EmployeeID, ProjectID, WorkHours, and LogDate."),

    ("Determine the average stay duration of guests in each hotel category.\nHotel stay records are kept in 'guest_stays', which includes fields GuestID, HotelCategory, CheckInDate, CheckOutDate.",
     "In the database, 'guest_stays' is structured with fields like GuestID, HotelCategory, CheckInDate, CheckOutDate."),
    
    ("Identify the most frequently used facilities by members at the sports club.",
     "Facility usage is recorded in 'facility_log', encompassing FacilityID, MemberID, UsageDate, UsageDuration. Facility details are cataloged in 'facilities', with fields FacilityID, FacilityName, Location."),

    ("List the top 3 most prescribed medications in the cardiology department this year.",
     "Prescription records are stored in 'medication_prescriptions', including fields PrescriptionID, PatientID, MedicationID, DatePrescribed. Medications are detailed in 'medications', with fields MedicationID, MedicationName, Department."),

    ("Determine the average time taken to resolve customer complaints received via email.",
     "Complaint resolution data is maintained in 'complaints', containing fields ComplaintID, ReceivedDate, ResolutionDate, Channel. Channel specifics are noted in 'communication_channels', with fields ChannelID, ChannelType."),

    ("Calculate the total water consumption for each residential building last month.",
     "Water usage records are kept in 'water_usage', including BuildingID, Date, Consumption. Building details are listed in 'residential_buildings', with fields BuildingID, Address, NumberOfUnits."),

    ("Summarize the number of students attending each course who have scholarships.",
     "Student enrollments are logged in 'student_courses', containing fields StudentID, CourseID, EnrollmentDate. Scholarship information is in 'scholarships', with fields StudentID, ScholarshipType, Amount."),

    ("Find the busiest hours of operation for the downtown parking garage.",
     "Parking usage is tracked in 'parking_log', encompassing EntryID, VehicleID, EntryTime, ExitTime. The garage's details are in 'parking_garage', with fields GarageID, Location, Capacity."),

    ("List all employees who have not taken any sick leave this year.",
     "Employee attendance is recorded in 'employee_attendance', containing EmployeeID, Date, Status. Employee details are in 'employee_directory', with fields EmployeeID, Name, Department."),

    ("Identify the most viewed categories on the company's internal knowledge base portal.",
     "Portal activity is monitored in 'knowledge_base_access', with fields AccessID, EmployeeID, CategoryID, AccessDate. Category details are in 'content_categories', featuring fields CategoryID, CategoryName."),

    ("Calculate the average growth rate of house plants in the botany department.",
     "Plant growth tracking is done in 'plant_growth', encompassing RecordID, PlantID, MeasurementDate, Height. Plant details are cataloged in 'house_plants', with fields PlantID, Species, Department."),

    ("Determine the most common repair issues for laptops issued to employees.",
     "Laptop repair records are kept in 'laptop_repairs', including RepairID, LaptopID, IssueDate, IssueType. Laptop details are in 'company_laptops', with fields LaptopID, Model, EmployeeID."),
    
    ("Assess the performance of sales representatives based on customer feedback scores.",
     "Customer feedback is recorded in 'feedback', encompassing FeedbackID, SalesRepID, Score, Date. Sales representative details are in 'sales_representatives', with fields SalesRepID, Name, Region."),

    ("List the most common health issues reported by patients in the telemedicine consultations.",
     "Patient consultations are logged in 'telemedicine_sessions', containing SessionID, PatientID, IssueReported, ConsultationDate. Patient details are in 'patients', with fields PatientID, Name, Age."),

    ("Calculate the average daily foot traffic in each store branch.",
     "Foot traffic data is tracked in 'store_traffic', including BranchID, Date, NumberOfVisitors. Store branch details are in 'store_branches', with fields BranchID, Location, Size."),

    ("Summarize the frequency of equipment malfunctions in the manufacturing plant.",
     "Equipment malfunction records are kept in 'equipment_malfunctions', encompassing MalfunctionID, EquipmentID, Date, Severity. Equipment details are in 'manufacturing_equipment', with fields EquipmentID, Type, Location."),

    ("Determine the most popular genres in the online bookstore based on sales data.",
     "Book sales are recorded in 'book_sales', including SaleID, BookID, DateSold, Quantity. Book details are in 'books', featuring fields BookID, Title, Genre, Author."),

    ("Assess the average duration of stay for guests in different hotel categories.",
     "Guest stay records are maintained in 'hotel_stays', with fields StayID, GuestID, HotelID, CheckInDate, CheckOutDate. Hotel details are in 'hotels', encompassing HotelID, Name, Category, Location."),

    ("Find the average response time for emergency services in different city zones.",
     "Emergency service responses are logged in 'emergency_responses', containing ResponseID, ZoneID, CallTime, ArrivalTime. City zones are detailed in 'city_zones', with fields ZoneID, Name, Population."),

    ("List all courses with more than 100 students enrolled in the current academic year.",
     "Course enrollment is tracked in 'course_enrollment', including EnrollmentID, CourseID, StudentID, AcademicYear. Course details are in 'courses', with fields CourseID, CourseName, Instructor."),

    ("Calculate the total revenue generated by each product line this fiscal year.",
     "Revenue data is recorded in 'sales', encompassing SaleID, ProductID, SaleDate, Revenue. Product line details are in 'product_lines', with fields ProductID, LineName, Category."),

    ("Identify the most frequented destinations by the company's corporate travel program.",
     "Travel records are kept in 'corporate_travel', including TravelID, Destination, DepartureDate, ReturnDate. Destination details are in 'destinations', with fields DestinationID, Name, Country."),

    ("List the most attended events in the city's community centers this year.",
     "Event attendance is recorded in 'community_events', containing fields EventID, CenterID, EventDate, NumberOfAttendees. Community center details are in 'community_centers', with fields CenterID, CenterName, Location."),

    ("Calculate the average grade of students in the online learning program.",
     "Student performance is tracked in 'online_courses', encompassing fields StudentID, CourseID, Grade, CompletionDate. Course information is detailed in 'e_learning_courses', with fields CourseID, CourseName, Instructor."),

    ("Identify the regions with the highest number of service calls for appliance repairs.",
     "Service call data is maintained in 'appliance_service_calls', including fields CallID, ApplianceID, Region, ServiceDate. Appliance details are in 'appliances', with fields ApplianceID, Type, Brand."),

    ("Summarize the monthly electricity usage for industrial clients.",
     "Electricity consumption is recorded in 'industrial_electricity_usage', containing ClientID, Month, Year, Consumption. Client details are listed in 'industrial_clients', with fields ClientID, CompanyName, Sector."),

    ("Find the average duration of museum visits last quarter.",
     "Visitor logs are kept in 'museum_visits', encompassing fields VisitID, VisitorID, EntryTime, ExitTime. Museum information is in 'museums', with fields MuseumID, Name, Location."),

    ("Determine the most popular genres in the city library's book club discussions.",
     "Book club activities are tracked in 'library_book_clubs', containing ClubID, BookID, MeetingDate, Genre. Book details are in 'library_books', with fields BookID, Title, Author."),

    ("List all the animal species that have been newly added to the zoo in the past year.",
     "Animal records are maintained in 'zoo_animals', including fields AnimalID, Species, ArrivalDate, Habitat. Habitat details are in 'animal_habitats', with fields HabitatID, Name, EnvironmentType."),

    ("Calculate the average response time for emergency services in urban areas.",
     "Emergency response data is cataloged in 'emergency_calls', with fields CallID, ResponseTime, AreaType, IncidentType. Area details are in 'urban_areas', featuring fields AreaID, AreaName, Population."),

    ("Identify the most frequently borrowed equipment in the fitness center.",
     "Equipment loan records are stored in 'fitness_equipment_loans', containing LoanID, EquipmentID, BorrowDate, ReturnDate. Equipment details are in 'gym_equipment', with fields EquipmentID, Type, Brand."),

    ("Summarize the success rate of startups incubated in the local business accelerator over the last five years.",
     "Startup performance is tracked in 'business_accelerator', encompassing fields StartupID, EntryDate, ExitDate, SuccessMetric. Startup profiles are in 'startups', with fields StartupID, Name, Industry."),
    
    ("Track the growth in monthly subscriptions for the online streaming service.",
     "Subscription data is housed in 'subscription_records', including fields SubscriptionID, UserID, StartDate, EndDate. User profiles are detailed in 'users', with fields UserID, Name, JoinDate."),

    ("List the top-selling authors in the fiction category from the bookstore database.",
     "Sales records are stored in 'book_sales', containing fields SaleID, BookID, SaleDate, Quantity. Book details, including author information, are in 'books', with fields BookID, Title, AuthorID, Genre. Author profiles are in 'authors', with fields AuthorID, Name."),

    ("Determine the average occupancy rate of hotels in the coastal region during summer.",
     "Hotel booking data is maintained in 'hotel_bookings', encompassing BookingID, HotelID, CheckInDate, CheckOutDate. Hotel information is cataloged in 'hotels', with fields HotelID, Name, Location, Region."),

    ("Identify the most commonly reported issues in the latest smartphone model.",
     "Customer feedback is recorded in 'product_feedback', including FeedbackID, ProductID, SubmissionDate, IssueType. Product details are in 'smartphones', with fields ProductID, Model, ReleaseDate."),

    ("Calculate the total donation amount received by each charity organization last year.",
     "Donation records are kept in 'donations', containing DonationID, DonorID, CharityID, Amount, DonationDate. Charity details are in 'charities', with fields CharityID, Name, Cause."),

    ("Summarize the performance of sales representatives in the automotive sector.",
     "Sales performance is tracked in 'sales_records', encompassing SaleID, SalesRepID, ProductID, SaleAmount, SaleDate. Sales representative profiles are in 'sales_reps', with fields SalesRepID, Name, Region, Sector."),

    ("List all research projects that received government funding in the last fiscal year.",
     "Research funding details are recorded in 'research_funding', including ProjectID, FundingAgency, Amount, StartDate, EndDate. Project details are in 'research_projects', with fields ProjectID, Title, LeadResearcherID. Researcher profiles are in 'researchers', with fields ResearcherID, Name, Department."),

    ("Determine the frequency of public transport usage in urban vs. rural areas.",
     "Transport usage data is maintained in 'transit_records', containing TransitID, RouteID, BoardingTime, AlightingTime, AreaType. Route details are in 'transit_routes', with fields RouteID, StartPoint, EndPoint, AreaType."),

    ("Calculate the average energy consumption per household in different city districts.",
     "Energy usage is logged in 'energy_consumption', encompassing RecordID, HouseholdID, District, Consumption, RecordDate. Household details are in 'households', with fields HouseholdID, Address, District."),

    ("Identify the most frequently borrowed genres in the public library system.",
     "Library loan records are stored in 'library_loans', including LoanID, BookID, MemberID, CheckoutDate, ReturnDate. Book details, including genre, are in 'library_books', with fields BookID, Title, Genre, AuthorID."),

    ("Identify the most popular menu items in the cafeteria based on sales in the last month.",
     "Cafeteria sales are recorded in 'menu_sales', which includes fields like SaleID, MenuItemID, Date, QuantitySold. Menu item details are found in 'menu_items', with fields MenuItemID, ItemName, Price."),

    ("List all patients who have missed more than two appointments in the past six months.",
     "Patient appointment data is stored in 'patient_appointments', encompassing AppointmentID, PatientID, ScheduledDate, AttendanceStatus. Patient profiles are in 'patients', with fields PatientID, Name, DateOfBirth."),

    ("Calculate the average daily foot traffic in each store of the shopping mall.",
     "Foot traffic data is tracked in 'store_traffic', which includes RecordID, StoreID, Date, NumberOfVisitors. Store details are in 'mall_stores', with fields StoreID, StoreName, Size."),

    ("Summarize the total donations received by each department in the university last year.",
     "Donation records are kept in 'university_donations', containing DonationID, DepartmentID, DateReceived, Amount. Department information is in 'academic_departments', with fields DepartmentID, DepartmentName, FacultyHead."),

    ("Find the most frequently booked conference rooms in the corporate office.",
     "Room booking details are recorded in 'conference_room_bookings', encompassing BookingID, RoomID, BookingDate, Duration. Room specifics are in 'conference_rooms', with fields RoomID, RoomName, Capacity."),

    ("List the top performing sales representatives based on total sales value this quarter.",
     "Sales performance data is maintained in 'sales_records', including SalesID, RepresentativeID, SaleDate, SaleValue. Representative profiles are in 'sales_team', with fields RepresentativeID, Name, Region."),

    ("Determine the busiest hours for customer service calls.",
     "Customer service call logs are in 'service_calls', containing CallID, TimeReceived, Duration, IssueResolved. Employee shift details are in 'employee_shifts', with fields EmployeeID, ShiftStart, ShiftEnd."),

    ("Calculate the total number of outpatient procedures performed by each clinician last month.",
     "Outpatient procedure records are stored in 'clinic_procedures', encompassing ProcedureID, ClinicianID, ProcedureDate, Type. Clinician details are in 'clinic_staff', with fields ClinicianID, Name, Specialty."),

    ("Identify the most used study rooms in the university library during exam season.",
     "Study room usage is logged in 'library_room_usage', with fields UsageID, RoomID, Date, Duration. Room details are in 'library_rooms', featuring fields RoomID, RoomName, Capacity."),

    ("List all vehicles in the company fleet that are due for a service check.",
     "Fleet maintenance schedule is recorded in 'fleet_maintenance', containing VehicleID, LastServiceDate, NextServiceDue. Vehicle details are in 'company_vehicles', with fields VehicleID, Make, Model, Year."),
    
    ("Track the number of unique visitors to each exhibition in the museum last year.",
     "Visitor logs are stored in 'exhibition_visits', which includes fields VisitID, ExhibitionID, VisitorID, VisitDate. Exhibition details are cataloged in 'exhibitions', with fields ExhibitionID, ExhibitionName, StartDate, EndDate."),

    ("Summarize the yearly energy consumption for each factory location.",
     "Energy usage data is recorded in 'factory_energy_usage', encompassing FactoryID, Consumption, RecordDate. Factory profiles are listed in 'factories', with fields FactoryID, Location, Size."),

    ("List all the ingredients used more than 100 times in the restaurant's kitchen last month.",
     "Ingredient usage is tracked in 'kitchen_inventory', which includes IngredientID, UsageCount, LastUsedDate. Ingredient details are in 'ingredients', with fields IngredientID, Name, Type."),

    ("Identify the most frequent health issues reported by residents in the elderly care facility.",
     "Health records are maintained in 'resident_health', containing fields ResidentID, IssueDate, HealthIssue. Resident profiles are in 'care_residents', with fields ResidentID, Name, Age."),

    ("Calculate the average daily footfall in each branch of the retail chain.",
     "Footfall data is logged in 'branch_footfall', encompassing BranchID, Date, VisitorCount. Branch details are in 'retail_branches', with fields BranchID, Address, Size."),

    ("Determine the most popular online courses based on completion rates.",
     "Course completion data is stored in 'online_courses', including CourseID, StudentID, EnrollmentDate, CompletionDate. Course details are in 'course_catalog', with fields CourseID, CourseName, Instructor."),

    ("List vehicles in the transportation fleet that have exceeded 100,000 miles.",
     "Vehicle mileage is tracked in 'fleet_mileage', containing VehicleID, Mileage. Fleet details are in 'transport_fleet', with fields VehicleID, Model, Year, Status."),

    ("Identify the top-selling authors in the bookstore for the past year.",
     "Sales records are kept in 'book_sales', including SaleID, BookID, SaleDate, Quantity. Book details are in 'books_inventory', with fields BookID, Title, Author, Genre."),

    ("Summarize the occupancy rate of hotel rooms during peak tourist season.",
     "Room occupancy is recorded in 'hotel_bookings', encompassing BookingID, RoomID, CheckInDate, CheckOutDate. Room details are in 'hotel_rooms', with fields RoomID, Type, Capacity."),

    ("Determine the average duration of phone calls made by the customer service team.",
     "Call logs are maintained in 'service_calls', containing CallID, EmployeeID, CallDuration, CallDate. Employee details are in 'service_team', with fields EmployeeID, Name, Role."),
    
    ("Rank the departments in the company based on the average employee salary, showing the top 5 highest paying departments.",
     "Employee salary details are in 'employee_salaries', with fields EmployeeID, Salary, DepartmentID. Department information is stored in 'departments', encompassing DepartmentID, DepartmentName. This task requires a JOIN between the two tables and the use of DENSE_RANK."),

    ("Find the total sales made by each salesperson, include only those who have sold to more than three unique clients.",
     "Sales data is tracked in 'sales_transactions', containing SalespersonID, ClientID, SaleAmount. This requires grouping by SalespersonID and filtering based on a count of unique ClientIDs."),

    ("List the top 3 most borrowed book genres in the library, along with the names of the most frequent borrowers for each genre.",
     "Borrowing records are in 'book_loans', with fields LoanID, BookID, BorrowerID, LoanDate. Book details are in 'books', containing BookID, Title, GenreID. Borrower information is in 'borrowers', with fields BorrowerID, Name. This task involves multiple JOINs and subqueries."),

    ("Identify employees who have never missed a deadline for their projects.",
     "Project assignment records are stored in 'project_assignments', encompassing EmployeeID, ProjectID, Deadline, CompletionDate. This requires filtering for cases where CompletionDate is always on or before the Deadline."),

    ("Calculate the average number of days taken to ship products after an order is placed, categorized by product category.",
     "Order details are in 'orders', with fields OrderID, OrderDate, ShipDate. Product information is in 'products', containing ProductID, CategoryID, Name. This task involves a JOIN and the use of date functions."),

    ("Determine the most frequently attended courses by students who have a GPA above 3.5.",
     "Student grades are in 'student_grades', containing StudentID, GPA. Course enrollments are in 'course_enrollments', with fields EnrollmentID, CourseID, StudentID. This task requires a JOIN and filtering on the GPA."),

    ("Rank the suppliers based on the total quantity of products supplied, showing suppliers who have supplied more than 1000 units overall.",
     "Supplier deliveries are tracked in 'supplier_deliveries', with fields SupplierID, ProductID, Quantity. Supplier information is in 'suppliers', containing SupplierID, Name. This involves aggregating quantities and filtering suppliers based on the total."),

    ("List the names of patients who have been admitted more than twice in the last year for the same diagnosis.",
     "Patient admissions are recorded in 'patient_admissions', encompassing PatientID, AdmissionDate, Diagnosis. This requires filtering for repeated diagnoses and counting admissions per patient."),

    ("Find the average duration of stay for guests in each hotel, ranked from highest to lowest.",
     "Guest stay records are in 'hotel_stays', including GuestID, HotelID, CheckInDate, CheckOutDate. Hotel information is in 'hotels', with fields HotelID, Name. This task involves calculating durations and ranking hotels based on the average stay."),

    ("Determine the employees who have attended all mandatory training sessions.",
     "Training records are stored in 'employee_training', containing EmployeeID, SessionID. Mandatory sessions are listed in 'training_sessions', with fields SessionID, Mandatory. This requires a JOIN and filtering for employees who have attended all mandatory sessions."),
    
    ("Rank departments by the average employee salary and list the top 3.",
     "Employee salaries are stored in 'employee_salaries', containing fields EmployeeID, DepartmentID, Salary. Department details are in 'departments', with fields DepartmentID, DepartmentName. This task requires calculating the average salary per department and then applying a DENSE_RANK."),

    ("Find the most popular product in each category based on sales, using a window function.",
     "Sales data is in 'product_sales', encompassing ProductID, SaleAmount, SaleDate. Product details, including categories, are in 'products', with fields ProductID, ProductName, CategoryID. A window function can be used to rank products within each category based on total sales."),

    ("Identify employees who have not participated in any training session this year, using a left join.",
     "Employee details are in 'employees', containing EmployeeID, Name, DepartmentID. Training participation is logged in 'training_sessions', with fields SessionID, EmployeeID, Date. A left join between these tables can identify employees without any training session records for the current year."),

    ("List the top 5 customers based on their purchase frequency and amount, using subqueries and joins.",
     "Customer purchases are recorded in 'customer_orders', with fields OrderID, CustomerID, PurchaseAmount, PurchaseDate. Customer details are in 'customers', including CustomerID, Name, ContactInfo. This task requires a join between the two tables and a subquery to calculate the purchase frequency and amount."),

    ("Determine the month with the highest number of employee sick leaves, using a group by and order by clauses.",
     "Employee sick leaves are tracked in 'sick_leave_records', containing LeaveID, EmployeeID, StartDate, EndDate. This task involves grouping the data by month and ordering it by the count of sick leaves."),

    ("Calculate the year-over-year growth rate of sales for each product, using self-joins.",
     "Product sales over years are in 'annual_sales', encompassing Year, ProductID, TotalSales. A self-join on the 'annual_sales' table is required to compare sales across different years for each product."),

    ("Identify suppliers who have consistently increased their prices over the last three years, using window functions.",
     "Supplier pricing data is in 'supplier_prices', with fields SupplierID, ProductID, Year, Price. A window function can be used to compare the prices across years for each supplier-product combination."),

    ("Rank employees by their total working hours in the last month and list any ties in rank, using DENSE_RANK.",
     "Employee work hours are logged in 'work_hours', containing EmployeeID, Date, HoursWorked. The task involves summing the hours worked for each employee and then applying DENSE_RANK to handle ties in total hours."),

    ("Find the average product rating for each category, including only products with more than 10 ratings, using HAVING and JOIN clauses.",
     "Product ratings are in 'product_ratings', with fields ProductID, Rating. Product categories are in 'product_categories', containing ProductID, CategoryID. This task requires a join between the two tables and filtering using the HAVING clause based on the count of ratings."),

    ("List all employees who have switched departments more than twice, using a combination of GROUP BY and HAVING clauses.",
     "Employee department history is recorded in 'department_history', encompassing EmployeeID, DepartmentID, StartDate, EndDate. This task involves grouping by employee and counting the number of department changes, then filtering those who have more than two changes."),

    ("Identify the top three highest-earning employees in each department.",
     "Employee salaries are recorded in 'salaries', with fields EmployeeID, DepartmentID, Salary. Employee details are in 'employees', including EmployeeID, Name. Departments are listed in 'departments', with DepartmentID, DepartmentName."),

    ("List the names of patients who have had more than two types of surgeries, along with the types of surgeries.",
     "Patient surgical history is stored in 'surgeries', encompassing PatientID, SurgeryType, SurgeryDate. Patient details are in 'patients', with fields PatientID, PatientName."),

    ("Determine the most popular product combinations bought together in the last year.",
     "Sales transactions are logged in 'sales', containing TransactionID, Date, TotalAmount. Product details in each transaction are in 'sales_products', with fields TransactionID, ProductID. Products are listed in 'products', including ProductID, ProductName."),

    ("Find the average time taken to ship products for each supplier, ranked by speed.",
     "Shipping records are kept in 'shipments', including ShipmentID, SupplierID, ShipDate, DeliveryDate. Supplier details are in 'suppliers', with fields SupplierID, SupplierName."),

    ("Identify customers who have not made any purchases in the last six months but were previously frequent shoppers.",
     "Customer purchase history is recorded in 'purchases', with fields CustomerID, PurchaseDate, Amount. Customer profiles are in 'customers', encompassing CustomerID, CustomerName, JoinDate."),

    ("List the titles of research papers published by each department, along with the count of papers published, ordered by department size.",
     "Research papers are cataloged in 'research_papers', containing PaperID, Title, DepartmentID, PublishDate. Department sizes are in 'departments', with DepartmentID, DepartmentName, NumberOfResearchers."),

    ("Calculate the month-over-month growth rate in sales for each product category.",
     "Monthly sales data is stored in 'monthly_sales', with fields Month, CategoryID, TotalSales. Product categories are detailed in 'product_categories', including CategoryID, CategoryName."),

    ("Determine the three most common issues reported in customer service calls, categorized by product type.",
     "Service call logs are in 'service_calls', including CallID, ProductID, IssueType, CallDate. Product details are in 'products', with fields ProductID, ProductName."),

    ("Identify the busiest travel routes based on the number of flights and passenger count, using dense ranking.",
     "Flight records are maintained in 'flights', encompassing FlightID, RouteID, Date, PassengerCount. Route details are in 'routes', with fields RouteID, Origin, Destination."),

    ("List employees who have switched departments more than once, along with their current department and total tenure in the company.",
     "Employee department history is tracked in 'department_history', containing EmployeeID, DepartmentID, StartDate, EndDate. Current department and tenure details are in 'employees', with fields EmployeeID, CurrentDepartmentID, HireDate."),
    
    ("Rank employees by the total sales achieved, displaying top 10 salespersons across all regions.",
     "Employee sales data is in 'employee_sales', containing fields EmployeeID, SaleAmount, SaleDate. Employee details are in 'employees', with EmployeeID, Name, RegionID. Regions are defined in 'sales_regions', with fields RegionID, RegionName."),

    ("Identify the most prescribed medication for each type of illness, based on patient records.",
     "Patient prescriptions are in 'patient_medications', encompassing fields PatientID, IllnessType, MedicationID, PrescriptionDate. Medication details are in 'medications', with fields MedicationID, MedicationName."),

    ("List the latest project each employee worked on, along with the project duration and department.",
     "Project assignments are recorded in 'employee_projects', with fields EmployeeID, ProjectID, StartDate, EndDate. Project details are in 'projects', including ProjectID, ProjectName, DepartmentID. Department information is in 'departments', with fields DepartmentID, DepartmentName."),

    ("Calculate the average duration of calls for each customer support agent, including only calls longer than 5 minutes.",
     "Call records are maintained in 'support_calls', including fields CallID, AgentID, CallDuration, CallDate. Agent details are in 'support_agents', with fields AgentID, Name, TeamID."),

    ("Determine the total number of hours each student spent in extracurricular activities, ranked by activity type.",
     "Student activity logs are in 'student_activities', containing fields StudentID, ActivityID, Hours, ParticipationDate. Activity details are in 'activities', with fields ActivityID, ActivityType, ActivityName."),

    ("List the top 5 suppliers based on the quantity of products supplied, excluding discontinued products.",
     "Supplier deliveries are tracked in 'supplier_deliveries', including SupplierID, ProductID, Quantity, DeliveryDate. Product information is in 'products', with fields ProductID, ProductName, Status."),

    ("Identify the department with the highest number of employees who have been with the company for over 10 years.",
     "Employee tenure is documented in 'employee_tenure', encompassing EmployeeID, HireDate. Employee details are in 'employees', with fields EmployeeID, Name, DepartmentID. Department data is in 'departments', with DepartmentID, DepartmentName."),

    ("Rank customers based on their total purchase amount, displaying customers who have spent more than $1000.",
     "Customer purchases are recorded in 'customer_orders', containing fields CustomerID, OrderID, TotalAmount, OrderDate. Customer profiles are in 'customers', with fields CustomerID, Name, Address."),

    ("Determine the average test scores for each school, sorted by the number of students who scored above 90%.",
     "Test scores are stored in 'student_scores', with fields StudentID, SchoolID, TestScore, TestDate. School information is in 'schools', including SchoolID, SchoolName, Location."),

    ("Find the most common repair types for cars manufactured before 2000, including the average cost of repairs.",
     "Car repair records are kept in 'car_repairs', encompassing RepairID, CarID, RepairType, Cost. Car details are in 'cars', with fields CarID, Model, ManufactureYear."),
    
    ("Retrieve a list of customers who made the highest purchase amount in each product category.",
     "Database Schema: Sales data is organized in 'sales_transactions', encompassing fields such as TransactionID, CustomerID, ProductID, PurchaseAmount, PurchaseDate. Product categories are detailed in 'product_categories', with fields CategoryID, CategoryName."),

    ("Rank employees by their total sales revenue in descending order for the current quarter.",
     "Employee sales records are stored in 'employee_sales', which includes fields EmployeeID, SaleDate, SaleAmount. Employee details are cataloged in 'employee_details', with fields EmployeeID, EmployeeName."),

    ("List the top 5 performing students based on their average test scores across all subjects.",
     "Student test scores are maintained in 'student_test_scores', containing fields StudentID, Subject, TestScore. Student details are in 'student_information', with fields StudentID, StudentName."),

    ("Find the average time spent by each user on the website, considering both login and session duration.",
     "Website user activity is logged in 'user_activity', with fields UserID, LoginTime, LogoutTime, SessionDuration. User details are in 'user_profiles', featuring fields UserID, UserName."),

    ("Retrieve a list of customers who have made purchases on consecutive days, along with the dates of their purchases.",
     "Customer purchase records are stored in 'customer_purchases', including fields CustomerID, PurchaseDate. Customer details are cataloged in 'customer_details', with fields CustomerID, CustomerName."),

    ("Identify the employees who have worked in multiple departments and rank them by the number of departments they've worked in.",
     "Employee department history is logged in 'employee_departments', containing fields EmployeeID, DepartmentID, StartDate, EndDate. Employee details are in 'employee_information', with fields EmployeeID, EmployeeName."),

    ("List all products that have never been part of any special promotions or discounts.",
     "Product promotion history is recorded in 'product_promotions', with fields ProductID, PromotionID, PromotionStartDate, PromotionEndDate. Product details are in 'product_catalog', featuring fields ProductID, ProductName."),

    ("Determine the top 3 most popular travel destinations among customers who have purchased premium travel packages.",
     "Customer travel data is stored in 'travel_history', encompassing fields CustomerID, Destination, PackageType, PurchaseDate. Destination details are in 'travel_destinations', with fields DestinationID, DestinationName."),

    ("Calculate the DENSE_RANK of students based on their cumulative exam scores in ascending order.",
     "Student exam scores are cataloged in 'student_scores', with fields StudentID, ExamID, Score. Student details are in 'student_information', featuring fields StudentID, StudentName."),

    ("Retrieve the list of employees who have completed at least two different training courses and participated in team-building activities.",
     "Employee training records are logged in 'training_records', with fields EmployeeID, CourseID, TrainingDate. Team-building activities are recorded in 'team_building', featuring fields EmployeeID, ActivityDate."),
    
    ("Retrieve a list of customers who made the highest purchase amount in each product category.",
     "Database Schema: Sales data is organized in 'sales_transactions', encompassing fields such as TransactionID, CustomerID, ProductID, PurchaseAmount, PurchaseDate. Product categories are detailed in 'product_categories', with fields CategoryID, CategoryName."),

    ("Rank employees by their total sales revenue in descending order for the current quarter.",
     "Employee sales records are stored in 'employee_sales', which includes fields EmployeeID, SaleDate, SaleAmount. Employee details are cataloged in 'employee_details', with fields EmployeeID, EmployeeName."),

    ("List the top 5 performing students based on their average test scores across all subjects.",
     "Student test scores are maintained in 'student_test_scores', containing fields StudentID, Subject, TestScore. Student details are in 'student_information', with fields StudentID, StudentName."),

    ("Find the average time spent by each user on the website, considering both login and session duration.",
     "Website user activity is logged in 'user_activity', with fields UserID, LoginTime, LogoutTime, SessionDuration. User details are in 'user_profiles', featuring fields UserID, UserName."),

    ("Retrieve a list of customers who have made purchases on consecutive days, along with the dates of their purchases.",
     "Customer purchase records are stored in 'customer_purchases', including fields CustomerID, PurchaseDate. Customer details are cataloged in 'customer_details', with fields CustomerID, CustomerName."),

    ("Identify the employees who have worked in multiple departments and rank them by the number of departments they've worked in.",
     "Employee department history is logged in 'employee_departments', containing fields EmployeeID, DepartmentID, StartDate, EndDate. Employee details are in 'employee_information', with fields EmployeeID, EmployeeName."),

    ("List all products that have never been part of any special promotions or discounts.",
     "Product promotion history is recorded in 'product_promotions', with fields ProductID, PromotionID, PromotionStartDate, PromotionEndDate. Product details are in 'product_catalog', featuring fields ProductID, ProductName."),

    ("Determine the top 3 most popular travel destinations among customers who have purchased premium travel packages.",
     "Customer travel data is stored in 'travel_history', encompassing fields CustomerID, Destination, PackageType, PurchaseDate. Destination details are in 'travel_destinations', with fields DestinationID, DestinationName."),

    ("Calculate the DENSE_RANK of students based on their cumulative exam scores in ascending order.",
     "Student exam scores are cataloged in 'student_scores', with fields StudentID, ExamID, Score. Student details are in 'student_information', featuring fields StudentID, StudentName."),

    ("Retrieve the list of employees who have completed at least two different training courses and participated in team-building activities.",
     "Employee training records are logged in 'training_records', with fields EmployeeID, CourseID, TrainingDate. Team-building activities are recorded in 'team_building', featuring fields EmployeeID, ActivityDate."),
    
    ("List the names of customers who have made the highest number of purchases in each product category.",
     "Database Schema: Customer purchase records are stored in 'customer_purchases' with fields PurchaseID, CustomerID, ProductID, PurchaseDate. Product details are in 'products' with fields ProductID, ProductName, CategoryID. Categories are listed in 'product_categories' with fields CategoryID, CategoryName."),

    ("Calculate the DENSE_RANK of each student's score in the Mathematics exam, partitioned by grade level.",
     "Database Schema: Student exam scores are stored in 'student_scores' with fields StudentID, GradeLevel, Subject, ExamScore, ExamDate."),

    ("Retrieve the top 5 highest-earning employees in each department, ordered by salary.",
     "Database Schema: Employee information is in 'employees' with fields EmployeeID, DepartmentID, Name, Salary. Department details are in 'departments' with fields DepartmentID, DepartmentName."),

    ("Identify customers who have made at least 5 consecutive monthly purchases of the same product.",
     "Database Schema: Customer purchase records are in 'customer_purchases' with fields PurchaseID, CustomerID, ProductID, PurchaseDate. Product details are in 'products' with fields ProductID, ProductName. The 'PurchaseDate' field is of type 'Date'."),

    ("List the most recent comments on each article, along with the article title and author's name.",
     "Database Schema: Article comments are stored in 'article_comments' with fields CommentID, ArticleID, CommentText, CommentDate. Article details are in 'articles' with fields ArticleID, Title, AuthorID. Author information is in 'authors' with fields AuthorID, AuthorName."),

    ("Calculate the average rating of movies in each genre, and rank them by average rating in descending order.",
     "Database Schema: Movie ratings are in 'movie_ratings' with fields MovieID, MovieTitle, Genre, Rating. Movie details are in 'movies' with fields MovieID, MovieTitle, Genre."),

    ("Retrieve a list of employees who have attended the most training sessions, along with the count of sessions attended.",
     "Database Schema: Employee training attendance is logged in 'training_attendance' with fields EmployeeID, SessionID, AttendanceDate. Training sessions are in 'training_sessions' with fields SessionID, SessionName."),

    ("Find the employees with the highest and lowest salaries in each department.",
     "Database Schema: Employee information is in 'employees' with fields EmployeeID, DepartmentID, Name, Salary. Department details are in 'departments' with fields DepartmentID, DepartmentName."),

    ("Identify the top 3 most common reasons for customer support calls and the number of times each reason occurred.",
     "Database Schema: Customer support call details are in 'support_calls' with fields CallID, ReasonID, CallDate. Call reasons are listed in 'call_reasons' with fields ReasonID, ReasonText."),

    ("Calculate the total revenue generated by each product category, and list them in descending order of revenue.",
     "Database Schema: Sales information is in 'sales_data' with fields SaleID, ProductID, SaleDate, SaleAmount. Product details are in 'products' with fields ProductID, ProductName, CategoryID. Categories are listed in 'product_categories' with fields CategoryID, CategoryName."),
    
    ("Retrieve a list of customers who made purchases on both Black Friday and Cyber Monday.",
     "Sales transactions are stored in 'sales_transactions', with fields CustomerID, TransactionID, PurchaseDate. Special sale dates are in 'sale_dates', featuring fields SaleDate, SaleType."),

    ("Rank the top 5 highest-paid employees in each department based on their salaries.",
     "Employee salary details are in 'employee_salaries', encompassing fields EmployeeID, Department, Salary. Employee information is listed in 'employee_details', with fields EmployeeID, Name, Department."),

    ("Find the average rating of products in each category, and rank the categories by average rating.",
     "Product ratings are stored in 'product_ratings', including fields ProductID, Rating. Product category information is in 'product_categories', with fields CategoryID, CategoryName."),

    ("Identify the top 3 most frequently occurring words in customer reviews, excluding common stop words.",
     "Customer reviews are cataloged in 'customer_reviews', featuring fields ReviewID, CustomerID, ReviewText. Stop words are listed in 'stop_words', with fields StopWordID, Word."),

    ("Retrieve a list of students who have the same average test score as at least one other student in their grade.",
     "Student test scores are maintained in 'student_scores', encompassing fields StudentID, GradeLevel, TestScore. Grade-level averages are calculated using a CTE (Common Table Expression)."),

    ("Calculate the total revenue for each product, considering both direct sales and affiliate sales.",
     "Sales records are stored in 'sales_records', including fields ProductID, SaleAmount, SaleType. Affiliate sales data is in 'affiliate_sales', with fields ProductID, AffiliateSaleAmount."),

    ("List all employees who have worked continuously for the company for at least 5 years.",
     "Employee tenure is tracked in 'employee_tenure', with fields EmployeeID, HireDate. A DENSE_RANK window function is used to calculate continuous service years."),

    ("Find the customers who have made the largest number of consecutive purchases without any gaps in the last year.",
     "Purchase history is recorded in 'purchase_history', encompassing fields CustomerID, PurchaseDate. A recursive CTE is used to identify consecutive purchases."),

    ("Rank the most visited pages on the company website by counting unique page views.",
     "Website analytics data is stored in 'page_views', featuring fields PageID, VisitorID, VisitDate. DENSE_RANK is applied to rank pages based on unique views."),

    ("Identify the top 3 bestselling book authors based on the total number of copies sold.",
     "Book sales records are kept in 'book_sales', with fields BookID, AuthorID, CopiesSold. Author information is in 'authors', including fields AuthorID, AuthorName."),
    
    ("Find the top 3 employees with the highest sales revenue in the last quarter, including their manager's name.",
     "Sales data is stored in 'sales_data' with fields SaleID, EmployeeID, SaleDate, SaleAmount. Employee details are in 'employees' with fields EmployeeID, EmployeeName, ManagerID."),

    ("Rank students in each class by their average test scores in descending order.",
     "Student test scores are recorded in 'test_scores' with fields StudentID, ClassID, TestDate, Score. Class information is in 'classes' with fields ClassID, ClassName."),

    ("Identify customers who have made at least 3 consecutive monthly purchases and rank them by the number of consecutive months.",
     "Purchase history is kept in 'purchases' with fields CustomerID, PurchaseDate, Amount. Customer details are in 'customers' with fields CustomerID, CustomerName."),

    ("List all employees who have attended both the 'Management Training' and 'Leadership Seminar' sessions.",
     "Training attendance is logged in 'training_sessions' with fields EmployeeID, SessionName, SessionDate. Employee details are in 'employees' with fields EmployeeID, EmployeeName."),

    ("Calculate the average salary of employees in each department, considering only the top 2 earners in each department.",
     "Employee salary data is stored in 'employee_salaries' with fields EmployeeID, DepartmentID, Salary. Department details are in 'departments' with fields DepartmentID, DepartmentName."),

    ("Find the departments with the highest average employee tenure, including the department with the highest and lowest tenure.",
     "Employee tenure information is in 'employee_tenure' with fields EmployeeID, DepartmentID, TenureMonths. Department details are in 'departments' with fields DepartmentID, DepartmentName."),

    ("Identify the top 5 product categories with the most customer reviews, including the number of reviews for each category.",
     "Product reviews are stored in 'product_reviews' with fields ProductID, CustomerID, ReviewDate, Rating. Product categories are in 'product_categories' with fields CategoryID, CategoryName."),

    ("Rank hospitals by the average length of stay for patients over 65 years old in ascending order.",
     "Patient admission data is recorded in 'patient_admissions' with fields HospitalID, PatientID, AdmissionDate, DischargeDate, Age. Hospital details are in 'hospitals' with fields HospitalID, HospitalName."),

    ("Identify the top 3 performing sales regions based on total sales revenue, and include the names of the salespeople with the highest sales in each region.",
     "Sales data includes fields RegionID, SalespersonID, SaleDate, SaleAmount. Salesperson details are in 'salespeople' with fields SalespersonID, SalespersonName. Region details are in 'sales_regions' with fields RegionID, RegionName."),

    ("Rank customers by their total purchases using DENSE_RANK, and list the top 3 customers with the same rank.",
     "Customer purchase history is in 'customer_purchases' with fields CustomerID, PurchaseDate, Amount. Customer details are in 'customers' with fields CustomerID, CustomerName."),
    
    ("Find the top 5 research papers with the highest citation counts in the physics database.",
     "The physics research papers database consists of 'research_papers' with fields PaperID, Title, AuthorID, PublicationDate, CitationCount, and 'authors' with fields AuthorID, AuthorName."),

    ("List the names of scientists who have authored papers in both the biology and chemistry databases.",
     "The biology research papers are in 'biology_papers' with fields PaperID, Title, AuthorID, and the chemistry research papers are in 'chemistry_papers' with the same fields. Scientists' details are in 'scientists' with fields AuthorID, AuthorName."),

    ("Calculate the DENSE_RANK for students based on their test scores in the mathematics exam, within their respective schools.",
     "Student scores for the mathematics exam are in 'math_scores' with fields StudentID, SchoolID, Score. School information is in 'schools' with fields SchoolID, SchoolName."),

    ("Retrieve the top 3 most frequently occurring scientific terms from the corpus of biology research articles.",
     "The biology research articles' text corpus is in 'biology_corpus' with fields ArticleID, ArticleText. Scientific terms are extracted and stored in 'scientific_terms' with fields TermID, TermText."),

    ("Find the average temperature change per year for a specific region in the climate dataset.",
     "The climate dataset is in 'climate_data' with fields Year, RegionID, Temperature. Region details are in 'regions' with fields RegionID, RegionName."),

    ("List the experiments where the observed results deviated from the expected results by more than 10% in the physics laboratory database.",
     "Physics experiments data is in 'physics_experiments' with fields ExperimentID, ExperimentName, ExpectedResult, ObservedResult. Experiment details are in 'experiment_details' with fields ExperimentID, ExperimentDescription."),

    ("Calculate the DENSE_RANK for publications based on their impact factor in the scientific journal database.",
     "The scientific journals database contains 'journals' with fields JournalID, JournalName, ImpactFactor, and 'publications' with fields PublicationID, JournalID, Title, PublicationDate."),

    ("Retrieve a list of researchers who have collaborated on at least 3 research projects in the genetics database.",
     "The genetics research projects are in 'genetics_projects' with fields ProjectID, ProjectName. Researcher collaborations are tracked in 'researcher_collaborations' with fields ResearcherID, ProjectID."),

    ("Find the top 5 most cited scientific articles authored by researchers with a PhD degree in the field of chemistry.",
     "The chemistry research articles database contains 'chemistry_articles' with fields ArticleID, Title, AuthorID, CitationCount. Researcher details are in 'researchers' with fields AuthorID, AuthorName, Degree."),

    ("Calculate the average precipitation rate per month for a specific geographic location in the meteorological dataset.",
     "Meteorological data is in 'meteorological_data' with fields Month, LocationID, PrecipitationRate. Location details are in 'locations' with fields LocationID, LocationName.")
]