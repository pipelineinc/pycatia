#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.collection import Collection


class BasicComponents(Collection):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     BasicComponents
                | 
                | The collection of Basic Components defining and analysis
                | object.
                | These components are agregated by another basic component, an entity or a
                | set.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.basic_components = com_object

    def item(self, i_variant: CATVariant) -> BasicComponent:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iVariant) As BasicComponent
                | 
                |     Returns an Basic Component using its index or its name from the Basic
                |     Components collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Basic Component to retrieve from the
                |             collection of Basic Component. As a numerics, this index is the rank of the
                |             Basic Component. in the collection. The index of the first Basic Component in
                |             the collection is 1, and the index of the last Basic Component is Count. As a
                |             string, it is the name you assigned to the Basic Component using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved Basic Component

        :param CATVariant i_variant:
        :return: BasicComponent
        :rtype: BasicComponent
        """
        return BasicComponent(self.basic_components.Item(i_variant.com_object))

    def __repr__(self):
        return f'BasicComponents(name="{ self.name }")'
