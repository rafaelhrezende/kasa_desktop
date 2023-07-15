from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, Date
from sqlalchemy.orm import relationship

from .database import Base

class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    description = Column(String(250), index=True)
    category = Column(String(50))
    initial_value = Column(Numeric(10,2))
    payment_day = Column(Integer)
    is_active = Column(Boolean, default=True, nullable=False)

    invoices = relationship("Invoice", back_populates="bill")
    
    def to_string(self):
        return f"{self.id} - {self.title} R$ {self.initial_value}"
    
    def __str__(self):
        return f"{self.id} - {self.title} R$ {self.initial_value}"

    def update_attributes(self, new_data):
        self.title = new_data.title
        self.description = new_data.description
        self.category = new_data.category
        self.initial_value = new_data.initial_value
        self.payment_day = new_data.payment_day
        self.is_active = new_data.is_active
        
    
class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    method = Column(String(50))
    reference_year = Column(Integer)
    reference_month = Column(Integer)
    description = Column(String(300), nullable=True)
    value = Column(Numeric(10,2))
    due_date = Column(Date)
    completion_date = Column(Date)
    pay_day = Column(Date)
    status = Column(Integer)
    bill_id = Column(Integer, ForeignKey("bills.id"))

    bill = relationship("Bill", back_populates="invoices")
    
    def get_field(self, field):
        if field == 'bill' and self.bill != None:
            return self.bill.title
        return getattr(self, field)

class Process(Base):
    __tablename__ = "processes"

    id = Column(Integer, primary_key=True, index=True)
    process_key = Column(String(50), nullable=False)
    created_at = Column(Date, nullable=False)
    start_at = Column(Date)
    finish_at = Column(Date)
    status = Column(String(25))
    observation = Column(String(150))
    
    def get_field(self, field):
        return getattr(self, field)
    
    def update_attributes(self, process):
        self.process_key = process.process_key
        self.created_at = process.created_at
        self.start_at = process.start_at
        self.finish_at = process.finish_at
        self.status = process.status
        self.observation = process.observation
