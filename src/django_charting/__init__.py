from django_charting.charts import Chart
from django_charting.columns import BaseColumn, DateColumn, NumberColumn, StringColumn

try:
    from importlib.metadata import metadata
except ImportError:
    from importlib_metadata import metadata

meta = metadata("django-charting")

__version__ = meta["Version"]

__all__ = [
    "__version__",
    "Chart",
    "BaseColumn",
    "StringColumn",
    "NumberColumn",
    "DateColumn",
]
