export interface IRangeVector {
    readonly position: number;

    readonly length: number;
}

export class RangeVector implements IRangeVector {
    readonly position: number = 0;

    readonly length: number = 0;

    constructor(position: number, length: number) {
        this.position = position;

        this.length = length;
    }
}
