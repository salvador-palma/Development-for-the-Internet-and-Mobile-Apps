import Header from "./Header";
import {Container, Row, Col} from "reactstrap";
import CompanyTable from "./CompanyTable";
function Home() {
     return (
         <>
         <Header />
         <Content />
         </>
     );
}
function Content() {
     return (
         <Container style={{marginTop: "20px", maxWidth: "800px"}}>
             <Row>
                 <Col>
                    <CompanyTable/>
                 </Col>
             </Row>
         </Container>
     );
}
export default Home;