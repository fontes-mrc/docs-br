import { assert } from "chai";
import { DocBrCPF, DocBrCNPJ } from "./docbr";

suite("DocBrCPF", () => {
  test("should validate a valid CPF", () => {
    assert.isTrue(DocBrCPF.validate('93481451008'));
  });

  test("should not validate an invalid CPF", () => {
    assert.isFalse(DocBrCPF.validate('93481451007'));
  });

  test("should format CPF without mask", () => {
    assert.equal(DocBrCPF.format('93481451008', false), '93481451008');
  });

  test("should format CPF with mask", () => {
    assert.equal(DocBrCPF.format('93481451008', true), '934.814.510-08');
  });

  test("should generate a valid CPF", () => {
    const result = DocBrCPF.generate();
    assert.lengthOf(result, 11);
    assert.isTrue(DocBrCPF.validate(result));
  });
});

suite("DocBrCNPJ", () => {
  test("should validate a valid CNPJ", () => {
    assert.isTrue(DocBrCNPJ.validate('39593854000164'));
  });

  test("should not validate an invalid CNPJ", () => {
    assert.isFalse(DocBrCNPJ.validate('39593854000165'));
  });

  test("should format CNPJ without mask", () => {
    assert.equal(DocBrCNPJ.format('39593854000164', false), '39593854000164');
  });

  test("should format CNPJ with mask", () => {
    assert.equal(DocBrCNPJ.format('39593854000164', true), '39.593.854/0001-64');
  });

  test("should generate a valid CNPJ", () => {
    const result = DocBrCNPJ.generate();
    assert.lengthOf(result, 14);
    assert.isTrue(DocBrCNPJ.validate(result));
  });
});