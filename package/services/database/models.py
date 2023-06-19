from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, Date, DateTime
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

class Process(Base):
    __tablename__ = "processes"

    id = Column(Integer, primary_key=True, index=True)
    process_key = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False)
    start_at = Column(DateTime)
    finish_at = Column(DateTime)
    status = Column(String(25))
    observation = Column(String(150))
