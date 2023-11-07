export class Carta{
    constructor(pinta, denominacion){
        let valor = 0;
        if (denominacion == "J" || denominacion == "Q" || denominacion == "K" || denominacion == "A"){
            valor = 10;
        }
        else{
            valor = Number(denominacion);
        };

        this.carta = {
            nombre: `${pinta}${denominacion}`,
            denominacion: denominacion,
            pinta: pinta,
            valor: valor,
            source: `../img/Classic/${pinta}/${pinta}${denominacion}.png`
        };
    };

    changeStyle(newStyle){
        this.carta.source = `../img/${newStyle}/${pinta}/${pinta}${denominacion}.png`;
    };
};
