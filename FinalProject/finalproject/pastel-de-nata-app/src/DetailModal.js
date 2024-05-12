import React, {useState } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import axios from "axios";
import DetailData from "./DetailData";
function DetailModal({company}) {
     const URL_OPTIONS = "http://localhost:8000/PastelDeNata/api/rating/";
     const [showModal, setShowModal] = useState(false);
     const [ratingList, setRatingList] = useState([]);
     const getOptions = () => {
         axios.get(URL_OPTIONS + company.pk).then(request => { setRatingList(request.data);});
     };
     const toggleModal = () => {
         if (!showModal) getOptions();
         setShowModal(showModal => !showModal);
     };
     return (
         <>
             <Button onClick={toggleModal} color="warning"> {}
                 info.
             </Button>
             <Modal isOpen={showModal} toggle={toggleModal}> {}
                 <ModalHeader toggle={toggleModal}>
                     {company.first_name}
                 </ModalHeader>
                 <ModalBody>
                     <DetailData ratings={ratingList}
                     company={company}
                     toggle={toggleModal}/> {}
                 </ModalBody>
             </Modal>
         </>
     );
}
export default DetailModal;