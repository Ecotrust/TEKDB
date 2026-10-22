import React from "react";
import { Outlet } from "react-router";
import { useLogin } from "../context/loginContext";

/** Return a 404 if the user is not authenticated */
const PrivateRoute: React.FC = () => {
  const { loginForm } = useLogin();
  console.log("PrivateRoute", loginForm);
  if (loginForm.isCheckingAuth) {
    return <></>;
  }

  return loginForm.isAuthenticated ? (
    <Outlet />
  ) : (
    <h1>404 Not Found</h1>
  );
};

export default PrivateRoute;
