import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Form from "react-bootstrap/Form";
import React from "react";

type LoginModalProps = {
  show: boolean;
  handleClose: () => void;
  handleSubmit: (formData: FormData) => void;
  isPending: boolean;
  error: string | null;
};

const LoginModal: React.FC<LoginModalProps> = ({
  show,
  handleClose,
  handleSubmit,
  isPending,
  error,
}) => {
  return (
    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Please Log In</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <form action={handleSubmit}>
          <Form.Group controlId="username">
            <Form.Label>Username</Form.Label>
            <Form.Control
              type="text"
              name="username"
              placeholder="Username"
              required
              className="form-control"
            />
          </Form.Group>
          <Form.Group controlId="password">
            <Form.Label>Password</Form.Label>
            <Form.Control
              type="password"
              name="password"
              placeholder="Password"
              required
              className="form-control"
            />
          </Form.Group>
          <Button variant="primary" type="submit" disabled={isPending}>
            Log In
          </Button>
        </form>
      </Modal.Body>
      {error && (
        <Modal.Footer>
          <div className="text-danger">{error}</div>
        </Modal.Footer>
      )}
    </Modal>
  );
};

export default LoginModal;
