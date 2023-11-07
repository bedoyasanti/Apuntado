import {Baraja} from "./Baraja.js"
export class Partida{
    constructor(turnos){
        let BarajaJuego = new Baraja();
        this.mazo = {};
        this.turnos = turnos;

        for (let i = 0; i <= BarajaJuego.baraja.length;i++){
            this.mazo[BarajaJuego.baraja[i]] = 2;
        };
    };
}