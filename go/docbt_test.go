package docbr

import (
	"testing"
)

func TestValidateCPFValid(t *testing.T) {
	if !DocBrCPF.Validate("93481451008") {
		t.Error("Expected valid CPF to return true")
	}
}

func TestValidateCPFInvalid(t *testing.T) {
	if DocBrCPF.Validate("93481451007") {
		t.Error("Expected invalid CPF to return false")
	}
}

func TestValidateCNPJValid(t *testing.T) {
	if !DocBrCNPJ.Validate("39593854000164") {
		t.Error("Expected valid CNPJ to return true")
	}
}

func TestValidateCNPJInvalid(t *testing.T) {
	if DocBrCNPJ.Validate("39593854000165") {
		t.Error("Expected invalid CNPJ to return false")
	}
}

func TestFormatCPFMaskFalse(t *testing.T) {
	if result := DocBrCPF.Format("93481451008", false); result != "93481451008" {
		t.Errorf("Expected formatted CPF without mask to be '93481451008', got '%s'", result)
	}
}

func TestFormatCPFMaskTrue(t *testing.T) {
	if result := DocBrCPF.Format("93481451008", true); result != "934.814.510-08" {
		t.Errorf("Expected formatted CPF with mask to be '934.814.510-08', got '%s'", result)
	}
}

func TestFormatCNPJMaskFalse(t *testing.T) {
	if result := DocBrCNPJ.Format("39593854000164", false); result != "39593854000164" {
		t.Errorf("Expected formatted CNPJ without mask to be '39593854000164', got '%s'", result)
	}
}

func TestFormatCNPJMaskTrue(t *testing.T) {
	if result := DocBrCNPJ.Format("39593854000164", true); result != "39.593.854/0001-64" {
		t.Errorf("Expected formatted CNPJ with mask to be '39.593.854/0001-64', got '%s'", result)
	}
}

func TestGenerateCPF(t *testing.T) {
	result := DocBrCPF.Generate(false)
	if len(result) != 11 {
		t.Errorf("Expected generated CPF length to be 11, got %d", len(result))
	}
	if !DocBrCPF.Validate(result) {
		t.Errorf("Expected generated CPF to be valid, got %s", result)
	}
}

func TestGenerateCNPJ(t *testing.T) {
	result := DocBrCNPJ.Generate(false)
	if len(result) != 14 {
		t.Errorf("Expected generated CNPJ length to be 14, got %d", len(result))
	}
	if !DocBrCNPJ.Validate(result) {
		t.Errorf("Expected generated CNPJ to be valid, got %s", result)
	}
}