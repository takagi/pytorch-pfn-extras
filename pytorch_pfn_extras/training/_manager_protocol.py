from typing import Dict, Mapping, Optional, TYPE_CHECKING
from typing_extensions import Protocol

import torch

if TYPE_CHECKING:
    from pytorch_pfn_extras.training.extension import Extension
    from pytorch_pfn_extras import writing
    from pytorch_pfn_extras import reporting


class ExtensionsManagerProtocol(Protocol):

    @property
    def iteration(self) -> int:
        ...

    @property
    def epoch(self) -> int:
        ...

    @property
    def epoch_detail(self) -> float:
        ...

    @property
    def models(self) -> Dict[str, torch.nn.Module]:
        ...

    @property
    def raw_models(self) -> Mapping[str, torch.nn.Module]:
        ...

    @property
    def optimizers(self) -> Mapping[str, torch.optim.Optimizer]:
        ...

    @property
    def elapsed_time(self) -> float:
        ...

    @property
    def is_before_training(self) -> bool:
        ...

    @property
    def stop_trigger(self) -> bool:
        ...

    @property
    def out(self) -> str:
        ...

    @property
    def writer(self) -> Optional['writing.Writer']:
        ...

    @property
    def reporter(self) -> 'reporting.Reporter':
        ...

    def get_extension(self, name: str) -> 'Extension':
        ...
