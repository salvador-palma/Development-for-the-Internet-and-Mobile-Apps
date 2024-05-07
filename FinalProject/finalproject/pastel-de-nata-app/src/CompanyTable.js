import React, {useEffect, useState} from "react";
import {Table} from "reactstrap";
import DetailModal from "./DetailModal";
import VoteModal from "./VoteModal";
import axios from "axios";
import './react.css';
function CompanyTable() {
     const URL_COMPANIES = "http://localhost:8000/PastelDeNata/api/enterprise/"; // (1)
     const [companyList, setCompanyList] = useState([]); // (2)
     const getCompanies = () => { // (3)
        axios.get(URL_COMPANIES).then((request) => {
            setCompanyList(request.data)
            console.log(request.data)
        });
     };
     useEffect( () => { getCompanies();}, []);
     const centered = { textAlign: "center"};
     return (
         <Table style={{backgroundColor: "#F3A128"}}> {/* (5) */}
             <thead>
                 <tr >
                     <th >Nome</th>
                     <th style={centered}>Opções</th>
                 </tr>
             </thead>
             <tbody>
                 {
                 companyList.map( (company) => ( // (6)
                 <tr key={company.user}>
                     <td>{company.first_name}</td>
                     <td style={centered}>
                         <DetailModal company={company}/>
                         &nbsp;
                         {/*<VoteModal company={company}/>*/}
                     </td>
                 </tr>
                 )
                 )}
             </tbody>
         </Table>
     );
}
export default CompanyTable;