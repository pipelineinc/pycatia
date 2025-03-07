#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.funct_system_interfaces.functional_action import FunctionalAction
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class FunctActionsGroup(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FunctActionsGroup
                | 
                | The interface to access a group of functional actions in a
                | system.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.funct_actions_group = com_object

    @property
    def actions_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActionsCount() As long (Read Only)
                | 
                |     Get the count of actions referenced by the actions' group.

        :return: int
        :rtype: int
        """

        return self.funct_actions_group.ActionsCount

    def add(self, i_action: FunctionalAction) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Add(FunctionalAction iAction)
                | 
                |     Adds an action to the actions' group.
                | 
                |     Fails if the action :
                | 
                |         is already in a group
                |         has "From" and "To" extremities inconsistent with the existing actions.
                |         
                | 
                |     In case of an ordered group, the added action will be
                |     appended.
                |     (i.e. for flows sequencing actions)
                | 
                |     Parameters:
                | 
                |         iAction
                |             The action to be added to the group of actions.

        :param FunctionalAction i_action:
        :return: None
        :rtype: None
        """
        return self.funct_actions_group.Add(i_action.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add'
        # # vba_code = """
        # # Public Function add(funct_actions_group)
        # #     Dim iAction (2)
        # #     funct_actions_group.Add iAction
        # #     add = iAction
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_extremities(self, o_input_x: float, o_input_y: float, o_output_x: float, o_output_y: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetExtremities(double oInputX,
                | double oInputY,
                | double oOutputX,
                | double oOutputY)
                | 
                |     Get coordinates of Input and Output extremities.

        :param float o_input_x:
        :param float o_input_y:
        :param float o_output_x:
        :param float o_output_y:
        :return: None
        :rtype: None
        """
        return self.funct_actions_group.GetExtremities(o_input_x, o_input_y, o_output_x, o_output_y)

    def remove(self, i_action: FunctionalAction) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(FunctionalAction iAction)
                | 
                |     Removes an action from the actions' group.
                | 
                |     Parameters:
                | 
                |         iAction
                |             The action to be removed from the group of
                |             actions.

        :param FunctionalAction i_action:
        :return: None
        :rtype: None
        """
        return self.funct_actions_group.Remove(i_action.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(funct_actions_group)
        # #     Dim iAction (2)
        # #     funct_actions_group.Remove iAction
        # #     remove = iAction
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_position(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemovePosition(long iPosition)
                | 
                |     Removes an action from the actions' group.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position of the action to be removed from the group of
                |             actions.

        :param int i_position:
        :return: None
        :rtype: None
        """
        return self.funct_actions_group.RemovePosition(i_position)

    def retrieve(self, i_index: cat_variant) -> FunctionalAction:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Retrieve(CATVariant iIndex) As FunctionalAction
                | 
                |     Returns an action using its index or its name from the actions
                |     group.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the action to retrieve from the group of
                |             actions. As a numerics, this index is the rank of the action in the group. The
                |             index of the first action in the group is 1, and the index of the last action
                |             is Count. As a string, it is the name you assigned to the action using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved action 
                |     Example:
                |         This example retrieves in Obj1 the fifth action in the group and in
                |         Obj2 the action named Valve.
                | 
                |          Dim Act1 As FunctionalAction
                |          Set Act1 = ActionsGrp.Retrieve(5)
                |          Dim Act2 As FunctionalAction
                |          Set Act2 = ActionsGrp.Retrieve("Reduces noise")

        :param CATVariant i_index:
        :return: FunctionalAction
        :rtype: FunctionalAction
        """
        return FunctionalAction(self.funct_actions_group.Retrieve(i_index))

    def set_extremities(self, i_input_x: float, i_input_y: float, i_output_x: float, i_output_y: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExtremities(double iInputX,
                | double iInputY,
                | double iOutputX,
                | double iOutputY)
                | 
                |     Set coordinates of Input and Output extremities.

        :param float i_input_x:
        :param float i_input_y:
        :param float i_output_x:
        :param float i_output_y:
        :return: None
        :rtype: None
        """
        return self.funct_actions_group.SetExtremities(i_input_x, i_input_y, i_output_x, i_output_y)

    def __repr__(self):
        return f'FunctActionsGroup(name="{self.name}")'
