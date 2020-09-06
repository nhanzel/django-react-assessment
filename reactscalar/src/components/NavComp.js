import React, {useState} from 'react';

import {Navbar, Nav, NavDropdown, Form, FormControl, Button} from 'react-bootstrap';

function NavComp() {
    return(
        <Navbar bg="light" expand="lg">
            <Navbar.Brand href="">Django-React</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
                <Nav.Link href="#home">Home</Nav.Link>
                <Nav.Link href="#link">Link</Nav.Link>
            </Nav>
        </Navbar.Collapse>
        </Navbar>
    )
}

export default NavComp;