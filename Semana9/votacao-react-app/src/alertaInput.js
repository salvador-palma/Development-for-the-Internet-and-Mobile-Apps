import { useState } from "react";

function AlertaInput(){

    const [alerta, setAlerta] = useState(""); 

    const displayAlerta = (event) => {
        alert(alerta);
    };

    return (
        <form onSubmit={displayAlerta}>
            <label>Texto do alerta:
            <input type="text" value={alerta} onChange={(e) => setAlerta(e.target.value)}/>
            </label>
            <input type="submit" value="criar"/>
        </form>
    )
}

export default AlertaInput;
