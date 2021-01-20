#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.collection import Collection


class AnalysisMeshLocalSpecifications(Collection):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AnalysisMeshLocalSpecifications
                | 
                | The interface to access a AnalysisMeshLocalSpecifications.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_mesh_local_specifications = com_object

    def add(self, i_type: str) -> AnalysisMeshLocalSpecification:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(CATBSTR iType) As AnalysisMeshLocalSpecification
                | 
                |     Creates a new local specification and adds it to the local specification
                |     collection.
                |     The local specification will be created linked to the AnalysisMeshManager
                |     object.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of mesh part to create. 
                | 
                |     Returns:
                |         The created local specification

        :param str i_type:
        :return: AnalysisMeshLocalSpecification
        :rtype: AnalysisMeshLocalSpecification
        """
        return AnalysisMeshLocalSpecification(self.analysis_mesh_local_specifications.Add(i_type))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a local specification using its index or its name from the local
                |     specification collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the local specification to retrieve from
                |             the collection of local specification . As a numeric, this index is the rank of
                |             the local specification in the collection. The index of the first local
                |             specification in the collection is 1, and the index of the last local
                |             specification is Count. As a string, it is the name you assigned to the local
                |             specification using the 
                | 
                |         AnyObject.Name property.

        :param CATVariant i_index:
        :return: None
        :rtype: None
        """
        return self.analysis_mesh_local_specifications.Remove(i_index.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(analysis_mesh_local_specifications)
        # #     Dim iIndex (2)
        # #     analysis_mesh_local_specifications.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AnalysisMeshLocalSpecifications(name="{ self.name }")'
