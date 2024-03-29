from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional

class SchoolGenderEnum(str, Enum):
    Female = 'Female'
    Male = 'Male'
    Mixed = 'Mixed'

class StudentGenderEnum(str, Enum):
    Female = 'Female'
    Male = 'Male'
    Unspecified = 'Unspecified'

# school model
class SchoolBase(BaseModel):
    name: str
    country: str
    city: str
    gender_school: SchoolGenderEnum
    id: Optional[str]


class School(SchoolBase):
    class Config:
        orm_mode = True


# cohort model
class CohortBase(BaseModel):
    name: str
    description: Optional[str] = ""
    school: str

class Cohort(CohortBase):
    class Config:
        orm_mode = True

# student model
class StudentBase(BaseModel):
    name: str
    email: EmailStr
    school: str
    gender: StudentGenderEnum
    pseudonym: str
    personal_id: str
    cohort: Optional[str]
    phone_number: Optional[str]
    cardano_wallet: Optional[str]
    atala_prism_did: Optional[str]
    milestones_achieved: Optional[int] = 0
    pschool_token: Optional[str]
    pAcceptance_token: Optional[str]
    grant_received: Optional[float] = 0.0
    total_grant: Optional[float] = 0.0
    student_image: Optional[str]
    stake_address: Optional[str]
    school_id: Optional[str]
    cohort_id: Optional[str]
    location: Optional[str]
    description: Optional[str]
    telegram: Optional[str]
    linkedin: Optional[str]
    twitter: Optional[str]
    whatsapp: Optional[str]
    github: Optional[str]

class StudentCreate(StudentBase):
    pseudonym: str
    personal_id: str
    cohort: Optional[str]
    phone_number: Optional[str]
    cardano_wallet: Optional[str]
    atala_prism_did: Optional[str]
    milestones_achieved: Optional[int] = 0
    pschool_token: Optional[str]
    pAcceptance_token: Optional[str]
    grant_received: Optional[float] = 0.0
    total_grant: Optional[float] = 0.0
    student_image: Optional[str]
    stake_address: Optional[str]
    school_id: Optional[str]
    cohort_id: Optional[str]
    location: Optional[str]
    description: Optional[str]
    telegram: Optional[str]
    linkedin: Optional[str]
    twitter: Optional[str]
    whatsapp: Optional[str]
    github: Optional[str]

class Student(StudentBase):
    class Config:
        orm_mode = True

# milestone model
class MilestoneBase(BaseModel):
    description: Optional[str]
    step_nbr: int
    cohort_name: str

class Milestone(MilestoneBase):
    class Config:
        orm_mode = True
