import React, { ReactElement } from "react";
import { Navigate, Outlet, useLocation } from "react-router";
import { useLogin } from "../context/loginContext";

/** Redirect to the login if the user is not authenticated*/
export const PrivateRoute = (): ReactElement => {
  const location = useLocation();
  const { loginForm } = useLogin();

  return loginForm.isAuthenticated ? (
    <Outlet />
  ) : (
    <Navigate to="/login" state={{ from: location }} replace />
  );
};
