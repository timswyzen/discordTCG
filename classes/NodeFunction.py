class NodeFunction:

    def __init__(self, func, trigger_type):
        """Each Node should now have a list of NodeFunctions.
        NodeFunctions have triggers, which will also include start of turn, self is spawned, and self dies.
        In doing so, we will only need a function and a trigger type."""
        self.func = func
        self.trigger_type = trigger_type # Change start of turn, self-spawned, and death into triggers