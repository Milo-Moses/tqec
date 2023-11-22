from tqec.enums import ABOVE_OF, BELOW_OF, LEFT_OF, RIGHT_OF
from tqec.templates.base import TemplateWithPlaquettes
from tqec.templates.scalable.rectangle import ScalableRectangle
from tqec.templates.scalable.square import ScalableAlternatingSquare
from tqec.templates.orchestrator import TemplateOrchestrator


class ScalableQubitSquare(TemplateOrchestrator):
    def __init__(self, dim: int) -> None:
        _templates = [
            # Central square, containing plaquettes of types 3 and 4
            TemplateWithPlaquettes(ScalableAlternatingSquare(dim), [3, 4]),
            # Top rectangle, containing plaquettes of type 1 only
            TemplateWithPlaquettes(ScalableRectangle(dim, 1), [0, 1]),
            # Left rectangle, containing plaquettes of type 2 only
            TemplateWithPlaquettes(ScalableRectangle(1, dim), [2, 0]),
            # Right rectangle, containing plaquettes of type 5 only
            TemplateWithPlaquettes(ScalableRectangle(1, dim), [0, 5]),
            # Bottom rectangle, containing plaquettes of type 6 only
            TemplateWithPlaquettes(ScalableRectangle(dim, 1), [0, 6]),
        ]
        _relations = [
            (1, ABOVE_OF, 0),
            (2, LEFT_OF, 0),
            (3, RIGHT_OF, 0),
            (4, BELOW_OF, 0),
        ]
        TemplateOrchestrator.__init__(self, _templates)
        for source, relpos, target in _relations:
            self.add_relation(source, relpos, target)


class ScalableQubitRectangle(TemplateOrchestrator):
    def __init__(self, width: int, height: int) -> None:
        _templates = [
            # Central square, containing plaquettes of types 3 and 4
            TemplateWithPlaquettes(ScalableRectangle(width, height), [3, 4]),
            # Top rectangle, containing plaquettes of type 1 only
            TemplateWithPlaquettes(ScalableRectangle(width, 1), [0, 1]),
            # Left rectangle, containing plaquettes of type 2 only
            TemplateWithPlaquettes(ScalableRectangle(1, height), [2, 0]),
            # Right rectangle, containing plaquettes of type 5 only
            TemplateWithPlaquettes(ScalableRectangle(1, height), [0, 5]),
            # Bottom rectangle, containing plaquettes of type 6 only
            TemplateWithPlaquettes(ScalableRectangle(width, 1), [0, 6]),
        ]
        _relations = [
            (1, ABOVE_OF, 0),
            (2, LEFT_OF, 0),
            (3, RIGHT_OF, 0),
            (4, BELOW_OF, 0),
        ]
        TemplateOrchestrator.__init__(self, _templates)
        for source, relpos, target in _relations:
            self.add_relation(source, relpos, target)