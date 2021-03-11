import simpy
import logging
from .num_spec import NumSpec
from .structure_item import StructureItem


class Function(StructureItem):
    """
    A Function is a transformation that accepts one or more inputs (items)
    and transforms them into outputs (items).
    """

    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 construct_id: str, systemModel: dict, structureItem: dict):

        super(Function, self).__init__(env, logger,
                                       construct_id, systemModel, structureItem)
        self.structureType = "Function"
        self.name = structureItem['referenceName']

        # **** Need to retrieve duration and timeout from systemModel ****
        self.duration = NumSpec()
        self.timeout = NumSpec()

    def simulate(self):
        """
        Setup the Simpy simulation for a Function
        """

        self.log_start()
        self.begin()
        yield self.env.timeout(self.duration.getValue())
        self.exit()
        self.end()
        self.log_end()

    def begin(self):
        """
        Begin Logic is executed at the very beginning of function execution
        (after enablement and triggering but before resources are acquired).
        """
        return

    def exit(self):
        """
        Exit Logic determines which exit to use for a multi-exit function.
        If the exit logic is empty, the probabilities associated with the
        exits are used to choose the exit.
        """
        return

    def end(self):
        """
        End Logic is executed at the very end of function execution
        (after resources are produced and items are output).
        """
        return
