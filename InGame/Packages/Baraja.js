import {Carta} from "./Carta.js";
export class Baraja{
    constructor(){
        this.baraja = [];
        let pintas = ["Clubs","Diamonds","Hearts","Spades"];
        for (let i = 0; i <= 3; i++){
            let pinta = pintas[i]
            for (let j = 2; j <= 14; j++){
                if (j == 11){
                    this.baraja.push(new Carta(pinta,"J"));
                }
                else if (j == 12){
                    this.baraja.push(new Carta(pinta,"Q"));
                }
                else if (j == 13){
                    this.baraja.push(new Carta(pinta,"K"));
                }
                else if (j == 14){
                    this.baraja.push(new Carta(pinta,"A"));
                }
                else{
                    this.baraja.push(new Carta(pinta,`${j}`));
                };
            };
        };
    };
};