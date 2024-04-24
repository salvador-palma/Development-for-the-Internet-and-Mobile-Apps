import { useState } from "react";

function Contador(){

    const [amount, setAmount] = useState(0); 

    const incrementar = () => {
        setAmount(amount + 1);
    };

    return (
        <>
            <button onClick={incrementar}>Incrementar</button>
            {amount}
        </>
    )
}

export default Contador;
