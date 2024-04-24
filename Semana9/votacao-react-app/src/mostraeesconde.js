import { useState } from "react";

function HideShow(){

    const [isShow, setShow] = useState(true); 

    const flipShow = () => {
        setShow(!isShow);
    };

    return (
        <>
            <button onClick={flipShow}>Flip</button>
            {isShow && <p>Texto Exemplo</p>}
            {!isShow && <img src="https://thechive.com/wp-content/uploads/2019/12/person-hilariously-photoshops-animals-onto-random-things-xx-photos-25.jpg?attachment_cache_bust=3136487&quality=85&strip=info&w=400"></img>}
        </>
    )
}

export default HideShow;
