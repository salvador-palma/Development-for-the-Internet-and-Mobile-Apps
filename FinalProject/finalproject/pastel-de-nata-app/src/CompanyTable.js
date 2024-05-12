import React, {useEffect, useState} from "react";
import {Table} from "reactstrap";
import DetailModal from "./DetailModal";
import axios from "axios";

function CompanyTable() {
     const URL_COMPANIES = "http://localhost:8000/PastelDeNata/api/enterprise/";
     const [companyList, setCompanyList] = useState([]);
     const getCompanies = () => {
        axios.get(URL_COMPANIES).then((request) => {
            setCompanyList(request.data)
            console.log(request.data)
        });
     };
     useEffect( () => { getCompanies();}, []);
     const centered = { textAlign: "center"};
     return (
         <Table> {}
             <thead>
                 <tr >
                     <th >Nome</th>
                     <th>Avaliação</th>
                     <th style={centered}>Opções</th>
                 </tr>
             </thead>
             <tbody>
                 {
                 companyList.map( (company) => (
                 <tr key={company.user}>
                     <td>{company.first_name}</td>
                     <td>{"⭐".repeat(company.rating_average.toFixed(0))}
                         <span style={{filter:"saturate(0)"}}>{"⭐".repeat(5- company.rating_average.toFixed(0))}</span></td>
                     <td style={centered}>
                         <DetailModal company={company}/>
                     </td>
                 </tr>
                 )
                 )}
             </tbody>
         </Table>
     );
}
export default CompanyTable;