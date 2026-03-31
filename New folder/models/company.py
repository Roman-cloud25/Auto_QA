"""
Модель данных компании.

Содержит класс Company для представления данных компании.
"""

from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict


@dataclass
class Company:
    """
    Класс для представления данных компании.

    Attributes:
        name: Название компании
        description: Описание компании
        is_active: Активна ли компания
        company_id: ID компании (опционально)
    """

    name: str
    description: str
    is_active: bool = True
    company_id: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        """
        Преобразует объект Company в словарь.

        Returns:
            Dict[str, Any]: Словарь с данными компании
        """
        data = asdict(self)
        if 'company_id' in data:
            del data['company_id']
        return data

    @classmethod
    def from_response(cls, data: Dict[str, Any]) -> 'Company':
        """
        Создает объект Company из ответа API.

        Args:
            data: Словарь с данными из API

        Returns:
            Company: Объект компании
        """
        return cls(
            name=data.get('name', ''),
            description=data.get('description', ''),
            is_active=data.get('is_active', True),
            company_id=data.get('id')
        )