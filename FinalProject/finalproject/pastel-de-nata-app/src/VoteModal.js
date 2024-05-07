import React, {useState} from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import axios from "axios";
import ReviewForm from "./ReviewForm";
function VoteModal({company}) {
     const URL_OPTIONS = "http://localhost:8000/votacao/api/rating/";
     const [showModal, setShowModal] = useState(false);

     const toggleModal = () => {
         if (!showModal)
         setShowModal(showModal => !showModal);
         };
     return (
         <>
             <Button onClick={toggleModal} color="success">
                Review
             </Button>
             <Modal isOpen={showModal} toggle={toggleModal}>
                 <ModalHeader toggle={toggleModal}>
                    Avaliar {company.first_name}
                 </ModalHeader>
                 <ModalBody>
                     <ReviewForm company={company}
                    toggle={toggleModal}/>
                 </ModalBody>
             </Modal>
         </>
     );
    }
export default VoteModal;