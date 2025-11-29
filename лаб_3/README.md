# Проект: Туристическая компания

# tours

Tour 13 11 → Booking, Destination, Flight, Guide, Hotel

AdventureTour 12 5 → 

CulturalTour 11 5 → 

DayTour 10 5 → 

GroupTour 11 5 → 

IndividualTour 10 5 → 

Excursion 11 5 → 

Cruise 13 6 → 

Package 11 5 → 

9 9 4

---

# destinations

Destination 11 9 → Attraction, City, Country, Hotel

Country 11 6 → 

City 12 6 → 

Attraction 11 6 → 

Hotel 12 9 → City, Destination, Reservation

Restaurant 11 6 → 

6 6 3

---

# transportation

Flight 12 9 → Booking, Reservation, Tour

Bus 12 6 → 

Car 13 6 → 

Train 13 6 → 

4 4 1

---

# booking

Booking 11 9 → Invoice, Payment, Tour, Turist

Reservation 10 7 → Hotel, Turist

Order 9 5 → 

Ticket 12 8 → 

Voucher 9 5 → 

Cancellation 9 5 → 

Checkout 10 5 → 

7 7 2

---

# customers

Turist 11 10 → Booking, Card, Insurance, Passport, Wallet

Passport 11 8 → Turist, Visa

Visa 10 6 → 

Insurance 11 6 → 

4 4 2

---

# staff

Guide 11 5 → 

Agent 11 5 → 

Consultant 10 5 → 

Manager 10 5 → 

Admin 11 5 → 

Accountant 10 5 → 

Support 10 5 → 

Photographer 11 5 → 

Driver 11 5 → 

9 9 0

---

# finance

Payment 10 9 → Account, Booking, Card, Transaction

Transaction 10 6 → 

Invoice 11 5 → 

Account 11 8 → Bank, Card

Card 10 7 → 

Wallet 9 7 → 

Bank 11 8 → 

7 7 3

---

# services

Review 11 11 → Hotel, Tour, Turist

Complaint 10 9 → Booking, Support, Turist

Question 10 6 → 

3 3 2

---

# exceptions

BookingNotFoundException 2 0 → 

CancellationNotAllowedException 3 0 → 

CardNotFoundException 2 0 → 

HotelFullException 3 0 → 

InsufficientFundsException 3 0 → 

InvalidCardNumberException 2 0 → 

InvalidEmailException 2 0 → 

InvalidPasswordException 1 0 → 

PassportExpiredException 3 0 → 

TourFullException 2 0 → 

TourNotFoundException 2 0 → 

VisaRequiredException 2 0 → 

12 12 0

---

Классы: 48

Поля: 542

Поведения: 322

Ассоциации: 40

Исключения: 12
