from random import randint
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
    def _digits_from_string(cls, doc: str) -> list[int]:
        doc = doc.upper()
        return [ord(d) - cls._digit_offset for d in doc if d in cls._charset]

    @classmethod
    def _string_from_digits(cls, digits: list[int]) -> str:
        chars = [chr(d + cls._digit_offset) for d in digits]
        return "".join(chars)

    @classmethod
    def _get_validators(cls, digits: list[int]) -> list[int]:
        validators: list[int] = []
        temp_digits = digits.copy()

        for seq in cls._sequences:
            pos = len(seq)
            digit = sum([seq[i] * temp_digits[i] for i in range(pos)])
            digit = digit % cls._modulo
            digit = cls._modulo_transformer(digit)

            temp_digits[pos] = digit
            validators.append(digit)

        return validators

    @classmethod
    def _check_validators(
        cls,
        digits: list[int],
        validators: list[int],
    ) -> bool:
        pos = len(validators)
        return digits[-pos:] == validators

    @classmethod
    def generate(cls, mask: bool = False) -> str:
        idx = [randint(0, len(cls._charset) - 1) for _ in range(cls._len)]
        doc = "".join(cls._charset[i] for i in idx)
        digits = cls._digits_from_string(doc)
        validators = cls._get_validators(digits)

        for i, v in enumerate(validators):
            digits[-len(validators) + i] = v

        doc = cls._string_from_digits(digits)

        if mask:
            return cls._fmt_mask.replace("#", "{}").format(*doc)

        return doc

    @classmethod
    def validate(cls, doc: str) -> bool:
        digits = cls._digits_from_string(doc)

        if len(digits) != cls._len:
            return False

        if len(set(digits)) == 1:
            return False

        validators = cls._get_validators(digits)
        return cls._check_validators(digits, validators)

    @classmethod
    def format(cls, doc: str, mask: bool = False) -> str:
        digits = cls._digits_from_string(doc)
        doc = cls._string_from_digits(digits)

        if mask:
            return cls._fmt_mask.replace("#", "{}").format(*doc)

        return doc


class DocBrCPF(DocBr):
    _len = 11
    _modulo = 11
    _sequences = [
        (10, 9, 8, 7, 6, 5, 4, 3, 2),
        (11, 10, 9, 8, 7, 6, 5, 4, 3, 2),
    ]
    _modulo_transformer = lambda x: 0 if x < 2 else 11 - x  # noqa: E731
    _charset = "0123456789"
    _fmt_mask = "###.###.###-##"


class DocBrCNPJ(DocBr):
    _len = 14
    _modulo = 11
    _sequences = [
        (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2),
        (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2),
    ]
    _modulo_transformer = lambda x: 0 if x < 2 else 11 - x  # noqa: E731
    _charset = "0123456789ABCDEFGHIJKLMNOPQSRTUVWXYZ"
    _fmt_mask = "##.###.###/####-##"
