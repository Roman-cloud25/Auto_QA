"""
Employee data model.
"""
from typing import Optional, Dict, Any
from dataclasses import dataclass, asdict


@dataclass
class Employee:
    first_name: str
    last_name: str
    email: str
    phone: str
    company_id: int
    position: Optional[str] = None
    salary: Optional[int] = None
    department: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}

    @classmethod
    def from_response(cls, data: Dict[str, Any]) -> 'Employee':
        return cls(
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            email=data.get('email', ''),
            phone=data.get('phone', ''),
            company_id=data.get('company_id', 0),
            position=data.get('position'),
            salary=data.get('salary'),
            department=data.get('department'),
            address=data.get('address'),
            city=data.get('city')
        )

    def validate(self) -> bool:
        if not self.first_name or not self.last_name:
            return False
        if not self.email or '@' not in self.email:
            return False
        if not self.phone or not self.phone.startswith('+'):
            return False
        if self.company_id <= 0:
            return False
        return True