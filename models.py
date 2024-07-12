from pydantic import BaseModel
from datetime import date

class HealthCareData(BaseModel):
    external_account_id: int
    original_balance: float
    origination_date: date
    account_status: str
    date_last_worked: date
    number_of_payments: int
    date_last_paid: date
    date_last_promise: date
    number_of_broken_promises: int
    date_last_broken: date
    number_of_calls: int
    number_of_contacts: int
    date_last_contacted: date
    number_of_letters_sent: int
    number_of_emails_sent: int
    number_of_emails_opened: int
    email_response: str
    date_last_email_sent: date
    date_last_email_open: date
    date_last_email_response: date
    number_of_texts_sent: int
    text_response: str
    date_last_text: date
    date_last_text_response: date
    web_vists: int
    payment_channel: str
    date_of_treatment: date
    insurance_carrier: str
    judgement_date: date
    current_balance: float
    is_historical: str
    communication_preference: str
    number_of_calls_received: int
    number_of_estatements_sent: int
    last_payment_amount: float
    last_payment_type: str
    financial_class: str
    primary_insurance: str
    secondary_insurance: str
    patient_type: str
    collection_type: str
    date_received: date
    first_name: str
    last_name: str
    social_security_number: str
    date_of_birth: date
    external_person_id: int
    address1: str
    address2: str
    city: str
    state: str
    zip_code: int
    email_address: str
    phone_number: int
    formatted_phone_number: str
    # created: str

