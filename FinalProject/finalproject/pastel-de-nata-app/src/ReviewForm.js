import {useState} from "react";
import { Button, Form, FormGroup, Label, Dropdown, DropdownMenu, DropdownItem, DropdownToggle} from "reactstrap";
import axios from "axios";
import moment from "moment";
function ReviewForm({company, toggle}){
     const URL_OPTION = "http://localhost:8000/votacao/api/rating/"; // (1)
     const [reviewText, setReviewText] = useState([]);
     const [ratingValue, setRatingValue] = useState([]);
     const voteAndCloseModal = (event) => { // (3)
         event.preventDefault();
         axios.put(URL_OPTION + company.pk, {
             'pk': company.pk, 'review': reviewText,
             'value': ratingValue,
         }).then();
         toggle()
     }
     const textChangeHandler = (event) => { // (4)
         const val = event.target.value;
         setRatingValue(val);
     }
     const ratingChangeHandler = (event) => { // (4)
         const txt = parseInt(event.target.value);
         setReviewText(txt);
     }
     return(
         <>
             <Form onSubmit={voteAndCloseModal}> {/* (5) */}
                 <FormGroup>
                     <b>Texto:</b><p>{company.first_name}</p>
                 </FormGroup>
                 <FormGroup>
                     <FormGroup check>


                     </FormGroup>
                 </FormGroup>
                 <Button>Submeter</Button> {/* (5) */}
             </Form>
         </>
     );
}
export default ReviewForm;