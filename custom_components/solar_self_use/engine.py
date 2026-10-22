"""Calculate instantaneous solar self-use from power measurements."""
from __future__ import annotations

def watts(value: float, unit: str | None) -> float:
    if unit == "kW":
        return value * 1000.0
    if unit not in ("W", "kW"):
        raise ValueError("power sensor must report W or kW")
    return value

def calculate(config, values, units):
    try:
        pv = watts(float(values["pv_power_entity"]), units["pv_power_entity"])
        export = watts(float(values["export_power_entity"]), units["export_power_entity"])
        if config["export_sign"] == "negative":
            export = -export
        pv = max(0.0, pv)
        export = min(max(0.0, export), pv)
        used = max(0.0, pv - export)
        ratio = (used / pv * 100.0) if pv > 0 else None
        return {"self_used": round(used, 1), "export": round(export, 1), "self_use_percent": round(ratio, 1) if ratio is not None else None}
    except (TypeError, ValueError, OverflowError):
        return {"self_used": None, "export": None, "self_use_percent": None}
