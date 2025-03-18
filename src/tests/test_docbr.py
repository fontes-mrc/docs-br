import unittest

from docbr import DocBrCNPJ, DocBrCPF


class TestDocBr(unittest.TestCase):
    def test_validate_cpf_valid(self):
        self.assertTrue(DocBrCPF.validate("93481451008"))

    def test_validate_cpf_invalid(self):
        self.assertFalse(DocBrCPF.validate("93481451007"))

    def test_validate_cnpj_valid(self):
        self.assertTrue(DocBrCNPJ.validate("39593854000164"))

    def test_validate_cnpj_invalid(self):
        self.assertFalse(DocBrCNPJ.validate("39593854000165"))

    def test_format_cpf_mask_false(self):
        self.assertEqual(
            DocBrCPF.format("93481451008", mask=False),
            "93481451008",
        )

    def test_format_cpf_mask_true(self):
        self.assertEqual(
            DocBrCPF.format("93481451008", mask=True),
            "934.814.510-08",
        )

    def test_format_cnpj_mask_false(self):
        self.assertEqual(
            DocBrCNPJ.format("39593854000164", mask=False),
            "39593854000164",
        )

    def test_format_cnpj_mask_true(self):
        self.assertEqual(
            DocBrCNPJ.format("39593854000164", mask=True),
            "39.593.854/0001-64",
        )

    def test_generate_cpf(self):
        result = DocBrCPF.generate()
        self.assertEqual(
            len(result),
            11,
        )
        self.assertTrue(DocBrCPF.validate(result))

    def test_generate_cnpj(self):
        result = DocBrCNPJ.generate()
        self.assertEqual(
            len(result),
            14,
        )
        self.assertTrue(DocBrCNPJ.validate(result))


if __name__ == "__main__":
    unittest.main()
