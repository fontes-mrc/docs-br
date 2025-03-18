import numpy as np
import numpy.typing as npt
from typing import Callable, Sequence


class DocBr:
    _len: int
    _modulo: int
    _sequences: Sequence[Sequence[int]]
    _modulo_transformer: Callable
    _charset: Sequence[str]
    _fmt_mask: str
    _digit_offset: int = ord("0")

    @classmethod
    def _digits_from_string(cls, docs: npt.NDArray[np.str_]) -> npt.NDArray[np.uint8]:
        count = docs.shape[0]
        docs = docs.view((str, 1))
        docs = docs.reshape(count, -1)
        docs = docs.astype("S1")
        docs_int = docs.view(np.uint8)
        docs_int -= cls._digit_offset
        return docs_int

    @classmethod
    def _string_from_digits(cls, digits: npt.NDArray[np.uint8]) -> npt.NDArray[np.str_]:
        digits += cls._digit_offset
        digits = digits.view("S" + str(digits.shape[1]))
        digits_str = digits.astype(str)
        digits_str = digits_str.ravel()
        return digits_str

    @classmethod
    def _get_validators(cls, digits: npt.NDArray[np.uint8]) -> npt.NDArray[np.uint8]:
        temp_digits = digits.copy()
        docs_count = digits.shape[0]
        
        for i, seq in enumerate(cls._sequences):
            pos = len(seq)
            seq_array = np.repeat([seq], docs_count, axis=0)

            digit = (temp_digits[:, :pos] * seq_array[:, :pos])
            digit = digit.sum(axis=1)
            digit = digit % cls._modulo

            digit = cls._modulo_transformer(digit)
            temp_digits[:, pos] = digit

        out = temp_digits[:, -len(cls._sequences):]
        return out
    
    @classmethod
    def _check_validators(
        cls,
        digits: npt.NDArray[np.uint8],
        validators: npt.NDArray[np.uint8],
    ) -> npt.ArrayLike:
        pos = len(cls._sequences)
    
        test: npt.NDArray[np.bool_] = digits[:, -pos:] == validators

        return test.all(axis=1)

    @classmethod
    def _resolve_mask(cls, docs: npt.NDArray[np.uint8]) -> npt.NDArray[np.uint8]:
        format_ = cls._digits_from_string(np.array([cls._fmt_mask], dtype=str))
        format_ = np.repeat(format_, len(docs), axis=0)

        format_1d = format_.ravel()        
        mask = format_1d == ord("#")
        format_1d[mask] = docs.ravel()

        return format_1d.reshape(format_.shape)

    @classmethod
    def generate(cls, mask: bool = False, n: int = 1) -> npt.NDArray[np.str_]:
        docs = np.random.choice(list(cls._charset), (n, cls._len))

        docs_str = np.apply_along_axis(lambda x: "".join(x), 1, docs)
        docs_digits = cls._digits_from_string(docs_str)
        validators = cls._get_validators(docs_digits)

        docs_digits[:, -len(cls._sequences):] = validators

        if mask:
            docs_digits = cls._resolve_mask(docs_digits)

        return cls._string_from_digits(docs_digits)
        
    @classmethod
    def validate(cls, docs: npt.NDArray[np.str_]) -> npt.ArrayLike:
        if not all(len(doc) == cls._len for doc in docs):
            raise ValueError(f"There are documents with invalid length. Expected {cls._len} characters.")
        
        docs_digits = cls._digits_from_string(docs)
        validators = cls._get_validators(docs_digits)
        test = cls._check_validators(docs_digits, validators)
        return test
    
    @classmethod
    def format(cls, docs: npt.NDArray[np.str_], mask: bool = False) -> npt.NDArray[np.str_]:
        docs_digits = cls._digits_from_string(docs)
        if mask:
            docs_digits = cls._resolve_mask(docs_digits)
        return cls._string_from_digits(docs_digits)


class DocBrCPF(DocBr):
    _len = 11
    _modulo = 11
    _sequences = [
        (10, 9, 8, 7, 6, 5, 4, 3, 2),
        (11, 10, 9, 8, 7, 6, 5, 4, 3, 2),
    ]
    _modulo_transformer = lambda x: np.where(x < 2, 0, 11 - x)  # noqa: E731
    _charset = "0123456789"
    _fmt_mask = "###.###.###-##"


class DocBrCNPJ(DocBr):
    _len = 14
    _modulo = 11
    _sequences = [
        (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2),
        (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2),
    ]
    _modulo_transformer = lambda x: np.where(x < 2, 0, 11 - x)  # noqa: E731
    _charset = "0123456789ABCDEFGHIJKLMNOPQSRTUVWXYZ"
    _fmt_mask = "##.###.###/####-##"

