"""
Company data model.
"""
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict


@dataclass
class Company:
    name: str
    description: str
    is_active: bool = True
    company_id: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        if 'company_id' in data:
            del data['company_id']
        return data

    @classmethod
    def from_response(cls, data: Dict[str, Any]) -> 'Company':
        return cls(
            name=data.get('name', ''),
            description=data.get('description', ''),
            is_active=data.get('is_active', True),
            company_id=data.get('id')
        )