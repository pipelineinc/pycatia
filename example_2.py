#! /usr/bin/python3.6

"""

    Example 2:

    Get all the points in the geometrical set 'Points' and print the co-ordinate.

"""
from pycatia import CATIAApplication
from pycatia import CATIAMeasurable
from pycatia import create_reference, create_measurable
from pycatia import create_spa_workbench

catia = CATIAApplication()

documents = catia.documents()
documents.open(r'tests\CF_catia_measurable_part.CATPart')

document = catia.document()
part = document.part()
spa_workbench = create_spa_workbench(document.document)

hybrid_body = part.get_hybrid_body_by_name('Points')
points = part.get_hybrid_shapes_from_hybrid_body(hybrid_body)

for point in points:
    reference = create_reference(part.part, point)
    measurable = create_measurable(spa_workbench, reference)
    point_measurable = CATIAMeasurable(measurable)
    coordinates = point_measurable.get_point(catia)
    print(f'{point.name}: {coordinates}')
