# entities
Gallery 5 3 → GalleryHall, GalleryBranch  
GalleryBranch 4 2 → Gallery  
GalleryHall 5 3 → Exhibit, Event, Booking  
Exhibit 6 4 → Artist, GalleryHall, Exhibition  
Painting 6 3 → Artist, RestorationRecord, StorageRoom  
Sculpture 5 2 → Artist, StorageRoom  
Artist 4 2 → ArtStyle  
ArtStyle 3 0 →  
ExhibitItem 3 1 → Exhibit  
StorageRoom 4 2 → Exhibit, InventoryItem  
RestorationRecord 5 2 → Painting, Restorer  
Visitor 6 4 → Ticket, MemberCard, Invoice, Donation  
Ticket 4 2 → Exhibition, Visitor  
MemberCard 4 2 → Visitor, DiscountPolicy  
Transaction 5 3 → Payment, Accountant, Invoice  
Payment 5 3 → Visitor, Cashier, Invoice  
Invoice 5 3 → Visitor, Payment, Statement  
Member 3 1 → MemberCard  
Address 3 0 →  
Exhibition 5 3 → Exhibit, GalleryHall, Curator  
ExhibitAssignment 3 2 → Exhibit, GalleryHall  
StorageEntry 3 1 → StorageRoom  
Catalog 2 1 → Exhibit  
25 16 7

---

# management
Employee 5 3 → GalleryHall, Assignment, Expense  
Cashier 4 2 → Payment, Transaction  
Accountant 4 2 → Transaction, Audit  
Curator 5 3 → Exhibition, Exhibit, Director  
Restorer 5 2 → Painting, RestorationRecord  
Cleaner 4 2 → GalleryHall  
Guide 4 2 → Exhibition, Tour  
Security 4 2 → Ticket, IncidentReport  
Technician 4 2 → Tool, MaintenanceLog  
Director 4 3 → Curator, FinancialReport, Budget  
GuideSchedule 3 1 → TimeSlot  
IncidentReport 3 2 → Security, Exhibit  
Payroll 3 2 → Employee, Statement  
28 14 6

---

# inventory
InventoryItem 4 2 → Warehouse, Supplier  
Warehouse 4 3 → InventoryItem, StorageRoom, StaffAssignment  
Supplier 4 2 → Order, Delivery  
Order 4 3 → Supplier, InventoryItem, Invoice  
Tool 4 2 → Technician, MaintenanceLog  
MaintenanceLog 4 2 → Technician, EquipmentLog  
Stock 3 2 → InventoryItem, Warehouse  
Receiving 3 2 → Order, Warehouse  
InventoryManager 4 3 → Stock, PurchaseOrder, Supplier  
Batch 3 1 → InventoryItem  
PriceCalculator 2 2 → InventoryItem, PurchaseOrder  
24 12 5

---

# finance
BankAccount 4 3 → Gallery, Transaction, Invoice  
Budget 4 3 → Expense, FinancialReport, Director  
Expense 4 2 → Employee, Budget  
FinancialReport 3 2 → Budget, Director  
Donation 4 2 → Visitor, Exhibit  
CreditCard 4 2 → Visitor, Payment  
Loan 4 2 → Gallery, Payment  
Revenue 3 2 → Invoice, Statement  
BillingItem 4 2 → Invoice, DiscountPolicy  
PaymentGateway 3 2 → Payment, BankAccount  
InsuranceClaim 3 2 → Invoice, Insurance  
Refund 3 2 → Invoice, Payment  
Audit 3 2 → Accountant, AuditLog  
Statement 3 2 → Account, Invoice  
35 18 6

---

# events
Event 4 2 → GalleryHall, Participant  
Tour 4 2 → Guide, Exhibit  
Workshop 4 2 → Instructor, Materials  
Auction 4 2 → Painting, Bid  
Bid 3 1 → Collector  
Donor 3 1 → Exhibit  
Sponsor 3 1 → Event  
Collector 3 1 → Painting  
TicketedEvent 3 2 → Event, Ticket  
Schedule 3 2 → TimeSlot, Room  
WaitingList 2 1 → TimeSlot  
40 19 6

---

# lab and services
Lab 4 2 → Sample, TestResult  
Sample 4 2 → Test, Analyzer  
Test 4 2 → Sample  
Analyzer 3 1 → Sample  
TechnicianLab 3 1 → Sample  
Report 3 1 → TestResult  
QualityControl 3 1 → TestResult  
EquipmentLog 2 1 → Technician, Tool  
18 9 3

---

# pharmacy (if present)
Pharmacy 4 2 → Inventory, Pharmacist  
Inventory 3 2 → Drug, Batch  
Drug 4 2 → Batch, Supplier  
Batch 3 1 → Drug  
Pharmacist 3 2 → DispenseLog, RefillRequest  
RefillRequest 3 1 → Patient  
DispenseLog 3 2 → Pharmacist, Drug  
Supplier 3 1 → Order  
20 11 4

---

# scheduling & notifications
TimeSlot 3 2 → Calendar, WaitingList  
Appointment 4 2 → Patient/Visitor, Doctor/Guide, TimeSlot  
DoctorAvailability 3 1 → TimeSlot  
Room 3 1 → Booking  
Booking 3 2 → Appointment, Room  
Calendar 2 1 → TimeSlot  
Reminder 2 1 → Appointment  
Notification 2 1 → Appointment  
22 11 4

---

Классы: 62  
Поля: 175  
Поведения: 117  
Ассоциации: 243  
Исключения: 12
