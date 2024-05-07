import React, {useState } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import axios from "axios";
import DetailData from "./DetailData";
function DetailModal({company}) { // (1)
     const URL_OPTIONS = "http://localhost:8000/PastelDeNata/api/rating/"; // (2)
     const [showModal, setShowModal] = useState(false); // (3)
     const [ratingList, setRatingList] = useState([]); // (4)
     const getOptions = () => { // (5)
         axios.get(URL_OPTIONS + company.pk).then(request => { setRatingList(request.data);});
     };
     const toggleModal = () => { // (6)
         if (!showModal) getOptions();
         setShowModal(showModal => !showModal);
     };
     return (
         <>
             <Button onClick={toggleModal} color="warning"> {/* (7) */}
                 info.
             </Button>
             <Modal isOpen={showModal} toggle={toggleModal}> {/* (8) */}
                 <ModalHeader toggle={toggleModal}>
                     {company.first_name}
                 </ModalHeader>
                 <ModalBody>
                     <DetailData ratings={ratingList}
                     company={company}
                     toggle={toggleModal}/> {/* (9) */}
                 </ModalBody>
             </Modal>
         </>
     );
}
export default DetailModal;