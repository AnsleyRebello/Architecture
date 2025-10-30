"""
Service layer for Booking operations
"""
from backend.models import db, Booking
from datetime import datetime


class BookingService:
    @staticmethod
    def create_booking(user_name, email, phone=None):
        
        booking = Booking(
            user_name=user_name,
            email=email,
            phone=phone,
            booking_date=datetime.utcnow()
        )
        db.session.add(booking)
        db.session.commit()
        return booking
    
    @staticmethod
    def get_all_bookings():
        """Get all bookings"""
        return Booking.query.all()
    
    @staticmethod
    def get_booking_by_id(booking_id):
        """Get booking by ID"""
        return Booking.query.get_or_404(booking_id)
    
    @staticmethod
    def update_booking(booking_id, **kwargs):
        """Update booking information"""
        booking = Booking.query.get_or_404(booking_id)
        
        if 'user_name' in kwargs:
            booking.user_name = kwargs['user_name']
        if 'email' in kwargs:
            booking.email = kwargs['email']
        if 'phone' in kwargs:
            booking.phone = kwargs['phone']
        
        db.session.commit()
        return booking
    
    @staticmethod
    def delete_booking(booking_id):
        """Delete a booking"""
        booking = Booking.query.get_or_404(booking_id)
        db.session.delete(booking)
        db.session.commit()
