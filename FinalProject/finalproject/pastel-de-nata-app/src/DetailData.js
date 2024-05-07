import React from "react";
import { Button, Form, FormGroup, Table } from "reactstrap";
import moment from "moment";
function DetailData({ratings, company, toggle}) { // (1)
     const closeModal = (e) => { // (2)
         e.preventDefault();
         toggle();
     }
     return (
         <Form onSubmit={closeModal}> {/* (3) */}
             <FormGroup>

                 <p>{company.address}</p>
                 <p>⭐{company.rating_average.toFixed(2)}</p>
             </FormGroup>
             <FormGroup>
                 <Table> {/* (5) */}
                     <thead>
                         <tr>
                             <th style={{textAlign: "left"}}>User</th>
                             <th style={{textAlign: "right"}}>Avaliação</th>
                         </tr>
                    </thead>
                    <tbody>
                         {ratings.map( (r) => // (6)
                         <tr>
                             <td style={{textAlign: "left"}}>{ r.user_first_name}</td>
                             <td style={{textAlign: "right"}}>{ "⭐".repeat(r.value)}</td>
                         </tr>
                         )}
                    </tbody>
                 </Table>
             </FormGroup>
             <Button>Fechar</Button> {/* (3) */}
         </Form>
     );
}
export default DetailData;