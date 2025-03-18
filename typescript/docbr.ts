type Sequence = number[];

class DocBr {
    protected static _len: number;
    protected static _modulo: number;
    protected static _sequences: Sequence[];
    protected static _moduloTransformer: (digit: number) => number;
    protected static _charset: string[];
    protected static _fmtMask: string;
    protected static _digitOffset: number = "0".charCodeAt(0);

    protected static _digitsFromString(doc: string): number[] {
        doc = doc.toUpperCase();
        return Array.from(doc)
            .filter(d => this._charset.includes(d))
            .map(d => d.charCodeAt(0) - this._digitOffset);
    }

    protected static _stringFromDigits(digits: number[]): string {
        return digits.map(d => String.fromCharCode(d + this._digitOffset)).join('');
    }

    protected static _getValidators(digits: number[]): number[] {
        const validators: number[] = [];
        const tempDigits = digits.slice();

        for (const seq of this._sequences) {
            const pos = seq.length;
            let digit = seq.reduce((sum, value, i) => sum + value * tempDigits[i], 0);
            digit = digit % this._modulo;
            digit = this._moduloTransformer(digit);

            tempDigits[pos] = digit;
            validators.push(digit);
        }

        return validators;
    }

    protected static _checkValidators(digits: number[], validators: number[]): boolean {
        const pos = validators.length;
        return digits.slice(-pos).every((digit, i) => digit === validators[i]);
    }

    static generate(mask: boolean = false): string {
        const idx = Array.from({ length: this._len }, () => Math.floor(Math.random() * this._charset.length));
        let doc = idx.map(i => this._charset[i]).join('');
        let digits = this._digitsFromString(doc);
        const validators = this._getValidators(digits);

        validators.forEach((v, i) => {
            digits[digits.length - validators.length + i] = v;
        });

        doc = this._stringFromDigits(digits);

        if (mask) {
            return this._fmtMask.replace(/#/g, () => doc.charAt(0));
        }

        return doc;
    }

    static validate(doc: string): boolean {
        const digits = this._digitsFromString(doc);

        if (digits.length !== this._len) {
            return false;
        }

        if (new Set(digits).size === 1) {
            return false;
        }

        const validators = this._getValidators(digits);
        return this._checkValidators(digits, validators);
    }

    static format(doc: string, mask: boolean = false): string {
        const digits = this._digitsFromString(doc);
        doc = this._stringFromDigits(digits);
    
        if (mask) {
            let maskedDoc = this._fmtMask;
            for (const digit of doc) {
                maskedDoc = maskedDoc.replace('#', digit);
            }
            return maskedDoc;
        }
    
        return doc;
    }
}

export class DocBrCPF extends DocBr {
    protected static _len = 11;
    protected static _modulo = 11;
    protected static _sequences: Sequence[] = [
        [10, 9, 8, 7, 6, 5, 4, 3, 2],
        [11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
    ];
    protected static _moduloTransformer = (x: number) => (x < 2 ? 0 : 11 - x);
    protected static _charset = "0123456789".split('');
    protected static _fmtMask = "###.###.###-##";
}

export class DocBrCNPJ extends DocBr {
    protected static _len = 14;
    protected static _modulo = 11;
    protected static _sequences: Sequence[] = [
        [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
        [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
    ];
    protected static _moduloTransformer = (x: number) => (x < 2 ? 0 : 11 - x);
    protected static _charset = "0123456789ABCDEFGHIJKLMNOPQSRTUVWXYZ".split('');
    protected static _fmtMask = "##.###.###/####-##";
}