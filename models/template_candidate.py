"""Template metadata for button detection."""

from dataclasses import dataclass
from typing import List, Any, Optional

from numpy.typing import NDArray
from numpy import float32


@dataclass(frozen=True)
class TemplateCandidate:
    """Descriptor metadata for drawing debug info.

    Includes keypoints (`kps`) for the template so we can compute an accurate
    homography-based mapping from template center -> image coordinates.
    """

    desc: NDArray[float32]
    width: int
    height: int
    kps: Optional[List[Any]] = None
