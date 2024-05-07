function Header() {
     return (
         <>
             <div className="text-center">
                 <img
                 src="/PastelDeNata.png" // (1)
                 width="300"
                 alt="ISCTE"
                 className="img-thumbnail"
                 style={{ marginTop: "20px" }} // (2)
                 />
                 <h2>Pastel de Nata</h2>
                 <h3>Os Estabelecimentos</h3>
             </div>
         </>
     );
}
export default Header;