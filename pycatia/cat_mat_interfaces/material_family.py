#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.cat_mat_interfaces.materials import Materials
from pycatia.system_interfaces.any_object import AnyObject


class MaterialFamily(AnyObject):
    """
    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.AnyObject
            |                     MaterialFamily
            |
            | Represents a Material Family object.
            | This object is used to group Materials objects in a material
            | document.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.material_family = com_object

    @property
    def materials(self) -> Materials:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Materials() As Materials (Read Only)
                |
                |     Returns the material collection object from the current
                |     material family.

        :return: Materials
        :rtype: Materials
        """

        return Materials(self.material_family.Materials)

    def __repr__(self):
        return f'MaterialFamily(name="{self.name}")'
