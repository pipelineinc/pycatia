#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.hybrid_shape_interfaces.point import Point
from pycatia.in_interfaces.reference import Reference


class HybridShapePointTangent(Point):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointTangent
                | 
                | Point Tangent.
                | Role: Allows to access data of the point feature created as follow
                | :
                | The tangent to the curve at this point is colinear to a given
                | direction.
                | Note: The resulting feature can contain several points.
                | 
                | See also:
                |     Length 
                | See also:
                |     Reference 
                | See also:
                |     HybridShapeDirection 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_tangent = com_object

    @property
    def curve(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Curve() As Reference
                | 
                |     Returns or Gets the supporting curve.
                |     Sub-element(s) supported (see Boundary object): Edge.
                | 
                |     Example
                |     :
                |         This example retrieves in oCurve the supporting Curve for the
                |         PointTangent feature.
                | 
                |          Dim oCurve As CATIAReference   
                |          Set oCurve  = PointTangent.Curve

        :return: Reference
        """

        return Reference(self.hybrid_shape_point_tangent.Curve)

    @curve.setter
    def curve(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_point_tangent.Curve = value

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Direction() As HybridShapeDirection
                | 
                |     Returns or Sets the direction.
                | 
                |     Example
                |     :
                |         This example retrieves in oDirection the tangent direction use to
                |         compute on supporting curve the PointTangent feature.
                | 
                |          Dim oDirection As CATIAHybridShapeDirection
                |          Set oDirection  = PointTangent.Direction

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_point_tangent.Direction)

    @direction.setter
    def direction(self, value):
        """
        :param HybridShapeDirection value:
        """

        self.hybrid_shape_point_tangent.Direction = value

    def __repr__(self):
        return f'HybridShapePointTangent(name="{ self.name }")'
