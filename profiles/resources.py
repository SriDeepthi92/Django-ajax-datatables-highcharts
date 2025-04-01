from import_export import resources
from materials.models import compound

class compoundResource(resources.ModelResource):
    class Meta:
        model = compound