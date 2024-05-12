import React from "react";
import { Button, Form, FormGroup, Table } from "reactstrap";

function DetailData({ratings, company, toggle}) {
     const closeModal = (e) => {
         e.preventDefault();
         toggle();
     }
     return (
         <Form onSubmit={closeModal}> {}
             <FormGroup>

                 <p>{company.address}</p>
                 <p>⭐{company.rating_average.toFixed(2)}</p>
             </FormGroup>
             <FormGroup>
                 <Table> {}
                     <thead>
                         <tr>
                             <th style={{textAlign: "left"}}>User</th>
                             <th style={{textAlign: "right"}}>Avaliação</th>
                         </tr>
                    </thead>
                    <tbody>
                         {ratings.map( (r) =>
                         <tr>
                             <td style={{textAlign: "left"}}>{ r.user_first_name}</td>
                             <td style={{textAlign: "right"}}>{ "⭐".repeat(r.value)}</td>
                         </tr>
                         )}
                    </tbody>
                 </Table>
             </FormGroup>
             <Button>Fechar</Button> {}
         </Form>
     );
}
export default DetailData;