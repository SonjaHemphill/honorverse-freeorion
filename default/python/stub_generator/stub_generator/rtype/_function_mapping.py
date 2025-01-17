from stub_generator.stub_generator.rtype._base_rtype_mapping import make_type
from common.fo_typing import EmpireId, Turn

_rtypes_map = {
    "currentTurn": Turn.__name__,
    "empireID": EmpireId.__name__,
    "allEmpireIDs": f"Vec[{EmpireId.__name__}]",
}


def update_function_rtype(name: str, rtype: str) -> str:
    key = (name,)
    if key in _rtypes_map:
        return _rtypes_map[key]
    else:
        return make_type(rtype)
