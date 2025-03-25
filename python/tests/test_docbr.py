import unittest

from docbr import DocBrCNPJ, DocBrCPF, DocBrCNH, DocBrTE, DocBrPIS, DocBrCertidao


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

    def test_validate_cnh_valid(self):
        self.assertTrue(DocBrCNH.validate("72146812913"))

    def test_validate_cnh_invalid(self):
        self.assertFalse(DocBrCNH.validate("72146812914"))

    def test_format_cnh_mask_false(self):
        self.assertEqual(
            DocBrCNH.format("72146812913", mask=False),
            "72146812913",
        )

    def test_format_cnh_mask_true(self):
        self.assertEqual(
            DocBrCNH.format("72146812913", mask=True),
            "721 468 129 13",
        )

    def test_generate_cnh(self):
        result = DocBrCNH.generate()
        self.assertEqual(
            len(result),
            11,
        )
        self.assertTrue(DocBrCNH.validate(result))

    def test_validate_te_valid(self):
        self.assertTrue(DocBrTE.validate("652510840116"))

    def test_validate_te_invalid(self):
        self.assertFalse(DocBrTE.validate("652510840117"))

    def test_format_te_mask_false(self):
        self.assertEqual(
            DocBrTE.format("652510840116", mask=False),
            "652510840116",
        )

    def test_format_te_mask_true(self):
        self.assertEqual(
            DocBrTE.format("652510840116", mask=True),
            "6525.1084.0116",
        )

    def test_generate_te(self):
        result = DocBrTE.generate()

        self.assertEqual(
            len(result),
            12,
        )
        self.assertTrue(DocBrTE.validate(result))

    def test_validate_pis_valid(self):
        self.assertTrue(DocBrPIS.validate("10558353026"))

    def test_validate_pis_invalid(self):
        self.assertFalse(DocBrPIS.validate("10558353027"))

    def test_format_pis_mask_false(self):
        self.assertEqual(
            DocBrPIS.format("10558353026", mask=False),
            "10558353026",
        )

    def test_format_pis_mask_true(self):
        self.assertEqual(
            DocBrPIS.format("10558353026", mask=True),
            "105.58353.02-6",
        )

    def test_generate_pis(self):
        result = DocBrPIS.generate()
        self.assertEqual(
            len(result),
            11,
        )
        self.assertTrue(DocBrPIS.validate(result))

    def test_validate_certidao_valid(self):
        self.assertTrue(DocBrCertidao.validate("24581501552011121241007260521813"))

    def test_validate_certidao_invalid(self):
        self.assertFalse(DocBrCertidao.validate("24581501552011121241007260521814"))

    def test_format_certidao_mask_false(self):
        self.assertEqual(
            DocBrCertidao.format("24581501552011121241007260521813", mask=False),
            "24581501552011121241007260521813",
        )

    def test_format_certidao_mask_true(self):
        self.assertEqual(
            DocBrCertidao.format("24581501552011121241007260521813", mask=True),
            "245815.01.55.2011.1.21241.007.2605218-13",
        )

    def test_generate_certidao(self):
        result = DocBrCertidao.generate()
        self.assertEqual(
            len(result),
            32,
        )
        self.assertTrue(DocBrCertidao.validate(result))

if __name__ == "__main__":
    unittest.main()
