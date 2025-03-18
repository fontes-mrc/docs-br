import unittest
import numpy as np

from docbr import DocBrCNPJ, DocBrCPF


class TestDocBr(unittest.TestCase):
    def test_validate_cpf_valid(self):
        self.assertTrue(DocBrCPF.validate(np.array(["93481451008"])))

    def test_validate_cpf_invalid(self):
        self.assertFalse(DocBrCPF.validate(np.array(["93481451007"])))

    def test_validate_cnpj_valid(self):
        self.assertTrue(DocBrCNPJ.validate(np.array(["39593854000164"])))

    def test_validate_cnpj_invalid(self):
        self.assertFalse(DocBrCNPJ.validate(np.array(["39593854000165"])))

    def test_format_cpf_mask_false(self):
        self.assertEqual(
            DocBrCPF.format(np.array(["93481451008"]), mask=False),
            np.array(["93481451008"]),
        )

    def test_format_cpf_mask_true(self):
        self.assertEqual(
            DocBrCPF.format(np.array(["93481451008"]), mask=True),
            np.array(["934.814.510-08"]),
        )

    def test_format_cnpj_mask_false(self):
        self.assertEqual(
            DocBrCNPJ.format(np.array(["39593854000164"]), mask=False),
            np.array(["39593854000164"]),
        )

    def test_format_cnpj_mask_true(self):
        self.assertEqual(
            DocBrCNPJ.format(np.array(["39593854000164"]), mask=True),
            np.array(["39.593.854/0001-64"]),
        )

    def test_generate_cpf(self):
        result = DocBrCPF.generate(n=2)
        self.assertEqual(
            len(result),
            2,
        )
        self.assertTrue(all(DocBrCPF.validate(result)))

    def test_generate_cnpj(self):
        result = DocBrCNPJ.generate(n=2)
        self.assertEqual(
            len(result),
            2,
        )
        self.assertTrue(all(DocBrCNPJ.validate(result)))


if __name__ == "__main__":
    unittest.main()
