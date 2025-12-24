import React, { useActionState, useEffect } from "react";
import { Link } from "react-router";
import LoginModal from "./login-modal";
import "./header.css";
import { useLogin } from "../context/loginContext";

export type HeaderProps = {
  projIcons: {
    logo: string;
  };
  projTextPlacement: string;
  projLogoText: string;
  pageTitle: string;
  isAuthenticated?: boolean;
};

const Header: React.FC<HeaderProps> = ({
  projIcons,
  projTextPlacement,
  projLogoText,
  pageTitle,
}) => {
  const { loginForm, showLoginModal, setShowLoginModal } = useLogin();

  const logoUrl = projIcons.logo
    ? // @ts-ignore
      `${import.meta.env.VITE_API_BASE_URL}${projIcons.logo}`
    : "";

  return (
    <header>
      <nav className="navbar navbar-expand-md navbar-light">
        <div className="container">
          <a className="navbar-brand" href="/">
            <div
              className={`navbar-brand-wrapper text-${projTextPlacement}`}
              style={{ backgroundImage: `url(${logoUrl})` }}
            >
              <div className="navbar-brand-text">{projLogoText}</div>
            </div>
          </a>

          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>

          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-md-0 justify-content-end align-items-center">
              <li
                className={`nav-item ${pageTitle === "About" ? "active" : ""}`}
              >
                <Link to="/about" className="nav-link">
                  About
                </Link>
              </li>
              <li
                className={`nav-item ${pageTitle === "Results" || pageTitle === "Search" ? "active" : ""}`}
              >
                <>
                  {loginForm.isAuthenticated ? (
                    <Link to="/explore" className="nav-link nav-explore">
                      Search
                    </Link>
                  ) : (
                    <a className="nav-link nav-explore disabled">Search</a>
                  )}
                </>
              </li>
              <li
                className={`nav-item ${pageTitle === "Help" ? "active" : ""}`}
              >
                <Link to="/help" className="nav-link">
                  Help
                </Link>
              </li>
              {loginForm.isAuthenticated ? (
                <li className="nav-item dropdown user-menu">
                  <a
                    className="nav-link dropdown-toggle"
                    href="#"
                    role="button"
                    id="userDropdown"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  ></a>
                  <ul className="dropdown-menu" aria-labelledby="userDropdown">
                    <li>
                      <a
                        className="dropdown-item"
                        href="/admin"
                        target="_blank"
                      >
                        Administration
                      </a>
                    </li>
                    <li>
                      <a className="dropdown-item" href="/logout?next=/">
                        Logout
                      </a>
                    </li>
                  </ul>
                </li>
              ) : (
                <li className="nav-item user-menu">
                  <button
                    className="header-button nav-link"
                    onClick={() => setShowLoginModal(true)}
                  >
                    Login
                  </button>
                </li>
              )}
            </ul>
          </div>
        </div>
      </nav>
      <LoginModal
        show={showLoginModal}
        handleClose={() => setShowLoginModal(false)}
        handleSubmit={loginForm.formAction}
        isPending={loginForm.isPending}
        error={loginForm.error}
      />
    </header>
  );
};

export default Header;
