"""Data models for representing results from karstification simulations.
These models serve as Python wrappers around the corresponding C++ classes in the `pykarstnsim_core` module,
so that callers do not need to directly interact with pykarstnsim_core.
"""

from dataclasses import dataclass

import pykarstnsim_core


@dataclass
class Vector3:
    """
    3D vector representing a point in space. Python wrapper around `pykarstnsim_core.Vector3`.
    """

    x: float
    y: float
    z: float

    @staticmethod
    def from_karstnsim_vector(v: pykarstnsim_core.Vector3) -> "Vector3":
        return Vector3(x=v.x, y=v.y, z=v.z)


@dataclass
class ResultPoint:
    """
    Point result containing spatial coordinates and simulation properties. Python wrapper around `pykarstnsim_core.ResultPoint`.
    """

    branch_id: int
    """Branch ID this point belongs to in the karst network."""

    cost: float
    """Cost associated with the point during simulation."""

    equivalent_radius: float
    """Equivalent radius computed for the point."""

    p: Vector3
    """3D coordinates of the point (Vector3)."""

    vadose_flag: bool
    """Flag indicating if the point is in the vadose zone (True) or phreatic zone (False)."""

    @staticmethod
    def from_karstnsim_point(pt: pykarstnsim_core.ResultPoint) -> "ResultPoint":
        return ResultPoint(
            branch_id=pt.branch_id,
            cost=pt.cost,
            equivalent_radius=pt.equivalent_radius,
            p=Vector3.from_karstnsim_vector(pt.p),
            vadose_flag=pt.vadose_flag,
        )


@dataclass
class ResultSegment:
    """
    Segment result connecting two points in the karst network. Python wrapper around `pykarstnsim_core.ResultSegment`.
    """

    start: ResultPoint
    """Starting point of the segment"""
    end: ResultPoint
    """Ending point of the segment"""

    @staticmethod
    def from_karstnsim_segment(seg: pykarstnsim_core.ResultSegment) -> "ResultSegment":
        return ResultSegment(
            start=ResultPoint.from_karstnsim_point(seg.start),
            end=ResultPoint.from_karstnsim_point(seg.end),
        )


@dataclass
class KarstNSimResult:
    """
    Result of a karstification simulation containing all segments. Python wrapper around `pykarstnsim_core.KarstNetworkResult`.
    """

    _res: pykarstnsim_core.KarstNetworkResult
    segments: list[ResultSegment]
    """List of segments in the karst network."""

    def __init__(self, res: pykarstnsim_core.KarstNetworkResult):
        self._res = res
        self.segments = [
            ResultSegment.from_karstnsim_segment(seg) for seg in res.segments
        ]

    def to_string(self) -> str:
        """Get a string representation of the result."""
        return self._res.to_string()
