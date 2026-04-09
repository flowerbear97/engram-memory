"""Neuragram exception hierarchy."""


class NeuragramError(Exception):
    """Base exception for all Neuragram errors."""


class MemoryNotFoundError(NeuragramError):
    """Raised when a memory with the given ID does not exist."""

    def __init__(self, memory_id: str) -> None:
        self.memory_id = memory_id
        super().__init__(f"Memory not found: {memory_id}")


class StoreError(NeuragramError):
    """Raised when a storage backend operation fails."""


class EmbeddingError(NeuragramError):
    """Raised when an embedding operation fails."""


class ConfigError(NeuragramError):
    """Raised when configuration is invalid."""


class BackendNotAvailableError(NeuragramError):
    """Raised when a requested storage backend is not installed or available."""

    def __init__(self, backend: str, reason: str = "") -> None:
        self.backend = backend
        msg = f"Backend not available: {backend}"
        if reason:
            msg += f" ({reason})"
        super().__init__(msg)
