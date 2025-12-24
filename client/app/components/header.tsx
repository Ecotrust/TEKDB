import React, { useActionState, useEffect } from "react";
import { Link } from "react-router";
import LoginModal from "./login-modal";
import { tekdbApi, primeCsrf } from "../api/tekdbApi";
import "./header.css";

export type HeaderProps = {
  projIcons: {
    logo: string;
  };
  projTextPlacement: string;
  projLogoText: string;
  pageTitle: string;
  isAuthenticated?: boolean;
};

type LoginState = {
  success?: boolean;
  error?: string | null;
};

type UseLoginFormReturn = {
  isAuthenticated: boolean;
  formAction: (formData: FormData) => void;
  isPending: boolean;
  error: string | null;
};

const useLoginForm = (
  action: (prevState: LoginState, formData: FormData) => Promise<LoginState>,
  onSuccess: () => void,
  onError: () => void
): UseLoginFormReturn => {
  const [state, formAction, isPending] = useActionState<LoginState, FormData>(
    action,
    {
      success: false,
      error: null,
    }
  );
  const [isAuthenticated, setIsAuthenticated] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);

  useEffect(() => {
    if (state?.success) {
      setIsAuthenticated(true);
      setError(null);
      onSuccess();
    } else {
      setIsAuthenticated(false);
      if (state?.error) {
        setError(state.error);
        onError();
      }
    }
  }, [state?.success, state?.error, onSuccess, onError]);

  return {
    isAuthenticated,
    formAction,
    isPending,
    error,
  };
};

const submitAction = async (
  prevState: LoginState,
  formData: FormData
): Promise<LoginState> => {
  const username = String(formData.get("username") ?? "");
  const password = String(formData.get("password") ?? "");

  // Prime CSRF cookie/token first
  const csrfToken = await primeCsrf();

  // Use form-encoded body
  const body = new URLSearchParams();
  body.append("username", username);
  body.append("password", password);

  const login = await tekdbApi.post("/login_async/", body, {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "X-CSRFToken": csrfToken,
    },
    withCredentials: true,
  });

  if (
    login.status !== 200 ||
    login.statusText !== "OK" ||
    !login.data.success
  ) {
    return {
      ...prevState,
      success: false,
      error: login.data.error || "Invalid username or password",
    };
  } else if (login.status == 200) {
    return { ...prevState, success: true, error: null };
  }
  return {
    ...prevState,
    success: false,
    error: "Invalid username or password",
  };
};

const Header: React.FC<HeaderProps> = ({
  projIcons,
  projTextPlacement,
  projLogoText,
  pageTitle,
}) => {
  const [showLoginModal, setShowLoginModal] = React.useState(false);
  const handleCloseLoginModal = () => setShowLoginModal(false);
  const handleShowLoginModal = () => setShowLoginModal(true);
  const {
    isAuthenticated,
    formAction: loginFormAction,
    isPending,
    error,
  } = useLoginForm(
    submitAction,
    () => handleCloseLoginModal(),
    () => {
      // Handle error (optional)
    }
  );

  const logoUrl = projIcons.logo
    ? `${import.meta.env.VITE_API_BASE_URL}${projIcons.logo}`
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
                  {isAuthenticated ? (
                    <Link to="/explore" className="nav-link nav-explore">
                      Search
                    </Link>
                  ) : (
                    // <a href="/explore" className="nav-link nav-explore">
                    //   Search
                    // </a>
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
                {/* <a onClick={() => setPageName("Help")} className="nav-link">
                  Help
                </a> */}
              </li>
              {isAuthenticated ? (
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
                    onClick={handleShowLoginModal}
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
        handleClose={handleCloseLoginModal}
        handleSubmit={loginFormAction}
        isPending={isPending}
        error={error}
      />
    </header>
  );
};

export default Header;
