package docbr

import (
	"math/rand"
	"strings"
	"time"
)

type DocBr struct {
	len            int
	modulo         int
	sequences      [][]int
	moduloTransformer func(int) int
	charset        string
	fmtMask        string
}

func NewDocBr(len int, modulo int, sequences [][]int, moduloTransformer func(int) int, charset string, fmtMask string) *DocBr {
	return &DocBr{
		len:              len,
		modulo:           modulo,
		sequences:        sequences,
		moduloTransformer: moduloTransformer,
		charset:          charset,
		fmtMask:          fmtMask,
	}
}

func (d *DocBr) digitsFromString(doc string) []int {
	digits := []int{}
	for _, char := range strings.ToUpper(doc) {
		if index := strings.IndexByte(d.charset, byte(char)); index != -1 {
			digits = append(digits, index)
		}
	}
	return digits
}

func (d *DocBr) stringFromDigits(digits []int) string {
	var sb strings.Builder
	for _, digit := range digits {
		sb.WriteByte(d.charset[digit])
	}
	return sb.String()
}

func (d *DocBr) getValidators(digits []int) []int {
	validators := []int{}
	tempDigits := make([]int, len(digits))
	copy(tempDigits, digits)

	for _, seq := range d.sequences {
		pos := len(seq)
		sum := 0
		for i := 0; i < pos; i++ {
			sum += seq[i] * tempDigits[i]
		}
		digit := sum % d.modulo
		digit = d.moduloTransformer(digit)

		if len(tempDigits) > pos {
			tempDigits[pos] = digit
		} else {
			tempDigits = append(tempDigits, digit)
		}
		validators = append(validators, digit)
	}

	return validators
}

func (d *DocBr) checkValidators(digits []int, validators []int) bool {
	pos := len(validators)
	for i := 0; i < pos; i++ {
		if digits[len(digits)-pos+i] != validators[i] {
			return false
		}
	}
	return true
}

func (d *DocBr) Generate(mask bool) string {
	rand.Seed(time.Now().UnixNano())
	idx := make([]int, d.len)
	for i := range idx {
		idx[i] = rand.Intn(len(d.charset))
	}
	doc := d.stringFromDigits(idx)
	digits := d.digitsFromString(doc)
	validators := d.getValidators(digits)

	for i, v := range validators {
		digits[len(digits)-len(validators)+i] = v
	}

	doc = d.stringFromDigits(digits)

	if mask {
		return applyMask(doc, d.fmtMask)
	}

	return doc
}

func (d *DocBr) Validate(doc string) bool {
	digits := d.digitsFromString(doc)

	if len(digits) != d.len {
		return false
	}

	if len(unique(digits)) == 1 {
		return false
	}

	validators := d.getValidators(digits)
	return d.checkValidators(digits, validators)
}

func (d *DocBr) Format(doc string, mask bool) string {
	digits := d.digitsFromString(doc)
	doc = d.stringFromDigits(digits)

	if mask {
		return applyMask(doc, d.fmtMask)
	}

	return doc
}

func applyMask(doc string, mask string) string {
	var sb strings.Builder
	docIndex := 0
	for _, char := range mask {
		if char == '#' {
			sb.WriteByte(doc[docIndex])
			docIndex++
		} else {
			sb.WriteByte(byte(char))
		}
	}
	return sb.String()
}

func unique(ints []int) []int {
	keys := make(map[int]bool)
	var list []int
	for _, entry := range ints {
		if _, value := keys[entry]; !value {
			keys[entry] = true
			list = append(list, entry)
		}
	}
	return list
}

var (
	DocBrCPF = NewDocBr(
		11,
		11,
		[][]int{
			{10, 9, 8, 7, 6, 5, 4, 3, 2},
			{11, 10, 9, 8, 7, 6, 5, 4, 3, 2},
		},
		func(x int) int {
			if x < 2 {
				return 0
			}
			return 11 - x
		},
		"0123456789",
		"###.###.###-##",
	)

	DocBrCNPJ = NewDocBr(
		14,
		11,
		[][]int{
			{5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2},
			{6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2},
		},
		func(x int) int {
			if x < 2 {
				return 0
			}
			return 11 - x
		},
		"0123456789ABCDEFGHIJKLMNOPQSRTUVWXYZ",
		"##.###.###/####-##",
	)
)